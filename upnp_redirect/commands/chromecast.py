import pychromecast
import logging


class Chromecast(object):
    def __init__(self, args):
        super(Chromecast, self).__init__()
        self._args = args

    def run(self):
        logging.info('run chromecast command:%s' % self._args.chromecast_cmd)

        chromecasts, _ = pychromecast.get_chromecasts()
        for cc in chromecasts:
            if self._args.chromecast_cmd == 'list':
                print(cc.device)
            elif self._args.chromecast_cmd == 'status':
                print(cc.device, cc.status)
