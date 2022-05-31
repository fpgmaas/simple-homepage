# simple-homepage

[![Release](https://img.shields.io/github/v/release/fpgmaas/simple-homepage)](https://img.shields.io/github/v/release/fpgmaas/simple-homepage)
[![Build status](https://img.shields.io/github/workflow/status/fpgmaas/simple-homepage/merge-to-main)](https://img.shields.io/github/workflow/status/fpgmaas/simple-homepage/merge-to-main)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://fpgmaas.github.io/simple-homepage/)
[![Code style with black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports with isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)
[![License](https://img.shields.io/github/license/fpgmaas/simple-homepage)](https://img.shields.io/github/license/fpgmaas/simple-homepage)

`simple-homepage` is a command line utility that helps you create a simple static homepage for your browser. The documentation can be found [here](https://fpgmaas.github.io/simple-homepage/).

### Light ([Link to demo](https://fpgmaas.github.io/simple-homepage/demo/light/homepage.html))


<img src="static/screenshot-light.png" alt="Example light homepage" width="500"/>

### Dark ([Link to demo](https://fpgmaas.github.io/simple-homepage/demo/dark/homepage.html))

<img src="static/screenshot-dark.png" alt="Example dark homepage" width="500"/>

## Quick start

To get started, first install the package:

```
pip install simple-homepage
```

Then, navigate to a directory in which you want to create your homepage, and run

```
homepage init
```

or, for the dark version of the homepage:

```
homepage init --dark
```

Then, modify `settings.yaml` to your liking, and run

```
homepage build
```

Your custom homepage is now available under `public/homepage.html`.

## Acknowledgements

Inspiration for this project comes from [this](https://www.reddit.com/r/startpages/comments/hca1dj/simple_light_startpage/) post on Reddit by [/u/akauro](https://www.reddit.com/user/akauro/).

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
