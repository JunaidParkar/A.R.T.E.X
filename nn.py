import subprocess
import json

def get_installed_apps():
  """Gets the list of all installed apps from Windows."""

  output = subprocess.check_output(["wmic", "product", "get", "name", "pathname"])
  apps = []
  for app in output.decode("utf-8").split("\r\n"):
    name, path = app.split("  ")
    apps.append({"name": name.strip(), "path": path.strip()})

  return apps

def create_apps_json():
  """Creates a `apps.json` file and stores the executable path of their respective app with its name."""

  apps = get_installed_apps()

  with open("apps.json", "w") as f:
    json.dump(apps, f)

if __name__ == "__main__":
  create_apps_json()
