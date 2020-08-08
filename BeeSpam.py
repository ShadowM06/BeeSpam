import pyautogui, time
file = input("Name of the file to spam: ")
try:
    f = open(file, 'r')
    print("reading file...")
    readed = True
except:
    print('cannot read file. maybe it is missing or corrupted')
    readed = False
if readed:
    print("file readed...")
    print("Starting spam in 5 seconds")
    time.sleep(5)
    for line in f:
        if line.strip():
            pyautogui.typewrite(line)
            pyautogui.press("enter")
            print(line)