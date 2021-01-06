from datetime import datetime
from dataclasses import dataclass, field
from concurrent.futures import ThreadPoolExecutor
from typing import Optional, List, Union, Sequence
import webbrowser
from pathlib import Path

import requests
from papers.base import Contributor, Timeline


class PaperBase:
    doi: str
    title: str
    download_url: Optional[str] = None
    full_text_url: Optional[str] = None

    def cite(self, style="apa"):
        pass

    def view(self):
        """
        View paper in browser

        """
        if self.full_text_url is not None:
            webbrowser.open_new_tab(self.full_text_url)
        else:
            doi_url = f"https://doi.org/{self.doi}"
            webbrowser.open_new_tab(doi_url)

    def download(self,
                 name: Optional[str] = None,
                 directory: Union[Path, str, None] = None,
                 ):
        """
        Download the paper if applicable in current network environment

        Args:
            name: Default to the title, if not available, fallback to DOI.
            directory: Default to current directory

        """
        if name is None:
            if self.title is not None:
                name = f"{self.title}.pdf"
            else:
                name = f"{self.doi}.pdf"
        save_dir = Path(f"./{name}")
        if directory is not None:
            if isinstance(directory, str):
                directory = Path(directory)
            if not directory.exists():
                directory.mkdir(exist_ok=True, parents=True)
            save_dir = directory / name

        file = requests.get(self.download_url)
        with open(save_dir, "wb") as f:
            f.write(file.content)

        print(f"Download {name} complete!")


@dataclass
class Paper(PaperBase):
    """
    Instance to store information of a paper

    Attrs:
        doi: The Digital Object Identifier
        title: The title of the paper
        references_count: Number of reference in the paper

    """
    # ====== Required Field =======
    # the original info
    raw: dict
    # basic info of the paper
    doi: str
    title: str
    publisher: str
    cited_count: int
    type: str
    # ====== Optional Field =======
    # important info
    author: Optional[List[Contributor]] = field(default=None)
    abstract: Optional[List[str]] = field(default=None)
    # resource info
    download_url: Optional[str] = field(default=None)  # link -> URL where link -> content-type = application/pdf
    full_text_url: Optional[str] = field(default=None)  # link -> URL where link -> content-type = application/html
    # other info
    timeline: Optional[Timeline] = field(default=None)
    references_count: Optional[int] = field(default=None)
    issue: Optional[str] = field(default=None)
    volume: Optional[str] = field(default=None)
    page: Optional[str] = field(default=None)

    def __add__(self, other):
        if isinstance(other, Paper):
            return Papers([self, other])
        elif isinstance(other, Papers):
            return Papers([self] + other.papers)
        else:
            raise TypeError("You can only add Paper/Papers")


class Papers:
    papers: List[Paper]

    def __init__(self, papers):
        if isinstance(papers, Paper):
            self.papers = [papers]
        else:
            self.papers = papers

    def __add__(self, other):
        if isinstance(other, Paper):
            return Papers(self.papers + [other])
        elif isinstance(other, Papers):
            return Papers(self.papers + other.papers)
        else:
            raise TypeError("You can only add Paper/Papers")

    def download(self, directory):
        with ThreadPoolExecutor() as pool:
            for paper in self.papers:
                pool.submit(paper.download, directory=directory)

    def cite(self):
        pass

    def citation_files(self):
        pass
