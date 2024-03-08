from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import time
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

# script1.py
import sys

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    print(f"Received input in Script 1: {user_input}")
else:
    print("No input provided to Script 1")


# user_input="https://www.instagram.com/p/C16d0ggPiJg/"
class ImageScraperSelenium:
    def __init__(self):
                
        service = Service(executable_path='C:/Users/VAISHNAVI/Desktop/Internship/chromedriver-win64/chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get(user_input)
       
        time.sleep(3)
        self.image_folder = 'images_selenium'
        os.makedirs(self.image_folder, exist_ok=True)

    def fetch_vdo_img_url(self):
        
        time.sleep(5)
   
        try:
             article  = self.driver.find_element(By.TAG_NAME,'article')
             time.sleep(3)
             try:
                    video = article.find_element(By.TAG_NAME, 'video')
                    self.vdo_url = video.get_attribute('src') if video.get_attribute('src') else None
                    print(self.vdo_url)
                    scraper.save_vdo_from_url()
             except NoSuchElementException:
                    img = article.find_element(By.TAG_NAME, 'img')
                    self.img_url = [img.get_attribute('src') if img.get_attribute('src') else None]
                    print(self.img_url)
                    scraper.save_image_from_url()


        except Exception as e:
                print(f"An error occurred: {e}")

        finally:
                self.driver.quit()

       

    def save_vdo_from_url(self):
        if self.vdo_url:
            try:
                response = requests.get(self.vdo_url)
                response.raise_for_status()  # Raise an HTTPError for bad responses
                response = requests.get(self.vdo_url, stream=True)

                if response.status_code == 200:
                    local_filepath = "C:/Users/VAISHNAVI/Desktop/books_images/video.mp4"  # Replace with the desired local file path

                    with open(local_filepath, 'wb') as file:
                        for chunk in response.iter_content(chunk_size=1024):
                            if chunk:
                                file.write(chunk)

                    print(f"Video downloaded successfully to: {local_filepath}")

                else:
                    print(f"Failed to retrieve the video. Status code: {response.status_code}")

            except requests.exceptions.HTTPError as errh:
                print(f"HTTP Error: {errh}")
            except requests.exceptions.ConnectionError as errc:
                print(f"Error Connecting: {errc}")
            except requests.exceptions.Timeout as errt:
                print(f"Timeout Error: {errt}")
            except requests.exceptions.RequestException as err:
                print(f"Request Exception: {err}")
            
            except Exception as e:
                print(f"An error occurred v: {e}")
        else:
            print("Image URL is empty. Make sure to fetch the URL first.")


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
                print(f"An error occurred i: {e}")
        else:
            print("Image URL is empty. Make sure to fetch the URL first.")


        

url_to_scrape = user_input
scraper = ImageScraperSelenium()
scraper.fetch_vdo_img_url()
