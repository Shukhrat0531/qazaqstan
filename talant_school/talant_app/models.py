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

# В models.py
class FooterContact(models.Model):
    address = models.CharField(max_length=200, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    working_hours = models.CharField(max_length=100, verbose_name="Рабочие часы")
    map_url = models.URLField(verbose_name="Ссылка на карту", blank=True, null=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Контакты футера"
        verbose_name_plural = "Контакты футера"
        
        
        

class Admission(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок страницы")
    documents_title = models.CharField(max_length=200, verbose_name="Заголовок блока документов", default="Необходимые документы")
    documents_list = models.TextField(verbose_name="Список документов", help_text="Перечислите документы через запятую или в формате HTML списка")
    subjects_title = models.CharField(max_length=200, verbose_name="Заголовок блока предметов", default="Профилирующие предметы")
    subjects_list = models.TextField(verbose_name="Список предметов", help_text="Перечислите предметы через запятую или в формате HTML списка")
    additional_info_title = models.CharField(max_length=200, verbose_name="Заголовок дополнительной информации", default="Дополнительная информация")
    additional_info = models.TextField(verbose_name="Дополнительная информация")
    reception_info = models.CharField(max_length=200, verbose_name="Информация о приёме документов")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    official_site_url = models.URLField(verbose_name="Ссылка на официальный сайт", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Как поступить"
        verbose_name_plural = "Как поступить"        



class StudentParliament(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок страницы")
    description = models.TextField(verbose_name="Описание")
    goals_title = models.CharField(max_length=200, verbose_name="Заголовок целей и задач", default="Цели и задачи")
    goals_list = models.TextField(verbose_name="Список целей и задач", help_text="Перечислите цели через запятую или в формате HTML списка")
    activities_title = models.CharField(max_length=200, verbose_name="Заголовок направлений деятельности", default="Направления деятельности")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Студенческий парламент"
        verbose_name_plural = "Студенческий парламент"

class ParliamentActivity(models.Model):
    parliament = models.ForeignKey(StudentParliament, on_delete=models.CASCADE, related_name='activities', verbose_name="Парламент")
    title = models.CharField(max_length=200, verbose_name="Название направления")
    description = models.TextField(verbose_name="Описание направления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Направление деятельности парламента"
        verbose_name_plural = "Направления деятельности парламента"        
        
from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название специальности")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='specialties/', verbose_name="Изображение", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"        
        


class Rule(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок страницы", default="Правила внутреннего распорядка")
    description = models.TextField(verbose_name="Описание")
    general_title = models.CharField(max_length=200, verbose_name="Заголовок общих положений", default="Общие положения")
    general_rules = models.TextField(verbose_name="Список общих положений", help_text="Перечислите правила через запятую или в формате HTML списка")
    behavior_title = models.CharField(max_length=200, verbose_name="Заголовок поведения", default="Поведение в учебном заведении")
    behavior_rules = models.TextField(verbose_name="Список правил поведения", help_text="Перечислите правила через запятую или в формате HTML списка")
    discipline_title = models.CharField(max_length=200, verbose_name="Заголовок дисциплинарных мер", default="Дисциплинарные меры")
    discipline_rules = models.TextField(verbose_name="Список дисциплинарных мер", help_text="Перечислите меры через запятую или в формате HTML списка")
    conclusion = models.TextField(verbose_name="Заключение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Правило внутреннего распорядка"
        verbose_name_plural = "Правила внутреннего распорядка"        

from django.db import models

class Schedule(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название расписания")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='schedules/', verbose_name="Изображение", blank=True, null=True)
    google_drive_link = models.URLField(verbose_name="Ссылка на Google Drive", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"    
        
from django.db import models

class Accreditation(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок страницы")
    description = models.TextField(verbose_name="Описание")
    goals_title = models.CharField(max_length=200, verbose_name="Заголовок целей", default="Цели аккредитации")
    goals_list = models.TextField(verbose_name="Список целей", help_text="Перечислите цели через запятую или в формате HTML списка")
    documents_title = models.CharField(max_length=200, verbose_name="Заголовок документов", default="Документы аккредитации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Аккредитация"
        verbose_name_plural = "Аккредитация"

class AccreditationDocument(models.Model):
    accreditation = models.ForeignKey(Accreditation, on_delete=models.CASCADE, related_name='documents', verbose_name="Аккредитация")
    title = models.CharField(max_length=200, verbose_name="Название документа")
    description = models.TextField(verbose_name="Описание документа")
    file_url = models.URLField(verbose_name="Ссылка на файл", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Документ аккредитации"
        verbose_name_plural = "Документы аккредитации"            