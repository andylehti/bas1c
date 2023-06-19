def generate_start_number(n):
    return int('1' * n + '0')

def convert_to_bas1c(number):
    if number == 0:
        return '0'

    digits = len(str(number))
    start_value = generate_start_number(digits - 1)

    compact_number = number - start_value
    while compact_number < 0:
        digits -= 1
        start_value = generate_start_number(digits - 1)
        compact_number = number - start_value

    return str(compact_number).zfill(digits)

def convert_to_base10(compact_number):
    digits = len(compact_number)
    start_value = generate_start_number(digits - 1)

    return int(compact_number) + start_value

convert_to_bas1c(100) #000
convert_to_base10("000") #100

# authored by Andrew Lehti
