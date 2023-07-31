import os
import json
import winreg

def get_installed_app_names():
    installed_apps = []
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall") as key:
        try:
            index = 0
            while True:
                subkey_name = winreg.EnumKey(key, index)
                with winreg.OpenKey(key, subkey_name) as subkey:
                    try:
                        app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                        installed_apps.append(app_name)
                    except FileNotFoundError:
                        pass
                    except Exception as e:
                        print(f"Error reading registry key: {e}")
                index += 1
        except OSError:
            pass

    return installed_apps

def save_to_json(apps_list, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(apps_list, json_file, indent=4)

def main():
    apps_list = get_installed_app_names()
    file_path = "installed_app_names.json"
    save_to_json(apps_list, file_path)
    print(f"List of installed app names has been saved to {file_path}")

if __name__ == "__main__":
    main()
