import os
import sys
sys.path.append(os.environ.get('Zubia'))
import winreg
import urllib3
from Zubia.Brain.Paths import TEMP_FOLDER, CHROME_DRIVER_FILE
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from zipfile import ZipFile
import requests
import shutil
from Zubia.Brain.Links import getDriverLink, GET_LATEST_VERSION, DOWNLOAD_DRIVER, DOWNLOAD_TEST_DRIVER, GET_VERSION
from Zubia.Brain.NeuralNetwork.Base import tokenize
from Zubia.Brain.Errors import CHROME_ERROR

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
        print(f"An error occurred while fetching Chrome version: {e}")
        return None

def download_chrome():
    try:
        print('Starting Chrome download')
        chrome_installer_url = 'https://dl.google.com/chrome/install/latest/chrome_installer.exe'
        chrome_installer_path = os.path.join(TEMP_FOLDER, 'chrome_installer.exe')
        
        http = urllib3.PoolManager()
        response = http.request('GET', chrome_installer_url)
        
        if response.status == 200:
            with open(chrome_installer_path, 'wb') as f:
                f.write(response.data)
            print(f'Chrome installer downloaded to {chrome_installer_path}')
            return chrome_installer_path
        else:
            print(f'Failed to download Chrome installer. Status code: {response.status}')
            return None
    except Exception as e:
        print(f'An error occurred while downloading')
        return None

def install_chrome(chrome_installer_path: str):
    try:
        print(f'Starting Chrome installation from {chrome_installer_path}')
        return_code = os.system(f'start /wait "" "{chrome_installer_path}" /silent /install')
        if return_code == 0:
            os.remove(chrome_installer_path)
            print('Chrome installation complete')
            return True
        else:
            print('Chrome installation failed')
            return False
    except Exception:
        print(f'An error occurred during Chrome installation')
        return False

def testDriver():
    if os.path.isfile(CHROME_DRIVER_FILE):
        try:
            drivv = webdriver.Chrome(service=Service(executable_path=CHROME_DRIVER_FILE))
            drivv.get("https://github.com/JunaidParkar")
            drivv.quit()
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            print("WebDriver may not be supported or an issue occurred while testing.")
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
    try:
        if int(LatestVersionAvailable.split(".")[0]) < int(version.split(".")[0]):
            print(1)
            print(getDriverLink(DOWNLOAD_TEST_DRIVER, version))
            downloadedDriver = requests.get(getDriverLink(DOWNLOAD_TEST_DRIVER, version))
        else:
            print(2)
            availVersion = requests.get(getDriverLink(GET_VERSION, version)).text
            print(getDriverLink(DOWNLOAD_DRIVER, availVersion))
            downloadedDriver = requests.get(getDriverLink(DOWNLOAD_DRIVER, availVersion))
    except Exception as e:
        print(e)
        return None
    with open(driverZipPath, 'wb') as f:
        f.write(downloadedDriver.content)
        f.close()
        print("Driver downloaded")
    
    try:
        with ZipFile(driverZipPath, 'r') as zip_ref:
            zip_contents = zip_ref.namelist()
            avail = False
            for file_path in zip_contents:
                if file_path.endswith('chromedriver.exe'):
                    avail = True
                    with zip_ref.open(file_path) as src, open(chromedriver_path, 'wb') as dest:
                        dest.write(src.read())
                    print("driver extracted")
                    shutil.move(chromedriver_path, CHROME_DRIVER_FILE)

            if avail is False:
                print("chromedriver.exe not found in the ZIP archive")
                return None
    except:
        print("No zip file found...")
        return None
        
    if os.path.isfile(driverZipPath):
        os.remove(driverZipPath)
    if os.path.isfile(chromedriver_path):
        shutil.rmtree(chromedriver_path)
    return True

def chromeSetUp():
    path = getChromePath()
    if path is None:
        print("Chrome cannot be detected. would you like to download it? reply in yes or no...")
        reply1 = input(">> ")
        reply1 = tokenize(reply1)
        if "yes" in reply1:
            installerPth = download_chrome()
            if installerPth is None:
                return None
            else:
                installed = install_chrome(installerPth)
                if installed is False:
                    return None
                else:
                    return True
        else:
            return None
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