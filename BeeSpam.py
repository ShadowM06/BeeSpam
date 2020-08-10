import pyautogui, time
file = input("Name of the file to spam: ")
count = 0
try:
    f = open(file, 'r')
    print("reading file...")
    readed = True
except:
    print('Cannot read the file. Unsupported or inexistent')
    readed = False
if readed:
    print("file readed...")
    print("Starting spam in 5 seconds")
    time.sleep(5)
    for line in f:
        if line.strip():
            pyautogui.typewrite(line)
            pyautogui.press("enter")
            count + 1
print('spammed '+count+' lines')
print('quitting in 30s...')
time.sleep(30)
print('quit')