sample_list = [1,2,2,5,4,1,1]
count_dict = {}

for val in sample_list:
    if not(val in count_dict.keys()):
        count_dict[val] = 1
    else:
        count_dict[val] = count_dict[val]+1
# print(count_dict)
for key, value in count_dict.items():
    if value>1:
        print(key)

