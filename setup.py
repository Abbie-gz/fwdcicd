from setuptools import find_packages, setup
from fwdcicd import __version__

setup(
    name="fwdcicd",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="FWD cicd test sample",
    author="Bob",
)
