

Create templates
================
A template is a directory with files that will be copied to the final path in your app.
Template files can use `Django Templates Syntax <https://docs.djangoproject.com/en/dev/topics/templates/>`_. When
templates are generated, the app models are available to be used with the django template syntax.

For example if you create the template *mytemplate* you can use it for your app *myapp^with the command::

    $ python manage.py generate mytemplate myapp


Template locations
------------------
There are several places to locate the directories for your templates. The templates will be loaded in this order:

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

For example, running ``manage.py generate mytemplate myapp`` the
file ``~/.config/dcg_templates/mytemplate/admin.py`` will be copied and rendered to ``myproject/myapp/admin.py``.


Template context
----------------
These variables are available during rendering:

* **models**: a list of the models in the app. See :class:`django_code_generator.models.Models` class. The listing
  contains :class:`django_code_generator.models.Model` instances.
* **app**: a `AppConfig <https://docs.djangoproject.com/en/3.0/ref/applications/#configurable-attributes>`_ instance.

You can also use the included :ref:`template tags<code_generator_tags>`. To use the tags you must put
at the beginning of the template ``{% load code_generator_tags %}``.


Examples
--------

.. literalinclude:: ../django_code_generator/templates/admin/admin/__init__.py
   :language: django
   :linenos:
   :caption: admin/__init__.py

.. literalinclude:: ../django_code_generator/templates/api/api/__init__.py
   :language: django
   :linenos:
   :caption: api/__init__.py

.. literalinclude:: ../django_code_generator/templates/api/api/serializers.py
   :language: django
   :linenos:
   :caption: api/serializers.py

.. literalinclude:: ../django_code_generator/templates/api/api/viewsets.py
   :language: django
   :linenos:
   :caption: api/viewsets.py
