import time
import win32gui
import win32process
from pycaw.pycaw import AudioUtilities

def get_spotify_pid():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name().lower() == "spotify.exe":
            return session.Process.pid
    return None

def get_all_spotify_titles(target_pid):
   
    titles = []

    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == target_pid:
                text = win32gui.GetWindowText(hwnd)
                if text:
                    titles.append(text)

    win32gui.EnumWindows(callback, None)
    return titles

def set_mute(mute, target_pid):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.pid == target_pid:
            volume = session.SimpleAudioVolume
            volume.SetMute(1 if mute else 0, None)
            return

def main():
    print("Local Ad Muter is running... (Ghost Window Fix active)")
    is_muted = False

    while True:
        current_pid = get_spotify_pid()
        
        if current_pid:
            
            all_titles = get_all_spotify_titles(current_pid)
            
            
            is_ad = False
            
            if not all_titles:
                is_ad = False 
            else:
                
                for title in all_titles:
                    if title == "Spotify" or "Advertisement" in title or "Spotify Free" in title:
                        is_ad = True
                        current_title = title
                        break
                
                
                if not is_ad:
                    
                    song_titles = [t for t in all_titles if " - " in t]
                    if song_titles:
                        is_ad = False
                        current_title = song_titles[0]
                    else:
                       
                        is_ad = True
                        current_title = all_titles[0]

            if is_ad:
                if not is_muted:
                    print(f"Ad detected. Muting... (Found: {all_titles})")
                    set_mute(True, current_pid)
                    is_muted = True
            else:
                if is_muted:
                    print(f"Song detected: {current_title}. Unmuting...")
                    set_mute(False, current_pid)
                    is_muted = False
        
        time.sleep(1)

if __name__ == "__main__":
    main()