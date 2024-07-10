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
		related_name='categories',
		on_delete=models.CASCADE, verbose_name = 'Категория')
	name = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Полное название объекта')
	main_img = models.ImageField(upload_to='case_headers/', null=True, blank=True, verbose_name = 'Фото в шапку страницы')
	main_video = models.ImageField(upload_to='case_headers/', null=True, blank=True, verbose_name = 'Видео в шапку страницы')

	address = models.CharField(max_length=150, null=True, blank=True, verbose_name = 'Адрес')
	customer = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Заказчик')
	performer = models.CharField(max_length=150, null=True, blank=True, verbose_name = 'Исполнитель', default='АИК «Реновация»')
	architector = models.CharField(max_length=300, null=True, blank=True, verbose_name = 'Архитектор')
	engeneer = models.CharField(max_length=300, null=True, blank=True, verbose_name = 'Инженер')
	square = models.CharField(max_length=30, null=True, blank=True, verbose_name = 'Площадь (только цифры)')
	year = models.CharField(max_length=250, null=True, blank=True, verbose_name = 'Год')

	realize_text = models.TextField(max_length=2500, null=True, blank=True, verbose_name = 'Текст о Реализации')
	image_r_1 = models.ImageField(upload_to='realize/', null=True, blank=True, verbose_name = 'Реализация | 1')
	image_r_2 = models.ImageField(upload_to='realize/', null=True, blank=True, verbose_name = 'Реализация | 2')
	image_r_3 = models.ImageField(upload_to='realize/', null=True, blank=True, verbose_name = 'Реализация | 3')
	image_r_4 = models.ImageField(upload_to='realize/', null=True, blank=True, verbose_name = 'Реализация | 4')
	image_r_5 = models.ImageField(upload_to='realize/', null=True, blank=True, verbose_name = 'Реализация | 5')
	image_r_6 = models.ImageField(upload_to='realize/', null=True, blank=True, verbose_name = 'Реализация | 6')
	visualization_text = models.TextField(max_length=2500, null=True, blank=True, verbose_name = 'Текст о Визуализации')
	image_v_1 = models.ImageField(upload_to='visualization/',null=True,blank=True)
	image_v_2 = models.ImageField(upload_to='visualization/',null=True,blank=True)
	image_v_3 = models.ImageField(upload_to='visualization/',null=True,blank=True)
	image_v_4 = models.ImageField(upload_to='visualization/',null=True,blank=True)
	image_v_5 = models.ImageField(upload_to='visualization/',null=True,blank=True)
	image_v_6 = models.ImageField(upload_to='visualization/',null=True,blank=True)
	analisys_text = models.TextField(max_length=2500, null=True, blank=True, verbose_name = 'Текст о Градостроительном анализе')
	image_a_1 = models.ImageField(upload_to='analisys/',null=True,blank=True)
	image_a_2 = models.ImageField(upload_to='analisys/',null=True,blank=True)
	image_a_3 = models.ImageField(upload_to='analisys/',null=True,blank=True)
	image_a_4 = models.ImageField(upload_to='analisys/',null=True,blank=True)
	image_a_5 = models.ImageField(upload_to='analisys/',null=True,blank=True)
	image_a_6 = models.ImageField(upload_to='analisys/',null=True,blank=True)
	concept_text = models.TextField(max_length=2500, null=True, blank=True, verbose_name = 'Текст о Концепции')
	image_c_1 = models.ImageField(upload_to='concept/',null=True,blank=True)
	image_c_2 = models.ImageField(upload_to='concept/',null=True,blank=True)
	image_c_3 = models.ImageField(upload_to='concept/',null=True,blank=True)
	image_c_4 = models.ImageField(upload_to='concept/',null=True,blank=True)
	image_c_5 = models.ImageField(upload_to='concept/',null=True,blank=True)
	image_c_6 = models.ImageField(upload_to='concept/',null=True,blank=True)

	class Meta:
		ordering = ['name']
		indexes = [
			models.Index(fields=['id', 'address']),
			models.Index(fields=['name']),
		]
		verbose_name = 'Объект'
		verbose_name_plural = 'Объекты'


# Order call form

class CallMe(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30, verbose_name = 'Имя')
	phone = models.CharField(max_length=30, verbose_name = 'Телефон')
	email = models.CharField(max_length=30, verbose_name = 'E-mail')
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-created']
		verbose_name = 'Запрос звонка'
		verbose_name_plural = 'Запросы звонков'