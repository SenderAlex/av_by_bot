from bs4 import BeautifulSoup

with open('title.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Находим все теги <span> с классом "catalog__title" внутри <div class="catalog__list">
brand_names = [span.text for span in soup.select('div.catalog__list span.catalog__title')]

# Выводим названия марок
for name in brand_names:
    print(name)
