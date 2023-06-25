from typing import Dict
import fetch as _scraper
import json as _json


def create_quote_dict() -> Dict:
  """
  """
  quotes = dict()

  for page in range(101):
    if page not in quotes:
      quotes[page] = dict()

    quotes[page]["content"] = _scraper.popular_quotes(page)
  return quotes


def save_quotes():
  """
  """
  events = create_quote_dict()
  with open("quotes.json", mode="w") as events_file:
    _json.dump(events, events_file, ensure_ascii=False)
  return


# if __name__ == '__main__':
#   events = create_quote_dict()
#   with open("quotes.json", mode="w") as events_file:
#     _json.dump(events, events_file, ensure_ascii=False)
