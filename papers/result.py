from dataclasses import dataclass

from typing import Optional


@dataclass
class Paper:

    doi: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None
    references_count: Optional[int] = None
    url: Optional[str] = None
    raw: Optional[dict] = None


@dataclass
class Citation:

    doi: Optional[str] = None
    apa: Optional[str] = None
    harvard: Optional[str] = None
    nature: Optional[str] = None
    modern: Optional[str] = None
    chicago: Optional[str] = None
    vancouver: Optional[str] = None
