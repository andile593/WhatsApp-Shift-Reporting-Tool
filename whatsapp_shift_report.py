import pygetwindow as gw
import pyautogui
import schedule
import webbrowser
import time
from datetime import datetime
import os
DEBUG_MODE = False 
guards = {
    "Jonas": {
        "sites": {
            "Game Site": {
                "radio": "Silver 7",
                "screenshot_target": "silver7.png"  # screenshot anchor image for locateOnScreen
            }
        }
    }
}

# Define your reusable coordinates here
MAPTYPE_BUTTON = (1174, 149)
SELECT_GOOGLEMAPS = (1120, 199)
SATELITE_BUTTON = (463, 206)
EXPAND_DEVICES = (102, 249)
CHATS_TAB = (32, 100)
SEARCH_BAR = (177, 156)
ATTACH_ICON = (513, 679)
PHOTO_VIDEO_BUTTON = (529, 369)
IMAGE_PICK_COORDS = (356, 171)
SEND_BUTTON = (1315, 682)

def jonas_morning_job():
    guard_name = "Jonas"
    site_name = "Game Site"

    radio_info = guards[guard_name]["sites"][site_name]
    radio_name = radio_info["radio"]
    radio_image = radio_info["screenshot_target"]
    caption = f"{guard_name}'s nightshift patrols at {site_name} (Radio: {radio_name})"
    image_path = f"C:/Users/contr/Pictures/{guard_name}_{site_name.replace(' ', '_')}_morning.png"

    if prepare_puxing_tab():
        success = capture_radio_area(radio_image, image_path)
        if success:
            whatsapp_group = sites[site_name]["whatsapp_group"]
            send_image_to_group(whatsapp_group, image_path, caption)
    else:
        print("Failed to prepare PUXING tab")


def prepare_puxing_tab():
    print(f"[{datetime.now()}] Activating Microsoft Edge and locating PUXING tab...")
    
    edge_windows = gw.getWindowsWithTitle("Edge")
    if not edge_windows:
        print("Microsoft Edge not found.")
        return False

    edge_window = edge_windows[0]
    print(f"Found Edge window: {edge_window}")
    print(f"Is window minimized? {edge_window.isMinimized}")

    # Bring to front
    edge_window.restore()
    edge_window.activate()
    edge_window.maximize()
    time.sleep(2)
    
      # Try to locate tab on screen
    try:
        tab_location = pyautogui.locateOnScreen('puxing_tab.png', confidence=0.75)
        if tab_location:
            x, y = pyautogui.center(tab_location)

            if DEBUG_MODE:
                pyautogui.moveTo(x, y, duration=0.5)
                print(f"[{datetime.now()}] Found PUXING tab (debug mode, no click).")
            else:
                pyautogui.click(x, y)
                print(f"[{datetime.now()}] Clicked on PUXING tab.")
                time.sleep(3)
        else:
            print(f"[{datetime.now()}] Could not locate the PUXING tab.")
            return False
    except pyautogui.ImageNotFoundException:
        print("ImageNotFoundException: puxing_tab.png not found on screen.")
        return False

    return True

def click_once_when_found(image_name, description, confidence=0.8, retries=3, delay=1):
    for attempt in range(retries):
        location = pyautogui.locateCenterOnScreen(image_name, confidence=confidence)
        if location:
            pyautogui.moveTo(location, duration=0.5)
            pyautogui.click()
            print(f"Clicked {description}.")
            time.sleep(2)
            return True
        else:
            print(f"{description} not found, attempt {attempt + 1}/{retries}")
            time.sleep(delay)
    print(f"Failed to click {description} after {retries} attempts.")
    return False


def ensure_sidebar_open():
    print("Checking if sidebar is open...")
    try:
        search_bar = pyautogui.locateOnScreen('search_bar.png', confidence=0.8)
        if search_bar:
            print("Sidebar is already open.")
        else:
            print("Sidebar seems to be closed. Clicking to open it...")
            pyautogui.click(75, 400)  # Coordinates to open the sidebar
            time.sleep(2)  # Allow sidebar to open
    except pyautogui.ImageNotFoundException:
        print("Sidebar state could not be determined. Attempting to open it anyway...")
        pyautogui.click(75, 400)
        time.sleep(2)


