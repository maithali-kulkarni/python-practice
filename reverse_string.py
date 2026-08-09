string_value = "Vision must be clear"
reversed_string = string_value[::-1]
print(reversed_string)

## What if I want this sentence to be printed in reverse order by keeping the words same

words = string_value.split(" ")
reversed_words = words[::-1]
reversed_sentence = " ".join(reversed_words)
print(reversed_sentence)