from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from zipfile import ZipFile
import shutil
import requests
import urllib3
from bs4 import BeautifulSoup
from Zubia.Brain.Links import getDriverLink, GET_LATEST_VERSION, DOWNLOAD_DRIVER, DOWNLOAD_TEST_DRIVER, GET_VERSION
from Zubia.Brain.Paths import CHROME_DRIVER_FILE, TEMP_FOLDER

def downloadDriver(version: str):
    LatestVersionAvailable = requests.get(getDriverLink(GET_LATEST_VERSION)).text
    driverZipPath = os.path.join(TEMP_FOLDER, "driver.zip")
    chromedriver_path = os.path.join(TEMP_FOLDER, 'chromedriver.exe')
    try:
        if LatestVersionAvailable.split(".")[0] < version.split(".")[0]:
            downloadedDriver = requests.get(getDriverLink(DOWNLOAD_TEST_DRIVER, version))
        else:
            availVersion = requests.get(getDriverLink(GET_VERSION, version)).text
            downloadedDriver = requests.get(getDriverLink(DOWNLOAD_DRIVER, availVersion))
    except Exception as e:
        print(e)
        return
    with open(driverZipPath, 'wb') as f:
        f.write(downloadedDriver.content)
        f.close()
        print("Driver downloaded")
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
        
    if os.path.isfile(driverZipPath):
        os.remove(driverZipPath)
    if os.path.isfile(chromedriver_path):
        shutil.rmtree(chromedriver_path)

def validateDriver(driverVersion, browserVersion, driverPath = None):
    if driverVersion.split(".")[0] != browserVersion.split(".")[0]:
        if not driverPath is None:
            os.remove(driverPath)

def test_chromedriver_compatibility(driver_path: str):
    print(driver_path)
    try:
        options = Options()
        options.binary_location = driver_path
        wdriver = webdriver.Chrome(options=options)
        print('Chrome and ChromeDriver are compatible')
        wdriver.quit()
        return True
    except Exception as e:
        print(f'Error: {e}')
        print('Chrome and ChromeDriver may not be compatible')
        return False

driver = webdriver.Chrome()
browserVersion = driver.capabilities['browserVersion']
driverVersion = driver.capabilities["chrome"]["chromedriverVersion"].split(" ")[0]
driver.quit()

def testDriver():
    import time
    drivv = webdriver.Chrome(service=Service(executable_path=CHROME_DRIVER_FILE))
    drivv.get("https://github.com/JunaidParkar")
    time.sleep(10)


# print(driverVersion)
# test_chromedriver_compatibility(os.path.join(os.environ.get("Zubia"), "Driver.exe"))
# download_chromedriver(driverVersion, os.path.join(os.environ.get("Zubia"), "Driver.exe"))
# testDriver()
# download_chromedriver(revision=browserVersion)
# print(os.name)
# downloadDriver("114.0.5735.90")
downloadDriver(driverVersion)
testDriver()