import re
from os import path

import requests


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
    posts_json = response.json()

    posts = []
    for post in posts_json[-3:]:
        posts.append(f"- {post['title']}")
    return posts


def main():
    n_last_posts = 3
    posts = fetch_posts("https://xlxs4.com/index.json")
    last_posts = '\n' + '\n'.join(posts[:n_last_posts]) + '\n'
    original = open_readme()
    updated = modify_readme(original, last_posts, identifier='BLOG')
    write_readme(updated)


if __name__ == '__main__':
    main()
