import pyautogui
import time

def countdown():
    """Perform a 5-second countdown before starting the script."""
    print("Starting in...")
    for i in range(10, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Go!")

def click_at_position():
    """Move the cursor to the specified position and click every 1 second."""
    try:
        # Set pyautogui failsafe (move cursor to upper-left corner to stop the script)
        pyautogui.FAILSAFE = True
        # Set a small pause between actions to avoid overwhelming the system
        pyautogui.PAUSE = 0.1

        # Perform countdown
        countdown()

        # Target position
        target_x, target_y = 190, 1199
        print(f"Moving cursor to position: ({target_x}, {target_y})")
        print("Starting cursor movement and clicking. Press Ctrl+C to stop.")

        while True:
            # Move to the specified position
            pyautogui.moveTo(target_x, target_y, duration=0)
            # Perform a click
            pyautogui.click()
            current_pos = pyautogui.position()  # Get current cursor position
            print(f"Position clicked: ({target_x}, {target_y}), Current position: {current_pos}")

            # Wait for 1 second
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nScript stopped by user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    click_at_position()