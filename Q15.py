alphabets=0
special_chars=0
digits=0
word='hell00ooooo1234885(.      )*&^'
for char in word:
    if char.isnumeric():
        digits+=1
    elif char.isalpha():
        alphabets+=1
    else:
        special_chars+=1

print(alphabets, special_chars, digits)