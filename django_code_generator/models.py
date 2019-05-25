from django.db.models.fields import CharField, TextField, IntegerField, DateField, AutoField

try:
    from django.db.models.loading import get_models
except ImportError:
    def get_models(app):
        for model in app.get_models():
            yield model


STRING_FIELDS = (CharField, TextField)
FILTER_FIELDS = (CharField, IntegerField, DateField, AutoField)


def get_field_names(fields):
    return [x.name for x in fields]


class Model:
    def __init__(self, model):
        self.model = model

    @property
    def name(self):
        return self.model._meta.object_name

    @property
    def field_names(self):
        return get_field_names(self.model._meta.fields)

    @property
    def local_field_names(self):
        return get_field_names(self.model._meta.local_fields)

    @property
    def concrete_field_names(self):
        return get_field_names(self.model._meta.concrete_fields)

    @property
    def string_field_names(self):
        return get_field_names(filter(lambda x: isinstance(x, STRING_FIELDS),
                                      self.model._meta.concrete_fields))

    @property
    def filter_field_names(self):
        return get_field_names(filter(lambda x: isinstance(x, FILTER_FIELDS),
                                      self.model._meta.concrete_fields))

    def __str__(self):
        return self.name


class Models(list):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.extend([Model(model) for model in get_models(self.app)])
