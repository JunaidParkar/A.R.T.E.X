from ProgramFiles.AppManager.registry import AppRegistry

def get_all_apps():
    a = AppRegistry()
    print(a.read_apps())

def get_app_details(package_name):
    a = AppRegistry()
    print(a.get_app(package_name))

def delete_app_from_registry(id):
    a = AppRegistry()
    a.delete_app(id)

def register_app(app_name, package_name, version, default=0):
    a = AppRegistry()
    a.register_app(app_name, package_name, version, default)

def update_app(id, app_name=None, app_package_name=None, version=None, is_default_app=None):
    a = AppRegistry()
    a.update_app(id, app_name, app_package_name, version, is_default_app)