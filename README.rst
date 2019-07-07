#####################
django-code-generator
#####################


.. image:: https://img.shields.io/travis/Nekmo/django-code-generator.svg?style=flat-square&maxAge=2592000
  :target: https://travis-ci.org/Nekmo/django-code-generator
  :alt: Latest Travis CI build status

.. image:: https://img.shields.io/pypi/v/django-code-generator.svg?style=flat-square
  :target: https://pypi.org/project/django-code-generator/
  :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/pyversions/django-code-generator.svg?style=flat-square
  :target: https://pypi.org/project/django-code-generator/
  :alt: Python versions

.. image:: https://img.shields.io/codeclimate/maintainability/Nekmo/django-code-generator.svg?style=flat-square
  :target: https://codeclimate.com/github/Nekmo/django-code-generator
  :alt: Code Climate

.. image:: https://img.shields.io/codecov/c/github/Nekmo/django-code-generator/master.svg?style=flat-square
  :target: https://codecov.io/github/Nekmo/django-code-generator
  :alt: Test coverage

.. image:: https://img.shields.io/requires/github/Nekmo/django-code-generator.svg?style=flat-square
     :target: https://requires.io/github/Nekmo/django-code-generator/requirements/?branch=master
     :alt: Requirements Status


Generate code from Django models for faster development. This project can generate a Django Rest Framework API
or an admin for your app. You can also **create your own templates** so you can generate code for whatever you want.


To install django-code-generator, run this command in your terminal:

.. code-block:: console

    $ sudo pip install django-code-generator

This is the preferred method to install django-code-generator, as it will always install the most recent stable release.


Then add it to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'django_code_generator',
    ]


Usage
=====
Generating code is as easy as::

    $ python manage.py generator <template> <project app>

This project includes two default templates: ``admin`` and ``api``. For example::

    $ python manage.py generator admin myapp


Create templates
================
There are several places to locate the directories of your templates. The templates will be loaded in this order:

#. Template directories in ``DJANGO_CODE_GENERATOR_TEMPLATES`` environment variable. The directories are separated
   by a colon char (``:``). For example: ``DJANGO_CODE_GENERATOR_TEMPLATES=/path/templates/``.
#. Templates from the folder ``.dcg_templates/`` in the current directory.
#. Template directories from ``DJANGO_CODE_GENERATOR_TEMPLATES = []`` list in your Django settings.
#. Templates from folder ``.dcg_templates/`` in ``manage.py`` directory.
#. Templates from ``~/.config/dcg_templates/`` directory.
#. Templates from django_code_generator project

To create the template, make a directory with the name of the template in the templates folder. For example:
``~/.config/dcg_templates/mytemplate/``. When you use the command ``manage.py generate <template> <project app>``
everything inside the template folder will be copied and rendered to the app folder in your Django project.

For example, running ``manage.py generate mytemplate myapp`` the file ``~/.config/dcg_templates/mytemplate/admin.py``
will be copied and rendered to ``myproject/myapp/admin.py``.

Django Code Generate uses `Django Templates Syntax <https://docs.djangoproject.com/en/dev/topics/templates/>`_ for
to render the templates. You can find examples in this project.
