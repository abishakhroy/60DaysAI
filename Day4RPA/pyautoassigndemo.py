import pyautogui
import webbrowser
import time

# 1. Open Google
print("Step 1: Opening Google...")
webbrowser.open("https://www.google.com")
time.sleep(4) # Wait for Google to load

# 2. Search for "autodraw"
print("Step 2: Searching...")
# Click the search bar (Middle of screen usually)
pyautogui.click(x=658, y=512) 
pyautogui.write("autodraw", interval=0.1)
pyautogui.press('enter')
time.sleep(3) # Wait for search results

# 3. Click the first result (AutoDraw.com)
print("Step 3: Clicking the first link...")
# This coordinate usually hits the first blue link on Google
pyautogui.click(x=270, y=380) 
time.sleep(5) # Wait for the drawing site to load

# 4. Select the drawing tool
# On AutoDraw, the 'Draw' tool is on the left sidebar
print("Step 4: Selecting the Pencil tool...")
pyautogui.click(x=43, y=405) 
time.sleep(1)

# 5. Start Drawing the Spiral
print("Step 5: Drawing...")
# Move to the center of the canvas to start
pyautogui.moveTo(600, 500)
distance = 200

while distance > 0:
    # We use button='left' to fix the Mac/Python 3.13 error
    pyautogui.dragRel(distance, 0, duration=0.2, button='left')
    pyautogui.dragRel(0, distance, duration=0.2, button='left')
    pyautogui.dragRel(-distance, 0, duration=0.2, button='left')
    pyautogui.dragRel(0, -distance, duration=0.2, button='left')
    
    distance = distance - 20 

print("Mission accomplished!")