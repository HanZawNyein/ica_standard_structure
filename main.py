from odooss import (
    create_addons,
    create_docker_compose,
    create_dockerfile,
    create_dockerignore,
    create_gitignore,
    create_precommit_config,
    create_readme,
    create_requirement,
    create_ruff,
    install_precommit,
)

if __name__ == "__main__":
    path = "/home/agga/Documents/odoo-dev/ica_standard_structure/test"
    version = 18.0
    python = 3.10

    # creating docker files
    create_dockerfile(path, odoo_version=version, python=python)
    create_dockerignore(path)
    create_docker_compose(path)

    create_gitignore(path)
    create_requirement(path)
    create_ruff(path)
    create_readme(path)
    create_addons(path)
    create_precommit_config(path)
    install_precommit(path)
