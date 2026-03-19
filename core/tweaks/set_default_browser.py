# core/tweaks/set_default_browser.py
import subprocess

def run():
    print("\n⏳ Abrindo configurações de aplicativos padrão...")
    subprocess.run("control /name Microsoft.DefaultPrograms /page pageDefaultProgram", shell=True)

# ESSA PARTE É OBRIGATÓRIA PARA O MENU FUNCIONAR:
INFO = {
    "name": "Definir Navegador Padrão",
    "desc": "Abre a interface para escolher o browser (Zen, Chrome, etc.)"
}