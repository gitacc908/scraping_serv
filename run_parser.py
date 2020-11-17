import codecs
import os, sys
from django.db import DatabaseError


proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'scraping_service.settings'


import django
django.setup()


from scraping.parser import *
from scraping.models import Vacancy, City, Language, Errors

parsers = ((hh, 'https://hh.ru/search/vacancy?st=searchVacancy&L_profession_id=29.8&area=2760&no_magic=true&text=%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82+Python'),
	(rabota, 'https://rabota.ua/zapros/python/%d0%ba%d0%b8%d0%b5%d0%b2'))

jobs, errors = [], []

for func, url in parsers:
	j, e = func(url)
	jobs += j
	errors += e

city = City.objects.filter(slug='ny').first()
language = Language.objects.filter(slug='python').first()


for job in jobs:
	
	obj = Vacancy(**job, city=city, Language=language)
	try:
		obj.save()
	except DatabaseError:
		pass

if errors:
	er = Errors(data=errors).save()

