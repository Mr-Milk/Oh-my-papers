from dataclasses import dataclass, field

from typing import Optional, List


@dataclass
class Contributor:

    family: str
    given: Optional[str] = field(default=None)
    full_name: Optional[str] = field(default=None)
    orcid: Optional[str] = field(default=None)
    affiliation: Optional[List[str]] = field(default=None)

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

    @staticmethod
    def from_dict(obj):
        return Contributor(
            family=obj['family'],
            given=obj.get('given'),
            orcid=obj.get('ORCID'),
            affiliation=obj.get('affiliation')
        )


