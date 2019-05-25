{%  load code_generator_tags %}from rest_framework import viewsets
{% from_module_import app.name|add:'.models' models %}
{% from_module_import app.name|add:'.api.serializers' models|add_to_items:'Serializer' %}{% comment %}
{% endcomment %}{% for model in models %}


class {{ model.name }}ViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = {{ model.name }}.objects.all()
    serializer_class = {{ model.name }}Serializer
    search_fields = (
        {% indent_items model.string_field_names 8 quote='simple' %}
    )
    filter_fields = (
        {% indent_items model.filter_field_names 8 quote='simple' %}
    )
    ordering_fields = (
        {% indent_items model.concrete_field_names 8 quote='simple' %}
    ){% comment %}
{% endcomment %}{% endfor %}
