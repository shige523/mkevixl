from setuptools import find_packages, setup

setup(
    name="mkevixl",
    version="1.0.0",
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        "appdirs",
        "click",
        "colorama",
        "et-xmlfile",
        "mypy-extensions",
        "openpyxl",
        "pathspec",
        "regex",
        "toml",
    ],
    entry_points={"console_scripts": ["mkevixl=mkevixl.core:cli"]},
)
