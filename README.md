# linklayer-backend-dashboard
Dashboard web server to manage linklayer VPN

### Requeriments
- Ubuntu 22 or higher to avoid possible compatibility issues.
- ROOT access
- Python 3

### INSTALL

_Install all dependencies_

```console
apt update && apt install python3 && apt install git 
```

_Instal Venv python_
```console
pip install --break-system-packages virtualenv
```

```console
cd /opt 
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