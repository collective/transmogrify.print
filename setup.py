from setuptools import setup, find_packages
import os

setup(
    name='transmogrify.print',
    version='0.6.0',
    author='Alex Clark',
    author_email='aclark@aclark.net',
    classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python :: 2.7',
    ],
    description='Transmogrifier blueprint to print pipeline item keys',
    long_description=open('README.rst').read() + open('CHANGES.rst').read(),
    entry_points = {
        'z3c.autoinclude.plugin': 'target = transmogrify',
    },
    keywords=[
        'Plone Python Transmogrifier',
    ],
    license='GPL',
    include_package_data=True,
    install_requires=[
        'collective.transmogrifier',
    ],
    packages=find_packages(),
    namespace_packages=[
        'transmogrify',
    ],
    test_suite='transmogrify.print.tests.TestSuite',
    url='https://github.com/collective/transmogrify.print',
    zip_safe=False,
)
