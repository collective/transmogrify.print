
Introduction
============

.. Note:: As of version 1.3 Transmogrifier provides a similar feature, via a blueprint called: ``collective.transmogrifier.sections.logger``.

This `Transmogrifier`_ blueprint is based on ``collective.transmogrifier.sections.tests.PrettyPrinter``, which anyone can use in their project by creating a utility like so::

    <utility
        component="collective.transmogrifier.sections.tests.PrettyPrinter"
        name="print" />

Then adding a section to your pipeline like so::

    [transmogrifier]
    pipeline =
        …
        print

    [print]
    blueprint = print

``transmogrify.print`` has has two advantages over the above approach:

    * It adds the utility for you
    * It allows you to specify a ``keys`` parameter to print individual keys. If no key is provided, it prints the entire item.

.. _`Transmogrifier`: http://pypi.python.org/pypi/collective.transmogrifier

Installation
------------

Make sure to require ``transmogrify.print`` in your project, e.g.::

    from setuptools import setup

    setup(
        name='migrate',
        py_modules=['migrate'],
        install_requires=[
            'plone.app.transmogrifier',
            'transmogrify.filesystem',
            'transmogrify.print',
        ]
    )

Then you may use it in your pipelines, e.g.::

    [transmogrifier]
    pipeline =
        data
        constructor
    #    schema 
        print

    [constructor]
    blueprint = collective.transmogrifier.sections.constructor

    [data]
    blueprint = transmogrify.filesystem
    directory = silly_content
    file-type = Document

    [print]
    blueprint = transmogrify.print
    keys = _path

    [schema]
    blueprint = plone.app.transmogrifier.atschemaupdater

See: https://github.com/aclark4life/silly_content_import for a working example.

