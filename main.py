from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time

# Creates browser
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://orteil.dashnet.org/cookieclicker/')


# Thread Class
class MyThread(threading.Thread):
    def __init__(self, threadNum):
        # Inits Thread
        threading.Thread.__init__(self)
        # Shows which thread is in use
        self.threadNum = threadNum

    def run(self):
        # Print thread in use
        print(self.threadNum)
        # Clicks the cookie 100 times for each thread
        for y in range(100):
            browser.find_element_by_xpath("/html/body/div/div[2]/div[15]/div[8]/div[1]").click()


# Creates dictionary
diction = {}
# Creates 1000 keys and values for the dictionary
# Which will be used as variables for the threads
for x in range(1, 1000):
    diction["thread{0}".format(x)] = "newThread"

while True:
    # Loops through dictionary keys
    for key in diction:
        # Sets dictionary key to a variable for the thread
        key = MyThread(key)
        # Starts thread
        key.start()
        # Waits for thread to finish to continue to the next
        key.join()
