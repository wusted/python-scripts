# This will work for any integer in base between 2 and 16

def toStr(n , base):
    convertstring = "0123456789ABCDEF"
    if n < base:
        return convertstring[n]
    elif n > base:
        return toStr(n//base,base) + convertstring[n%base]

integer = int(input("Which number do you want to convert to string? "))
base = int(input("To which base do you want to convert your number? "))
print("Your number: " , integer)
print("It's type: " , type(integer))
string = toStr(integer, base)
print("Converted to string: " , string , " - In base:" , base)
print("It's new type" , type(string))
