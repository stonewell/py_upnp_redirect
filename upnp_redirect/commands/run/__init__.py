import uuid
import logging
import media_renderer
import threading
import socket

from .media_renderer_delegate import MediaRendererDelegateImpl
from upnp_redirect.output import create_output


class RunRedirect(object):
    def __init__(self, args):
        super(RunRedirect, self).__init__()
        self._args = args
        self._device_uuid = uuid.uuid4()
        self._output = create_output(self._args.output_type, self._args.output_args)

        if not self._output:
            raise Exception('Invalid Output:{} with argument {}'.format(self._args.output_type, self._args.output_args))

        self._media_renderer = media_renderer.create_media_renderer(MediaRendererDelegateImpl(self._output).__disown__(),
                                                                    'Upnp Redirector (%s)' % socket.gethostname(),
                                                                    False,
                                                                    str(uuid),
                                                                    0,
                                                                    True)

    def run(self):
        self._media_renderer.Start()

        event_exit = threading.Event()

        while(event_exit.wait(timeout=10)):
            pass

        self._media_renderer.Stop()
