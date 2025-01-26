import re

def validate_luhn(card_number):
    """
    Valida o número do cartão de crédito usando o algoritmo de Luhn.
    """
    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:  # Dobra os dígitos em posições ímpares (índice começa em 0)
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0

def identify_brand(card_number):
    """
    Identifica a bandeira do cartão com base no número fornecido.
    """

    # Definição de padrões de bandeiras
    brands = {
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "MasterCard": r"^(5[1-5][0-9]{4}|2[2-7][0-9]{4})[0-9]{10}$",
        "American Express": r"^3[47][0-9]{13}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "JCB": r"^(?:2131|1800|35[0-9]{3})[0-9]{11}$",
        "Hipercard": r"^(606282|3841)[0-9]{0,}$",
        "Aura": r"^50[0-9]{14,17}$",
        "Maestro": r"^(5018|5020|5038|5893|6304|6759|6761|6762|6763)[0-9]{12,19}$",
        "Solo": r"^(6334|6767)[0-9]{12,15}$",
        "Voyager": r"^8699[0-9]{11}$",
        "enRoute": r"^(2014|2149)[0-9]{11}$",
        "Elo": r"^(?:4011|4312|4389|4514|4576|5041|5066|509[0-9]|6277|6362|6363|6504|6505|6516|6550)[0-9]{0,}$"
    }

    for brand, pattern in brands.items():
        if re.match(pattern, card_number):
            return brand

    return "bandeira não cadastrada"

def main():
    card_number = input("Informe o número do cartão de crédito: ").strip()

    card_number = card_number.replace(" ", "")

    # Validação com o algoritmo de Luhn
    if not card_number.isdigit() or not validate_luhn(card_number):
        print("Número de cartão inválido.")
        return

    # Identificação da bandeira
    brand = identify_brand(card_number)
    print(f"Bandeira identificada: {brand}")

if __name__ == "__main__":
    main()
