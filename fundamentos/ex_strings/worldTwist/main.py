#! python3

VOWELS = set("aáãâeéêiíoõóôu")
# entrada
def is_valid_name(entry):
    return all(char.isalpha() or char.isspace() for char in entry)


def entry_name():
    while True:
        user_input = input("Digite seu nome: ")
        if is_valid_name(user_input):
            return user_input
        else:
            print("Entrada inválida. Por favor, digite apenas letras e espaços.")

# processamento
def swap_vowels(name):
    new_name = "".join(char.replace(char, "*") if char.lower() in VOWELS else char for char in name)
    return new_name


if __name__ == "__main__":    
    assert is_valid_name("Joao Pedro") is True
    assert is_valid_name("123 de oliveira 4") is False
    assert swap_vowels("JoÃo Pedro") == "J*** P*dr*"

    # entrada
    name = entry_name()
    # processamento
    new_name = swap_vowels(name)
    # saída
    print(f"Olá, {new_name}!")
