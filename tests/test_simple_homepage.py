import os
import shlex
import subprocess
from contextlib import contextmanager


@contextmanager
def run_within_dir(path: str):
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


def file_contains_text(file: str, text: str) -> bool:
    return open(file, "r").read().find(text) != -1


def test_init_command(tmp_path):
    with run_within_dir(tmp_path):

        subprocess.check_call(shlex.split("homepage init")) == 0
        expected_files = [
            "settings.yaml",
            "template/_homepage.html",
            "template/static/_stylesheet.css",
            "template/static/homepage.js",
            "template/static/images/placeholder.png",
        ]
        for file in expected_files:
            assert os.path.isfile(file)


def test_init_command_within_dir(tmp_path):
    with run_within_dir(tmp_path):
        subprocess.check_call(shlex.split("homepage init --dir test-dir")) == 0
        expected_files = [
            "test-dir/settings.yaml",
            "test-dir/template/_homepage.html",
            "test-dir/template/static/_stylesheet.css",
            "test-dir/template/static/homepage.js",
            "test-dir/template/static/images/placeholder.png",
        ]
        for file in expected_files:
            assert os.path.isfile(file)


def test_init_command_dark_mode(tmp_path):
    with run_within_dir(tmp_path):
        subprocess.check_call(shlex.split("homepage init --dark")) == 0
        assert file_contains_text("settings.yaml", "#26263C")


def test_build_command(tmp_path):
    with run_within_dir(tmp_path):
        subprocess.check_call(shlex.split("homepage init")) == 0
        subprocess.check_call(shlex.split("homepage build")) == 0
        expected_files = [
            "settings.yaml",
            "public/index.html",
            "public/static/stylesheet.css",
            "public/static/homepage.js",
            "public/static/images/placeholder.png",
        ]
        for file in expected_files:
            assert os.path.isfile(file)


def test_build_command_arguments(tmp_path):
    with run_within_dir(tmp_path):
        subprocess.check_call(shlex.split("homepage init")) == 0
        subprocess.check_call(shlex.split("homepage build --output-dir test --output-file test.html")) == 0
        expected_files = [
            "settings.yaml",
            "test/test.html",
            "test/static/stylesheet.css",
            "test/static/homepage.js",
            "test/static/images/placeholder.png",
        ]
        for file in expected_files:
            assert os.path.isfile(file)
