import requests
import json


def citation_styles():
    r = requests.get("https://citation.crosscite.org/styles/")
    styles = json.loads(r.text)
    return styles
