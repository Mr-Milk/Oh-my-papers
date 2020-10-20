import unittest

from papers.query import doi
from papers.citation import get_citation
from papers.base import request_parser

class Test_function(unittest.TestCase):
    def setUp(self):
        print('setup数据准备阶段——————')

    def tearDown(self):
        print('teardown数据清理收尾阶段————')

    def test_doi(self):
        doi_example = '10.1109/5.771073'
        self.assertEqual(doi(doi_example).title, ['Toward unique identifiers'])
        self.assertEqual(doi(doi_example).author, [{'given': 'N.', 'family': 'Paskin', 'sequence': 'first', 'affiliation': []}])
        self.assertEqual(doi(doi_example).references_count, 65)
        self.assertEqual(doi(doi_example).doi, doi_example)
        self.assertEqual(doi(doi_example).URL, 'http://dx.doi.org/10.1109/5.771073')

    def test_citation(self):
        doi_example = '10.1109/5.771073'
        self.assertEqual(get_citation(doi_example).apa, {'citation': 'Paskin, N. (1999). Toward unique identifiers. <i>Proceedings of the IEEE</i>, <i>87</i>(7), 1208–1227. http://doi.org/10.1109/5.771073',
  'style_fullname': 'American Psychological Association 6th edition',
  'style_shortname': 'apa'} )

        self.assertEqual(get_citation(doi_example).harvard, {'citation': 'Paskin, N., 1999. Toward unique identifiers. <i>Proceedings of the IEEE</i>, 87(7), pp.1208–1227. Available at: https://doi.org/10.1109/5.771073.',
  'style_fullname': 'Harvard Reference format 1 (author-date)',
  'style_shortname': 'harvard1'})

        self.assertEqual(get_citation(doi_example).nature, {'citation': '1.Paskin, N.. Toward unique identifiers. <i>Proc. IEEE</i> <b>87,</b> 1208–1227 (1999).',
  'style_fullname': 'Nature',
  'style_shortname': 'nature'})

        self.assertEqual(get_citation(doi_example).modern, {'citation': 'Paskin, N.. “Toward Unique Identifiers”. <i>Proceedings of the IEEE</i> 87.7 (1999): 1208–1227. <i>Crossref</i>. Web. <https://doi.org/10.1109/5.771073>...',
  'style_fullname': 'Modern Language Association 7th edition (with URL)',
  'style_shortname': 'modern-language-association-with-url'})

        self.assertEqual(get_citation(doi_example).chicago, {'citation': 'Paskin, N.. 1999. “Toward Unique Identifiers”. <i>Proceedings of the IEEE</i> 87 (7). Institute of Electrical and Electronics Engineers (IEEE): 1208–27. doi:10.1109/5.771073.',
  'style_fullname': 'Chicago Manual of Style 16th edition (author-date)',
  'style_shortname': 'chicago-author-date'}）

        self.assertEqual(get_citation(doi_example).vancouver, {'citation': '1. Paskin N. Toward unique identifiers. Proc IEEE [Internet]. Institute of Electrical and Electronics Engineers (IEEE); 1999Jul;87(7):1208–27. Available from: https://doi.org/10.1109/5.771073',
  'style_fullname': 'Vancouver',
  'style_shortname': 'vancouver'})





if __name__ == '__main__':
    unittest.main()
