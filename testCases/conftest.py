# cerating a fixture
import pytest
from selenium import webdriver



# for using particular browser we need to modify the configuration file
@pytest.fixture
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print('Launching Chrome')
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print('Lanching Firefox')

    return driver

def pytest_addoption(parser): # this will give value iin cmd like input
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # this will return the value in setup
    return request.config.getoption("--browser")

###### Pytest HTML Report  ######################
# this update is done for generation html reports
# It is the hook for adding enviroment info to HTML Reports
def pytest_configure(config):
    config._metadata['Project Name']='nop commerce'
    config._metadata['Module Name']='Customer'
    config._metadata['Tester'] = 'Suraj'

#It is the hook for delete or modify enviroment info to HTML
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)

# pytest -s -v -n=2 --html=Reports\testreport.html TestCases/test_login.py --browser chrome
