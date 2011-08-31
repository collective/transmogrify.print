from setuptools import setup, find_packages
import os

setup(
    name='transmogrify.print',
    version='0.5.0',
    author='Alex Clark',
    author_email='aclark@aclark.net',
    description='Transmogrifier blueprint to print pipeline item keys',
    long_description=open('README.rst').read() + open(os.path.join('docs', 'HISTORY.txt')).read(),
    entry_points = {
        'z3c.autoinclude.plugin': 'target = transmogrify',
    },
    include_package_data=True,
    install_requires=[
        'collective.transmogrifier',
    ],
    packages=find_packages(),
    namespace_packages=[
        'transmogrify',
    ],
    url='https://github.com/aclark4life/transmogrify.print',
)
