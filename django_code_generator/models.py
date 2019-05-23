
try:
    from django.db.models.loading import get_models
except ImportError:
    def get_models(app):
        for model in app.get_models():
            yield model


class Model:
    def __init__(self, model):
        self.model = model

    @property
    def name(self):
        return self.model._meta.object_name


class Models(list):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.extend([Model(model) for model in get_models(self.app)])
