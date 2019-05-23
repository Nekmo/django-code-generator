from rest_framework.serializers import ModelSerializer{% comment %}
{% endcomment %}{% for model in models %}


class {{ model.name }}Serializer(ModelSerializer):
    class Meta:
        model = {{ model.name }}
        fields = '__all__'{% comment %}
{% endcomment %}{% endfor %}
