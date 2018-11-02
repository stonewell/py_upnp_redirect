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
