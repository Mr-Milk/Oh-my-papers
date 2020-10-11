
'''
class Query:
    def __init__(self,DOI):
        self.DOI = DOI



    def getinf(self):
        url = "https://api.crossref.org/works/" + self.DOI
        r = requests.get(url)
        return r.text
'''

import requests

import json


class Query:

    def getinf(doi):
        url = "https://api.crossref.org/works/" + doi
        r = requests.get(url)
        text_python = json.loads(r.text)
        return text_python








