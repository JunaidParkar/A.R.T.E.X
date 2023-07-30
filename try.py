import json
import os
from winreg import ConnectRegistry, HKEY_LOCAL_MACHINE, OpenKeyEx, EnumKey, QueryValueEx



def get_installed_apps():
    apps = []
    reg_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'
    with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as reg:
        with OpenKeyEx(reg, reg_path) as key:
            for i in range(0, 10000):
                try:
                    sub_key_name = EnumKey(key, i)
                    with OpenKeyEx(key, sub_key_name) as sub_key:
                        try:
                            display_name, _ = QueryValueEx(sub_key, 'DisplayName')
                            try:
                                install_location, _ = QueryValueEx(sub_key, 'InstallLocation')
                                app_path = os.path.join(install_location, display_name + '.exe')
                            except FileNotFoundError:
                                uninstall_string, _ = QueryValueEx(sub_key, 'UninstallString')
                                app_path = uninstall_string.split(' ')[0]
                            apps.append({'name': display_name, 'path': app_path})
                        except FileNotFoundError:
                            pass
                except OSError:
                    break
    return apps

def main():
    apps = get_installed_apps()
    with open('apps.json', 'w') as f:
        json.dump(apps, f, indent=4)

if __name__ == '__main__':
    main()