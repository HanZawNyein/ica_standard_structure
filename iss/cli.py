import click

from .folder_structure import (
    create_addons,
    create_docker_compose,
    create_dockerfile,
    create_dockerignore,
    create_gitignore,
    create_readme,
    create_requirement,
    create_ruff,
)


@click.group()
def cli():
    pass


@cli.command()
@click.argument("path", type=click.Path())
@click.option("--odoo_version", default="18.0", help="Odoo version to use (e.g. 18.0)")
@click.option("--python", default="3.10", help="Python version to use (e.g. 3.10)")
def create(path, odoo_version, python):
    """Create the Odoo standard folder structure at PATH."""
    create_dockerfile(path, odoo_version=odoo_version, python=python)
    create_dockerignore(path)
    create_docker_compose(path)

    create_gitignore(path)
    create_requirement(path)
    create_ruff(path)
    create_readme(path)
    create_addons(path)


if __name__ == "__main__":
    cli()
