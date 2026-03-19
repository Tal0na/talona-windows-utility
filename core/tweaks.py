import os

def apply_tweaks():
    print("Aplicando tweaks...")

    os.system("powershell -ExecutionPolicy Bypass -File scripts/powershell/tweaks.ps1")