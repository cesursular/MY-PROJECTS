#kullanicidan bir plaka numarasi ister
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
#verilen plaka numarasini kurallara uygun olup ulmadigina bakar
def is_valid(s):
    if not (2 <= len(s) >= 6):
        return False #eger uzunluk 2 ile 6 karakter arasinda deglse false cikar
    #plakianizin ilk iki harfininin harf olup olmadigina bakar
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    #plakada yasak karakterler olup olmadigina bakar
    if any(char in ' .,' for char in s):
        return False
    #plakada rakam varsa bu rakamlarin sonunda olmadigini ve ilk rakamin 0 olmadigini kontrol eder.
    if any(char.isdigit() for char in s[2]):
        first_digit_index = next((index for index, char in enumerate(s) if char.isdigit()), None)
        if first_digit_index is None or s[first_digit_index] == '0' or not s[first_digit_index:].isdigit():
            return False
    return True
main()

