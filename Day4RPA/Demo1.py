import pyautogui
import time

# 1. Give yourself 3 seconds to switch to your desktop
print("Script starting in 3 seconds...")
time.sleep(3)

# 2. Click the Browser icon on your taskbar
# Replace 500, 1040 with your actual taskbar icon coordinates
pyautogui.click(x=273, y=913) 
time.sleep(2) # Wait for browser to pop up

# 3. Click the address bar and type the search
# Most browsers have the address bar near the top
pyautogui.click(x=631, y=446) 
pyautogui.write("india vs newzealand score 21st January 2026", interval=0.1)
pyautogui.press('enter')

# 4. Wait for Google to load the results
time.sleep(5)

# 5. Click the first link
# Replace these with the coordinates you found in Step 1
pyautogui.click(x=557, y=536)

print("Clicked the first link!")