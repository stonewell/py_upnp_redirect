def create_output(output_type, output_args):
    if (output_type == 'chromecast'):
        from .chromecast_output import create_chromecast_output
        return create_chromecast_output(output_args)
    elif output_type == 'local':
        from .local_output import create_local_output
        return create_local_output(output_args)
