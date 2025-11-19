import os
from pathlib import Path

# Try to load environment variables from a .env file so create_app
# can read SECRET_KEY and other config values when started with
# `python run.py` (not via the Flask CLI).
try:
    # Preferred: python-dotenv if installed
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # Fallback: simple parser for a .env file in the project root
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        for raw in env_path.read_text(encoding='utf-8').splitlines():
            line = raw.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                k, v = line.split('=', 1)
                # don't overwrite existing environment variables
                os.environ.setdefault(k.strip(), v.strip())

from project import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True
    )
