#!/usr/bin/env python
# coding: utf-8

"""Application Entryfile, Intance of application"""

from src.app import Cli

app = Cli()

if __name__ == "__main__":
    app.run()
