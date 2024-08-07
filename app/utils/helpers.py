def convert_to_float(string):
    if string[1] == ',':
        number = string[:1] + "." + string[2:]
        return  float(number)
    if string[2] == ",":
        number = string[:2] + "." + string[3:]
        return float(number)