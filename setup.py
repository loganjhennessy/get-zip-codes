from os import path
from setuptools import find_packages, setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="getzipcodes",
    version="0.1.0",
    description="Command line utility to get zip codes for"
                "a given city, state combination.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/loganjhennessy/get-zip-codes",
    author="Logan Hennessy",
    author_email="loganjhennessy@gmail.com",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    entry_points={
        "console_scripts": [
            "getzipcodes=getzipcodes.main:main"
        ]
    }
)
