import pychromecast
import logging
import time
import datetime
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

    def OnPlay(self, *args, **kwargs):
        logging.debug('OnPlay')
        self._cast.media_controller.play()
        self._cast.media_controller.block_until_active()

    def OnPause(self, *args, **kwargs):
        logging.debug('OnPause')
        self._cast.media_controller.pause()
        self._cast.media_controller.block_until_active()

    def OnStop(self, *args, **kwargs):
        logging.debug('OnStop')
        self._cast.media_controller.stop()
        self._cast.media_controller.block_until_active()
        return 0

    def OnSetMediaURI(self, *args, **kwargs):
        logging.debug('OnSetMediaURI: args={}'.format(args))
        self._cast.play_media(args[0], 'video/mp4')
        self._cast.media_controller.block_until_active()
        return 0

    def OnSeek(self, *args, **kwargs):
        t, unit = args

        if unit == 'REL_TIME':
            st = time.strptime(t, '%H:%M:%S')
            interval = datetime.timedelta(seconds=st.tm_sec,
                                          hours=st.tm_hour,
                                          minutes=st.tm_min)
            self._cast.media_controller.seek(interval.total_seconds())
            self._cast.media_controller.block_until_active()
            return 0

        logging.warning('Not implemented seek:{}'.format(args))
        return 0
