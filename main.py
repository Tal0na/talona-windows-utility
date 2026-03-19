import sys
from core.admin import is_admin, run_as_admin
from ui.menu import start_menu

if __name__ == "__main__":
    if is_admin():
        # Se já é admin, abre o menu
        start_menu()
    else:
        # Se não é, pede permissão e fecha a janela atual
        run_as_admin()
        sys.exit()