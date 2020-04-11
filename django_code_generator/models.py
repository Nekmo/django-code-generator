"""
The models module contains the classes available in the rendering of templates.

The available classes are:

* :class:`Models`: a list of models in a app. Each model in this listing uses the :ref:`Model` class.
* :class:`Model`: A wrapper of the app's Model class. It has methods that make it easier to get model fields.

"""
from django.db.models import ForeignKey
from django.db.models.fields import CharField, TextField, IntegerField, DateField, AutoField
from django.utils.text import camel_case_to_spaces

try:
    from django.db.models.loading import get_models
except ImportError:
    def get_models(app):
        """Get model classes from a AppConfig instance."""
        for model in app.get_models():
            yield model


#: CharField type fields. A CharField is string field with a limited size.
CHAR_FIELDS = (CharField,)
#: ForeignKey type fields. A ForeignKey is a one-to-many relationship.
FOREIGN_FIELDS = (ForeignKey,)
#: All fields that store text.
STRING_FIELDS = (CharField, TextField)
#: All the fields used to filter.
FILTER_FIELDS = (CharField, IntegerField, DateField, AutoField)


def get_field_names(fields):
    """Get the names of a list of fields"""
    return [x.name for x in fields]


class Model:
    """A wrapper of the app's Model class. It has methods that make it easier to get model fields.

    This class receives a Model django db class.
    """
    def __init__(self, model):
        """
        :param django.db.models.Model model: a django Model class.
        """
        self.model = model

    @property
    def name(self):
        """Original model name. Just like the class."""
        return self.model._meta.object_name

    @property
    def field_names(self):
        """A list of all forward field names on the model and its parents,
        excluding ManyToManyFields.
        """
        return get_field_names(self.model._meta.fields)

    @property
    def local_field_names(self):
        """A list of field names on the model.
        """
        return get_field_names(self.model._meta.local_fields)

    @property
    def concrete_field_names(self):
        """A list of all concrete field names on the model and its parents."""
        return get_field_names(self.model._meta.concrete_fields)

    @property
    def string_field_names(self):
        """A list of concrete field names of type string (see :const:`STRING_FIELDS`)."""
        return get_field_names(filter(lambda x: isinstance(x, STRING_FIELDS),
                                      self.model._meta.concrete_fields))

    @property
    def foreign_field_names(self):
        """A list of concrete field names of type foreign key (see :const:`FOREIGN_FIELDS`)."""
        return get_field_names(filter(lambda x: isinstance(x, FOREIGN_FIELDS),
                                      self.model._meta.concrete_fields))

    @property
    def char_field_names(self):
        """A list of concrete field names of type char (see :const:`CHAR_FIELDS`)."""
        return get_field_names(filter(lambda x: isinstance(x, CHAR_FIELDS),
                                      self.model._meta.concrete_fields))

    @property
    def filter_field_names(self):
        """A list of concrete field names used for filters (see :const:`FILTER_FIELDS`)."""
        return get_field_names(filter(lambda x: isinstance(x, FILTER_FIELDS),
                                      self.model._meta.concrete_fields))

    @property
    def snake_case_name(self):
        """Model name in snake case."""
        return camel_case_to_spaces(self.name).replace(' ', '_')

    def __str__(self):
        return self.name


class Models(list):
    """A list of models in a app. Each model in this listing uses the
    :ref:`Model` class.

    This class receives an AppConfig instance.
    """
    def __init__(self, app):
        """
        :param AppConfig app: a django AppConfig instance.
        """
        super().__init__()
        self.app = app
        self.extend([Model(model) for model in get_models(self.app)])
