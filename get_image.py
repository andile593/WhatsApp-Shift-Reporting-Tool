import pyautogui
loc = pyautogui.locateOnScreen('whatsapp_loaded.png', confidence=0.8)
print("Found!" if loc else "Not found.")