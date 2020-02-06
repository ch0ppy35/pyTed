## Tests

I run app_tests within pyCharm.  
Will need to figure out how to automate, and get more tests added.


Here's some output.  We'll need to look into some of the warnings...


Gotta do this if testing outside of pyCharm.  
```
$echo $PYTHONPATH                                              
/Users/mmiller/Projects/pyTed:/Users/mmiller/Projects/pyTed/app:/Users/mmiller/Projects/pyTed/tests
```

TravisCI has a setup we can use this and [this.](https://github.com/gothinkster/flask-realworld-example-app/blob/master/.travis.yml)
```
env: PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/tests:$TRAVIS_BUILD_DIR/foop

```

Here's how to run with pytest
`python -m pytest --rootdir=/Users/mmiller/Projects/pyTed tests/app_tests.py` 

```
(venv) [mmiller@Mikes-MBP pyTed (dev)]$ python -m pytest --rootdir=/Users/mmiller/Projects/pyTed tests/app_tests.py
======================================================================================== test session starts ========================================================================================
platform darwin -- Python 3.7.6, pytest-5.3.4, py-1.8.1, pluggy-0.13.1
rootdir: /Users/mmiller/Projects/pyTed
collected 7 items                                                                                                                                                                                   

tests/app_tests.py .......                                                                                                                                                                    [100%]

========================================================================================= warnings summary ==========================================================================================
tests/app_tests.py::FlaskpyTedTests::test_about
tests/app_tests.py::FlaskpyTedTests::test_about
tests/app_tests.py::FlaskpyTedTests::test_about
  /Users/mmiller/Projects/pyTed/app/tools/getInfo.py:12: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
    voltageNow = (float(root.getchildren()[2].getchildren()[0].getchildren()[0].text) / 10)

tests/app_tests.py::FlaskpyTedTests::test_about
tests/app_tests.py::FlaskpyTedTests::test_about
tests/app_tests.py::FlaskpyTedTests::test_about
  /Users/mmiller/Projects/pyTed/app/tools/getInfo.py:13: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
    wattsNow = (float(root.getchildren()[3].getchildren()[0].getchildren()[0].text) / 1000)

tests/app_tests.py::FlaskpyTedTests::test_about
tests/app_tests.py::FlaskpyTedTests::test_about
tests/app_tests.py::FlaskpyTedTests::test_about
  /Users/mmiller/Projects/pyTed/app/tools/getInfo.py:14: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
    kwhTotalNow = (float(root.getchildren()[3].getchildren()[0].getchildren()[2].text) / 1000)

-- Docs: https://docs.pytest.org/en/latest/warnings.html
=================================================================================== 7 passed, 9 warnings in 3.03s ===================================================================================
(venv) [mmiller@Mikes-MBP pyTed (dev)]$ 
```

And in pyCharm debugger

```
Testing started at 21:21 ...
/Users/mmiller/Projects/pyTed/venv/bin/python /Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm/_jb_pytest_runner.py --target app_tests.py::FlaskpyTedTests
Launching pytest with arguments app_tests.py::FlaskpyTedTests in /Users/mmiller/Projects/pyTed/tests

============================= test session starts ==============================
platform darwin -- Python 3.7.6, pytest-5.3.4, py-1.8.1, pluggy-0.13.1 -- /Users/mmiller/Projects/pyTed/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/mmiller/Projects/pyTed
collecting ... collected 7 items

app_tests.py::FlaskpyTedTests::test_about 
app_tests.py::FlaskpyTedTests::test_billData 
app_tests.py::FlaskpyTedTests::test_bills 
app_tests.py::FlaskpyTedTests::test_home_status_code 
app_tests.py::FlaskpyTedTests::test_host_variable 
app_tests.py::FlaskpyTedTests::test_rtkw 
app_tests.py::FlaskpyTedTests::test_runtasks 

=============================== warnings summary ===============================
tests/app_tests.py::FlaskpyTedTests::test_about
tests/app_tests.py::FlaskpyTedTests::test_about
tests/app_tests.py::FlaskpyTedTests::test_about
  /Users/mmiller/Projects/pyTed/app/tools/getInfo.py:12: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
    voltageNow = (float(root.getchildren()[2].getchildren()[0].getchildren()[0].text) / 10)

tests/app_tests.py::FlaskpyTedTests::test_about
tests/app_tests.py::FlaskpyTedTests::test_about
tests/app_tests.py::FlaskpyTedTests::test_about
  /Users/mmiller/Projects/pyTed/app/tools/getInfo.py:13: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
    wattsNow = (float(root.getchildren()[3].getchildren()[0].getchildren()[0].text) / 1000)

tests/app_tests.py::FlaskpyTedTests::test_about
tests/app_tests.py::FlaskpyTedTests::test_about
tests/app_tests.py::FlaskpyTedTests::test_about
  /Users/mmiller/Projects/pyTed/app/tools/getInfo.py:14: DeprecationWarning: This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.
    kwhTotalNow = (float(root.getchildren()[3].getchildren()[0].getchildren()[2].text) / 1000)

-- Docs: https://docs.pytest.org/en/latest/warnings.html
======================== 7 passed, 9 warnings in 3.08s =========================

Process finished with exit code 0
PASSED                      [ 14%]
PASSED                      [ 28%]
PASSED                      [ 42%]
PASSED                      [ 57%]
PASSED                      [ 71%]
PASSED                      [ 85%]
PASSED                      [100%]
```