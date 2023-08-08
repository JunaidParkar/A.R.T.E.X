
import os
import winreg
import urllib3

def getChromePath():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\chrome.exe')
        chrome_path, _ = winreg.QueryValueEx(key, '')
        return chrome_path
    except:
        return None

def fetchChromeVersion():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome")
    version = winreg.QueryValueEx(key, "DisplayVersion")[0]
    return version

def download_chrome():
    print('Starting Chrome download')
    print(os.path.join(os.environ['TEMP'], 'chrome_installer.exe'))
    chrome_installer_url = 'https://dl.google.com/chrome/install/latest/chrome_installer.exe'
    chrome_installer_path = os.path.join(os.environ['TEMP'], 'chrome_installer.exe')
    http = urllib3.PoolManager()
    response = http.request('GET', chrome_installer_url)
    with open(chrome_installer_path, 'wb') as f:
        f.write(response.data)
    print(f'Chrome installer downloaded to {chrome_installer_path}')
    return chrome_installer_path

def install_chrome(chrome_installer_path):
    print(f'Starting Chrome installation from {chrome_installer_path}')
    os.system(f'start /wait "" "{chrome_installer_path}" /silent /install')
    os.remove(chrome_installer_path)
    print('Chrome installation complete')
