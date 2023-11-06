GET_LATEST_VERSION = "bhbvkrir"
DOWNLOAD_DRIVER = "vbrjuvbrhug"
DOWNLOAD_TEST_DRIVER = "buhbvurihvuro"
GET_VERSION = "huirjgnvri"

def getDriverLink(type: str, version: str = None):
    if type == GET_LATEST_VERSION:
        return "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    elif type == DOWNLOAD_DRIVER:
        return f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip"
    elif type == DOWNLOAD_TEST_DRIVER:
        return f"https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{version}/win64/chromedriver-win64.zip"
    elif type == GET_VERSION:
        return f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{version.split('.')[0]}"