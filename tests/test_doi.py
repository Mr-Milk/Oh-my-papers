import pytest

from papers import doi, get_citation


def test_doi():
    mydoi = '10.1109/5.771073'
    result = doi(mydoi)
    assert result.title is not None
    assert result.author is not None
    assert result.doi is not None


def test_citation():
    mydoi = '10.1109/5.771073'
    get_citation(mydoi)
