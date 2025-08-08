from iss.utils import write_file


def create_requreiment(path: str):
    content = """"""
    write_file(path, content, filename="requirements.txt")


if __name__ == "__main__":
    path = "/home/agga/Documents/odoo-dev/ica_standard_structure/test"
    version = 18.0
    python = 3.10
    create_requreiment(path)
