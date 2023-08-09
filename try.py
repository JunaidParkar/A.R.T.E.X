import os
import shutil
import urllib3
from bs4 import BeautifulSoup
import subprocess
from zipfile import ZipFile
import requests
import winreg

def latestDriverVersion():
    print('Checking latest available version of ChromeDriver')
    response = requests.get("http://chromedriver.storage.googleapis.com/LATEST_RELEASE")
    version = response.text
    print(f"latest version is {version}")
    return version

def getChromePath():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\chrome.exe')
        chrome_path, _ = winreg.QueryValueEx(key, '')
        return chrome_path
    except:
        return None

def getChromeVersion():
    print('Checking installed version of Chrome')
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome")
    version = winreg.QueryValueEx(key, "DisplayVersion")[0]
    return version

def is_chrome_version_compatible(chrome_version, chromedriver_version):
    if chrome_version is None:
        return False
    chrome_major_version = int(chrome_version.split('.')[0])
    chromedriver_major_version = int(chromedriver_version.split('.')[0])
    return chrome_major_version == chromedriver_major_version

def uninstall_chrome(chromePath: str):
    print('Uninstalling Chrome')
    try:
        shutil.rmtree(chromePath)
        shutil.rmtree(os.path.expanduser('~/.config/google-chrome'))
        print('Chrome uninstalled successfully')
    except Exception as e:
        print(f'Error uninstalling Chrome: {e}')

def download_chrome(version):
    print(f'Starting download of Chrome version {version}')
    chrome_installer_url = f'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
    chrome_installer_path = os.path.join(os.environ['HOME'], 'Downloads', 'google-chrome-stable_current_amd64.deb')
    http = urllib3.PoolManager()
    response = http.request('GET', chrome_installer_url)
    with open(chrome_installer_path, 'wb') as f:
        f.write(response.data)
    print(f'Chrome installer downloaded to {chrome_installer_path}')
    return chrome_installer_path

def install_chrome(installer_path):
    print(f'Starting installation of Chrome from {installer_path}')
    subprocess.check_call(['sudo', 'dpkg', '-i', installer_path])
    os.remove(installer_path)
    print('Chrome installed successfully')

def download_chromedriver(version):
    print(f'Starting download of ChromeDriver version {version}')
    chromedriver_zip_url = f'https://chromedriver.storage.googleapis.com/{version}/chromedriver_linux64.zip'
    chromedriver_zip_path = os.path.join(os.environ['HOME'], 'Downloads', 'chromedriver_linux64.zip')
    http = urllib3.PoolManager()
    response = http.request('GET', chromedriver_zip_url)
    with open(chromedriver_zip_path, 'wb') as f:
        f.write(response.data)
    print(f'ChromeDriver downloaded to {chromedriver_zip_path}')
    return chromedriver_zip_path

def install_chromedriver(zip_path):
    print(f'Starting installation of ChromeDriver from {zip_path}')
    with ZipFile(zip_path, 'r') as zip_file:
        zip_file.extractall('/usr/local/bin')
    os.remove(zip_path)
    os.chmod('/usr/local/bin/chromedriver', 0o755)
    print('ChromeDriver installed successfully')

# latest_chromedriver_version = latestDriverVersion()
# chrome_version = getChromeVersion()
# if not is_chrome_version_compatible(chrome_version, latest_chromedriver_version):
#     if chrome_version is not None:
#         uninstall_chrome()
#     chrome_installer_path = download_chrome(latest_chromedriver_version)
#     install_chrome(chrome_installer_path)
# chromedriver_zip_path = download_chromedriver(latest_chromedriver_version)
# install_chromedriver(chromedriver_zip_path)

# driverAvailable = latestDriverVersion()
# chromeInstalled = getChromePath()
# chromeVersion = getChromeVersion()
# uninstall_chrome("C:\Program Files\Google\Chrome\Application")

# print(f"available driver is {driverAvailable}. {f'Chrome is installed at {chromeInstalled}. The version of your chrome is {chromeVersion}' if not chromeInstalled is None else f'Chrome is not installed'}")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
# import platform
import urllib3
from bs4 import BeautifulSoup
from Zubia.Brain.Links import getDriverLink, DRIVER_LATEST, TEST_DRIVER, DRIVER, GET_VERSION
from Zubia.Brain.Paths import CHROME_DRIVER_FILE

def downloadDriver(version: str):
    LatestVersionAvailable = requests.get(getDriverLink(DRIVER_LATEST)).text

    if LatestVersionAvailable.split(".")[0] < version.split(".")[0]:
        print("trial")
        print(getDriverLink(TEST_DRIVER, version))
        driverDownloadURL = requests.get(getDriverLink(TEST_DRIVER, version))
    else:
        print("avail")
        availVersion = requests.get(getDriverLink(GET_VERSION, version)).text
        print(getDriverLink(DRIVER, availVersion))
        driverDownloadURL = requests.get(getDriverLink(DRIVER, availVersion))
    print(os.path.join(os.environ.get("Zubia"), "driver.zip"))
    with open(os.path.join(os.environ.get("Zubia"), "driver.zip"), 'wb') as f:
        f.write(driverDownloadURL.content)
        print("wr")
        f.close()

    # Extract the ChromeDriver executable from the zip file
    with ZipFile(os.path.join(os.environ.get("Zubia"), "driver.zip"), 'r') as zipObj:
        zipObj.extractall()

    # Delete the zip file
    os.remove(os.path.join(os.environ.get("Zubia"), "driver.zip"))

    for root, dirs, files in os.walk(os.environ.get("Zubia")):
        for file in files:
            if file == 'chromedriver.exe':
                driverPath = os.path.join(root, file)
                shutil.move(driverPath, CHROME_DRIVER_FILE)
                print(os.path.dirname(driverPath))
                shutil.rmtree(os.path.dirname(driverPath))
                break

    # Determine the correct download URL based on the user's operating system
    # os_name = platform.system()
    # if os_name == 'Windows':
    #     os_folder = 'Win'
    # elif os_name == 'Linux':
    #     os_folder = 'Linux_x64'
    # elif os_name == 'Darwin':
    #     os_folder = 'Mac'
    # else:
    #     raise Exception(f'Unsupported operating system: {os_name}')

    # Get the specified revision of ChromeDriver, or the latest revision if no revision is specified
    # if revision is None:
    #     url = f'https://commondatastorage.googleapis.com/chromium-browser-snapshots/Win/LAST_CHANGE'
    #     response = requests.get(url)
    #     revision = response.text

    # # Construct the download URL for the specified revision of ChromeDriver
    # url = f'https://commondatastorage.googleapis.com/chromium-browser-snapshots/Win/{revision}/chromedriver.zip'
    # print(url)
    # # Download the ChromeDriver zip file
    # response = requests.get(url)
    # filename = os.path.join(os.environ.get("Zubia"), "Driver.exe")
    # with open(filename, 'wb') as f:
    #     f.write(response.content)
    #     print("wr")
    #     f.close()

    # # Extract the ChromeDriver executable from the zip file
    # # with ZipFile(filename, 'r') as zipObj:
    # #     zipObj.extractall()

    # # Delete the zip file
    # os.remove(filename)
        

    # if driver_path is None:
    #     driver_path = os.path.join(os.environ['TEMP'], 'chromedriver.zip')
    # print(f'Downloading ChromeDriver version {version} to {driver_path}')
    # response = http.request('GET', chromedriver_zip_url)
    # with open(driver_path, 'wb') as f:
    #     f.write(response.data)
    # print(f'ChromeDriver version {version} downloaded to {driver_path}')


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
# downloadDriver(driverVersion)
# testDriver()