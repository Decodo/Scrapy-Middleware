<p align="center">
<a href="https://dashboard.decodo.com/?page=residential-proxies&utm_source=socialorganic&utm_medium=social&utm_campaign=resi_trial_GITHUB"><img src="https://github.com/user-attachments/assets/60bb48bd-8dcc-48b2-82c9-a218e1e4449c"></a>
</p>

[![](https://dcbadge.vercel.app/api/server/Ja8dqKgvbZ)](https://discord.gg/Ja8dqKgvbZ)

<p align="center">
    <a href="https://github.com/Decodo/Decodo"> :house: Main Repository :house: </a>
</p>

### Disclaimer

In case you are not aware of what Scrapy is or how it works, we suggest researching [Scrapy](https://docs.scrapy.org/en/latest/) documentation in order to continue development with this tool.

### Prerequisites

To get started with Scrapy you will first need to install it using methods provided in their documentation. [Check here for more information](https://docs.scrapy.org/en/latest/intro/install.html)

### Installation

Once you get Scrapy up and running if you have not yet, make sure that you create your project folder:

```
scrapy startproject yourprojectname
```

<img src="https://i.imgur.com/smbyhNw.png" alt="scrapy startproject anaconda prompt">

When project directory is setup, you can deploy our middleware:

1. Open Terminal window.
2. Navigate to the main directory of your project folder using `cd yourprojectname`
3. Download our proxy middleware using the following command: `curl https://raw.githubusercontent.com/Smartproxy/Scrapy-Middleware/master/smartproxy_auth.py > smartproxy_auth.py`
4. You should now see your project folder populated with *smartproxy_auth.py* file.
<img src="https://file2.api.drift.com/drift-prod-file-uploads/94bb%2F94bb73fc522c281e170a6cc81a077ab5/3.png?mimeType=image%2Fpng">

### Configuration

To start using our middleware for proxy authentication, you'll need to configure settings for our proxy authentication.

Doing so is very simple:

1. Using file manager, navigate to your project folder, you should see *settings.py* file located at the bottom of the directory.
2. Edit the *settings.py* file using an editor of your choice and add the following properties at the bottom:
```
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'yourprojectname.smartproxy_auth.ProxyMiddleware': 100,
}

SMARTPROXY_USER = 'username' ## Smartproxy Username (Sub-user)
SMARTPROXY_PASSWORD = 'password' ## Password for your user
SMARTPROXY_ENDPOINT = 'gate.smartproxy.com' ## Endpoint you'd like to use
SMARTPROXY_PORT = '7000' ## Port of the endpoint you are using.
```
<img src="https://file2.api.drift.com/drift-prod-file-uploads/b7b3%2Fb7b36a1e9a1556fb7b361ed17144159a/4.png?mimeType=image%2Fpng">
<img src="https://file2.api.drift.com/drift-prod-file-uploads/348f%2F348f7143ae28ad224fa3a46c2dc7716e/5.png?mimeType=image%2Fpng" alt="smartproxy scrapy middleware http proxy configuration with username password authentication">

3. In `DOWNLOADER_MIDDLEWARES` change `yourprojectname` line to the name of your project.

<img src="https://file2.api.drift.com/drift-prod-file-uploads/87d4%2F87d428d4f2d47e29f3e986e109005d26/6.png?mimeType=image%2Fpng">

4. Make sure that you enter your details account details as well as proxy details within punctuation marks (''). 
5. Save the file.

Once all that is done, all of your spiders will be going through our proxies, if you are not sure how to setup a spider, take a look [here](https://docs.scrapy.org/en/latest/intro/tutorial.html#our-first-spider)

## Need help?
Email - sales@smartproxy.com
<br><a href="https://smartproxy.com">Live chat 24/7</a>
