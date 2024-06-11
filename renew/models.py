from django.db import models

class Category(models.Model):
	id_cat = models.AutoField(primary_key=True)
	category = models.CharField(max_length=60, verbose_name='Категория')
	class Meta:
		ordering = ['category']
		indexes = [
			models.Index(fields=['category']),
		]
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'	

	def __str__(self):
		return self.category



class Case(models.Model):
	id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category,
		related_name='cases',
		on_delete=models.CASCADE, verbose_name = 'Категория')
	name = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Полное название объекта')
	main_img = models.ImageField(upload_to='case_headers/', verbose_name = 'Фото в шапку страницы')
	main_video = models.ImageField(upload_to='case_headers/', verbose_name = 'Видео в шапку страницы')

	address = models.CharField(max_length=150, null=True, blank=True, verbose_name = 'Адрес')
	customer = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Заказчик')
	performer = models.CharField(max_length=150, null=True, blank=True, verbose_name = 'Исполнитель', default='АИК «Реновация»')
	architector = models.CharField(max_length=300, null=True, blank=True, verbose_name = 'Архитектор')
	square = models.CharField(max_length=30, null=True, blank=True, verbose_name = 'Площадь (только цифры)')
	year = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Год')

	realize_img = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Путь в директорию Реализация')
	visualization_img = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Путь в директорию Визуализация')
	analisys_img = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Путь в директорию Градостроительный анализ')
	concept_img = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Путь в директорию Концепция')

	realize_text = models.TextField(max_length=250, null=True, blank=True, verbose_name = 'Текст о Реализации')
	visualization_img = models.TextField(max_length=250, null=True, blank=True, verbose_name = 'Текст о Визуализации')
	analisys_img = models.TextField(max_length=250, null=True, blank=True, verbose_name = 'Текст о Градостроительном анализе')
	concept_img = models.TextField(max_length=250, null=True, blank=True, verbose_name = 'Текст о Концепции')

	class Meta:
		ordering = ['name']
		indexes = [
			models.Index(fields=['id', 'address']),
			models.Index(fields=['name']),
		]
		verbose_name = 'Объект'
		verbose_name_plural = 'Объекты'



class CallMe(models.Model):
	call_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	email = models.CharField(max_length=30, verbose_name = 'E-mail')
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-created']