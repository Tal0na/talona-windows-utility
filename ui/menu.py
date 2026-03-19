def start_menu():
    while True:
        print("\n=== Talona Windows Utility ===")
        print("1. Instalar programas")
        print("2. Aplicar tweaks")
        print("3. Personalização")
        print("4. Atualizar aplicativos")
        print("0. Sair")

        escolha = input("Escolha: ")

        if escolha == "1":
            from core.installer import install_apps, load_apps
            apps = load_apps()
            install_apps(apps)

        elif escolha == "2":
                    from core.tweaks import ALL_TWEAKS
                    
                    while True:
                        print("\n=== 🛠️  Menu de Tweaks (Personalização) ===")
                        for i, tweak in enumerate(ALL_TWEAKS, 1):
                            print(f"{i}. {tweak.INFO['name']} - {tweak.INFO['desc']}")
                        
                        print("0. Voltar")
                        op = input("\nEscolha o tweak: ")
                        
                        if op == "0":
                            break
                        
                        try:
                            idx = int(op) - 1
                            ALL_TWEAKS[idx].run()
                        except (ValueError, IndexError):
                            print("Opção inválida!")

        elif escolha == "3":
            from modules.personalization import run
            run()

        elif escolha == "4":
            from core.updater import update_all_apps
            update_all_apps()

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")