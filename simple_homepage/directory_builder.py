import logging
import os
import shutil

import oyaml
import pkg_resources


class DirectoryBuilder:
    """
    Class to populate the directory with the template files required to build a custom homepage.
    """
    def __init__(self, dark: bool = False):
        self.dark = dark

    def build(self):
        self._copy_files_from_package()
        self._rename_placeholder_images()
        if self.dark:
            self._change_colors_in_settings_to_dark_mode()
        logging.info("Template files and settings.yaml created.")

    def _copy_files_from_package(self):
        """
        Copy the files in the 'files' directory from the package contents to the local client.
        """
        try:
            files_location = pkg_resources.resource_filename(__name__, "files")
            shutil.copytree(files_location, os.getcwd(), dirs_exist_ok=True)
        finally:
            pkg_resources.cleanup_resources()

    def _rename_placeholder_images(self):
        """
        Keep the correct placeholder image based on if dark mode is selected, and remove the other one.
        """
        image_dir = "template/static/images"
        if self.dark:
            os.rename(f"{image_dir}/placeholder_white.png", f"{image_dir}/placeholder.png")
            os.remove(f"{image_dir}/placeholder_black.png")
        else:
            os.rename(f"{image_dir}/placeholder_black.png", f"{image_dir}/placeholder.png")
            os.remove(f"{image_dir}/placeholder_white.png")


    def _change_colors_in_settings_to_dark_mode(self):

        with open("settings.yaml") as f:
            settings = oyaml.safe_load(f)

        settings["colors"]["background"] = "#26263C"
        settings["colors"]["text"] = "#dedeee"
        settings["colors"]["placeholder"] = "#dedeee"
        settings["colors"]["header"] = "white"
        settings["colors"]["accent"] = "orange"

        with open("settings.yaml", "w") as f:
            oyaml.dump(settings, f)
