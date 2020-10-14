from .base import doi_validator, request_parser
from .result import CitationResult

CITATION_URL = "http://api.citeas.org/product/"


def get_citation(doi: str):
    doi = doi_validator(doi)

    url = f"{CITATION_URL}{doi}"

    result = request_parser(url)

    meta = CitationResult()
    meta.doi = doi

    meta.apa = result['citations'][0]
    meta.harvard = result['citations'][1]
    meta.nature = result['citations'][2]
    meta.modern = result['citations'][3]
    meta.chicago = result['citations'][4]
    meta.vancouver = result['citations'][5]

    return meta
