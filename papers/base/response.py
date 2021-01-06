from datetime import datetime
from typing import Optional, List

from papers.paper import Paper
from .contributor import Contributor
from .funder import Funder
from .timeline import Timeline
from .utils import field_check


class DOIRecord:
    @staticmethod
    def to_datetime(v):
        if v is None:
            return None
        else:
            return datetime(*v['date-parts'][0])


class CrossrefDOIRecord(DOIRecord):
    def to_paper(self, obj) -> Paper:
        p = Paper(
            raw=obj,
            doi=obj['DOI'],
            title=obj['title'][0],
            publisher=obj['publisher'],
            references_count=obj['references-count'],
            cited_count=obj['is-referenced-by-count'],
            type=obj['type'],
            # optional field
            abstract=obj.get("abstract"),
            author=Contributor.from_dict(obj.get('author')),
            issue=obj.get('issue'),
            volume=obj.get('volume'),
            page=obj.get('page'),
        )

        t = Timeline(
            accepted=self.to_datetime(obj.get("accepted")),
            available=self.to_datetime(obj.get("issued")),
            printed=self.to_datetime(obj.get("published-print")),
            online=self.to_datetime(obj.get("published-online")),
        )

        p.member_id = obj.get('member')
        p.funder = field_check([Funder.from_dict(people) for people in obj.get('funder', [])])
        p.editor = field_check([Contributor.from_dict(people) for people in obj.get('editor', [])])
        issn_info = obj.get('issn-type', [])
        p.issn = field_check([i['value'] for i in issn_info]),
        p.issn_type = field_check([i['type'] for i in issn_info]),
        p.isbn = obj.get('ISBN'),
        p.subject = obj.get('subject')

        # handle link
        links = obj.get('link', [])
        for link in links:
            content_type = link['content-type']
            url = link['URL']
            download_url = None
            full_text_url = None
            if content_type == 'application/pdf':
                download_url = url
            elif content_type == 'application/html':
                full_text_url = url
            else:
                if link.endswith("pdf"):
                    download_url = url
                else:
                    full_text_url = url
            if download_url is not None:
                if p.download_url is not None:
                    p.download_url = url
            if full_text_url is not None:
                if p.download_url is not None:
                    p.download_url = download_url

        # clinical trail
        p.clinical_trial_number = field_check(
            [number['clinical-trial-number'] for number in obj.get('clinical_trail', [])])

        return p

    def get_contributor(self):
        pass


class DataciteDOIRecord:
    def to_paper(self):
        pass

    def get_contributor(self):
        pass


class MEDRADOIRecord:
    def to_paper(self):
        pass

    def get_contributor(self):
        pass
