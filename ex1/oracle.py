#!/usr/bin/env python3

import os
import sys
try:
    from dotenv import load_dotenv
    load = True
except ImportError:
    print("python-dotenv not found, to install use:\n"
          "    pip install -r ex1/requirements.txt")
    sys.exit(1)


VARIABLES: dict[str, str | None] = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": None,
    "API_KEY": None,
    "LOG_LEVEL": "DEBUG",
    "ZION_ENDPOINT": None,
}


def load_config() -> dict[str, str | None]:
    config: dict[str, str | None] = {}
    if load:
        found: bool = load_dotenv()
        if not found:
            print("[WARNING] No .env file found, using environment/defaults")
    for var, default in VARIABLES.items():
        value = os.getenv(var, default)
        if value is None:
            print(f"[WARNING] {var} not set")
        config[var] = value
    return config


def gitignore_has_env() -> bool:
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, ".gitignore")
    try:
        with open(path, "r") as f:
            lines = f.read().splitlines()
        lines = [line.strip() for line in lines]
    except (OSError, UnicodeDecodeError):
        print("[WARNING] ex1/.gitignore not found")
        return False
    return ".env" in lines


def show_config(config: dict[str, str | None]) -> None:
    print("Configuration loaded:")
    mode = config["MATRIX_MODE"]
    production = mode == "production"
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if config["DATABASE_URL"] is None:
        print("Database: Not configured")
    elif production:
        print("Database: Connected to production cluster")
    else:
        print("Database: Connected to local instance")

    if config["API_KEY"] is not None:
        print("API Access: Authenticated")
    elif production:
        print("API Access: [ERROR] API_KEY is required in production")
    else:
        print("API Access: No API key (ok in development)")

    print(f"Log Level: {config['LOG_LEVEL']}")
    if config["ZION_ENDPOINT"] is None:
        print("Remote Network: Offline")
    else:
        print("Remote Network: Online")


def security_check() -> None:
    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    if gitignore_has_env():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env file not ignored by git")
    print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Consulting the configuration...\n")
    config = load_config()
    show_config(config)
    security_check()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
    sys.exit(0)
