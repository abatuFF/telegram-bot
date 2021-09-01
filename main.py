import requests
from bs4 import BeautifulSoup as BS


def get_html(url):
	resp = requests.get(url)
	return resp.text

def get_soup(html):
	soup = BS(html,'lxml')
	return soup

def get_titles():
	url = 'https://www.ts.kg/'
	# print(get_html(url))
	html=get_html(url)#получаем исходный код html страницы
	soup=get_soup(html)#получаем объект BS
	items=soup.find('div', class_='col-xs-8').find_all('div',class_='show')
	print(len(items))
	titles=[]
	for item in items:
		title=item.find('p',class_='show-title').get_text()
		print(title)
		titles.append(title)
	return titles


def get_date(soup):
			#код html и название парсера
	date = soup.find('div', class_='row hidden-xs').find('h3').get_text()
	return date

def main():
	url = 'https://www.ts.kg/'
	# print(get_html(url))
	html=get_html(url)#получаем исходный код html страницы
	soup=get_soup(html)#получаем объект BS
	date=get_date(soup)#персим названия сериалов
	titles=get_titles(soup)
	print(date)
	print(*titles,sep='\n')

if __name__ == '__main__':
	main()