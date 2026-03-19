import subprocess
import shutil

def update_all_apps():
    if not shutil.which("winget"):
        print("winget não está instalado.")
        return

    confirm = input("Atualizar todos os apps? (s/n): ")
    if confirm.lower() != "s":
        return

    print("\nAtualizando...\n")

    cmd = [
        "winget",
        "upgrade",
        "--all",
        "--silent",
        "--accept-package-agreements",
        "--accept-source-agreements"
    ]

    subprocess.run(cmd)

    print("\nAtualização concluída.")