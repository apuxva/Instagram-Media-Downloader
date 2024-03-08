from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import time
from selenium.webdriver.chrome.service import Service
# script1.py
import sys

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    print(f"Received input in Script 1: {user_input}")
else:
    print("No input provided to Script 1")



class ImageScraperSelenium:
    def __init__(self):
                
        service = Service(executable_path='C:/Users/VAISHNAVI/Desktop/Internship/chromedriver-win64/chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)# This instance will be used to log into LinkedIn
        self.driver.get(user_input)
        # time.sleep(5)

        # username = self.driver.find_element(By.ID, "username")
        # username.send_keys("vaishnavisavadhut@gmail.com") 

        # pword = self.driver.find_element(By.ID, "password")
        # pword.send_keys("$ecret9689")	 

        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # time.sleep(5)

        # self.driver.get("https://www.linkedin.com/in/riya-dangra-a22325213/")
        time.sleep(3)
        self.image_folder = 'images_selenium'
        os.makedirs(self.image_folder, exist_ok=True)

    def fetch_image_urls(self):
        # driver = webdriver.Chrome()
        # driver.get(self.url)
        time.sleep(5)


        
        try:
             article  = self.driver.find_element(By.TAG_NAME,'article')
             img = article.find_element(By.TAG_NAME,'img')
             self.img_url = [img.get_attribute('src') if img.get_attribute('src') else None]
             print(self.img_url)
        except Exception as e:
                print(f"An error occurred: {e}")

        finally:
                self.driver.quit()

        # try:
        #      img_element  = driver.find_element(By.TAG_NAME,'img')
        #      self.img_url = [img_element.get_attribute('src') if img_element.get_attribute('src') else None]
        #      print(self.img_url)
        # div = section.find_element(By.CLASS_NAME,'mt2.relative')
        # name = div.find_element(By.TAG_NAME,'h1').text
        # print(name)

    def save_image_from_url(self):
        if self.img_url:
            try:
                response = requests.get(self.img_url[0])
                response.raise_for_status()  # Raise an HTTPError for bad responses
                image = Image.open(BytesIO(response.content))
                filename = "insta_image.jpg"  # add file extension
                image.save(os.path.join(self.image_folder, filename), "JPEG")
                print("Image saved successfully.")
            except requests.exceptions.HTTPError as errh:
                print(f"HTTP Error: {errh}")
            except requests.exceptions.ConnectionError as errc:
                print(f"Error Connecting: {errc}")
            except requests.exceptions.Timeout as errt:
                print(f"Timeout Error: {errt}")
            except requests.exceptions.RequestException as err:
                print(f"Request Exception: {err}")
            except UnidentifiedImageError:
                print("The fetched content is not a recognized image format.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Image URL is empty. Make sure to fetch the URL first.")




url_to_scrape = user_input
scraper = ImageScraperSelenium()
scraper.fetch_image_urls()
scraper.save_image_from_url()

