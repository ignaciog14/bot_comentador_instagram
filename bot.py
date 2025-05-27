#bot
#PARA USAR:
#0. CONFIGURAR ARCHIVO lista_nombres.py
#1. ABRIR LA PAGINA DE INSTAGRAM
#2. CORRER EL CODIGO
#3. (SELENIUM CHANGE) ENSURE YOU ARE LOGGED IN AND HANDLE COOKIE POPUPS.
#4. ESPERAR QUE EL BOT TERMINE DE COMENTAR

import configparser
import random
import time
from comentarios_nombres import combinaciones_formato as cf
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Instagram Comment Bot starting...")

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

comment_delay = int(config['General']['comment_delay'])
post_url = config['General']['post_url']

print(f"Loaded configuration: Comment delay set to {comment_delay} seconds. Post URL: {post_url}")

print("The bot will open Instagram. Please ensure you are already logged in. You may also need to manually handle cookie consent pop-ups if they appear, before the bot can start commenting.")

# Initialize WebDriver
# Assuming chromedriver is in PATH or same directory
print(f"Navigating to post: {post_url}")
driver = webdriver.Chrome()
driver.get(post_url)

for comentario in cf:
    print(f"Attempting to post comment: {comentario}")
    try:
        comment_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[aria-label="Add a comment…"]'))
        )
    except:
        # Fallback if the primary selector fails (Instagram might change its UI)
        try:
            comment_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Add a comment…"]'))
            )
        except Exception as e:
            print(f"Error finding comment box: {e}")
            print("Please ensure you are logged into Instagram and the post page is correct.")
            print("You might also need to accept cookies if prompted by Instagram.")
            print("Skipping this comment.")
            # Optionally, take a screenshot for debugging
            # driver.save_screenshot('debug_screenshot_comment_box.png')
            continue # Skip to next comment or handle error appropriately
    
    comment_box.click() # Click to focus
    comment_box.send_keys(comentario)
    comment_box.send_keys(Keys.RETURN)
    print("Comment posted successfully.")
    time.sleep(comment_delay)

print("All comments posted. Closing browser.")
driver.quit()
