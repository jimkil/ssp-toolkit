"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import click
import yaml

from tools.helpers.helpers import get_project_path, load_yaml_files


class Config:
    config: dict
    keys: dict
    config_files: list[tuple[str, str]] = []
    default_keys: dict = {
        "artifacts.yaml": "artifact",
        "config-management.yaml": "cm",
        "info_system.yaml": "information_system",
        "justifications.yaml": "justify",
    }

    def __init__(self):
        self.project_path = get_project_path()
        if self.project_path.joinpath("configuration.yaml").exists():
            self.config = load_yaml_files(
                self.project_path.joinpath("configuration.yaml")
            )
        else:
            raise FileNotFoundError("configuration.yaml not found in project root.")
        self.load_keys()

    def load_keys(self):
        for filename in self.project_path.joinpath("keys").glob("*.yaml"):
            key = self.default_keys.get(filename.name, filename.stem)
            self.config_files.append((filename.name, key))
            self.config[key] = load_yaml_files(file_path=filename)

    def check_config_values(self, file: str, key: str = "") -> str | dict:
        if key:
            values = self.config.get(file, {}).get(key, "")
        else:
            values = self.config.get(file, {})
        return values


@click.group()
@click.pass_context
def check_config(ctx):
    ctx.obj = Config()


@check_config.command()
@click.option(
    "--file",
    "-f",
    required=True,
)
@click.option(
    "--key",
    "-k",
    required=False,
    help="The name of the configuration key whose value should be shown.",
)
@click.pass_context
def get_value(ctx, file: str, key: str = ""):
    config = ctx.obj
    if key:
        click.echo(config.check_config_values(file, key))
    else:
        click.echo(yaml.dump(config.check_config_values(file), indent=4, width=80))


@check_config.command()
@click.pass_context
def list_files(ctx):
    """List all the files loaded from the keys directory"""
    config = ctx.obj
    click.echo("Key files and configuration keys:")
    click.echo("---------------------------------")
    for files in config.config_files:
        click.echo(f"{files[0]} using alias {files[1]}")


if __name__ == "__main__":
    check_config()
