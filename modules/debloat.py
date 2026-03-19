import os

def run():
    print("Removendo bloat...")
    os.system("powershell -ExecutionPolicy Bypass -File scripts/powershell/debloat.ps1")