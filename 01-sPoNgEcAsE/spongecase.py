import sPoNgEcAsE_art


def print_title() -> None:
    """Print title to the screen.
    """
    print("Welcome to the...")
    print(sPoNgEcAsE_art.title)
    print("                               program!!!")


def ask_user_input() -> str:
    """Asks user for input

    :return: phrase that will be translated into sPoNgEcAsE.
    """
    return input("\nWhat phrase do you want to translate into sPoNgEcAsE???\n> ")


def translate(phrase_to_be_translated: str) -> str | None:
    """Translates a phrase into a sPoNgEcAsE phrase.
    
    :param phrase_to_be_translated: a phrase that will be translated into sPoNgEcAsE.

    :return: translated phrase into sPoNgEcAsE if valid phrase, None otherwise.
    """
    translated = ""
    if validate_phrase(phrase_to_be_translated):
        for i, char in enumerate(phrase_to_be_translated):
            if i % 2 == 0:
                translated += char.lower()
            else:
                translated += char.upper()
        return translated
    return None


def validate_phrase(phrase: str) -> bool:
    """Validates that the phrase is valid - it has to have at least 1 char.
    
    :param phrase: the phrase that we will validate
    :return: True if length of phrase is larger than 0, False otherwise.
    """
    return len(phrase) > 0


def main() -> None:
    print_title()
    phrase = ask_user_input()
    translated_phrase = translate(phrase)
    if translated_phrase is None:
        print("Try again, pal!!!")
        return
    print("\nTranslated:\n" + translated_phrase)
    print("\nThanks for using the app, chum!")


if __name__ == "__main__":
    main()