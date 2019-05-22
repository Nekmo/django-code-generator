from rest_framework import viewsets


class {{ model.name }}ViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = {{ model.name }}.objects.all()
    serializer_class = {{ model.name }}Serializer
    search_fields = ()
    filter_fields = ()
    ordering_fields = ()
