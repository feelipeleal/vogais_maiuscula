vogais = 'aeiou'
texto = str(input('Digite uma palavra: '))
lista=[]
for letra in texto:
    if letra in vogais:
        lista.append(letra.upper())
    else:
        lista.append(letra.lower())
junto = ''.join(lista)
print(junto)