# Import the necessary libraries
import pyautogui  # for GUI automation
import time  # for time delays
import random  # for generating random values
import PIL  # for image processing

# Set initial values
x = 0
BattleCheck = None

# Delay to move to the pokemonMMO window
time.sleep(3)

# Loop through the code continuously
while x == 0:
        
        # Check if player is in battle
        BattleCheck = pyautogui.locateOnScreen('battlecheck.png', confidence=0.9)
        
        if (BattleCheck != None): #if player is in battle
                # Check if wild pokemon is a shiny
                ShinySearch = pyautogui.locateOnScreen('shiny.png', grayscale = True, confidence=0.9)
                
                if (ShinySearch == None): #if found pokemon is not shiny
                        print('NoShiny') #terminal info for debugging
                        # Click to run from battle
                        pyautogui.click(x=random.randrange(514, 700), y=random.randrange(763, 799))
                
                if (ShinySearch != None): #if found pokemon is shiny
                        print('ShinyFound') #terminal info for debugging
                        BattleCheck = None

        if (BattleCheck == None): #If player is not in battle, execute this code to move randomly
                # Generate random float value between 0 and 2 for the wait time
                WalkTimer = random.randrange(0, 3)
                # Move up
                pyautogui.keyDown('w') #Press W key down
                time.sleep(WalkTimer)
                pyautogui.keyUp('w') #Lift W key up
                # Move down
                pyautogui.keyDown('s') #Press S key down
                time.sleep(WalkTimer)
                pyautogui.keyUp('s') #Lift S key up
