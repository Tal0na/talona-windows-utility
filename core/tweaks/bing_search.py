import winreg

def run():
    # Caminho da chave de busca do Windows
    path = r"Software\Policies\Microsoft\Windows\Windows Search"
    
    try:
        # Tenta criar/abrir a chave de política
        key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_SET_VALUE)
        
        # 0 significa Desativado
        winreg.SetValueEx(key, "ConnectedSearchUseWeb", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, "DisableWebSearch", 0, winreg.REG_DWORD, 1)
        
        winreg.CloseKey(key)
        
        print("✅ Bing Search desativado!")
        print("💡 Reinicie o 'Explorer.exe' ou o PC para aplicar a mudança.")
        
    except Exception as e:
        print(f"❌ Erro ao desativar Bing: {e}")

INFO = {
    "name": "Desativar Bing no Menu Iniciar",
    "desc": "Remove resultados da web e deixa a busca local mais rápida"
}