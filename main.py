import requests
from bs4 import BeautifulSoup


def get_word_definition(word):
    url = f"https://ru.wiktionary.org/wiki/{word}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Ищем определение слова
    definition = ""
    definition_element = soup.find("span", {"class": "mw-headline", "id": "Значение"})
    if definition_element:
        definition = definition_element.find_next("ol").text.strip()

    # Ищем правила орфографии
    spelling_rules = ""
    rules_element = soup.find("span", {"class": "mw-headline", "id": "Орфографические_правила"})
    if rules_element:
        spelling_rules = rules_element.find_next("ul").text.strip()

    return definition, spelling_rules


word = input("Введите слово: ")
definition, rules = get_word_definition(word)
if definition:
    print(f"Определение слова '{word}':")
    print(definition)
else:
    print(f"Определение слова '{word}' не найдено.")

if rules:
    print(f"Правила орфографии для слова '{word}':")
    print(rules)
else:
    print(f"Правила орфографии для слова '{word}' не найдены.")
