sample_string = "what is your name"
count_dict = {}

for val in sample_string.replace(" ",""):
    if not(val in count_dict.keys()):
        count_dict[val] = 1
    else:
        count_dict[val] = count_dict[val]+1
print(count_dict)