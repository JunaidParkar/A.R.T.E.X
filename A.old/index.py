from ProgramFiles import AppRegistry, EnvironmentDatabase
from ArtexConfigure import Configuration
# import eel

appRegistry = AppRegistry()
envRegistry = EnvironmentDatabase()
configure = Configuration(envRegistry.get_variable_path("SETTING_CONFIGURATION_FILE"))

# @eel.expose
def get_all_apps():
    print(appRegistry.read_apps())

# @eel.expose
def get_app_details(package_name):
    print(appRegistry.get_app(package_name))

# @eel.expose
def delete_app_from_registry(id):
    appRegistry.delete_app(id)

# @eel.expose
def register_app(app_name, package_name, version, default=0):
    appRegistry.register_app(app_name, package_name, version, default)

# @eel.expose
def update_app(id, app_name=None, app_package_name=None, version=None, is_default_app=None):
    appRegistry.update_app(id, app_name, app_package_name, version, is_default_app)

# @eel.expose
def setSetting(section, settings):
    configure.store_settings(section=section, settings=settings)

# @eel.expose
def getSetting(section, key):
    configure.get_setting(section=section, key=key)

# @eel.expose
def modifySetting(section, key, value):
    configure.modify_setting(section=section, key=key, value=value)

if __name__ == "__main__":
    get_all_apps()