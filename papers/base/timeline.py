from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Timeline:
    accepted: Optional[datetime] = field(default=None)
    available: Optional[datetime] = field(default=None)
    printed: Optional[datetime] = field(default=None)
    online: Optional[datetime] = field(default=None)

