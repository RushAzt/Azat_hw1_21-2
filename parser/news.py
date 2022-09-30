import requests
from bs4 import BeautifulSoup as BS

URL = "https://www.securitylab.ru/news/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all('a', class_='article-card inline-card')
    news = []
    for item in items:
        news.append({
            'title': item.find("h2", class_='article-card-title').getText(),
            'desc': item.find("p").getText(),
            'link': "https://www.securitylab.ru" + item.get('href'),
            'time': item.find("time").getText(),

        })
    return news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answers = []
        for page in range(1, 3):
            html = get_html(f"{URL}page1_{page}.php")
            current_page = get_data(html.text)
            answers.extend(current_page)
        return answers
    else:
        raise Exception("Error in parser!")



