from setuptools import setup, find_packages
from typing import List


__version__ = "0.0.1"
REPO_NAME = "SQL_Connect"
PKG_NAME= "load_MySQL"
AUTHOR_USER_NAME = "meetpanchal58"
AUTHOR_EMAIL = "meetpanchal0580@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with sql database and performing its essential operations.",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    
    
)