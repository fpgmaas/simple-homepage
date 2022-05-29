import argparse
import logging
import os
import shutil
import sys

import oyaml
import pkg_resources

from simple_homepage.directory_builder import DirectoryBuilder
from simple_homepage.homepage_generator import HomepageGenerator

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])

def cli():
    CommandLineInterface()

class CommandLineInterface:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Generate a simple homepage",
            usage="""homepage <command> [<args>]

            The available commands:
            init     Initialize the file structure for the homepage
            build    Build the homepage from template files and settings.yaml
            """
        )

        parser.add_argument("command", help="Subcommand to run")
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized command")
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def init(self):
        parser = argparse.ArgumentParser(description="Initialize the file structure for the homepage")
        parser.add_argument("--dark", dest="dark", action="store_true", help="Initialize page in dark mode")
        args = parser.parse_args(sys.argv[2:])
        DirectoryBuilder(dark=vars(args)["dark"]).build()

    def build(self):
        parser = argparse.ArgumentParser(description="Build the homepage from template files and settings.yaml")
        args = parser.parse_args(sys.argv[2:])
        HomepageGenerator().build()
