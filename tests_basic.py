import unittest
from app import app


class BasicTests(unittest.TestCase):
    def test_main_page(self):
        c = app.test_client()
        response = c.get('/', follow_redirects=True)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
