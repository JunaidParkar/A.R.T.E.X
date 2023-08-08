import os
import re
import winreg
import urllib.request
from zipfile import ZipFile

def getChromePath():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\chrome.exe')
        chrome_path, _ = winreg.QueryValueEx(key, '')
        return chrome_path
    except:
        # If an error occurs, return None
        return None

def fetchChromeVersion(chrome_exe_path):
    version = os.popen(f'"{chrome_exe_path}" --version').read().strip()
    version = re.search(r'\d+\.\d+\.\d+\.\d+', version).group()
    return version

def downloadChrome():
    # Download the latest version of Chrome from the official website
    chrome_installer_url = 'https://dl.google.com/chrome/install/latest/chrome_installer.exe'
    chrome_installer_path = os.path.join(os.environ['TEMP'], 'chrome_installer.exe')
    urllib.request.urlretrieve(chrome_installer_url, chrome_installer_path)
    return chrome_installer_path

def chromeInstaller(chrome_installer_path):
    # Install Chrome using the downloaded installer
    os.system(f'start /wait "" "{chrome_installer_path}" /silent /install')
    os.remove(chrome_installer_path)

def downloadChromeDriver(version):
    # Download the ChromeDriver for the specified version of Chrome from the official website
    major_version = version.split('.')[0]
    chromedriver_url = f'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{major_version}'
    chromedriver_version = urllib.request.urlopen(chromedriver_url).read().decode('utf-8').strip()
    chromedriver_zip_url = f'https://chromedriver.storage.googleapis.com/{chromedriver_version}/chromedriver_win32.zip'
    chromedriver_zip_path = os.path.join(os.environ['TEMP'], 'chromedriver.zip')
    urllib.request.urlretrieve(chromedriver_zip_url, chromedriver_zip_path)
    return chromedriver_zip_path

def chromeDriverExtractor(chromedriver_zip_path, project_directory):
    # Move ChromeDriver to the specified project directory by extracting the downloaded zip file
    with ZipFile(chromedriver_zip_path, 'r') as zip_file:
        zip_file.extractall(project_directory)
    os.remove(chromedriver_zip_path)

# Get the path to the Chrome executable
chrome_exe_path = getChromePath()

# Check if Chrome is installed
if not os.path.exists(chrome_exe_path):
    # If Chrome is not installed, download and install it
    chrome_installer_path = downloadChrome()
    chromeInstaller(chrome_installer_path)

# Get the version of Chrome installed
version = fetchChromeVersion(chrome_exe_path)

# Download and move the corresponding version of ChromeDriver to your project directory
project_directory = 'C:\\path\\to\\your\\project\\directory'
chromedriver_zip_path = downloadChromeDriver(version)
chromeDriverExtractor(chromedriver_zip_path, project_directory)
