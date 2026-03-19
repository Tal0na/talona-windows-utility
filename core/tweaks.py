import winreg
import subprocess

class TweakManager:
    def __init__(self):
        # Lista de tweaks disponíveis atualizada com nomes funcionais
        self.registry = [
            ("Definir Navegador Padrão", self.set_default_browser, "Abre a interface para escolher o browser (Zen, Chrome, etc.)"),
            ("Habilitar Long Paths", self.enable_long_paths, "Corrige erros de node_modules no Windows"),
            ("Desativar Bing Search", self.disable_bing, "Remove resultados da web do menu iniciar")
        ]

    def set_default_browser(self):
        """Abre a janela oficial do Windows para troca de aplicativos padrão."""
        print("💡 Abrindo configurações de aplicativos padrão...")
        try:
            # Comando que leva direto para a página de escolha de programas
            subprocess.run("control /name Microsoft.DefaultPrograms /page pageDefaultProgram", shell=True)
            print("✅ Selecione o navegador desejado na janela que abriu.")
        except Exception as e:
            print(f"❌ Erro ao abrir configurações: {e}")

    def enable_long_paths(self):
        """Habilita suporte a caminhos de arquivos longos no Windows e Git."""
        path = r"SYSTEM\CurrentControlSet\Control\FileSystem"
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, "LongPathsEnabled", 0, winreg.REG_DWORD, 1)
            
            # Tweak essencial para desenvolvedores que usam Git
            subprocess.run("git config --global core.longpaths true", shell=True)
            print("✅ Long Paths habilitados no Windows e no Git!")
        except PermissionError:
            print("❌ Erro: Você precisa rodar o terminal como ADMINISTRADOR!")

    def disable_bing(self):
        """Remove a integração do Bing no Menu Iniciar via Registro."""
        path = r"Software\Policies\Microsoft\Windows\Windows Search"
        try:
            # Cria a chave se não existir e define os valores de bloqueio
            key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "ConnectedSearchUseWeb", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key, "DisableWebSearch", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print("✅ Bing Search desativado! (Pode ser necessário reiniciar o Explorer)")
        except Exception as e:
            print(f"❌ Erro ao acessar o registro: {e}")

    def list_and_run(self):
        """Interface de menu para o gerenciador de tweaks."""
        while True:
            print("\n--- 🛠️  Central de Tweaks ---")
            for i, (name, _, desc) in enumerate(self.registry, 1):
                print(f"{i}. {name} - ({desc})")
            print("0. Voltar")

            escolha = input("\nSelecione um tweak: ")
            if escolha == "0": break
            
            try:
                idx = int(escolha) - 1
                name, func, _ = self.registry[idx]
                print(f"\n[Executando: {name}]")
                func()
            except (ValueError, IndexError):
                print("Opção inválida.")