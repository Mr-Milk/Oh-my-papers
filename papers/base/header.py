from typing import Optional


class HeaderBase:
    _header = None

    @property
    def header(self) -> dict:
        return self._header


class CrossrefHeader(HeaderBase):
    """
    Customize header for crossref request

    Args:
        token: Crossref Plus token
        email: Your email address, specific email address will give a stable performance
        limit: Number of request per second

    Attrs:
        header: Return the header object

    """

    token: Optional[str] = None
    email: Optional[str] = None
    limit: Optional[str] = None

    def __init__(self,
                 token: Optional[str] = None,
                 email: Optional[str] = None,
                 limit: Optional[str] = None
                 ):
        self.email = email
        self.limit = limit
        self._header = {"X-Rate-Limit-Interval": "1s"}
        if token is not None:
            self._header["Crossref-Plus-API-Token"] = f"Bearer {token}"
        if email is not None:
            self._header["User-Agent"] = f"mailto:{email}"
        if limit is not None:
            self._header['X-Rate-Limit-Limit'] = limit
        else:
            self._header['X-Rate-Limit-Limit'] = 50


class CitationHeader(HeaderBase):

    def __init__(self):
        pass
