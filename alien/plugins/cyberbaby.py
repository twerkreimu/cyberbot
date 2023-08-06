from pyrogram import Client, filters
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")
GOOGLE_CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")

@Client.on_message(filters.command(["gobitch"]))
async def gobitch(bot, message):
    url = message.text.split(None, 1)[1]
    if len(message.command) != 2:
        await message.reply_text("/gobitch link")
        return
    await message.reply_text("Got link, doing further process")
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument('--window-size=1920x1080')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    prefs = {'download.default_directory': './'}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)

    driver.get(url)

    total_height = driver.execute_script("return document.body.scrollHeight")

    total_time = 240

    scroll_increment = total_height / total_time

    start_time = time.time()
    
    while time.time() - start_time < total_time:
        driver.execute_script(f"window.scrollBy(0, {scroll_increment});")  
        time.sleep(2)
    driver.quit()
    await message.reply_text("Successfully done my love!")