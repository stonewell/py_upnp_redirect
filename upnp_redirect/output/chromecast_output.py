import pychromecast
import logging

from . import OutputBase


def create_chromecast_output(output_args):
    chromecasts = pychromecast.get_chromecasts()
    cast = next(cc for cc in chromecasts if cc.device.friendly_name == output_args)

    if not cast:
        return None

    cast.wait()
    return ChromecastOutput(cast)

class ChromecastOutput(OutputBase):
    def __init__(self, cast):
        super(ChromecastOutput, self).__init__()
        self._cast = cast
        self._mc = cast.media_controller

    def OnPlay(self, *args, **kwargs):
        logging.debug('OnPlay')
        self._mc.play()

    def OnPause(self, *args, **kwargs):
        logging.debug('OnPause')
        self._mc.pause()

    def OnStop(self, *args, **kwargs):
        logging.debug('OnStop')
        self._mc.stop()
        return 0

    def OnSetMediaURI(self, *args, **kwargs):
        logging.debug('OnSetMediaURI: args={}'.format(args))
        self._mc.play_media(args[0], 'video/mp4')
        self._mc.block_until_active()
        return 0
