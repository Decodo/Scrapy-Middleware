import base64

class ProxyMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self, settings):
        self.user = settings.get('DECODO_USER')
        self.password = settings.get('DECODO_PASSWORD')
        self.endpoint = settings.get('DECODO_ENDPOINT')
        self.port = settings.get('DECODO_PORT')

    def process_request(self, request, spider):

        user_credentials = '{user}:{passw}'.format(user=self.user, passw=self.password)
        basic_authentication = 'Basic ' + base64.b64encode(user_credentials.encode()).decode()
        host = 'http://{endpoint}:{port}'.format(endpoint=self.endpoint, port=self.port)
        request.meta['proxy'] = host
        request.headers['Proxy-Authorization'] = basic_authentication
