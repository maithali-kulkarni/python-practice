words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_dict = {}

for word in words:
    key = "".join(sorted(word))

    if key not in anagram_dict:
        anagram_dict[key] = []

    anagram_dict[key].append(word)

# print(anagram_dict)

print(list(anagram_dict.values()))
    