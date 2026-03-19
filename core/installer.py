import json
import subprocess

def load_apps(path="config/apps.json"):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{RED}Erro: Arquivo {path} não encontrado!{RESET}")
        return []
    except json.JSONDecodeError:
        print(f"{RED}Erro: O arquivo {path} está com o formato JSON inválido!{RESET}")
        return []

def build_command(app_id):
    return f"winget install -e --id {app_id}"

def run_command(cmd):
    return subprocess.run(cmd, shell=True)

# ADICIONE ESTA FUNÇÃO AQUI:
def is_app_available(app_id):
    # --exact garante que ele não retorne vários apps similares
    # --source winget foca no repositório oficial
    cmd = f"winget search --id {app_id} --exact --source winget"
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.returncode == 0

# Códigos de cores ANSI
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def install_apps(apps):
    failed_apps = []

    for app in apps:
        if is_app_available(app['id']):
            print(f"{GREEN}✅ Instalando {app['name']}...{RESET}")
            cmd = build_command(app["id"])
            run_command(cmd)
        else:
            print(f"{RED}❌ Erro: {app['name']} não encontrado.{RESET}")
            failed_apps.append(app['name'])

    # Resumo Final com cores
    print(f"\n{CYAN}=== RESUMO DA INSTALAÇÃO ==={RESET}")
    if not failed_apps:
        print(f"{GREEN}🎉 Todos os aplicativos foram processados com sucesso!{RESET}")
    else:
        print(f"{YELLOW}⚠️ Os seguintes apps NÃO foram encontrados: {', '.join(failed_apps)}{RESET}")
        print(f"{CYAN}Dica: Verifique se o ID no apps.json está correto.{RESET}")