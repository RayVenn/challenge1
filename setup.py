from setuptools import setup, find_packages

with open('requirements.txt', 'r') as reqs_file:
    reqs = reqs_file.readlines()

setup(
    name='challenge1',
    version='0.0.1',
    description='challenge1',
    packages=find_packages(),
    install_requires=reqs
)
