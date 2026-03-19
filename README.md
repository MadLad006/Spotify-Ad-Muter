# Spotify-Ad-Muter
An automated system-level audio controller that monitors active media streams and toggles the mute state upon the detection of an ad. Lightweight and configuration free.
# Features
+ **Zero-Touch Automation:** Automatically mutes the system when an ad starts and restores volume when the next track begins.
+ **Process Monitoring:** Specifically targets Spotify audio session without affecting other system sounds.
+ **Auto-Launch:** Logic included to ensure the script starts whenever Spotify is opened.
# Requirements
To run this script, you will need:
  + Python 3.x
  + `pycaw` (Python Common Audio Windows Library)
  + `pywin32` (For Windows GUI interaction)
Install dependencies via pip:
  `pip install pycaw pywin32`
# How It Works
The script utilises the win32gui library to monitor the window title of the Spotify application.
When Spotify plays an advertisement, the window title changes. The script detects this change and uses pycaw to toggle the mute state of the Spotify process until the title returns to a song name.
# Automation
To make the muter open automatically every time you start Spotify, you can create a simple Windwows Batch script using the Notepad.
  ### Step 1: Create the Batch File
  1. Open Notepad.
  2. Paste the following code (make sure to replace the paths with your actual Spotify and     script locations):
  ```
  @echo off
  :: Start the Spotify Application
  start "" "C:\Users\YourUsername\AppData\Roaming\Spotify\Spotify.exe"
  
  :: Start the Python Ad Muter script in the background
  start /b python "C:\Path\To\Your\Script\main.py"
  
  exit
  ```
  3. Save the file as `SpotifySmart.bat` (ensure the extension is `.bat` and not `.txt`).
  ### Step 2: Usage
  Instead of opening Spotify directly, just double-click your `SpotifySmart.bat` file. It will launch Spotify and your Muter script at the same time, then close the command window automatically.
# Installation
1. Clone the repository:
  ```
  git clone https://github.com/MadLad006/Spotify-Ad-Muter.git
  ```
2. Navigate to the directory and install requirements.
3. Set up your `.bat` file as shown above.
# Contributing
Feel free to fork this project, report issues, or submit pull requests for new features.
# Optional: Make the Shortcut Look Like Spotify
Since Windows doesn't allow you to change the icon of a `.bat` file directly, you can create a shortcut to make it look exactly like the official app on your desktop or taskbar.

1. Right-click your `SpotifySmart.bat` file and select **Send to** > **Desktop (create shortcut)**.
2. Go to your desktop, right-click the new shortcut, and select **Properties**.
3. Under the **Shortcut** tab, click the **Change Icon...** button.
4. Click **Browse...** and paste this path into the address bar at the top: `%AppData%\Spotify`.
5. Select the `Spotify.exe` file and click **Open**. 
6. Choose the green Spotify icon from the list and click **OK**, then **Apply**.

**Pro Tip:** Rename the shortcut to simply "Spotify" and pin it to your Taskbar or Start Menu for a seamless, ad-free experience every time you listen!
