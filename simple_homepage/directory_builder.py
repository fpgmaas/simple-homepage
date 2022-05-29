import logging
import os
import shutil

import oyaml
import pkg_resources
from pathlib import Path

class DirectoryBuilder:
    """
    Class to populate the directory with the template files required to build a custom homepage.
    """

    def __init__(self, dark: bool = False, directory: str = None, overwrite: bool = False):
        self.dark = dark
        self.directory = directory
        self.directory_path =  Path(os.getcwd()) / directory if directory else Path(os.getcwd())
        self.overwrite = overwrite

    def build(self):

        if self.directory:
            self._create_directory()
        if not self.overwrite:
            self._verify_that_template_files_dont_exist()
        self._copy_files_from_package()
        self._rename_placeholder_images()
        if self.dark:
            self._change_colors_in_settings_to_dark_mode()

        logging.info("Template files and settings.yaml created.")

    def _create_directory(self):
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        else:
            if not self.overwrite:
                raise OSError(f"A folder '{self.directory}' already exists within the current directory!")

    def _verify_that_template_files_dont_exist(self):
        if os.path.isdir(self.directory_path / 'template') or os.path.isfile(self.directory_path / 'settings.yaml'):
            raise FileExistsError('The directory already contains template files.')

    def _copy_files_from_package(self):
        """
        Copy the files in the 'files' directory from the package contents to the local client.
        """
        try:
            files_location = pkg_resources.resource_filename(__name__, "files")
            shutil.copytree(files_location, str(self.directory_path), dirs_exist_ok=True)
        finally:
            pkg_resources.cleanup_resources()

    def _rename_placeholder_images(self):
        """
        Keep the correct placeholder image based on if dark mode is selected, and remove the other one.
        """
        image_dir_path = self.directory_path / 'template' / 'static' / 'images'
        if self.dark:
            os.rename(image_dir_path / 'placeholder_white.png', image_dir_path / 'placeholder.png')
            os.remove(image_dir_path / "placeholder_black.png")
        else:
            os.rename(image_dir_path / 'placeholder_black.png', image_dir_path / 'placeholder.png')
            os.remove(image_dir_path / "placeholder_white.png")

    def _change_colors_in_settings_to_dark_mode(self):

        with open(self.directory_path / "settings.yaml") as f:
            settings = oyaml.safe_load(f)

        settings["colors"]["background"] = "#26263C"
        settings["colors"]["text"] = "#dedeee"
        settings["colors"]["placeholder"] = "#dedeee"
        settings["colors"]["header"] = "white"
        settings["colors"]["accent"] = "orange"

        with open(self.directory_path / "settings.yaml", "w") as f:
            oyaml.dump(settings, f)
