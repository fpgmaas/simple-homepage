import json
import os
import shutil

import yaml
from jinja2 import Environment, FileSystemLoader, Template


class Generator:
    def __init__(
        self, template_dir: str = "template", settings_yaml: "str" = "settings.yaml", output_dir: str = "public"
    ):
        self.env = Environment(loader=FileSystemLoader("template"))
        self.settings_yaml = settings_yaml
        self.output_dir = output_dir

    def render(self):
        self._clear_output_dir_if_exists()
        self._create_output_dir()
        self._copy_static_dir()
        self._render_pages()

    def _clear_output_dir_if_exists(self):
        if os.path.isdir(self.output_dir):
            try:
                shutil.rmtree(self.output_dir)
            except:
                raise ValueError(f"Error encountered while cleaning {self.output_dir} directory.")

    def _create_output_dir(self):
        try:
            os.mkdir(self.output_dir)
        except:
            raise ValueError(f"Encountered an error while trying to create the '{self.output_dir}' directory")

    def copy_static_dir(self):
        try:
            shutil.copytree(f"{self.template_dir}/static", f"{self.output_dir}/static")
        except:
            print("Error copying static files.")

    def _render_pages(self):
        template = self.env.get_template("_homepage.html")
        with open(self.settings_yaml, "rt") as f:
            settings = yaml.safe_load(f.read())
        with open(f"{self.output_dir}/index.html", "w+") as file:
            html = template.render(settings=settings)
            file.write(html)
