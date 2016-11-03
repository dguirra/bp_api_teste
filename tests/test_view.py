from ..my_app.views import test
import unittest

app = test()


class Test(unittest.TestCase):
    def test_request(self):
        response = self.app.get('/')
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
