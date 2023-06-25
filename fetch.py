from typing import List
import re
import bs4 as _bs4
import requests as _requests


def _generate_url(page: int) -> str:
  """
  """
  url = f"https://www.goodreads.com/quotes?page={page}"
  return url


def _get_page_url(url: str) -> _bs4.BeautifulSoup:
  """
  """
  page = _requests.get(url)
  soup = _bs4.BeautifulSoup(page.content, "html.parser")
  return soup


def popular_quotes(page: int) -> List[str]:
  """
  """
  url = _generate_url(page)
  page = _get_page_url(url)

  raw_quotes = page.find_all(class_="quote")
  quotes = [quote.text for quote in raw_quotes]
  output = dict()
  for i in range(len(quotes)):
    encode = quotes[i].encode(encoding="UTF-8", errors="ignore").decode()
    clean_text = " ".join([word for word in encode.split()])
    if "tags:" in clean_text:
      output[i] = {
        "quote":
        clean_text[clean_text.index("“"):clean_text.index("”") + 1],
        "name":
        clean_text[clean_text.index("”") + 4:clean_text.index("tags:") - 1],
        "tags":
        clean_text[clean_text.index("tags:") + 5:clean_text.
                   index(re.findall("[0-9]+", clean_text)[0])].split(),
        "likes":
        re.findall("[0-9]+", clean_text)[0]
      }
    else:
      output[i] = {
        "quote":
        clean_text[clean_text.index("“"):clean_text.index("”") + 1],
        "name":
        clean_text[clean_text.index("”") +
                   4:clean_text.index(re.findall("[0-9]+", clean_text)[0])],
        "tags":
        "no tags",
        "likes":
        re.findall("[0-9]+", clean_text)[0]
      }
  return output
