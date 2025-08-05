import pygetwindow as gw
import pyautogui
import schedule
import webbrowser
import time
from datetime import datetime
import os

# Define your reusable coordinates here
MAPTYPE_BUTTON(1174, 149)
SELECT_GOOGLEMAPS(1120, 199)
SATELITE_BUTTON(463,206)
EXPAND_DEVICES(102, 249)
CHATS_TAB = (32, 100)
SEARCH_BAR = (177, 156)
ATTACH_ICON = (513, 679)
PHOTO_VIDEO_BUTTON = (529, 369)
IMAGE_PICK_COORDS = (356, 171)
SEND_BUTTON = (1315, 682)

def prepare_puxing_tab():
    print(f"[{datetime.now()}]) Activating Microsoft Egde and clicking PUXING tab...")

    edge_windows = gw.getWindowsWithTitle("Edge")
    if not edge_windows:
        print("❌ Microsoft Edge not found.")
        return False

    edge_window = edge_windows[0]
    edge_window.activate()
    edge_window.restore()
    edge_window.maximize()
    time.sleep(2)

    # 📌 Click PUXING tab at fixed coordinates
    pyautogui.click(MAPTYPE_BUTTON) 
    print(f"[{datetime.now()}] Clicked on fixed tab position.")
    time.sleep(2)

   return True



def screenshot_window_partial(title_part, save_path):
    windows = gw.getWindowsWithTitle(title_part)
    if not windows:
        print(f"[{datetime.now()}] No window found containing: {title_part}")
        return False

    win = windows[0]
    win.activate()
    win.restore()
    win.maximize()
    time.sleep(2)

    left = win.left - 8
    top = win.top - 30
    width = win.width + 60
    height = win.height + 60

    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save(save_path)
    print(f"[{datetime.now()}] Screenshot saved to {save_path}")
    return True

def wait_for_whatsapp_load(timeout=30):
    print(f"[{datetime.now()}] Waiting for WhatsApp to load...")
    for i in range(timeout):
        try:
            location = pyautogui.locateOnScreen('whatsapp_loaded.png', confidence=0.8)
            if location:
                print(f"[{datetime.now()}] WhatsApp is loaded.")
                return True
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(1)
    print(f"[{datetime.now()}] WhatsApp did not load in time.")
    return False

def send_image_to_group(group_name, image_path, caption="End of shift screenshot 📸"):
    print(f"[{datetime.now()}] Opening WhatsApp Web...")
    webbrowser.open("https://web.whatsapp.com/")
    time.sleep(5)

    if not wait_for_whatsapp_load():
        return

    # Step 1: Ensure we're on "Chats" tab (not Unread)
    pyautogui.click(CHATS_TAB)
    time.sleep(1)

    # Step 2: Click search bar, type group name, press Enter
    pyautogui.click(SEARCH_BAR)
    time.sleep(0.5)
    pyautogui.typewrite(group_name, interval=0.1)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

    # Step 3: Attach image
    pyautogui.click(ATTACH_ICON)
    time.sleep(2)
    pyautogui.click(PHOTO_VIDEO_BUTTON)
    time.sleep(2)
    pyautogui.click(IMAGE_PICK_COORDS)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)

    # Step 4: Type caption & send
    if caption:
        pyautogui.typewrite(caption, interval=0.05)
        time.sleep(1)
    pyautogui.press('enter')
    print(f"[{datetime.now()}] Image sent successfully!")

def job():
    print(f"[{datetime.now()}] Starting job...")
    image_path = "C:/Users/contr/Pictures/screenshot.png"
    success = screenshot_window_partial("PUXING物联云系统调度平台", image_path)
    if success:
        send_image_to_group("Test", image_path)

# Schedule daily
schedule.every().day.at("02:52").do(job)

print("⏳ Waiting for scheduled time... Press CTRL+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(60)