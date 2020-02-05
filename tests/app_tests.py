from app import app
import unittest, logging

from app.routes import scheduler


class FlaskpyTedTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.disable(logging.CRITICAL)
        pass

    @classmethod
    def tearDownClass(cls):
        if scheduler.running:
            scheduler.shutdown()
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_rtkw(self):
        result = self.app.get('/rtkw')
        self.assertEqual(result.status_code, 200)