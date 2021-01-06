from .config import Config
from .search import search
from .paper import Paper, Papers
from .citation import Citation, citation_locals, citation_styles

import uvloop
uvloop.install()
