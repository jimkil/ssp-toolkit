# create-files

***Commands are run within the SSP Toolkit root directory.***

The `create-files` command is used to generate files from the templates. The command takes
one optional argument, which is the name of the template, or directory of templates, to
render. If no argument is provided, all templates in the templates directory will be rendered.
The templates are rendered to the `/rendered` directory and maintain the same directory structure
as the templates. So, if a template is located in `/templates/appendices/`, the rendered file will
be written to `/rendered/appendices/`.

## Usage

```bash
uv run cli create-files --templates templates/appendices/
```

```bash
Usage: cli create-files [OPTIONS]

Options:
  -t, --templates DIRECTORY  Template directory
  --help                     Show this message and exit.
```
