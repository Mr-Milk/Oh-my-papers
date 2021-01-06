# Oh-my-papers

The tool that help you **search**, **download**, **cite**
your research literatures.

## Quick Start

### Command Line Usage
```shell
papers search --keywords "covid-19" --download --cite "apa"
```

### Write your own code
```python
import papers as pp

# For crossref search, include your email can have a better experience
from papers import Config
Config.email = "your@email.com"

covid_papers = pp.search(keywords="covid-19")

covid_papers.download()

covid_papers.cite(style='apa', to_clipboard=True)

covid_papers.citation_file(format="endnote")

```

To create citations

```python
from papers import Citation

c = Citation(doi=["doi1", "doi2"])
c.cite(style="chicago")
c.citation_file(format="bibtex")
```

## Installation

Requirement: Python >= 3.6

> Still in development, none of the following will work

### PIP
```shell
pip install oh-my-papers
```

### MacOS

```shell
brew install oh-my-papers
```

### Windows

```shell
choco install oh-my-papers
```

## Note on usage

If you are going to use the download function,
We strongly recommend that you should only download 
a reasonable amount of papers without exceeding the
daily limitation set by the publisher. Otherwise, it
might cause the service temporally unavailable throughout
your facilities and might get you and your facilities into
legal suit.

If you want to do some text mining, please contact each
publisher for special service.

## Legal Statement

This software (Oh-my-papers and it's related software) utilizes free public API to acquire DOI metadata,
And damage or illegal behaviour by using this software is responsible by the user, 
not by the developers of Oh-my-papers or the GitHub.
