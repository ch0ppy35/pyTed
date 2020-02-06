from app import app
import unittest, logging
from config import TestingConfig

from app.routes import scheduler


class FlaskpyTedTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.disable(logging.CRITICAL)
        app.config.from_object(TestingConfig)
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

    def test_host_variable(self):
        self.assertEqual(app.config['HOST'], "demo.theenergydetective.com")

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_rtkw(self):
        result = self.app.get('/rtkw')
        self.assertEqual(result.status_code, 200)

    def test_about(self):
        result = self.app.get('/about')
        self.assertEqual(result.status_code, 200)

    def test_bills(self):
        result = self.app.get('/bills')
        self.assertEqual(result.status_code, 200)

    def test_billData(self):
        result = self.app.get('/billData')
        # Need more infor on billid variable
        #self.assertEqual(result.status_code, 200)
        self.assertEqual(result.status_code, 302)

    def test_runtasks(self):
        result = self.app.get('/billData')
        self.assertEqual(result.status_code, 302)