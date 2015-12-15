HSBNEXero
======

Reporting tool for [HSBNE](http://hsbne.org) using Xero.

# IMPORTANT NOTE
This is a work in progress. It probably doesn't give the correct output yet. Don't rely on it.


## Installation
Install Python3 (if you don't aleady have it). Then,
```
sudo ./setup.py install
```

### Virtual Environment (Optional)
The application's environment can be kept separate from the host's in the typical Python fashion, explained below.

Before installing, with the project directory as the current working directory,

```
pyvenv-3.4 venv
source venv/bin/activate
./setup.py install
```
When complete,
```deactivate```

#### Debian / Ubuntu
pyvenv in Debian / Ubuntu is currently broken. [Link](http://askubuntu.com/questions/488529/pyvenv-3-4-error-returned-non-zero-exit-status-1)

```
pyvenv-3.4 --without-pip venv
source venv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
deactivate
source venv/bin/activate
```

# Running
```
./main.py
```

## Virtual Environment (Optional)
```
source venv/bin/activate
./main.py
deactivate
```

## Obtaining Credentials
Requires access to be granted through Xero (by the treasurer).
The "Consumer Key" goes into "./credentials/consumer_key"
The private RSA key goes into "./credentials/privatekey.pem"
The "Consumer Secret" is not required.

## Implementation Notes
This is a Xero "Private Application".
