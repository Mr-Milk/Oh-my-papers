from papers.base import request_get


def citation_styles():
    return request_get("https://citation.crosscite.org/styles/")


def citation_locals():
    return request_get("https://citation.crosscite.org/locals/")


class Citation:
    pass
