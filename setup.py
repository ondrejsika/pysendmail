#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "pysendmail",
    version = "1.1.0",
    url = 'https://github.com/sikaondrej/pysendmail/',
    license = 'MIT',
    description = "Send email from Python",
    author = 'Ondrej Sika',
    author_email = 'ondrej@ondrejsika.com',
    py_modules = ["libpysendmail"],
    scripts = ["pysendmail"],
    include_package_data = True,
    zip_safe = False,
)
