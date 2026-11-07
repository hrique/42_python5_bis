from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    valids = light_spellbook.light_spell_allowed_ingredients()
    for item in valids:
        if item in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
