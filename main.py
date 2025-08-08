from iss import (
    create_docker_compose,
    create_dockerfile,
    create_dockeriginore,
    create_gitignore,
    create_readme,create_addons,
    create_requreiment,
    create_ruff,
)

if __name__ == "__main__":
    path = "/home/agga/Documents/odoo-dev/ica_standard_structure/test"
    version = 18.0
    python = 3.10

    # creating docker files
    create_dockerfile(path, version=version, python=python)
    create_dockeriginore(path)
    create_docker_compose(path)

    create_gitignore(path)
    create_requreiment(path)
    create_ruff(path)
    create_readme(path)
    create_addons(path)
