import pyautogui
import random
import time
message_list =[]
num = int(input("Enter number of messages "))
index = 0
while index < num:
    message = input("Enter your message ")
    message_list.insert(index, message)
    index = index+1
repeat = int(input("Enter number of repeats "))
time.sleep(10)
count = 0
i = 0
while i <= repeat:
    pyautogui.typewrite(message_list[count])
    pyautogui.press("enter")
    if count < num -1:
        count = count +1
    else:
        count = 0
        i = i+1
        random.shuffle(message_list)