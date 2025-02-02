from setuptools import setup, find_packages

setup(
    name="ci_cd_project",
    version="0.1.0",
    packages=find_packages(where="src"),  # <-- on indique que les sources sont dans src/
    package_dir={"": "src"}
)
