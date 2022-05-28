import pkg_resources
import shutil
import os
import argparse
import sys
from simple_homepage.homepage_generator import HomepageGenerator

import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler()
    ]
)

class CommandLineInterface:

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Generate a simple homepage',
            usage='''homepage <command> [<args>]

            The available commands:
            init     Initialize the file structure for the homepage
            build    Build the homepage from template files and settings.yaml
            ''')

        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def init(self):
        parser = argparse.ArgumentParser(
            description='Initialize the file structure for the homepage')
        args = parser.parse_args(sys.argv[2:])
        try:
            files_location = pkg_resources.resource_filename(__name__, "files")
            shutil.copytree(files_location, os.getcwd(), dirs_exist_ok=True)
        finally:
            pkg_resources.cleanup_resources()
        logging.info('Template files and settings.yaml created.')


    def build(self):
        parser = argparse.ArgumentParser(
            description='Build the homepage from template files and settings.yaml')
        args = parser.parse_args(sys.argv[2:])
        HomepageGenerator().render()
