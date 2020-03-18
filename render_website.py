import json
import math
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

BOOKS_ON_PAGE = 10

def on_reload():
    with open('books_description.json', 'r', encoding='utf-8') as my_file:
        books_description_json = my_file.read()

    books_description = json.loads(books_description_json)

    books_description_parted = [books_description[x:x+BOOKS_ON_PAGE] for x in range(0, len(books_description), BOOKS_ON_PAGE)]
    
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

Path('pages').mkdir(parents=True, exist_ok=True)
on_reload()