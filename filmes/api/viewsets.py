from rest_framework import viewsets
from filmes.models import Filme
from filmes.api.serializers import FilmeSerializer


class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer