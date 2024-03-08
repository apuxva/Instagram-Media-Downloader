import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
# import urllib.request
from PIL import Image
from io import BytesIO
import sys

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    print(f"Received input in Script 2: {user_input}")
else:
    print("No input provided to Script 2")


driver = webdriver.Chrome()
driver.get("http://www.instagram.com")
driver.maximize_window()

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
username.send_keys("coinswitch93")
password.clear()
password.send_keys("shift@enter")

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


driver.get("https://www.instagram.com/explore/tags/" + user_input + "/")

time.sleep(3)
n_scrolls = 1
img_links = []
time.sleep(3)


for i in range(0, n_scrolls):
    anchors = driver.find_elements(By.TAG_NAME, 'a')
    anchors = [a.get_attribute('href') for a in anchors]
    anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]
    img_links += anchors

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

print('Found ' + str(len(img_links)) + ' links to images')
images = []

for a in img_links:
    driver.get(a)
    time.sleep(8)
    article  = driver.find_element(By.TAG_NAME,'article')
    img = article.find_element(By.TAG_NAME, 'img')
    img_url = img.get_attribute('src') if img.get_attribute('src') else None
    images.append(img_url)

print(images)

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
image_folder = os.path.join(desktop_path, f"{user_input}_images")
os.makedirs(image_folder, exist_ok=True)

for i, url in enumerate(images):
    response = requests.get(url)
    if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                filename = user_input+f"_{i + 1}.jpg"
                filepath = os.path.join(image_folder, filename)
                image.save(filepath, "JPEG")
                print(f"Image {i + 1} saved successfully at {image_folder}/{filename}")
    else:
                print(f"Failed to retrieve image {i + 1}. Status code: {response.status_code}")



driver.quit()
