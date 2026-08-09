string_value = "Vision must be clear"
words = string_value.split()
result_string = ""
for each_word in words:
    result_string = each_word + " " + result_string
print(result_string.strip())


words = string_value.split()

result = []

for i in range(len(words)-1, -1, -1):
    result.append(words[i])

print(" ".join(result))