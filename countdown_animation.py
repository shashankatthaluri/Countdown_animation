import sys, time
import sevseg  # Imports our updated sevseg.py program.
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

try:
    # Ask the user for the number of seconds:
    secondsLeft = int(input('Enter the number of seconds: '))

    while True:  # Main program loop.
        # Clear the screen by printing several newlines:
        print('\033c', end='')

        # Get the hours/minutes/seconds from secondsLeft:
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the digits:
        print(Fore.GREEN + hTopRow + '     ' + mTopRow + '     ' + sTopRow)
        print(Fore.GREEN + hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(Fore.GREEN + hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        if secondsLeft == 0:
            # Display larger "BOOM" message
            print()
            print(Fore.RED + Style.BRIGHT + '    * * * * BOOM * * * * Time Up! * * * *   ')
            break

        print(Fore.CYAN)
        print('Press Ctrl-C to quit.')

        time.sleep(1)  # Insert a one-second pause.
        secondsLeft -= 1

except KeyboardInterrupt:
    print('Countdown')
    sys.exit()  # When Ctrl-C is pressed, end the program.
