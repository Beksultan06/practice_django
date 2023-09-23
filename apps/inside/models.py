from django.db import models

class Inside(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовка"
    )
    context = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='inside_image',
        verbose_name='Фотография внутри портфолио'
    )

    def __Str__(self):
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройки внутриннего портфолий"

