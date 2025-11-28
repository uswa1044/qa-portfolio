import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="session")
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option("detach", True)  # <-- keeps browser open

    driver = webdriver.Chrome(service=service,options=options)
    driver.maximize_window()
    yield driver

class SauceDemo:
    @pytest.mark.parametrize("username, password, expected_url, expected_error", [
        ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html", None),
        ("locked_out_user", "secret_sauce", None, "Sorry, this user has been locked out.")
    ])
    def test_login(self, driver, username, password, expected_url, expected_error):
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        if expected_error:
            assert expected_error in driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        else:
            assert driver.current_url == expected_url

    def test_add_to_cart(self, driver):
        # add 1st iteam to cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"
        #  add 2nd item to cart
        driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bike-light"]').click()  # by Xpath
        # It will fail because we added 2 items and our expected count is 3
        actual_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert actual_count == "3", f"Expected cart count 3 but got {actual_count}"

    def test_complete_purchase(self, driver):
        # Add 2 items
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Go to cart & checkout
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        # Fill form
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        # calculated price is correct
        driver.find_element(By.ID, "finish").click()
        # Assert success
        assert driver.find_element(By.CLASS_NAME, "complete-header").text == "Thank you!"

