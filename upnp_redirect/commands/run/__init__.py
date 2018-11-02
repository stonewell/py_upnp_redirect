import uuid
import logging
import media_renderer


class RunRedirect(object):
    def __init__(self, args):
        super(RunRedirect, self).__init__()
        self._args = args
        self._device_uuid = uuid.uuid4()
        self._media_renderer = media_renderer.create_media_renderer(None,
                                                                  'Upnp Redirector',
                                                                  False,
                                                                  str(uuid),
                                                                  0,
                                                                  True)

    def run(self):
        self._media_renderer.Start()

        import sys
        while True:
            c = sys.stdin.read(1)
            if c == 'q':
                break
