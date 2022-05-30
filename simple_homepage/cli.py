import argparse
import logging
import sys

from simple_homepage.directory_builder import DirectoryBuilder
from simple_homepage.homepage_generator import HomepageGenerator

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()], format="%(message)s")


def cli() -> None:
    """
    Wrapper so commands do not not return the object.
    """
    CommandLineInterface()


class CommandLineInterface:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(
            description="Generate a simple homepage",
            usage="""homepage <command> [<args>]

            The available commands:
            init     Initialize the file structure for the homepage
            build    Build the homepage from template files and settings.yaml
            """,
        )

        parser.add_argument("command", help="Subcommand to run")
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized command")
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def init(self) -> None:
        parser = argparse.ArgumentParser(description="Initialize the file structure for the homepage")
        parser.add_argument(
            "--dark",
            dest="dark",
            action="store_true",
            help="""Optional. By default the template is initialized in light mode.
            Add this flag to initialize the page in dark mode.""",
        )
        parser.add_argument(
            "--dir",
            dest="dir",
            type=str,
            help="""Optional. Name of a directory (relative to the current directory) to create and place the templates in.
            If not specified, the template files will be placed in the current directory. """,
        )
        parser.add_argument(
            "--overwrite",
            dest="overwrite",
            action="store_true",
            help="""Optional. Ignore errors and overwrite existing files if they are found.""",
        )
        args = parser.parse_args(sys.argv[2:])
        dict_args = vars(args)
        try:
            DirectoryBuilder(
                dark=dict_args["dark"], directory=dict_args["dir"], overwrite=dict_args["overwrite"]
            ).build()
        except (FileExistsError) as e:
            logging.info(e)
            logging.info(
                "Run the command with the `--overwrite` flag to ignore these errors and overwrite existing files."
            )

    def build(self) -> None:
        parser = argparse.ArgumentParser(
            description="Build the homepage from template files and settings.yaml"
        )  # noqa: F841
        HomepageGenerator().build()
