
from app_main import app
from tests import OhmTestCase


class CommunityTest1(OhmTestCase):
    def test_get(self):
        with app.test_client() as c:
            response = c.get('/community')
            self.assertEqual(response.status_code, 200)


class CommunityTest2(OhmTestCase):
    def test_get(self):
        with app.test_client() as c:
            response = c.get('/community')
            assert "Chuck" in response.data

class CommunityTest3(OhmTestCase):
    def test_get(self):
        with app.test_client() as c:
            response = c.get('/community')
            assert "USA" in response.data

class CommunityTest4(OhmTestCase):
    def test_get(self):
        with app.test_client() as c:
            response = c.get('/community')
            assert "Silver" in response.data
