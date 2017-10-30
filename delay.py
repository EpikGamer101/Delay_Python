import time


def write(str):
    for letter in str:
        time.sleep(0.08)
        print(letter, end = '')
