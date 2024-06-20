import pyautogui
import time
import speech_recognition as sr
import pygetwindow as gw

def open_whatsapp():
    # Open WhatsApp (assuming it's pinned to the taskbar on Windows)
    pyautogui.press('win')
    pyautogui.write('whatsapp')
    pyautogui.press('enter')
    time.sleep(5)  # Wait for WhatsApp to open
    # Maximize WhatsApp window
    whatsapp_window = gw.getWindowsWithTitle('WhatsApp')[0]
    whatsapp_window.maximize()
    time.sleep(2)  # Wait for WhatsApp window to maximize

def split_screen():
    # Split the screen into two halves
    pyautogui.keyDown('win')
    pyautogui.keyDown('left')
    pyautogui.keyUp('left')
    pyautogui.keyUp('win')
    time.sleep(1)  # Wait for the split
    pyautogui.moveTo(1200, 540)
    pyautogui.click()

def search_contact(contact_name):
    # Click on the search bar
    pyautogui.click(100, 100)  # Adjust the coordinates according to your screen resolution
    time.sleep(1)
    # Type the contact name
    pyautogui.write(contact_name)
    time.sleep(2)  # Wait for search results to appear

def click_first_contact():
    # Click on the first search result
    pyautogui.click(200, 200)  # Adjust the coordinates according to your screen resolution
    time.sleep(1)

def voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand your audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

if __name__ == "__main__":
    open_whatsapp()
    split_screen()
    time.sleep(5)  # Wait for WhatsApp to fully load

    # Ask the user to speak the name of the contact
    print("Please speak the name of the contact you want to search:")
    contact_name = voice_to_text()

    # Search for the contact
    if contact_name:
        search_contact(contact_name)

    # Click on the first contact in the search results
    click_first_contact()

    # Listen for voice commands and perform actions accordingly

    while True:
        command = voice_to_text()
        if "voice call" in command:
            # Perform voice call action
            print("Initiating voice call...")
            pyautogui.moveTo(850, 100)
            pyautogui.click()
            # Implement voice call action using pyautogui
        elif "video call" in command:
            # Perform video call action
            print("Initiating video call...")
            pyautogui.moveTo(840, 100)
            pyautogui.click()
            # Implement video call action using pyautogui
        elif "type message" in command:
            # Type message action
            print("Please speak the message you want to type:")
            message = voice_to_text()
            pyautogui.write(message)
        elif "send message" in command:
            pyautogui.moveTo(920, 1030)
            pyautogui.click()
        elif "exit" in command:
            print("Exiting program...")
            break
        else:
            print("Command not recognized. Please try again.")


