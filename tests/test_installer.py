import unittest
from unittest.mock import patch, MagicMock
from core.installer import build_command, install_apps, is_app_available

class TestInstaller(unittest.TestCase):

    def test_build_command(self):
        cmd = build_command("Git.Git")
        self.assertEqual(cmd, "winget install -e --id Git.Git")

    @patch("subprocess.run")
    def test_is_app_available_success(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)
        self.assertTrue(is_app_available("Git.Git"))

    @patch("core.installer.is_app_available")
    @patch("core.installer.run_command")
    # REMOVI o patch do print aqui para você ver as mensagens na tela
    def test_install_apps_summary(self, mock_run, mock_check):
        apps = [
            {"name": "AppBom", "id": "ID.Certo"},
            {"name": "AppRuim", "id": "ID.Errado"}
        ]
        
        # Simula: o primeiro funciona (True), o segundo não (False)
        mock_check.side_effect = [True, False]
        
        print("\n" + "="*40)
        print("INICIANDO TESTE DE RESUMO:")
        install_apps(apps)
        print("="*40)
        
        # O teste passa se o mock_run foi chamado apenas 1 vez (para o AppBom)
        self.assertEqual(mock_run.call_count, 1)