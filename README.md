# py_upnp_redirect
Redirect UPnP request to Chromecast or local player.

## Prerequisites
* Python 3, running the redirector need Python3
* [swig](http://www.swig.org/index.php)

## Prepare
* Install Python3 and swig for Python.
* Get sources and init all submodules.
```
git clone https://github.com/stonewell/py_upnp_redirect.git
cd py_upnp_redirect
git submodule update --init --recursive
```
* Install Python dependencies, install for both Python2 and Python3.
```
pip3 install -r requirements.txt
```

## Build
```
make -f Makefile.mediarenderer
```

## Run
Use `list` command to find out Chromecast's friendly name and use it as the run argument.
```
export PYTHONPATH=libs
python3 -m upnp_redirect chromecast list
python3 -m upnp_redirect run --output_args "Family Room TV"
```

## TODO
- [x] Migrate everything build/run to Python3 only.
