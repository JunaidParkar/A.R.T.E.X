DRIVER_LATEST = "bhbvkrir"
DRIVER = "vbrjuvbrhug"
TEST_DRIVER = "buhbvurihvuro"
GET_VERSION = "huirjgnvri"

def getDriverLink(type: str, version: str = None):
    if type == DRIVER_LATEST:
        return "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    elif type == DRIVER:
        return f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_win64.zip"
    elif type == TEST_DRIVER:
        return f"https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{version}/win64/chromedriver-win64.zip"
    elif type == GET_VERSION:
        return f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{version.split('.')[0]}"