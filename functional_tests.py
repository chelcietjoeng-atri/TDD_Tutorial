from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
# Optional: Use WebDriverWait for better reliability
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # She enters "Buy peacock feathers"
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # Optional: more robust than time.sleep
        # WebDriverWait(self.browser, 10).until(
        #     EC.presence_of_element_located((By.ID, "id_list_table"))
        # )

        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # She enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table("1: Buy peacock feathers")
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")

        # Test finished, asserting that both items exist
        self.assertTrue(True)  # This line confirms the test should pass


if __name__ == '__main__':
    unittest.main()
