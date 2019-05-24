{%  load code_generator_tags %}from rest_framework.serializers import ModelSerializer
{% from_module_import app.name|add:'.models' models %}{% comment %}
{% endcomment %}{% for model in models %}


class {{ model.name }}Serializer(ModelSerializer):
    class Meta:
        model = {{ model.name }}
        fields = (
            {% indent_items models 12 quote='simple' %}
        ){% comment %}
{% endcomment %}{% endfor %}
