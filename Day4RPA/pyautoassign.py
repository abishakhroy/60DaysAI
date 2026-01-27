import pyautogui
import webbrowser
import time

# 1. Open the drawing website
print("Opening drawing tool...")
webbrowser.open("https://www.autodraw.com")

# 2. Wait for the page to load
time.sleep(10) 

# 3. Click the canvas
pyautogui.click(x=600, y=500) 


print("Canvas clicked. Starting to draw...")

# 4. Drawing Logic
distance = 200

while distance > 0:
    # Notice we added button='left' to every dragRel command
    pyautogui.dragRel(distance, 0, duration=0.2, button='left')
    pyautogui.dragRel(0, distance, duration=0.2, button='left')
    pyautogui.dragRel(-distance, 0, duration=0.2, button='left')
    pyautogui.dragRel(0, -distance, duration=0.2, button='left')
    
    distance = distance - 20 

print("Drawing complete!")