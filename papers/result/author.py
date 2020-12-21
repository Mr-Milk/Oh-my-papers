from dataclasses import dataclass, field

from typing import Optional


@dataclass
class Author:

    family: str
    given: Optional[str] = field(default=None)
    full_name: Optional[str] = field(default=None)
    orcid: Optional[str] = field(default=None)
    affiliation: Optional[str] = field(default=None)

    def __eq__(self, other):
        if (self.orcid is not None) & (other.orcid is not None):
            if self.orcid == other.orcid:
                return True
            else:
                return False
        elif self.full_name == self.full_name:
            return None
        else:
            return False
