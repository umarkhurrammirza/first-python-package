from setuptools import setup, find_packages


def load_requirements(file):
    with open(file, "r") as f:
        requirements = f.read().split("\n")
    return requirements


setup(
    name="divide",
    version="0.1",
    packages=find_packages(),
    description="A python package to divide two numbers",
    author="Umar Mirza",
    author_email="umarkhrum11@gmail.com",
    url="https://github.com/umarkhurrammirza/first-python-package",
    install_requires=load_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["division=division.divide:divide"],
    },
)
