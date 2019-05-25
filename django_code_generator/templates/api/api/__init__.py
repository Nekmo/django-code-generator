{%  load code_generator_tags %}from django.conf.urls import url, include
from rest_framework import routers

{% from_module_import app.name|add:'.api.viewsets' models|add_to_items:'ViewSet' %}


router = routers.DefaultRouter()
{% for model in models %}
router.register(r'{{ model.snake_case_name }}s', {{ model }}ViewSet){%endfor%}

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
