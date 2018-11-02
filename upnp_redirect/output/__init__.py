import logging


class OutputBase(object):
    def OnNext(self, *args, **kwargs):
        logging.warning('Not implemented, OnNext: args={}, kwargs={}'.format(*args, **kwargs))
        return 0

    def OnPause(self, *args, **kwargs):
        logging.warning('Not implemented, OnPause: args={}, kwargs={}'.format(*args, **kwargs))
        return 0

    def OnPlay(self, *args, **kwargs):
        logging.warning('Not implemented, OnPlay: args={}, kwargs={}'.format(*args, **kwargs))
        return 0

    def OnPrevious(self, *args, **kwargs):
        logging.warning('Not implemented, OnPrevious: args={}, kwargs={}'.format(*args, **kwargs))
        return 0

    def OnSeek(self, *args, **kwargs):
        logging.warning('Not implemented, OnSeek: args={}, kwargs={}'.format(*args, **kwargs))
        return 0

    def OnStop(self, *args, **kwargs):
        logging.warning('Not implemented, OnStop: args={}, kwargs={}'.format(*args, **kwargs))
        return 0

    def OnSetMediaURI(self, *args, **kwargs):
        logging.warning('Not implemented, OnSetMediaURI: args={}, kwargs={}'.format(*args, **kwargs))
        return 0

    def OnSetPlayMode(self, *args, **kwargs):
        logging.warning('Not implemented, OnSetPlayMode: args={}, kwargs={}'.format(*args, **kwargs))
        return 0

    def OnSetVolume(self, *args, **kwargs):
        logging.warning('Not implemented, OnSetVolume: args={}, kwargs={}'.format(*args, **kwargs))
        return 0

    def OnSetVolumeDB(self, *args, **kwargs):
        logging.warning('Not implemented, OnSetVolumeDB: args={}, kwargs={}'.format(*args, **kwargs))
        return 0

    def OnGetVolumeDBRange(self, *args, **kwargs):
        logging.warning('Not implemented, OnGetVolumeDBRange: args={}, kwargs={}'.format(*args, **kwargs))
        return 0

    def OnSetMute(self, *args, **kwargs):
        logging.warning('Not implemented, OnSetMute: args={}, kwargs={}'.format(*args, **kwargs))
        return 0


def create_output(output_type, output_args):
    if (output_type == 'chromecast'):
        from .chromecast_output import create_chromecast_output
        return create_chromecast_output(output_args)
    elif output_type == 'local':
        from .local_output import create_local_output
        return create_local_output(output_args)
