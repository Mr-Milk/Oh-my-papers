import unittest

from papers.query import doi
from papers.citation import get_citation
from papers.base import request_parser

class Test_function(unittest.TestCase):
    def setUp(self):
        self.doi_example = '10.1109/5.771073'
        print('setup数据准备阶段——————')

    def tearDown(self):
        print('teardown数据清理收尾阶段————')

    def test_doi(self):
        self.assertEqual(doi(self.doi_example).title, ['Toward unique identifiers'])
        self.assertEqual(doi(self.doi_example).author, [{'given': 'N.', 'family': 'Paskin', 'sequence': 'first', 'affiliation': []}])
        self.assertEqual(doi(self.doi_example).references_count, 65)
        self.assertEqual(doi(self.doi_example).doi, doi_example)
        self.assertEqual(doi(self.doi_example).URL, 'http://dx.doi.org/10.1109/5.771073')

    def test_citation(self):

        self.assertEqual(get_citation(self.doi_example).apa,  'Paskin, N. (1999). Toward unique identifiers. <i>Proceedings of the IEEE</i>, <i>87</i>(7), 1208–1227. http://doi.org/10.1109/5.771073',)

        self.assertEqual(get_citation(self.doi_example).harvard, 'Paskin, N., 1999. Toward unique identifiers. <i>Proceedings of the IEEE</i>, 87(7), pp.1208–1227. Available at: https://doi.org/10.1109/5.771073.',)

        self.assertEqual(get_citation(self.doi_example).nature,  '1.Paskin, N.. Toward unique identifiers. <i>Proc. IEEE</i> <b>87,</b> 1208–1227 (1999).',)

        self.assertEqual(get_citation(self.doi_example).modern, 'Paskin, N.. “Toward Unique Identifiers”. <i>Proceedings of the IEEE</i> 87.7 (1999): 1208–1227. <i>Crossref</i>. Web. <https://doi.org/10.1109/5.771073>...',)

        self.assertEqual(get_citation(self.doi_example).chicago, 'Paskin, N.. 1999. “Toward Unique Identifiers”. <i>Proceedings of the IEEE</i> 87 (7). Institute of Electrical and Electronics Engineers (IEEE): 1208–27. doi:10.1109/5.771073.',)

        self.assertEqual(get_citation(self.doi_example).vancouver,  '1. Paskin N. Toward unique identifiers. Proc IEEE [Internet]. Institute of Electrical and Electronics Engineers (IEEE); 1999Jul;87(7):1208–27. Available from: https://doi.org/10.1109/5.771073',)





if __name__ == '__main__':
    unittest.main()
