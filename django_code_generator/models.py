
try:
    from django.db.models.loading import get_models
except ImportError:
    def get_models(app):
        for model in app.get_models():
            yield model
