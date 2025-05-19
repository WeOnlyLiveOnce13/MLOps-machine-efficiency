from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="machines_efficiency_mlops",
    version="0.1",
    author="DanTshisungu",
    packages=find_packages(),
    install_requires = requirements,
)