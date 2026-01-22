"""
Copyright 2019-2024 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import shutil
from datetime import datetime
from pathlib import Path

import click
from dotenv import set_key
from loguru import logger

from tools.helpers.helpers import load_yaml_files, write_files, write_yaml_files
from tools.logging_config import setup_logging  # noqa: F401


def create_project_dir(project_name: str, projects_directory: str) -> Path:
    """
    Create a new project directory with the given name.

    :param project_name: the name of the project
    :param projects_directory: the base directory to create the project in
    :return:
    """
    project_path = Path(projects_directory) / project_name.replace(" ", "_").lower()
    try:
        project_path.mkdir(parents=True, exist_ok=False)
        click.echo(f"Project '{project_name}' created at {project_path.resolve()}")
        logger.info(f"Project '{project_name}' created at {project_path.resolve()}")
    except FileExistsError:
        click.echo(
            f"Error: Project '{project_name}' already exists at {project_path.resolve()}"
        )
        logger.error(
            f"Project '{project_name}' already exists at {project_path.resolve()}"
        )

    set_key(Path.cwd() / ".env", "PROJECT_PATH", str(project_path.resolve()))
    return project_path


def add_readme(project_directory: Path) -> None:
    """
    Add initial files to the project directory.

    :param project_directory: the project directory path
    """
    readme_path = project_directory / "README.md"
    now = datetime.now()
    content = (
        f"# {project_directory.name}\n\nProject created: {now.isoformat(sep=" ")}\n"
    )
    write_files(file_path=readme_path, content=content)


def copy_directories(project_directory: Path) -> None:
    """
    Copy all directories from the project_files directory into the project directory.

    :param project_directory: the project directory path
    """
    project_files_dir = Path(__file__).parent.parent.parent / "project_files"
    if not project_files_dir.exists() or not project_files_dir.is_dir():
        click.echo(
            f"project_files directory not found at {project_files_dir.resolve()}"
        )
        logger.error(
            f"project_files directory not found at {project_files_dir.resolve()}"
        )
        return

    for item in project_files_dir.iterdir():
        if item.is_dir():
            dest_dir = project_directory / item.name
            try:
                shutil.copytree(item, dest_dir, dirs_exist_ok=True)
                click.echo(f"Copied directory '{item.name}' to {dest_dir.resolve()}")
                logger.info(f"Copied directory '{item.name}' to {dest_dir.resolve()}")
            except FileExistsError as fee:
                click.echo(f"Error copying '{item.name}': {fee}")
                logger.error(f"Error copying '{item.name}': {fee}")
            except shutil.Error as err:
                click.echo(f"Error copying '{item.name}': {err}")
                logger.error(f"Error copying '{item.name}': {err}")


def create_opencontrol_file(project_name: str, project_directory: Path) -> None:
    """
    Create a prepopulated opencontrol.yaml file in the project directory.

    :param project_name: the name of the project
    :param project_directory: the directory path
    """
    opencontrol_path = (
        Path(__file__).parent.parent.parent / "project_files" / "opencontrol.yaml"
    )
    oc_file = load_yaml_files(file_path=opencontrol_path)
    oc_file["name"] = project_name
    write_yaml_files(file_path=project_directory / "opencontrol.yaml", content=oc_file)

    click.echo(f"Created opencontrol.yaml in {project_directory.resolve()}")
    logger.info(f"Created opencontrol.yaml in {project_directory.resolve()}")


def copy_config(project_directory: Path) -> None:
    copy_config_file = (
        Path(__file__).parent.parent.parent / "project_files" / "configuration.yaml"
    )
    try:
        shutil.copy2(copy_config_file, project_directory / "configuration.yaml")
        click.echo(
            f"Copied directory '{copy_config_file.name}' to {project_directory.resolve()}"
        )
        logger.info(
            f"Copied directory '{copy_config_file.name}' to {project_directory.resolve()}"
        )
    except FileExistsError as fee:
        click.echo(f"Error copying '{copy_config_file.name}': {fee}")
        logger.error(f"Error copying '{copy_config_file.name}': {fee}")
    except shutil.Error as err:
        click.echo(f"Error copying '{copy_config_file.name}': {err}")
        logger.error(f"Error copying '{copy_config_file.name}': {err}")


@click.command("create-project")
@click.option(
    "--name",
    "-n",
    "project_name",
    required=True,
    help="Name of the new project",
)
@click.option(
    "--directory",
    "-d",
    "projects_directory",
    required=True,
    default=".",
    help="Directory to create the new project in (default: current directory)",
)
def create_project_cmd(project_name: str, projects_directory: str) -> None:
    """
    Create a new project directory with the given name.
    """
    project_dir = create_project_dir(
        project_name=project_name, projects_directory=projects_directory
    )
    add_readme(project_directory=project_dir)
    copy_directories(project_directory=project_dir)
    create_opencontrol_file(project_name=project_name, project_directory=project_dir)
    copy_config(project_directory=project_dir)
