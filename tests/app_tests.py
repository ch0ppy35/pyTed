from app import app
from app.chores import cronTasks
from config import TestingConfig
from app.routes import scheduler
from app.tools import getInfo, scraper
import unittest, xmlunittest, logging


class FlaskpyTedTests(unittest.TestCase, xmlunittest.XmlTestMixin):

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

    def test_testing_variable(self):
        self.assertEqual(app.config['TESTING'], True)

    def test_host_variable(self):
        self.assertEqual(app.config['HOST'], "demo.theenergydetective.com")

    def test_disallowed(self):
        result = self.app.get('/routes')
        self.assertEqual(result.status_code, 404)

    def test_500s(self):
        with self.assertRaises(Exception):
            result = self.app.get('/billData?billid=foo')

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
        result = self.app.get('/billData?billid=2')
        self.assertEqual(result.status_code, 200)

    def test_runtasks(self):
        result = self.app.get('/runtasks')
        self.assertEqual(result.status_code, 302)

    def test_scraper(self):
        data = scraper.goget()
        self.assertXmlDocument(data)

    def test_scheduler(self):
        meterRead = app.config['METERREAD']
        scheduler.add_job(
            getInfo.getData,
            trigger='cron',
            second='*/30',
            max_instances=1
        )
        scheduler.add_job(
            cronTasks.dailyTasks,
            trigger='cron',
            hour='23',
            minute='59'
        )
        scheduler.add_job(
            cronTasks.weeklyTasks,
            trigger='cron',
            day_of_week='sun',
            hour='0',
            minute='0'
        )
        scheduler.add_job(
            cronTasks.monthlyTasks,
            trigger='cron',
            day='%(s)s' % {'s': meterRead},
            hour='0',
            minute='0'
        )
        scheduler.start()
        self.assertEqual(scheduler.running, True)
