import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from decouple import config



class GitBot():
    def __init__(self):
        self.driver = webdriver.Safari()
        self.USER = config('GIT_USER')
        self.PASSWORD = config('GIT_PASSWORD')
        self.PROJECT_NAME = sys.argv[1]
        self.TOKEN=config('TOKEN')


    def login(self):
        # Load login page
        self.driver.get('http://www.github.com/login')
        # Fill login field
        self.driver.find_element_by_xpath("//*[@id='login_field']").send_keys(self.USER)
        # Fill password field
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(self.PASSWORD)
        # Click login
        self.driver.find_element_by_xpath("//*[@id='login']/div[4]/form/input[14]").click()
        
        self.timeout()
        return


    def new_repository(self):
        # Find 'new' repository button
        self.driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()
        self.timeout()
        # Fill repository name field
        self.driver.find_element_by_xpath('//*[@id="repository_name"]').send_keys(self.PROJECT_NAME)
        
        # # Mark repository private
        # self.find_element_by_xpath('//*[@id="repository_visibility_private"]').click()
        # WebDriverWait(self.driver, 3)
        
        # Submit button
        self.driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button').click()
        
        self.timeout()
        return


    def timeout(self):
        timeout = 3
        try:
            element_present = EC.presence_of_element_located((By.ID, 'main'))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print("Loading page...")
        finally:
            print("Done")

        
if __name__ == "__main__":
    git = GitBot()
    git.login()
    git.new_repository()

