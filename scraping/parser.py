import requests 
import codecs
from bs4 import BeautifulSoup as BS

__all__ = ('hh', 'rabota')


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}


def hh(url):
	jobs = []
	errors = []
	resp = requests.get(url, headers=headers)
	if resp.status_code == 200:
		soup = BS(resp.content, 'html.parser')
		main_div = soup.find('div', attrs={'class': 'vacancy-serp'})
		if main_div:
			div_lst = main_div.find_all('div', attrs={'class': 'vacancy-serp-item'})
			for div in div_lst:
				title = div.find('a', attrs={'class': 'bloko-link HH-LinkModifier'})
				href = title['href']
				title = title.text
				content = div.find('div', attrs={'class': 'g-user-content'})
				content = content.text
				company = div.find('a', attrs={'class': 'bloko-link bloko-link_secondary'})
				company = company.text

				jobs.append({'title': title, 'url': href, 'description': content, 'company': company})
		else:
			errors.append({'url': 'url', 'title': 'Div does not exists'})
	else:
		errors.append({'url': 'url', 'title': 'Page do not response'})
	return jobs, errors 


def rabota(url):
	jobs = []
	errors = []
	url_domain = 'https://rabota.ua'
	resp = requests.get(url, headers=headers)
	if resp.status_code == 200:
		soup = BS(resp.content, 'html.parser')
		main_table = soup.find('table', id='ctl00_content_vacancyList_gridList')
		if main_table:
			table_lst = main_table.find_all('tr', attrs={'id': True})
			for tr in table_lst:
				title = tr.find('h2', attrs={'class': 'card-title'})
				href = title.a['href']
				title = title.text
				content = tr.find('div', attrs={'class': 'card-description'})
				content = content.text
				company = tr.find('a', attrs={'class': 'company-profile-name'})
				company = company.text

				jobs.append({'title': title, 'url': url_domain + href, 'description': content, 
							  'company': company})
		else:
			errors.append({'url': 'url', 'title': 'Div does not exists'})
	else:
		errors.append({'url': 'url', 'title': 'Page do not response'})
	return jobs, errors 


#if __name__ == '__main__':
	#url = 'https://hh.ru/search/vacancy?st=searchVacancy&L_profession_id=29.8&area=2760&no_magic=true&text=%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82+Python'
	#url = 'https://rabota.ua/zapros/python/%d0%ba%d0%b8%d0%b5%d0%b2'
	#jobs, errors = rabota(url)
	#h = codecs.open('work2.txt', 'w', 'utf-8')
	#h.write(str(jobs))
	#h.close()
