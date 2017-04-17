import unittest
import ebury


class TestCase(unittest.TestCase):

    def setUp(self):
        ebury.app.config["TESTING"] = True
        self.app = ebury.app.test_client()

    def test_get_mainpage(self):
        page = self.app.post("/", data=dict(name="Ebury"))
        assert page.status_code == 200
        assert 'Hello' in str(page.data)
        assert 'Ebury' in str(page.data)

    def test_html_escaping(self):
        page = self.app.post("/", data=dict(name='"><b>TEST</b><!--'))
        assert '<b>' not in str(page.data)


if __name__ == '__main__':
    unittest.main()
