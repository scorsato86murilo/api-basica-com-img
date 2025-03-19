import uuid
from django.db import models
import os


def upload_image(instance, filename):
    # Gera um nome único para o arquivo usando UUID
    file_extension = os.path.splitext(filename)[1]  # Obtém a extensão do arquivo (por exemplo, .jpg, .png)
    unique_filename = f"{uuid.uuid4()}{file_extension}"  # Cria um nome único para o arquivo
    return os.path.join('teste-arq', unique_filename)


class Filme(models.Model):
    id_filme = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=100)
    tempo = models.IntegerField()
    resumo = models.TextField()
    imagem = models.ImageField(upload_to=upload_image, blank=True, null=True)

    def __str__(self):
        return self.titulo
