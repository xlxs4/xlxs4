import re
from os import path

import requests
from bs4 import BeautifulSoup


def open_readme():
    directory = path.abspath(path.dirname(__file__))
    with open(path.join(directory, 'README.md'), encoding='utf-8') as f:
        readme = f.read()
    return readme


def write_readme(updated):
    directory = path.abspath(path.dirname(__file__))
    with open(path.join(directory, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(updated)


def modify_readme(readme, text, identifier=''):
    start_tag = f'{identifier}_START'
    end_tag = f'{identifier}_END'
    return re.sub(
        f'(?<=<!-- {start_tag} -->).*?(?=<!-- {end_tag} -->)',
        text,
        readme,
        flags=re.DOTALL
    )


def fetch_posts(url):
    response = requests.get(url)
    response.raise_for_status()
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    def clean_date(date_str):
        match = re.search(r'\d{4}-\d{2}-\d{2}', date_str)
        return match.group(0) if match else "No date"
    posts = []
    for link in soup.find_all('a', attrs={'aria-label': lambda v: v and v.startswith('post link to')}):
        title = link['aria-label'].replace('post link to ', '')
        url = link['href']
        # Navigate to the parent and find the previous sibling that contains the date
        date_container = link.find_previous_sibling(class_='archive-meta')
        if date_container and date_container.span:
            date_str = date_container.span.get('title', '')
            date = clean_date(date_str)
        else:
            date = "No date"
        posts.append(f"- [{title}]({url}) - {date}")
    return posts


def main():
    n_last_posts = 3
    posts = fetch_posts("https://xlxs4.com/archives/")
    last_posts = '\n' + '\n'.join(posts[:n_last_posts]) + '\n'
    original = open_readme()
    updated = modify_readme(original, last_posts, identifier='BLOG')
    write_readme(updated)


if __name__ == '__main__':
    main()
