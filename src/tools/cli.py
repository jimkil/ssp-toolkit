"""
Copyright 2019-2024 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import click
from loguru import logger

from tools.create_project import create_project_cmd
from tools.logging_config import setup_logging

setup_logging()


@click.group()
def cli():
    logger.info("CLI started")
    pass


cli.add_command(create_project_cmd)

if __name__ == "__main__":
    cli()
