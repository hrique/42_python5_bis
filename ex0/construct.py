#!/usr/bin/env python3

import sys
import os
import site


def main() -> None:
    status = "LABORATORY STATUS"
    venv_on = "The laboratory is sealed"
    venv_off = "You are working in the open"
    in_venv: bool = sys.prefix != sys.base_prefix
    if not in_venv:
        print(f"{status}: {venv_off}\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:\n"
              "python3 -m venv lab_env\n"
              "source lab_env/bin/activate # On Unix\n"
              "lab_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
    else:
        print(f"{status}: {venv_on}\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You are working in an isolated environment!\n"
              "Safe to install reagents without affecting\n"
              "the global system.\n")
        print("Reagent installation path:")
        print(site.getsitepackages()[0])
        print("Global path:")
        print(site.getsitepackages([sys.base_prefix])[0])


if __name__ == "__main__":
    main()
