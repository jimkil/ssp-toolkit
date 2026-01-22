"""
Copyright 2019-2024 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import click
from loguru import logger

from tools.create_files import create_files_cmd
from tools.create_project import create_project_cmd
from tools.load_project import load_project_cmd
from tools.logging_config import setup_logging
from tools.make_families import make_families_cmd

setup_logging()


@click.group()
def cli():
    logger.info("CLI started")
    pass


cli.add_command(create_project_cmd)
cli.add_command(load_project_cmd)
cli.add_command(create_files_cmd)
cli.add_command(make_families_cmd)


if __name__ == "__main__":
    cli()
