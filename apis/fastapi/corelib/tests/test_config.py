from corelib.config import get_settings, AppSettings
import unittest

class ConfigTests(unittest.TestCase):

    def test_get_settings(self):
        settings: AppSettings = get_settings()

        self.assertIsNotNone(settings)
        self.assertIsNotNone(settings.data_dir_root)
        self.assertIsNotNone(settings.data_manifest_file)
        self.assertIsNotNone(settings.db_filename)
        self.assertIsNotNone(settings.db_filepath)
        self.assertIsNotNone(settings.db_connection_string)