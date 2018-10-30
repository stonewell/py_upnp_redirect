import pychromecast


class Chromecast(object):
    def __init__(self, args):
        super(Chromecast, self).__init__()
        self._args = args

    def run(self):
        chromecasts = pychromecast.get_chromecasts()
        for cc in chromecasts:
            if self._args.chromecast_cmd == 'list':
                print(cc.device)
            elif self._args.chromecast_cmd == 'status':
                print(cc.device, cc.status)
