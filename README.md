# py_upnp_redirect
redirect upnp request to chromecast or local player

## Prerequisites
* Python 2, Platinum/scons build need python 2
* Python 3, running the redirector need python3
* [swig](http://www.swig.org/index.php)

## Prepare
* install python2 and swig for python
* get source and init all submodules
```
git clone https://github.com/stonewell/py_upnp_redirect.git
cd py_upnp_redirect
git submodule update --init --recursive
```
* install python dependence, install for both python2 and python3
```
pip2 install -r requirements
pip3 install -r requirements
```

## Build
```
make -f Makefile.mediarenderer
```

## Run
using list command to find out chromecast's friendly name and put friendly name in the run argument
```
export PYTHONPATH=libs
python3 -m upnp_redirect chromecast list
python3 -m upnp_redirect run --output_args "Family Room TV"
```

## TODO
* migrate everything build/run to python3 only
