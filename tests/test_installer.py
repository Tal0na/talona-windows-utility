import unittest
from unittest.mock import patch
from core.installer import build_command, install_apps

class TestInstaller(unittest.TestCase):

    def test_build_command(self):
        cmd = build_command("Git.Git")
        self.assertEqual(cmd, "winget install -e --id Git.Git")

    @patch("core.installer.run_command")
    def test_install_apps(self, mock_run):
        apps = [{"name": "Git", "id": "Git.Git"}]

        install_apps(apps)

        mock_run.assert_called_once()

if __name__ == "__main__":
    unittest.main()