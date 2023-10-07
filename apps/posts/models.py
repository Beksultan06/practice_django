from django.db import models

# Create your models here.

class About(models.Model):
    title = models.TextField(
        verbose_name='Заголовка главной строницы'
    )
    image_homepage = models.ImageField(
        upload_to="im_home/"
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Натройка главной строницы"


class Services(models.Model):
    descriptions = models.CharField(
        max_length=100,
        verbose_name="descriptions"
    )
    descriptions2 = models.CharField(
        max_length=100,
        verbose_name="descriptions"
    )
    descriptions3 = models.CharField(
        max_length=100,
        verbose_name="descriptions"
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Настройка сервисов"


class Portfolio(models.Model):
    title_porfoile = models.CharField(
        max_length=100,
        verbose_name="Описание портфойле"
    )
    my_image = models.ImageField(
        upload_to="Фото портфойля"
    )
    discription_image = models.CharField(
        max_length=50,
        verbose_name="Описание фото"
    )
    def __str__(self):
        return self.title_porfoile
    
    class Meta:
        verbose_name=""
        verbose_name_plural="настройка портфойля" 

class Blog(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название болга"
    )
    descriptions_blog = models.TextField(
        verbose_name="Описание блога"
    )
    image = models.ImageField(
        upload_to="im_blog"  
    )  
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройка блога"    

class Contacts(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name="Имя пользователя"
    )
    email = models.EmailField(
        verbose_name="Почта",
        null=True,blank=True
    )
    phone = models.CharField(
        max_length=155,
        verbose_name="Номер телефона"
    )
    message = models.TextField(
        verbose_name="Введите ваше сообщение"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"