import pytest
from _pytest.runner import runtestprotocol
from appium import webdriver
from ctreport_selenium.ctlistener import Session, Test
import configfile
from pathlib import Path


def pytest_sessionstart(session):
    import os
    if os.path.isdir(str(Path(__file__).parent) + r"/reports/" + "dailyreport/"):
        import shutil
        shutil.rmtree(str(Path(__file__).parent) + r"/reports/" + "dailyreport/")


@pytest.fixture(scope="session", autouse=True)
def getdriver(request, server_url):
    driver = webdriver.Remote(server_url, configfile.desired_caps)
    driver.implicitly_wait(30)

    Session.start(test_execution_name="Android Test Automation Report",
                  path=str(Path(__file__).parent) + r"/reports/",
                  driver=driver,
                  config_file=str(Path(__file__).parent) + "/reportconfig.json")

    def driver_quit():
        driver.quit()

    request.addfinalizer(driver_quit)
    return driver


def pytest_runtest_protocol(item, nextitem):
    global test
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when == 'setup':
            test = item.cls.test
        if report.when == 'call':
            if report.outcome == 'skipped':
                test.skip(report.longrepr[2])
            if report.outcome == 'failed':
                test.broken(report.longrepr.reprcrash.message)
            # if report.when == 'teardown':
            test.finish()
    temp = ""
    try:
        temp = nextitem.nodeid.split("::")[0]
    except Exception:
        pass
    if nextitem is None or temp != item.nodeid.split("::")[0]:
        Session.end(item.nodeid.split("::")[0].replace("test_", "").replace(".py", "").replace("tests/", ""))
        Session._tests.clear()
        Test._temp_verify_id = 0
        Test._temp_assert_id = 0
        Test._temp_error_id = 0
        Test._temp_screenshot_id = 0
        Test._temp_test_id = 0
        Test._id_li = 0
        Test._id_li = 0
    return False


# def pytest_sessionfinish(session):
# Session.end()


@pytest.fixture(scope="session")
def server_url(request):
    return request.config.getoption("-S")


def pytest_addoption(parser):
    parser.addoption("-S", "--server_url",
                     dest="url",
                     default=configfile.server_url,
                     help="command_executor url i.e. Appium server url")
