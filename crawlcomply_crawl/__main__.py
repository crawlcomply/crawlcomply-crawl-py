#!/usr/bin/env python

"""
`__main__` implementation, can be run directly or with `python -m crawlcomply_crawl`
"""
import asyncio
from argparse import ArgumentParser
from os import environ

from crawlcomply_crawl import __description__, __version__
from crawlcomply_crawl.serve import serve


def _build_parser():
    """
    Parser builder

    :return: instanceof ArgumentParser
    :rtype: ```ArgumentParser```
    """
    parser = ArgumentParser(
        prog="python -m crawlcomply_crawl",
        description=__description__,
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {__version__}".format(__version__=__version__),
    )

    subparsers = parser.add_subparsers()
    subparsers.required = True
    subparsers.dest = "command"

    ############
    # CLI exec #
    ############
    exec_parser = subparsers.add_parser(
        "exec",
        help="For testing on the command line",
    )

    exec_parser.add_argument(
        "url",
        help="Crawl from this URL",
        type=str,
    )

    #########
    # Serve #
    #########
    serve_parser = subparsers.add_parser("serve", help="Serve REST API")

    serve_parser.add_argument(
        "--hostname",
        help="Hostname or address to listen on",
        default=environ.get("HOSTNAME", "localhost"),
        dest="host",
        type=str,
    )
    serve_parser.add_argument(
        "--port",
        help="Port to listen on",
        default=int(environ.get("PORT", 4000)),
        type=int,
    )

    return parser


def main(cli_argv=None, return_args=False):
    """
    Run the CLI parser

    :param cli_argv: CLI arguments. If None uses `sys.argv`.
    :type cli_argv: ```Optional[List[str]]```

    :param return_args: Primarily use is for tests. Returns the args rather than executing anything.
    :type return_args: ```bool```

    :return: the args if `return_args`, else None
    :rtype: ```Optional[Namespace]```
    """
    _parser = _build_parser()
    args = _parser.parse_args(args=cli_argv)
    command = args.command
    args_dict = {k: v for k, v in vars(args).items() if k != "command"}
    if return_args:
        return args
    elif command == "exec":
        raise NotImplemented(command)
    elif command == "serve":
        asyncio.run(serve(**args_dict))


if __name__ == "__main__":
    main()

__all__ = ["main"]
