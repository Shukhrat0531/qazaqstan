from django.db import models



# Модель для слайдера
class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    link_text = models.CharField(max_length=100, verbose_name="Текст ссылки")
    link_url = models.URLField(verbose_name="URL ссылки")
    background_image = models.ImageField(upload_to='slider/', verbose_name="Фоновое изображение")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

# Модель для секции "О нас"
class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text1 = models.TextField(verbose_name="Первый абзац")
    text2 = models.TextField(verbose_name="Второй абзац")
    image = models.ImageField(upload_to='about/', verbose_name="Изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

# Модель для клубов
class Club(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название клуба")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='clubs/', verbose_name="Основное изображение")
    leader = models.CharField(max_length=100, verbose_name="Руководитель")
    schedule = models.CharField(max_length=200, verbose_name="Расписание", help_text="Например: Пн, Ср 15:00-16:30")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"

class ClubImage(models.Model):
    image = models.ImageField(upload_to='club_gallery/', verbose_name="Изображение")
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"Изображение для {self.club.name}"

    class Meta:
        verbose_name = "Изображение клуба"
        verbose_name_plural = "Изображения клуба"
# Модель для администрации
class AdministrationMember(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    position = models.CharField(max_length=200, verbose_name="Должность")
    photo = models.ImageField(upload_to='administration/', verbose_name="Фото")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Член администрации"
        verbose_name_plural = "Администрация"

# Модель для регистраций
class Registration(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        verbose_name = "Регистрация"
        verbose_name_plural = "Регистрации"

# Модель для уровней образования
class EducationLevel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название уровня")
    description = models.CharField(max_length=200, verbose_name="Описание")
    image = models.ImageField(upload_to='education/', verbose_name="Изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Уровень образования"
        verbose_name_plural = "Уровни образования"

# Модель для новостей
class News(models.Model):
    date = models.DateField(verbose_name="Дата")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='news/', verbose_name="Изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
