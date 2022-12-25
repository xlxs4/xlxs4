import feedparser
import time
import re

from os import path


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


def fetch_posts(feed):
    posts = []
    feed = feedparser.parse(feed)
    for entry in feed.entries:
        title = entry['title']
        link = entry['link']
        published = time.strftime('%Y-%m-%d', entry['published_parsed'])
        posts.append(f"- [{title}]({link}) ({published})")
    return posts


def main():
    n_last_posts = 3
    posts = fetch_posts("https://xlxs4.github.io/feed.xml")
    last_posts = '\n' + '\n'.join(posts[:n_last_posts]) + '\n'
    original = open_readme()
    updated = modify_readme(original, last_posts, identifier='BLOG')
    write_readme(updated)


if __name__ == '__main__':
    main()
