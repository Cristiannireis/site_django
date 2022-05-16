from django.db import models
from django.utils import timezone
# Create your models here.

lista_categoria = (
    ('ANALISES', 'Análises'),
    ('CAPILAR', 'Cuidados_capilares'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTROS', 'outros'),
)

# criar os cursos
class Cursos(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_curso')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=lista_categoria)
    visualizacao = models.ImageField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
