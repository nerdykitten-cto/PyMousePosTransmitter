# The OSC Mouse Client
# Starting here
# The Modules
import pyautogui
from pythonosc import udp_client

# Main Program
# This guy run's the client OSC side for the python
def main():
    # Variables for IP Address, IP Port, and Client
    ip_address = '127.0.0.1'
    port = 5005
    client = udp_client.SimpleUDPClient(ip_address, port)
    # Try and Except for the Mouse Position (to check whether the program is running or not)
    try:
        # The Client Part
        while True:
            # Mouse Position Tracker
            x, y = pyautogui.position()
            # Transmitter
            mousePosStart = 'X: ' + str(x).rjust(4) + ', Y: ' + str(y).rjust(4)
            client.send_message('/MousePos', mousePosStart)
            # For Debugging (If necessary)
            '''
            print(mousePosStart, end='')
            print('\b' * len(mousePosStart), end='', flush=True)
            mousePosStart = ''
            '''
    except KeyboardInterrupt:
        print('Closing Time')

# If statment on whether or not the program is running or not
if __name__ == "__main__":
    main()

