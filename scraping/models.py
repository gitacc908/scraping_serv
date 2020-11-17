from django.db import models
from django.utils.text import slugify
import jsonfield

def default_urls():
	return {'hh':''}
# Create your models here.
class City(models.Model):
	name = models.CharField(max_length=100, unique=True, verbose_name='City')
	slug = models.SlugField(unique=True, blank=True)

	class Meta:
		verbose_name = 'City'
		verbose_name_plural = 'Cities'

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(City, self).save(*args, **kwargs)
	

class Language(models.Model):
	name = models.CharField(max_length=100, unique=True, verbose_name='Programming Language')
	slug = models.SlugField(unique=True, blank=True)

	class Meta:
		verbose_name = 'Language'
		verbose_name_plural = 'Languages'

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Language, self).save(*args, **kwargs)


class Vacancy(models.Model):
	url = models.URLField(unique=True)
	title = models.CharField(max_length=250, verbose_name='Vacancy title')
	description = models.TextField()
	company = models.CharField(max_length=250, verbose_name='Company name')
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	Language = models.ForeignKey(Language, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Vacancy'
		verbose_name_plural = 'Vacancies'

	def __str__(self):
		return self.title


class Errors(models.Model):
	timestamp = models.DateField(auto_now_add=True)
	data = jsonfield.JSONField()

	class Meta:
		verbose_name = 'Error'
		verbose_name_plural = 'Errors'

	def __str__(self):
		return 'Errors'

class Url(models.Model):
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	Language = models.ForeignKey(Language, on_delete=models.CASCADE)
	url_data = jsonfield.JSONField(default=default_urls)

	class Meta:
		unique_together = ('city', 'Language')
		verbose_name = 'Url'
		verbose_name_plural = 'Urls'

	def __str__(self):
		return 'Urls'