def close_sidebar():
    sidebar_close = (319, 397)
    if sidebar_close:
        pyautogui.click(sidebar_close)
        print("Sidebar closed after actions.")
        time.sleep(1)
    else:
        print("Sidebar already closed or couldn't detect.")

def do_actions_with_sidebar():
    ensure_sidebar_open()

    # Your actions that require sidebar to be open here
    print("Performing actions with sidebar open...")
    
    time.sleep(3)  # replace with actual steps
    search_bar = pyautogui.locateCenterOnScreen('search_bar.png', confidence=0.8)
    if search_bar:
        pyautogui.click(search_bar)
        time.sleep(0.5)
        pyautogui.typewrite("silver 7", interval=0.2)
        time.sleep(1)
    else:
        print("Search bar not found.")
        return
    
    silver7_unchecked = (124, 270)
    if silver7_unchecked:
        pyautogui.click(silver7_unchecked)
        print("Clicked Silver 7 unchecked checkbox.")
        time.sleep(2)
    else:
        print("Silver 7 unchecked checkbox not found.")

    click_once_when_found('silver7_route.png', "Silver 7 route")
    click_once_when_found('close_btn.png', "Close Button")
    click_once_when_found('search_btn.png', "Search Button")
    click_once_when_found('close_btn.png', "Close Button")
    
    close_sidebar()
    time.sleep(2)

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

    left = win.left
    top = win.top
    width = win.width
    height = win.height

    print(f"[{datetime.now()}] Taking screenshot now...")
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save(save_path)
    print(f"[{datetime.now()}] Screenshot saved to {save_path}")
    return True


def wait_for_whatsapp_load(timeout=10):
    print(f"[{datetime.now()}] Waiting for WhatsApp to load...")
    for i in range(timeout):
        try:
            location = pyautogui.locateOnScreen('whatsapp_loaded.png', confidence=0.7)
        except pyautogui.ImageNotFoundException:
            location = None
        if location:
            print(f"[{datetime.now()}] WhatsApp loaded.")
            return True
        time.sleep(1)

    print(f"[{datetime.now()}] WhatsApp did not load in time. Waiting 20 more seconds just in case...")
    time.sleep(15)
    return True


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

    
    # Step 3: Attach image using image detection
    try:
        attach = pyautogui.locateCenterOnScreen('attach_icon.png', confidence=0.8)
        if attach:
            pyautogui.click(attach)
            time.sleep(1)
        else:
            print(f"[{datetime.now()}] Could not find attach icon.")
            return
    
        photo_btn = pyautogui.locateCenterOnScreen('photo_video_button.png', confidence=0.8)
        if photo_btn:
            pyautogui.click(photo_btn)
            time.sleep(3)
        else:
            (f"[{datetime.now()}] Could not find photo/video button.")
            return

        image_abs_path = os.path.abspath(image_path)
        print(f"[{datetime.now()}] Typing image path: {image_abs_path}")
        print("Waiting for image preview to load...")
        time.sleep(5)
        pyautogui.write(image_abs_path, interval=0.25)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(5)

        
    except pyautogui.ImageNotFoundException:
        print(f"[{datetime.now()}] Image matching failed.")
        return

    # Step 4: Type caption & send
    if caption:
        pyautogui.typewrite(caption, interval=0.05)
        time.sleep(1)
    pyautogui.press('enter')
    print(f"[{datetime.now()}] Image sent successfully!")


def job():
    print(f"[{datetime.now()}] Starting job...")
    # First, prepare the Puxing tab before screenshot
    if prepare_puxing_tab():
        do_actions_with_sidebar()
        image_path = "C:/Users/contr/Pictures/screenshot.png"
        success = screenshot_window_partial("PUXING物联云系统调度平台", image_path)
        if success:
            send_image_to_group("Test", image_path)
    else:
        print(f"[{datetime.now()}] Could not prepare PUXING tab; aborting job.")


# Schedule daily
schedule.every().day.at("04:05").do(job)

print("⏳ Waiting for scheduled time... Press CTRL+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(60)
