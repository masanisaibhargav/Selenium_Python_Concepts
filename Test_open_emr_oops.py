import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Open_emr():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://demo.openemr.io/a/openemr")
    def login(self):
        self.driver.find_element(By.ID, "authUser").send_keys("admin")
        self.driver.find_element(By.ID, "clearPass").send_keys("pass")
        select_lan = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_lan.select_by_visible_text("English (Indian)")
        self.driver.find_element(By.ID, "login-button").click()

class Add_Patient(Open_emr):
    def Patient(self):
        return 0

    def Patient(self):
        self.driver.find_element(By.XPATH, "//div[@class='menuLabel px-1 dropdown-toggle oe-dropdown-toggle']").click()
        self.driver.find_element(By.XPATH, "//div[text()='New/Search']").click()
        self.driver.switch_to.frame("pat")
        self.driver.find_element(By.ID, "form_fname").send_keys("Sai")
        self.driver.find_element(By.ID, "form_mname").send_keys("Bhargav")
        self.driver.find_element(By.ID, "form_lname").send_keys("Reddy")
        self.driver.find_element(By.ID, "form_suffix").send_keys("Masani")
        self.driver.find_element(By.NAME, "form_DOB").send_keys("29-05-2001")
        select_Gender = Select(self.driver.find_element(By.NAME, 'form_sex'))
        select_Gender.select_by_visible_text('Male')
        self.driver.find_element(By.ID, "create").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("modalframe")
        self.driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()


    def ele(self):
        try:
            self.driver.find_element(By.ID, "authUUser").click()

        except:
            print("Invalid id")

@pytest.fixture
def obj():
    return Add_Patient()

def test_Patient(obj):
    obj.login()
    obj.Patient()

def test_ele(obj):
    obj.login()
    obj.ele()