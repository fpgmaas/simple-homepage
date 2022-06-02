# Commands

## `homepage init`

This creates the following directory structure with template files:

```
.
├── settings.yaml
└── template
    ├── _homepage.html
    └── static
        ├── _stylesheet.css
        ├── favicon.svg
        ├── homepage.js
        └── images
            └── placeholder.png
```

### Arguments

- `--dark`: Optional. Initialize the template files for the dark version of the homepage. This modifies the default colors in `settings.yaml` and 
change the `placeholder.png` from black to white.
- `--dir <DIR>`: Optional. Name of a directory (relative to the current directory) to create and place the templates in.
If not specified, the template files will be placed in the current directory.
- `--overwrite`: Optional. Ignore errors and overwrite existing files if they are found.

## `homepage build`

Build the custom homepage from template files and write the output to a directory named `public`, so the resulting homepage is found in `public/homepage.html` This command should be run within the directory that contains the template files created with `homepage init`.

### Arguments

- `--output-dir <DIR>`: Optional. Name of a directory (relative to the current directory) to create and place the resulting page in. Defaults to `public`
- `--output-file <FILE>`: Optional. Name of the resulting html file. Defaults to homepage.html.