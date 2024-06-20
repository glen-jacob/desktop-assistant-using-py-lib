from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class YouTubePlayer():
    def __init__(self):
        chrome_driver_path = r'C:\Users\chromedriver-win64\chromedriver.exe'
        service = Service(executable_path=chrome_driver_path)
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.youtube.com/")

    def search_and_play_video(self, video_name):
        # Find the search box and search for the video
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys(video_name)
        search_box.submit()

        # Wait for the search results to load
        ui.WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "video-title")))

        # Click on the first video link that is not an ad
        video_link = self.driver.find_element(By.ID, "video-title")
        video_link.click()

        # Wait for video to start playing
        sleep(5)

        # Get the total duration of the video
        total_duration = int(self.driver.execute_script("return document.getElementsByTagName('video')[0].duration"))

        # Wait until video finishes (assuming autoplay is on)
        while True:
            # Get the current time elapsed
            current_time = int(self.driver.execute_script("return document.getElementsByTagName"
                                                          "('video')[0].currentTime"))
            # Check if the current time equals or exceeds the total duration
            if current_time >= total_duration:
                print("Video ended")
                break
            sleep(2)  # Check every 2 seconds

        # Quit the browser after the video ends
        self.driver.quit()

# Example usage:
#youtube_player = YouTubePlayer()
#youtube_player.search_and_play_video()
