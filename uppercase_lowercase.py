word = "NewAmbition"
count_upper = 0
lower_count = 0
for each_char in word:
    if each_char.isupper():
        count_upper += 1
    elif each_char.islower():
        lower_count += 1
print(count_upper)
print(lower_count)