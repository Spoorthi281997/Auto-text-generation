from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='Auto_Text_Generation',
    packages=find_packages(),
    version='0.1.0',
    description='Automatic generation of text using input words',
    long_description=readme,
    author='Spoorthi Chinivar',
    author_email='chinivarspoorthi@gmail.com'
    license=license,
    url='https://github.com/Spoorthi281997/Auto_Text_Generation'
)
