"""
I wanted to automate weapon cheat codes in a gta game
for that I needed to send keyboard input to the game window
I used keyboard library.
I took input for how many lines need to be typed, what to type, and how long does the wait need to be between lines
"""

import time
import keyboard as kb


def countdown(secs):
    for i in range(secs):
        print(secs - i)
        time.sleep(1)


def typeLine(word):
    kb.write(word)
    kb.press("enter")


def typeLines(all_lines, lines, time_bet_lines):
    for i in range(lines):
        currentLine = all_lines[i]
        print(f"typing {currentLine} in i={i}")
        typeLine(currentLine)
        time.sleep(time_bet_lines)


def main():
    print('How many lines do u want to be typed in sequence?')
    lines = int(input())
    print('\n')

    all_lines = []

    for i in range(lines):
        print(f"\nlines is {lines} and i is {i}")
        print(f"please input test to type in line {i + 1}")
        temp_line = input()
        all_lines.append(temp_line)

    print(f"so all_lines are {all_lines}")

    print("input time between lines")
    timeBetLines = int(input())
    print("input time between cycles")
    timeBetCycles = int(input())

    print("how many cycles? 0 for loop")
    noCycles = int(input())

    print("ok then starting in")
    countdown(5)

    if noCycles == 0:
        while True:
            typeLines(all_lines, lines, timeBetLines)
            time.sleep(timeBetCycles)
    else:
        for i in range(noCycles):
            typeLines(all_lines, lines, timeBetLines)
            time.sleep(timeBetCycles)


if __name__ == "__main__":
    main()
