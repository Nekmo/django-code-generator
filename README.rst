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
A template is a directory with files that will be copied to the final path in your app.
Template files can use `Django Templates Syntax <https://docs.djangoproject.com/en/dev/topics/templates/>`_. When
templates are generated, the app models are available to be used with the django template syntax.

For example if you create the template *mytemplate* you can use it for your app *myapp^with the command::

    $ python manage.py generate mytemplate myapp

A template file example:

.. code-block:: django

    {%  load code_generator_tags %}from django.contrib import admin
    {% from_module_import app.name|add:'.models' models %}{% comment %}
    {% endcomment %}
    {% for model in models %}

    @admin.register({{ model.name }})
    class {{ model.name }}Admin(admin.ModelAdmin):
        """
        """
        list_display = (
            {% indent_items model.filter_field_names 8 quote='simple' %}
        )
        search_fields = (
            {% indent_items model.char_field_names 8 quote='simple' %}
        )
        {% if model.foreign_field_names %}autocomplete_fields = (
            {% indent_items model.foreign_field_names 8 quote='simple' %}
        ){% endif %}{% endfor %}

For more information see `the docs<https://github.com/Nekmo/django-code-generator/blob/master/docs/templates.rst>`_.
