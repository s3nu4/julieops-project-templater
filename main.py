import os
import re
import sys

from jinja2 import Environment, FileSystemLoader

PREFIX = ""
PREFIX_PATTERN = "(\w*\.)"
PRINCIPAL = ""


def get_principal():
    global PRINCIPAL
    try:
        PRINCIPAL = sys.argv[2]
    except IndexError:
        print("Argument PRINCIPAL not set")
        sys.exit(1)


def get_prefix():
    global PREFIX
    try:
        PREFIX = sys.argv[1]
        if re.search(PREFIX_PATTERN, PREFIX) is None:
            print("The PREFIX is not valid")
            sys.exit(1)
    except IndexError:
        print("Argument PRINCIPAL not set")
        sys.exit(1)


def create_directories_recursive():
    try:
        os.makedirs("/".join(PREFIX.split(".")[:]))
    except FileExistsError:
        print("Directory already exists")


def create_files():
    create_template_file(**{"filename": "ClientConfig", "prefix": PREFIX, "cn": PRINCIPAL})
    create_template_file(**{"filename": "topology.yml", "prefix": PREFIX, "principal": PRINCIPAL})


def create_topology_file():
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("topology.yml")
    content = template.render(prefix=PREFIX, principal=PRINCIPAL)
    if os.path.exists("{}/topology.yml".format("/".join(PREFIX.split(".")[:]))):
        print("File already exists")
    else:
        with open("{}/topology.yml".format("/".join(PREFIX.split(".")[:])), mode="w",
                  encoding="utf-8") as client_config:
            client_config.write(content)
        print("File created!")


def create_template_file(**kwargs):
    filename = kwargs.get("filename")
    environment = Environment(loader=FileSystemLoader("../../templates/"))
    template = environment.get_template(filename)
    content = template.render(**kwargs)
    if os.path.exists("{}/{}".format("/".join(PREFIX.split(".")[:]), filename)):
        print("File already exists")
    else:
        with open("{}/{}".format("/".join(PREFIX.split(".")[:]), filename), mode="w",
                  encoding="utf-8") as client_config:
            client_config.write(content)
        print("File created!")


def bootstrap():
    get_prefix()
    get_principal()
    create_directories_recursive()
    create_files()


if __name__ == "__main__":
    bootstrap()
