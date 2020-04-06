from setuptools import find_packages, setup

setup(
    name="classroom",
    packages=find_packages("src"),
    package_dir={"": "src"},
)
