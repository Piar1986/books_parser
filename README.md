# Парсер книг с сайта tululu.org

Функционал: 

1. Скачивание книг в текстовом формате из [коллекции книг с научной фантастикой](http://tululu.org/l55/).

   В результате в папке с `parse_tululu_category.py` появятся папки`books/` и `images/`, а также файл `books_data.json` с описанием книг.

   В `books/` скачаются файлы с текстами книг, в `images/` - обложки книг.

2. Верстка сайта. 

   Для удобства просмотра скачанных книг реализована возможность представить информацию в виде сайта.

   [Пример сайта](https://piar1986.github.io/books_parser/pages/index1.html)

## Как установить

Для запуска парсера у вас уже должен быть установлен Python 3.

- Скачайте код
- Установите библиотеки командой `pip install -r requirements.txt`

## Аргументы

1. Скачивание книг.

   Возможно выбрать диапазон страниц для скачивания книг.

   * `start_page` — начальная страница, обязательный параметр.
   * `end_page` — конечная страница, необязательный параметр.

   Пример команды запуска: `python parse_tululu_category.py --start_page 1 --end_page 5`

   В результате скачаются книги с 1 по 5 страницы.Если указать только начальную страницу, то парсер будет работать пока не закончатся страницы, их 701 на момент февраля 2020 года.

2. Верстка сайта.

   Количество книг на странице сайта задается в файле `render_website.py`:

   `BOOKS_ON_PAGE = 10` - 10 книг на странице.

   Команда запуска: `python render_website.py`

   В папке `pages` появятся страницы сайта. Откройте их с помощью браузера.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org).
