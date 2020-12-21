from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor

from typing import Optional


@dataclass
class Paper:
    doi: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None
    references_count: Optional[int] = None
    url: Optional[str] = None
    raw: Optional[dict] = None


class PaperCollections:

    papers = None

    def download(self, directory):
        with ThreadPoolExecutor() as pool:
            for paper in self.papers:
                pool.submit(paper.download, directory=directory)

    def cite(self):
        pass

    def citation_files(self):
        pass
