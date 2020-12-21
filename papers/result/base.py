import requests
import webbrowser
from pathlib import Path
from typing import Optional, Union


class ResultBase:

    doi: Optional[str] = None
    title: Optional[str] = None
    download_url: Optional[str] = None

    def cite(self, style="apa"):
        pass

    def view(self):
        """
        View paper in browser

        """
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
