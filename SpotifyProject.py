import os
import time
import pyautogui
import wmi
import pygetwindow as gw

times_played = 0
stored_song = []
current_song = ""


def loadspotify_song():
    global times_played
    if times_played > 0:
        active_window = current_song
        # RETURN THE NAME OF THE CURRENT SONG BEING PLAYED THROUGH API
        #-
        #-
        #-
        print("active window :", active_window)
        master = gw.getWindowsWithTitle(f"{active_window}")[0]
        master.activate()
        print("LOADING APPLICATION")
        time.sleep(3)
        print("APPLICATION LOADED")
        pyautogui.hotkey("alt","k")
        pyautogui.write(f"{user_input}", interval= 0.01)

        for key in ["enter","pagedown","enter"]:
            time.sleep(1)
            pyautogui.press(key)

        times_played += 1 
        print(times_played)

    elif times_played <= 0:
        os.system("spotify")
        #win = gw.getWindowsWithTitle("spotify free")
        #print(win)
        print("LOADING APPLICATION")
        time.sleep(2)
        print("APPLICATION LOADED")
        pyautogui.hotkey("alt","k")
        pyautogui.write(f"{user_input}", interval= 0.001)

        for key in ["enter","pagedown"]:
            time.sleep(1)
            pyautogui.press(key)
        times_played = times_played + 1 
    else:
        print("ERROR: BAD REQUEST")

def loadspotify_playlist():
    os.system("spotify")
    print("LOADING APPLICATION")
    time.sleep(3)
    print("APPLICATION LOADED")   
    pyautogui.hotkey("alt","k")
    pyautogui.write(f"{user_input}", interval= 0.01)

    for key in ["enter","pagedown","enter","space"]:
        time.sleep(1)
        pyautogui.press(key)

while True:
    choice = input("Enter P for playlist / S for song :").lower()
    if choice == "s":
        user_input = str(input("What song do you want to listen to  :"))
        if len(stored_song) >= 1:
            print("STORED SONG :",stored_song[0])
            current_song = stored_song[0]
            stored_song.remove(stored_song[0])
            stored_song.append(user_input)
        else:
            stored_song.append(user_input)
        print(stored_song,"LEN : ",len(stored_song))
        loadspotify_song()

    elif choice == "p":
        user_input = str(input("What song do you want to listen to  :"))
        loadspotify_playlist()