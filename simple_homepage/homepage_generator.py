import logging
import os
import shutil

import yaml  # type: ignore
from jinja2 import Environment, FileSystemLoader


class HomepageGenerator:
    """
    Class to generate a custom homepage from template files. The template files can be created
    with the `DirectoryBuilder` class.
    """

    def __init__(
        self, template_dir: str = "template", settings_yaml: "str" = "settings.yaml", output_dir: str = "public"
    ) -> None:
        self.settings_yaml = settings_yaml
        self.output_dir = output_dir
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def build(self) -> None:
        self._verify_required_files_exist()
        self._clear_output_dir_if_exists()
        self._create_output_dir()
        self._copy_static_dir()
        self._render_page()
        self._add_images_list_to_js()
        logging.info(f"Page built. The resulting homepage can be found at {self.output_dir}/homepage.html")

    def _verify_required_files_exist(self) -> None:
        expected_files = [
            self.settings_yaml,
            f"{self.template_dir}/_homepage.html",
            f"{self.template_dir}/static/_stylesheet.css",
            f"{self.template_dir}/static/homepage.js",
        ]
        files_found = [os.path.exists(file) for file in expected_files]
        if not all(files_found):
            raise ValueError(
                "Not all required template files were found! Did you initialize the directory with `homepage init` first?"
            )

    def _clear_output_dir_if_exists(self) -> None:
        if os.path.isdir(self.output_dir):
            try:
                shutil.rmtree(self.output_dir)
            except Exception as e:
                logging.info(e)
                raise ValueError(f"Error encountered while cleaning {self.output_dir} directory.")

    def _create_output_dir(self) -> None:
        try:
            os.mkdir(self.output_dir)
        except Exception as e:
            logging.info(e)
            raise ValueError(f"Encountered an error while trying to create the '{self.output_dir}' directory")

    def _copy_static_dir(self) -> None:
        try:
            shutil.copytree(f"{self.template_dir}/static", f"{self.output_dir}/static")
        except Exception as e:
            logging.info(e)
            raise ValueError("Encountered an error while copying static files.")

    def _render_page(self) -> None:

        with open(self.settings_yaml, "rt") as f:
            settings = yaml.safe_load(f.read())

        template = self.env.get_template("_homepage.html")
        with open(f"{self.output_dir}/homepage.html", "w+") as file:
            html = template.render(settings=settings)
            file.write(html)

        template = self.env.get_template("static/_stylesheet.css")
        with open(f"{self.output_dir}/static/stylesheet.css", "w+") as file:
            html = template.render(settings=settings)
            file.write(html)

    def _add_images_list_to_js(self) -> None:
        """
        Scan for any images and add this as a list to the homepage.js files, so JavaScript can randomly pick
        one to display when the page is opened.
        """
        images = [f'"static/images/{image}"' for image in os.listdir("public/static/images")]

        with open("public/static/homepage.js", "r+") as f:
            content = f.read()
            f.seek(0, 0)
            line = f'var images = new Array({",".join(images)});'
            f.write(line.rstrip("\r\n") + "\n" + content)
