from .ssdp import SSDPServer
from .upnp_http_server import UPNPHTTPServer
import uuid
import netifaces as ni
from time import sleep
import logging

device_uuid = uuid.uuid4()
local_ip_address = '192.168.1.105'

http_server = UPNPHTTPServer(8088,
                             friendly_name="UPNP Redirector",
                             manufacturer="Jingnan Si",
                             manufacturer_url='http://github.com/stonewell/py_upnp_redirect',
                             model_description='UPNP Redirector 1.0',
                             model_name="UPNP Redirector",
                             model_number="1.0",
                             model_url="http://github.com/stonewell/py_upnp_redirect",
                             serial_number="upnp_redirect_1.0",
                             uuid=device_uuid,
                             presentation_url="http://{}:5000/".format(local_ip_address))

ssdp = SSDPServer()
ssdp.register('local',
              'uuid:{}::urn:schemas-upnp-org:device:MediaRenderer:1'.format(device_uuid),
              'urn:schemas-upnp-org:device:MediaRenderer:1',
              'http://{}:8088/upnp_redirect_1_0.xml'.format(local_ip_address))


class RunRedirect(object):
    def __init__(self, args):
        super(RunRedirect, self).__init__()
        self._args = args

    def run(self):
        http_server.start()
        ssdp.run()
