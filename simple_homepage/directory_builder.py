import oyaml
import os
import shutil
import pkg_resources
import logging

class DirectoryBuilder:

    def __init__(self, dark: bool = False):
        self.dark = dark

    def build(self):
        self._copy_files_from_package()
        self._rename_placeholder_images()
        if self.dark:
            self._change_colors_in_settings()
        logging.info('Template files and settings.yaml created.')

    def _copy_files_from_package(self):
        try:
            files_location = pkg_resources.resource_filename(__name__, "files")
            shutil.copytree(files_location, os.getcwd(), dirs_exist_ok=True)
        finally:
            pkg_resources.cleanup_resources()

    def _rename_placeholder_images(self):
        image_dir = 'template/static/images'
        if self.dark:
            os.rename(f'{image_dir}/placeholder_white.png', f'{image_dir}/placeholder.png')
            os.rename(f'{image_dir}/placeholder_black.png', f'{image_dir}/placeholder_alt.png')
        else:
            os.rename(f'{image_dir}/placeholder_black.png', f'{image_dir}/placeholder.png')
            os.rename(f'{image_dir}/placeholder_white.png', f'{image_dir}/placeholder_alt.png')

    def _change_colors_in_settings(self):
        with open('settings.yaml') as f:
            settings = oyaml.safe_load(f)
        settings['colors']['background'] = "#26263C" 
        settings['colors']['text'] = "#dedeee" 
        settings['colors']['placeholder'] = "#dedeee" 
        settings['colors']['header'] = "white" 
        settings['colors']['accent'] = "orange"
        with open('settings.yaml', 'w') as f:
            oyaml.dump(settings, f)
