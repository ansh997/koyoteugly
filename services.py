from typing import Dict, List
import json as _json
from random import randint


def get_all_quotes() -> Dict:
  """
  """
  with open("quotes.json", encoding="utf8") as quotes_file:
    data = _json.load(quotes_file)

  return data


def get_random_quote() -> Dict:
  """
  """
  quotes = get_all_quotes()
  rand_page = randint(0, 99)
  rand_quote = randint(0, 29)

  return quotes[f"{rand_page}"]["content"][f"{rand_quote}"]


def get_quote_by_name(name: str) -> List:
  """
  """
  quotes = get_all_quotes()
  result = []
  for page in quotes:
    for quote in range(29):
      if quotes[f"{page}"]["content"][f"{quote}"]["name"].lower(
      ) == name.lower():
        result.append(quotes[f"{page}"]["content"][f"{quote}"])
  return result


def get_quote_by_tag(tag: str) -> List:
  """
  """
  quotes = get_all_quotes()
  result = []
  for page in quotes:
    for quote in range(29):
      if tag.lower() in quotes[f"{page}"]["content"][f"{quote}"]["tags"]:
        result.append(quotes[f"{page}"]["content"][f"{quote}"])
  return result

