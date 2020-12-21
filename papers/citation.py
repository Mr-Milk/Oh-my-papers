from .base import doi_validator, request_parser
from papers.result import Citation

CITATION_URL = "http://api.citeas.org/product/"


def get_citation(doi: str):
    doi = doi_validator(doi)

    url = f"{CITATION_URL}{doi}"

    result = request_parser(url)

    meta = Citation()
    meta.doi = doi

    meta.apa = result['citations'][0]['citation']
    meta.harvard = result['citations'][1]['citation']
    meta.nature = result['citations'][2]['citation']
    meta.modern = result['citations'][3]['citation']
    meta.chicago = result['citations'][4]['citation']
    meta.vancouver = result['citations'][5]['citation']

    return meta
