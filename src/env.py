import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()

PARSER_URL: Final[str] = os.getenv("PARSER_URL", "http://127.0.0.1:8000")
DATABASE_URL: Final[str] = os.getenv("DATABASE_URL", "http://127.0.0.1:8001")
