#! python3
# hdTracksDownload.py - downloads HDTracks files from the web
# puts the files in their folder 

import shutil, zipfile, os, time, datetime, calendar
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# gets the current username to pull from the downloads folder
path = os.path.abspath('C:\\Users')
pathFolders = os.listdir(path)
for i in pathFolders:
    if i == 'user1':
        userName = i
    elif i == 'Kevqua':
        userName = i
    elif i == 'user2':
        userName = i
    elif i == 'user3':
        userName = i                                

# get the dates for the files
today = datetime.date.today()
year = datetime.datetime.today().year
year = str(year)
month = today.month
lastMonth = today.month -1
lastMonthName = calendar.month_name[lastMonth]

# open chrome browser and go to site
browser = webdriver.Chrome()
browser.get('https://www.hdtracks.com/customer/account/')
browser.maximize_window()

# logging in
emailElem = browser.find_element_by_class_name("input-text.required-entry.validate-email")
time.sleep(2)
emailElem.send_keys('username')
time.sleep(2)
passwordElem = browser.find_element_by_class_name('input-text.required-entry.validate-password')
time.sleep(2)
passwordElem.send_keys('Password')
time.sleep(2)
loginElem = browser.find_element_by_id('send2').click()
time.sleep(120)
reportLink = browser.find_element_by_link_text('Reports').click()
time.sleep(2)

# get all the available reports in list and click
fileList = browser.find_elements_by_link_text(str(lastMonthName)+', '+str(year))
for x in range(0,len(fileList)):
    if fileList[x].is_displayed():
        fileList[x].click()
time.sleep(10)
print(str(len(fileList))+' HDTracks files Downlaoded...')
time.sleep(20)

# move the files to their new folders
# create the new monthly folder
os.mkdir(r'\\Digital\HD Tracks\2019\\' + year + '-' + '{:02d}'.format(lastMonth))
sourcePath = os.path.abspath('C:\\Users\\' + userName + '\Downloads')
sourceFiles = os.listdir(sourcePath)
destinationPath = os.path.abspath(r'\\Digital\HD Tracks\2019\\' + year + '-' + '{:02d}'.format(lastMonth))



for file in sourceFiles:
    if file.startswith('Distributor_Revenue') and file.endswith('.txt'):
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath, file))
print(str(len(fileList))+' HD Tracks Files Have Been Moved')



