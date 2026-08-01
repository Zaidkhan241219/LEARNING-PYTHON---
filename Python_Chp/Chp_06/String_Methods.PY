# File Name :- String_Methods.py
# STRING METHODS

a="   Hey! I am First string    "
b="   Hey! I am Second string  "
c="   Hey! I am 1st 2nd   "
d="fhfhdhskjhsf"

print(a.lower())
print(b.upper())
print(a.title())
print(b.capitalize())
print(b.swapcase())
print(a.strip())
print(b.replace("Second" , "2nd"))
print(a.split())
print(b.find("am"))
print(a.count(" "))
print(b.startswith(" "))
print(a.startswith("H"))
print(a.isalpha())
print(c.isalpha())
print(d.isalpha())
print(d.center(25))
print(d.zfill(25))