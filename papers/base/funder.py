from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Funder:
    name: str
    doi: Optional[str] = field(default=None)
    award: Optional[List[str]] = field(default=None)

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    @staticmethod
    def from_dict(obj):
        if obj is None:
            return None
        else:
            return Funder(
                name=obj['name'],
                doi=obj.get('DOI'),
                award=obj.get('award')
            )
