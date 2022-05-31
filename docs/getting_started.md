# Getting Started

To get started, first install the package:

```
pip install homepage
```

## 1. Creating the template 

Navigate to a directory in which you want to create your homepage, and run

```
homepage init
```

or, for the dark version of the homepage:

```
homepage init --dark
```

This creates the necessary template files to generate your custom homepage. 

## 2. Modifying the template 

To personalize the homepage, open `settings.yaml` and modify it to your liking. The number of sections under `urls` is three by default, but you can add or remove sections simply by adding new entries to the list.

Next to that, you can add your own images to the `template/static/images` directory, and optionally remove `placeholder.png`. When there are multiple images in this directory, the homepage will randomly display one of them each time the page is openend or refreshed.

## 3. Building the homepage

```
homepage build
```

Your custom homepage is now available under `public/homepage.html`. 

## 3. Setting the HTML file as your homepage

Finally, to use the page as your homepage, modify your browser to open the `HTML` file whenever you open a new tab. The simplest way to get the path to the file is by opening the file in a browser with `open public/homepage.html`. Some browsers require extensions to modify the new-tab page. For example, for Chrome one could use [New Tab Redirect](https://chrome.google.com/webstore/detail/new-tab-redirect/icpgjfneehieebagbmdbhnlpiopdcmna) or for Mozilla one could use [New Tab Override](https://addons.mozilla.org/en-US/firefox/addon/new-tab-override/).