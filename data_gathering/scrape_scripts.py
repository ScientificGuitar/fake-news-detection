import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_americasfreedomfighters(pages=10):
    articles_list = []

    for page in range(pages):
        try:
            print(f'Scraping page: {page}')
            # Search page
            url = f'https://americasfreedomfighters.com/page/{page}/?s'
            search_page = requests.get(url)

            soup = BeautifulSoup(search_page.content, 'html.parser')
            articles = soup.find(id='recent-posts',).find_all('a', rel='bookmark')
            list_articles = [article['href'] for article in articles]
        except Exception as e:
            print(e)
            print(url)
            print(f'Page {page}\n')
        for i in range(20):
            # Article
            try:
                article_url = list_articles[i]
                article_page = requests.get(article_url)

                article_soup = BeautifulSoup(article_page.content, 'html.parser')
                title = article_soup.find('h1', class_='title').find('a').text.strip()
                title = title.replace(',', '')
                content_raw = article_soup.find('div', class_='entry').find_all('p')
                content = " ".join([p.text.strip() for p in content_raw[1:-12]])
                content = content.replace(',', '').replace('\n', '')

                articles_list.append(['americasfreedomfighters', title, content])
            except Exception as e:
                print(e)
                print(article_url)
                print(f'Search {page}, article {i}\n')
    articles_df = pd.DataFrame(data=articles_list, columns=['source', 'title', 'content'])
    articles_df.to_csv('data/americasfreedomfighters.csv', index=False)

def scrape_lastrefuge(pages=10):
    articles_list = []

    for page in range(pages):
        try:
            print(f'Scraping page: {page}')
            # Search page
            url = f'https://theconservativetreehouse.com/page/{page}/'
            search_page = requests.get(url)

            soup = BeautifulSoup(search_page.content, 'html.parser')
            articles = soup.find_all('a', class_='more-link')
            list_articles = [article['href'] for article in articles]
        except Exception as e:
            print(e)
            print(url)
            print(f'Page {page}\n')
        for article_url in list_articles:
            try:
                article_page = requests.get(article_url)

                article_soup = BeautifulSoup(article_page.content, 'html.parser')
                title = article_soup.find('article').find('h1').text.strip()
                title = title.replace(',', '')
                content_raw = article_soup.find('article').find('div', class_='post-content').find_all('p')
                content = " ".join([p.text.strip() for p in content_raw])
                content = content.replace(',', '').replace('\n', '')

                articles_list.append(['lastrefuge', title, content])
            except Exception as e:
                print(e)
                print(article_url)
    articles_df = pd.DataFrame(data=articles_list, columns=['source', 'title', 'content'])
    articles_df.to_csv('data/lastrefuge.csv', index=False)

def scrape_newspunch(pages=10):
    articles_list = []

    for page in range(pages):
        try:
            print(f'Scraping page: {page}')
            # Search page
            url = f'https://newspunch.com/page/{page}/'
            search_page = requests.get(url)

            soup = BeautifulSoup(search_page.content, 'html.parser')
            articles = soup.find_all('a', rel='bookmark')
            list_articles = [article['href'] for article in articles]
        except Exception as e:
            print(e)
            print(url)
            print(f'Page {page}\n')
        for article_url in list_articles:
            try:
                article_page = requests.get(article_url)

                article_soup = BeautifulSoup(article_page.content, 'html.parser')
                title = article_soup.find('article').find('h1').text.strip()
                title = title.replace(',', '')
                content_raw = article_soup.find('article').find('div', class_='entry-content').find_all('p', recursive=False)
                content = " ".join([p.text.strip() for p in content_raw])
                content = content.replace(',', '').replace('\n', '')

                articles_list.append(['newspunch', title, content])
            except Exception as e:
                print(e)
                print(article_url)
    articles_df = pd.DataFrame(data=articles_list, columns=['source', 'title', 'content'])
    articles_df.to_csv('data/newspunch.csv', index=False)

def scrape_rightwingtribune(pages=10):
    articles_list = []

    for page in range(pages):
        try:
            print(f'Scraping page: {page}')
            # Search page
            url = f'https://rightwingtribune.com/page/{page}/'
            search_page = requests.get(url)

            soup = BeautifulSoup(search_page.content, 'html.parser')
            articles = soup.find('div', id='main-content').find_all('a', rel='bookmark')
            list_articles = [article['href'] for article in articles]
        except Exception as e:
            print(e)
            print(url)
            print(f'Page {page}\n')
        for article_url in list_articles:
            try:
                article_page = requests.get(article_url)

                article_soup = BeautifulSoup(article_page.content, 'html.parser')
                title = article_soup.find('article').find('h1').text.strip()
                title = title.replace(',', '')
                content_raw = article_soup.find('article').find('div', class_='entry-content').find_all('p', recursive=False)
                content = " ".join([p.text.strip() for p in content_raw])
                content = content.replace(',', '').replace('\n', '')

                articles_list.append(['newspunch', title, content])
            except Exception as e:
                print(e)
                print(article_url)
    articles_df = pd.DataFrame(data=articles_list, columns=['source', 'title', 'content'])
    articles_df.to_csv('data/rightwingtribune.csv', index=False)


if __name__ == '__main__':
    # scrape_americasfreedomfighters(1100)
    # scrape_lastrefuge(3954)
    # scrape_newspunch(3958)
    scrape_rightwingtribune(228)