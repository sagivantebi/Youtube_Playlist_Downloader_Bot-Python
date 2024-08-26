
# YouTube Playlist Downloader Bot

This Python script automates the process of downloading videos from a YouTube playlist by using a third-party online converter. The bot is built using Selenium and automates the steps required to download each video in the playlist.




https://user-images.githubusercontent.com/84729141/164451720-cc14ba35-1309-4b23-98a3-4ded6daed827.mp4


## Prerequisites

- **Python 3.x**: Make sure Python is installed on your machine.
- **Google Chrome**: Install the latest version of Google Chrome.
- **ChromeDriver**: Download the version that matches your Chrome version from [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/).

## Setup

1. **Check your Chrome version**:
   - Go to `Settings -> About Chrome -> Version` to check your Chrome version.

2. **Download ChromeDriver**:
   - Visit [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/) and download the version that matches your Chrome version.
   - If needed, you can download an older version of Chrome from [SlimJet](https://www.slimjet.com/chrome/google-chrome-old-version.php).

3. **Install Selenium**:
   - Open Command Prompt (cmd) and run the following command to install Selenium:
     ```bash
     pip install selenium
     ```

4. **Place ChromeDriver**:
   - Place the downloaded `chromedriver.exe` file in the same folder as your script.

5. **Modify Playlist URL**:
   - Open `playlist.py` and replace the `playlist_url` variable with the URL of the YouTube playlist you want to download.

## Running the Bot

1. **Open Command Prompt**:
   - Navigate to the folder containing the script using the `cd` command.

2. **Run the Script**:
   - Execute the following command to run the bot:
     ```bash
     python3 downloadBot.py
     ```

3. **Interact with the Script**:
   - The bot will open the YouTube playlist and the downloader page, start downloading each video, and save them to your computer.
   - Do not close the command window during the process, as the bot needs to remain active until all downloads are completed.

## Important Notes

- **Do not close the command window**: The Python script must run continuously during the downloading process.
- **Bot Introduction**: The bot is introduced with a stylish ASCII art and a personal signature.


![youtube_craw](https://github.com/user-attachments/assets/9f246b45-e2f7-4347-9d54-7ba30afbb14e)


