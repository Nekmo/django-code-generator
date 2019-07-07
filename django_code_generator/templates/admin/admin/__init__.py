{%  load code_generator_tags %}from django.contrib import admin
{% from_module_import app.name|add:'.models' models %}{% comment %}
{% endcomment %}
{% for model in models %}

@admin.register({{ model.name }})
class {{ model.name }}Admin(admin.ModelAdmin):
    """
    """
    list_display = (
        {% indent_items model.filter_field_names 8 quote='simple' %}
    )
    search_fields = (
        {% indent_items model.char_field_names 8 quote='simple' %}
    )
    {% if model.foreign_field_names %}autocomplete_fields = (
        {% indent_items model.foreign_field_names 8 quote='simple' %}
    ){% endif %}{% endfor %}
