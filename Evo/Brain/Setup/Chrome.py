import os
import sys
sys.path.append(os.environ.get('Evo'))
import winreg
from Evo.Brain.Paths import TEMP_FOLDER, CHROME_DRIVER_FILE
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from zipfile import ZipFile
import requests
import shutil
from Evo.Brain.Links import getDriverLink, GET_LATEST_VERSION, DOWNLOAD_DRIVER, DOWNLOAD_TEST_DRIVER, GET_VERSION
from Evo.Body.Mouth import speak
from Evo.Brain.Community import writeLog

def removeSeleniumBackups():
    dirPaths = [f"C:\\Users\\{os.environ.get('USERNAME')}\\.cache\\selenium", f"C:\\Users\\{os.environ.get('USERNAME')}\\AppData\\Local\\Temp\\selenium", f"C:\\Users\\{os.environ.get('USERNAME')}\\AppData\\Roaming\\Temp\\selenium"]
    for folder in dirPaths:
        if os.path.isdir(folder):
            shutil.rmtree(folder)

def getChromePath():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\chrome.exe')
        chrome_path, _ = winreg.QueryValueEx(key, '')
        return chrome_path
    except:
        return None

def fetchChromeVersion():
    try:
        driver = webdriver.Chrome()
        browserVersion = driver.capabilities['browserVersion']
        driverVersion = driver.capabilities["chrome"]["chromedriverVersion"].split(" ")[0]
        driver.quit()
        return browserVersion, driverVersion
    except Exception as e:
        writeLog(f"An error occurred while fetching Chrome version: {e}")
        return None

def testDriver():
    if os.path.isfile(CHROME_DRIVER_FILE):
        try:
            drivv = webdriver.Chrome(service=Service(executable_path=CHROME_DRIVER_FILE))
            drivv.get("https://github.com/JunaidParkar")
            drivv.quit()
            return True
        except Exception as e:
            writeLog(f"An error occurred: {e}")
            speak("WebDriver may not be supported or an issue occurred while testing.")
            return False
    else:
        return None

def downloadDriver(version: str):
    if not os.path.isdir(TEMP_FOLDER):
        os.mkdir(TEMP_FOLDER)
    LatestVersionAvailable = requests.get(getDriverLink(GET_LATEST_VERSION)).text
    driverZipPath = os.path.join(TEMP_FOLDER, "driver.zip")
    chromedriver_path = os.path.join(TEMP_FOLDER, 'chromedriver.exe')
    if os.path.isfile(driverZipPath):
        os.remove(driverZipPath)
    if os.path.isfile(chromedriver_path):
        os.remove(chromedriver_path)
    speak("Downloading chrome driver.This might take a while. Please be patient...")
    try:
        if int(LatestVersionAvailable.split(".")[0]) < int(version.split(".")[0]):
            writeLog(f"Downloading chrome driver from {getDriverLink(DOWNLOAD_TEST_DRIVER, version)}")
            downloadedDriver = requests.get(getDriverLink(DOWNLOAD_TEST_DRIVER, version))
        else:
            availVersion = requests.get(getDriverLink(GET_VERSION, version)).text
            writeLog(f"Downloading chrome driver from {getDriverLink(DOWNLOAD_DRIVER, availVersion)}")
            downloadedDriver = requests.get(getDriverLink(DOWNLOAD_DRIVER, availVersion))
    except Exception as e:
        return None
    with open(driverZipPath, 'wb') as f:
        f.write(downloadedDriver.content)
        f.close()
        speak("Driver downloaded. Please wait while setting things up...")
    
    try:
        with ZipFile(driverZipPath, 'r') as zip_ref:
            zip_contents = zip_ref.namelist()
            avail = False
            for file_path in zip_contents:
                if file_path.endswith('chromedriver.exe'):
                    avail = True
                    with zip_ref.open(file_path) as src, open(chromedriver_path, 'wb') as dest:
                        dest.write(src.read())
                    writeLog("driver extracted")
                    shutil.move(chromedriver_path, CHROME_DRIVER_FILE)

            if avail is False:
                speak("chromedriver.exe not found in the ZIP archive. Please look on FAQ page at our website.")
                return None
    except:
        speak("No zip file found...")
        return None
        
    if os.path.isfile(driverZipPath):
        os.remove(driverZipPath)
    if os.path.isfile(chromedriver_path):
        shutil.rmtree(chromedriver_path)
    return True

def chromeSetUp():
    path = getChromePath()
    if path is None:
        speak("Chrome cannot be detected. Plese download and install google chrome first. If already installed then kindly re-install in default location.")
        return False
    else:
        return True

def driverSetup():
    testing1 = testDriver()
    if testing1 is False:
        if os.path.isfile(CHROME_DRIVER_FILE):
            os.remove(CHROME_DRIVER_FILE)    
    if testing1 is None:
        version = fetchChromeVersion()
        if version is None:
            return None
        else:
            driverDownloader = downloadDriver(version[1])
            if driverDownloader is None:
                return None
            else:
                testing2 = testDriver()
                if testing2 is None:
                    return None
                elif testing2 is False:
                    return None
                else:
                    return True
                
# ptt = getChromePath()
# printData(f"chrome path: {ptt}")
# if not ptt is None:
#     ver = fetchChromeVersion()
#     printData(f"chrome versions: {ver}")
#     drdown = downloadDriver(ver[1])
#     printData(f"driver download: {drdown}")
#     if drdown is True:
#         testDriver()