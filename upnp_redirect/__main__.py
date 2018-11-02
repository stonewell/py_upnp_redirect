import os
import argparse
import logging
import daemon

logging.getLogger('').setLevel(logging.INFO)

from .commands import chromecast, run


def arguments():
    parser = argparse.ArgumentParser(prog='upnp_redirect',
                                     description='upnp request receiver which redirect request to variant output')

    parser.add_argument('--daemon', action='store_true', help='run application in daemon mode', default=False, required=False)
    parser.add_argument('--verbose', action='store_true', help='show verbose debug messages', default=False, required=False)

    sub_parsers = parser.add_subparsers(dest='command')
    sub_parsers.required = True

    chromecast_parser = sub_parsers.add_parser('chromecast', help='chromecast related commands')
    chromecast_parser.add_argument(dest='chromecast_cmd', choices=['list', 'status'])
    chromecast_parser.set_defaults(func=lambda args:chromecast.Chromecast(args).run())

    run_parser = sub_parsers.add_parser('run', help='run the upnp redirector')
    run_parser.add_argument('--output_type', choices=['chromecast', 'local'], default='chromecast', help='redirect output type, default: chromecast')
    run_parser.add_argument('--output_args', type=str, required=True)
    run_parser.set_defaults(func=lambda args:run.RunRedirect(args).run())

    return parser

if __name__ == '__main__':
    args = arguments().parse_args()

    if (args.verbose):
        logging.getLogger('').setLevel(logging.DEBUG)

    if not args.daemon:
        args.func(args)
    else:
        with daemon.DaemonContext():
            args.func(args)
