str1 = input()
vowels = "aeuio"
consonants = "qwrtypsdfghjklzxcvbnm"
a1 = "a"
a2 = "e"
a3 = "i"
a4 = "o"
a5 = "u"

vowel_count = sum(str1.count(vowel) for vowel in vowels)
consonant_count = sum(str1.count(consonant) for consonant in consonants)
print(f"Vowels:", vowel_count, f"Consonants:", consonant_count)

b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0

for char in str1:
    if char == a1:
        b1 += 1
    if char == a2:
        b2 += 1
    if char == a3:
        b3 += 1
    if char == a4:
        b4 += 1
    if char == a5:
        b5 += 1
print(f"{a1}: {b1 if b1 != 0 else 'False'}")
print(f"{a2}: {b2 if b2 != 0 else 'False'}")
print(f"{a3}: {b3 if b3 != 0 else 'False'}")
print(f"{a4}: {b4 if b4 != 0 else 'False'}")
print(f"{a5}: {b5 if b5 != 0 else 'False'}")

        

    



        


 


