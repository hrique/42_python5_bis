#!/usr/bin/env python3

import importlib


REAGENTS: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
}


def imports() -> None:
    missing: list[str] = []
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")
    for name, desc in REAGENTS.items():
        try:
            mod = importlib.import_module(name)
            version = str(getattr(mod, "__version__", "?"))
            print(f"[OK] {name} ({version}) - {desc}")
        except ImportError:
            missing.append(name)
            print(f"[MISSING] {name} - not installed")
    if missing:
        print("\nTo install them use one of the commands below:")
        print("Install using pip = 'pip install -r requirements.txt'")
        print("Install using Poetry = 'poetry install'\n")
    print("\npip vs Poetry:")
    print("  requirements.txt declares what to install; "
          "pip resolves it at install time.")
    print("  pyproject.toml declares the same constraints,"
          " and Poetry pins the resolved")
    print("  versions in poetry.lock so every install is identical.\n")
    if not missing:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    imports()
