## Tests

I run app_tests within pyCharm.  
Will need to figure out how to automate, and get more tests added.


Here's some output.  We'll need to look into some of the warnings...

````
$`echo $PYTHONPATH                                              
/Users/mmiller/Projects/pyTed:/Users/mmiller/Projects/pyTed/app:/Users/mmiller/Projects/pyTed/tests
````


`python -m pytest --rootdir=/Users/mmiller/Projects/pyTed tests/app_tests.py` 

```
Testing started at 00:40 ...
/Users/mmiller/Projects/pyTed/venv/bin/python /Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm/_jb_pytest_runner.py --target app_tests.py::FlaskpyTedTests
Launching pytest with arguments app_tests.py::FlaskpyTedTests in /Users/mmiller/Projects/pyTed/tests

============================= test session starts ==============================
platform darwin -- Python 3.7.6, pytest-5.3.4, py-1.8.1, pluggy-0.13.1 -- /Users/mmiller/Projects/pyTed/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/mmiller/Projects/pyTed
collecting ... collected 2 items

app_tests.py::FlaskpyTedTests::test_home_status_code 
app_tests.py::FlaskpyTedTests::test_rtkw 

=============================== warnings summary ===============================
tests/app_tests.py::FlaskpyTedTests::test_home_status_code
tests/app_tests.py::FlaskpyTedTests::test_home_status_code
tests/app_tests.py::FlaskpyTedTests::test_home_status_code
  /Users/mmiller/Projects/pyTed/app/getInfo.py:11: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
    voltageNow = (float(root.getchildren()[2].getchildren()[0].getchildren()[0].text) / 10)

tests/app_tests.py::FlaskpyTedTests::test_home_status_code
tests/app_tests.py::FlaskpyTedTests::test_home_status_code
tests/app_tests.py::FlaskpyTedTests::test_home_status_code
  /Users/mmiller/Projects/pyTed/app/getInfo.py:12: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
    wattsNow = (float(root.getchildren()[3].getchildren()[0].getchildren()[0].text) / 1000)

tests/app_tests.py::FlaskpyTedTests::test_home_status_code
tests/app_tests.py::FlaskpyTedTests::test_home_status_code
tests/app_tests.py::FlaskpyTedTests::test_home_status_code
  /Users/mmiller/Projects/pyTed/app/getInfo.py:13: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
    kwhTotalNow = (float(root.getchildren()[3].getchildren()[0].getchildren()[2].text) / 1000)

-- Docs: https://docs.pytest.org/en/latest/warnings.html
======================== 2 passed, 9 warnings in 7.98s =========================

Process finished with exit code 0
PASSED                           [ 50%]
PASSED                           [100%]
```