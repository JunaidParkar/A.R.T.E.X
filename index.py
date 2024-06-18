import eel
from sq import AppRegistry

# eel.init("./System/Data")

apps = AppRegistry()

def getAllAppsForDisplay():
    app_list = apps.get_allApps()
    print(app_list)

allApps = getAllAppsForDisplay()

# eel.start("artex.ui/index.html")