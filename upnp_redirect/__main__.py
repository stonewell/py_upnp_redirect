import os
import argparse

from .output import chromecast, run


def arguments():
    parser = argparse.ArgumentParser(prog='upnp_redirect',
                                     description='upnp request receiver which redirect request to variant output')

    sub_parsers = parser.add_subparsers(dest='command')
    sub_parsers.required = True

    chromecast_parser = sub_parsers.add_parser('chromecast', help='chromecast related commands')
    chromecast_parser.add_argument(dest='chromecast_cmd', choices=['list', 'status'])

    run_parser = sub_parsers.add_parser('run', help='run the upnp redirector')
    run_parser.add_argument('--output_type', choices=['chromecast', 'local'], default='chromecast', help='redirect output type, default: chromecast')
    run_parser.add_argument('--output_args', type=str, required=True)

    return parser

if __name__ == '__main__':
    args = arguments().parse_args()

    if args.command == 'chromecast':
        chromecast.Chromecast(args).run()
    elif args.command == 'run':
        run.RunRedirect(args).run()
