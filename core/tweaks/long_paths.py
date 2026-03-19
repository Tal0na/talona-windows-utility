# core/tweaks/long_paths.py
import winreg
import subprocess

def run():
    path = r"SYSTEM\CurrentControlSet\Control\FileSystem"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "LongPathsEnabled", 0, winreg.REG_DWORD, 1)
        
        # Aproveita e seta no Git também
        subprocess.run("git config --global core.longpaths true", shell=True)
        print("✅ Long Paths habilitados com sucesso!")
    except PermissionError:
        print("❌ Erro: Você precisa rodar o terminal como ADMINISTRADOR.")

INFO = {
    "name": "Habilitar Long Paths",
    "desc": "Permite caminhos longos (>260 caracteres) para Node.js e Git"
}