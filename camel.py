#kullanici girisim (input)
camelCase = input("camelCase:")
#baslangicta bir yazdirma islemi- end="" yeni bir alt satira gecmeyi engelliyor
print("snake_case: ", end="")
#dongu baslar
for letter in camelCase:
    #buyuk harf kontrolu-buyuk harfi buldugu zaman "_" cekip devam ediyor.
    if letter.isupper():
        print("_" + letter.lower(), end="")
        #kucuk harfse harfi oldugu gibi ekler
    else:
        print(letter, end="")
print()