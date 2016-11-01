from .main import test
import unittest

response = test()


class Test(unittest.TestCase):
    def test_request(self):
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
