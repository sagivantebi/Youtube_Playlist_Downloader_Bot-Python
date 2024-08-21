"""
Creator - Sagiv Antebi
"""
from selenium import webdriver
from time import sleep
from playlist import playlist_url
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
# import KEYS
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
"""
* class name: downloadBot
* class Operation: main class of the bot
"""
class downloadBot():
    def __init__(self):
        #The chrome web driver path
        chrome_options = Options()
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        print("\n-------------------------------------------------------------")
        print("""\nＳａｇｉｖ Ａｎｔｅｂｉ － Ａｌｌ Ｒｉｇｈｔｓ Ｒｅｓｅｒｖｅｄ\n""")
        print("-------------------------------------------------------------\n")

    """
    * Function name: openDownloader
    * Function Operation: open the youtube downloader
    """
    def openDownloader(self): 
        #open the downloader page
        self.driver.get('https://ytmp3.cc/en22/')
    """
    * Function name: startDownload
    * Function Operation: start the download process
    """
    def startDownload(self,url):
        # Open a new window
        self.driver.execute_script("window.open('');")
        # Switch to the new window and open playlist page
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            # Open the playlist page
            self.driver.get(url)
        except Exception:
            print("URL Problem")
            print(" 𝗽𝗹𝗲𝗮𝘀𝗲 𝗶𝗻𝘀𝗲𝗿𝘁 𝗮 𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗨𝗥𝗟, 𝗮𝗻𝗱 𝗿𝘂𝗻 𝘁𝗵𝗲 𝗯𝗼𝘁 𝗮𝗴𝗮𝗶𝗻.")
        #mute the tab

        # Switch back to the youtube playlist page
        self.driver.switch_to.window(self.driver.window_handles[1])
        # create action chain object
        action = ActionChains(self.driver)
        # perform the operation
        sleep(5)
        action.send_keys('m').perform()
        sleep(2)
        #if the tab is to small it need to check one of two buttons
        try:
            #number of songs to download
            num_songs_str = self.driver.find_element(By.XPATH,'//*[@id="publisher-container"]/div/yt-formatted-string/span[3]').text
        except Exception:
            num_songs_str = self.driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-playlist-panel-renderer/div/div[1]/div/div[1]/div[1]/div/div/yt-formatted-string/span[3]").text
        #when a commercial pops up
        except Exception:
            sleep(10)
            close_btn = self.driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button")
            close_btn.click()
            sleep(5)
            try:
                #number of songs to download
                num_songs_str = self.driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/ytd-playlist-panel-renderer/div/div[1]/div/div[1]/div[1]/div/div/yt-formatted-string/span[3]").text
            except Exception:
                num_songs_str = self.driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-playlist-panel-renderer/div/div[1]/div/div[1]/div[1]/div/div/yt-formatted-string/span[3]").text
        num_songs = int(num_songs_str)
        while(int(num_songs) != 0):
            try:
                self.driver.switch_to.window(self.driver.window_handles[1])
                song_url = self.driver.current_url
                # Switch back to the downloader page
                self.driver.switch_to.window(self.driver.window_handles[0])
                sleep(0.5)
                url_box = self.driver.find_element(By.XPATH, '//*[@id="video"]')
                #writes the song_url 
                url_box.send_keys(song_url)
                convert_btn = self.driver.find_element(By.XPATH, '//*[@id="converter"]/div[3]/div[2]/input')
                #somtimes the convert button does not respond because of issues at the network connection 
                try:
                    convert_btn.click()
                    sleep(3)
                except Exception:
                    sleep(0.5)
                    self.driver.refresh()
                    sleep(3.5)
                    convert_btn.click()
                    sleep(2.5)
                #the download button
                sleep(5)
                download_btn = self.driver.find_element(By.XPATH, '//*[@id="download"]/a[1]')
                download_btn.click()
                sleep(5)
                #close the pop-up
                self.driver.switch_to.window(self.driver.window_handles[2])
                self.driver.close()
                #switch back to the download page
                self.driver.switch_to.window(self.driver.window_handles[0])
                convert_next_btn = self.driver.find_element(By.XPATH, '//*[@id="download"]/a[2]')
                convert_next_btn.click()
                sleep(0.2)
                # Switch back to the youtube playlist page
                self.driver.switch_to.window(self.driver.window_handles[1])
                sleep(0.5)
                # create action chain object
                action = ActionChains(self.driver)
                # perform the operation
                action.key_down(Keys.SHIFT).send_keys('n').perform()
                sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[0])
                num_songs-=1
            except Exception:
                self.driver.refresh()
                sleep(0.5)


def main():
    #creating copy of the bot
    bot = downloadBot()
    #open the tabs (youtube playlist + the downloader page)
    bot.openDownloader()
    #start command to download the playlis
    for url in playlist_url:
        bot.startDownload(url)
    print("Done")
    print("\n-------------------------------------------------------------")
    print("""\nＳａｇｉｖ Ａｎｔｅｂｉ － Ａｌｌ Ｒｉｇｈｔｓ Ｒｅｓｅｒｖｅｄ\n""")
    print("-------------------------------------------------------------\n")
    print("please wait until all the downloads finish")
    sleep(5000)
    input("Press enter to exit ;)")

if __name__ == "__main__":
    main()
