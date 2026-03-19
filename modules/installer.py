import json
import subprocess

def load_apps(path="config/apps.json"):
    with open(path) as f:
        return json.load(f)

def build_command(app_id):
    return f"winget install -e --id {app_id}"

def run_command(cmd):
    return subprocess.run(cmd, shell=True)

def install_apps(apps):
    for app in apps:
        print(f"Instalando {app['name']}...")
        cmd = build_command(app["id"])
        run_command(cmd)