{%  load code_generator_tags %}from rest_framework.serializers import ModelSerializer
{% from_module_import app.name|add:'.models' models %}{% comment %}
{% endcomment %}{% for model in models %}


class {{ model.name }}Serializer(ModelSerializer):
    class Meta:
        model = {{ model.name }}
        depth = 1
        fields = (
            {% indent_items model.field_names 12 quote='simple' %}
        )
        read_only_fields = (){% comment %}
{% endcomment %}{% endfor %}
