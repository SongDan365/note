file_total = open("total.txt", "r")
total_word_list = [word.split(" ")[0].strip("\n").lower() for word in file_total]
file_total.close()

test_file = open("test.txt", "r")
test_word_list = []
for row in test_file:
    row_word_list = row.split(" ")
    for word in row_word_list:
        test_word_list.append(word.strip("\n").lower())

new_word_list = []
for word in test_word_list:
    if word not in total_word_list and word not in new_word_list:
        new_word_list.append(word)

del total_word_list
del test_word_list

file_total = open("total.txt", "a")
for word in new_word_list:
    print(word)
    file_total.write(word+"\n")
file_total.close()
