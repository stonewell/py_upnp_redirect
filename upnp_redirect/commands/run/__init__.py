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

        self._delegate = MediaRendererDelegateImpl(self._output).__disown__()
        self._media_renderer = media_renderer.create_media_renderer(self._delegate,
                                                                    'Upnp Redirector (%s)' % socket.gethostname(),
                                                                    False,
                                                                    str(self._device_uuid),
                                                                    0,
                                                                    True)

    def run(self):
        self._media_renderer.Start()

        event_exit = threading.Event()

        logging.info('media render:{} started!'.format('Upnp Redirector (%s)' % socket.gethostname()))
        logging.debug('wait exit event...')

        while True:
            try:
                event_exit.wait(timeout=10)
            except KeyboardInterrupt:
                logging.exception('event exit')
                break
            except:
                pass

        logging.debug('stop media renderer')
        self._media_renderer.Stop()
