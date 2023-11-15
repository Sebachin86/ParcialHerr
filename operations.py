def ascii(caracter):
    return ord(caracter)

def binario(ascii):
    return bin(ascii)[2:]

def resultados(ascii,binario):
    return f"ASCII: {resultado_ascii} | Binario: {resultado_binario}"

def main():
    caracter = input("Dame un carácter: ")
    resultado_ascii = ascii(caracter)
    resultado_binario = binario(resultado_ascii)
    print(resultados(resultado_ascii, resultado_binario))

