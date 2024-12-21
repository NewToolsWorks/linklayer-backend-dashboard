# linklayer-backend-dashboard
Dashboard web server to manage linklayer VPN

### Requeriments
- Ubuntu 22 or higher to avoid possible compatibility issues.
- ROOT access
<<<<<<< HEAD
- Python 3.10.12 or higher 
=======
- Python 3
>>>>>>> parent of 0448e1e (update python3 version)

### INSTALL

_Install all dependencies_

```console
apt update && apt install python3 && apt install -y git && apt install -y python3-venv && apt install -y python3-pip 
```



_Clone repository_

```console
cd /opt && git clone https://github.com/NewToolsWorks/linklayer-backend-dashboard.git && cd linklayer-backend-dashboard
```

_Create virtual env_

```console
python3 -m venv dashweb && source dashweb/bin/activate
```

_Install dependencies_

```console
pip install -r requeriments.txt
```


_Install web dashboard_

- Replace [PORT] with your port example: 8000
- Replace [USERNAME] with your username example: admin
- REPLACE [PASSWORD] with your password example: admin

example command: 

> python3 install.py --port 8000 --host 0.0.0.0 --username admin --password admin


```console
python3 install.py --port [PORT] --host 0.0.0.0 --username [USERNAME] --password [PASSWORD]
```

Done with this the web dashboard is now installed, to access from the browser enter http://ipvps:port/login
example:

> http://45.25.8.6:8000/login

---

That's all, it's a basic web dashboard that we hope will be useful to you as well. We look forward to your push requests to improve this dashboard, especially that you can share it so that many people can use it. Thank you for supporting the project and again we hope that it will be useful to you.

[Telgram Group support](https://t.me/ntwtools)

[Telegram Channel Support](https://t.me/newtoolsworksCanal)

<<<<<<< HEAD
<<<<<<< HEAD
![](https://komarev.com/ghpvc/?username=NewToolsWorks&label=repository+view)
=======
![](https://komarev.com/ghpvc/?username=NewToolsWorks&label=repository view)
>>>>>>> parent of cbbaa00 (views)
=======
![](https://komarev.com/ghpvc/?username=NewToolsWorks&label=repository+view)
>>>>>>> parent of 0448e1e (update python3 version)
