"""Este módulo chequea calidad del codigo."""

import os


def main():
    """chequea funcionalidad"""
    os.makedirs("build")

    with open("build/index.html", 'w', encoding="utf-8") as var:
        var.write("<html><body><h1>mi propio pipeline<h1><body><html>")

    if __name__ == "__main__":
        main()
