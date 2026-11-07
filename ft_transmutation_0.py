#!/usr/bin/env python3

import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    gold = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {gold}")


if __name__ == "__main__":
    main()
