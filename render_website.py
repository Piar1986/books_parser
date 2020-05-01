import json
import math
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
from urllib.parse import quote
from more_itertools import chunked


BOOKS_ON_PAGE = 10

if __name__ == '__main__':
    Path('pages').mkdir(parents=True, exist_ok=True)
    with open('books_description.json', 'r', encoding='utf-8') as my_file:
        books_description_json = my_file.read()

    books_description = json.loads(books_description_json)

    for book in books_description:
        formated_img_src = quote(book['img_src'].replace('\\','/'))
        formated_book_address = quote(book['book_address'].replace('\\','/'))
        book['img_src'] = formated_img_src
        book['book_address'] = formated_book_address

    books_description_parted = chunked(books_description, BOOKS_ON_PAGE)
    page_quantity = math.ceil(len(books_description)/BOOKS_ON_PAGE)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('./templates/template.html')

    for page_number, part in enumerate(books_description_parted, 1):
        rendered_page = template.render(
            books_description=part,
            page_quantity=page_quantity,
            current_page_number=page_number
        )
        page_path = 'pages/index{}.html'.format(page_number)
        with open(page_path, 'w', encoding="utf8") as file:
            file.write(rendered_page)