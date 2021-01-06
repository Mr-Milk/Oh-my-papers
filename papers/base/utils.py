# try import ujson for faster json serialization
try:
    import ujson as json
except ImportError:
    import json

from typing import List


def JsonEncoder(*args, **kwargs):
    json.loads(*args, **kwargs)


def field_check(field: List):
    if len(field) == 0:
        return None
    else:
        return field
