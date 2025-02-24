from corelib.filesystem import get_parent_dir
from dataclasses import dataclass
from dotenv import load_dotenv
import os
from pathlib import Path

ENV_FILE = os.path.join(get_parent_dir(__file__), ".env")

load_dotenv(ENV_FILE)

@dataclass
class AppSettings:
    data_dir_root: str = None
    data_manifest_file: str = None
    db_filename: str = None
    db_filepath: str = None
    db_connection_string: str = None

def get_settings() -> AppSettings:

    result:AppSettings = AppSettings()

    result.data_dir_root = os.path.join(Path(get_parent_dir(__file__)).parent.parent, "data")
    result.data_manifest_file = os.getenv("DATA.MANIFEST.FILE")
    result.db_filename = os.getenv("DB.FILENAME")
    result.db_filepath = os.path.join(Path(get_parent_dir(__file__), result.db_filename))
    result.db_connection_string = f"sqlite:///{result.db_filepath}"

    return result