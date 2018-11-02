import logging
import media_renderer

class MediaRendererDelegateImpl(media_renderer.MediaRendererDelegate):
    def __init__(self, output):
        media_renderer.MediaRendererDelegate.__init__(self)
        self._output = output

    def OnGetCurrentConnectionInfo(self, uri, data):
        logging.debug('OnGetCurrentConnectionInfo: uri={}, data={}'.format(uri, data))
        return 0

    def OnNext(self, uri, data):
        logging.debug('OnNext: uri={}, data={}'.format(uri, data))
        self._output.OnNext(uri, data)
        return 0

    def OnPause(self, uri, data):
        logging.debug('OnPause: uri={}, data={}'.format(uri, data))
        self._output.OnPause(uri, data)
        return 0

    def OnPlay(self, uri, data):
        logging.debug('OnPlay: uri={}, data={}'.format(uri, data))
        self._output.OnPlay(uri, data)
        return 0

    def OnPrevious(self, uri, data):
        logging.debug('OnPrevious: uri={}, data={}'.format(uri, data))
        self._output.OnPrevious(uri, data)
        return 0

    def OnSeek(self, uri, data):
        logging.debug('OnSeek: uri={}, data={}'.format(uri, data))
        self._output.OnSeek(uri, data)
        return 0

    def OnStop(self, uri, data):
        logging.debug('OnStop: uri={}, data={}'.format(uri, data))
        self._output.OnStop(uri, data)
        return 0

    def OnSetAVTransportURI(self, uri, data):
        logging.debug('OnSetAVTransportURI: uri={}, data={}'.format(uri, data))
        self._output.OnSetMediaURI(uri, data)
        return 0

    def OnSetPlayMode(self, uri, data):
        logging.debug('OnSetPlayMode: uri={}, data={}'.format(uri, data))
        self._output.OnSetPlayMode(uri, data)
        return 0

    def OnSetVolume(self, uri, data):
        logging.debug('OnSetVolume: uri={}, data={}'.format(uri, data))
        self._output.OnSetVolume(uri, data)
        return 0

    def OnSetVolumeDB(self, uri, data):
        logging.debug('OnSetVolumeDB: uri={}, data={}'.format(uri, data))
        self._output.OnSetVolumeDB(uri, data)
        return 0

    def OnGetVolumeDBRange(self, uri, data):
        logging.debug('OnGetVolumeDBRange: uri={}, data={}'.format(uri, data))
        self._output.OnGetVolumeDBRange(uri, data)
        return 0

    def OnSetMute(self, uri, data):
        logging.debug('OnSetMute: uri={}, data={}'.format(uri, data))
        self._output.OnSetMute(uri, data)
        return 0
