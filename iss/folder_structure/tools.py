from iss.utils import write_file


def create_necessary_files(path: str):
    write_file(path, "", filename="addons/README.md")


if __name__ == "__main__":
    path = "/home/agga/Documents/odoo-dev/ica_standard_structure/test"
    version = 18.0
    python = 3.10
    create_necessary_files(path)
