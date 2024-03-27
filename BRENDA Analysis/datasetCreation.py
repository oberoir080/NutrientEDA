def count_occurrences(filename, word):
    count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            count += line.count(word)
    return count

filename = 'brenda_2023_1.txt'  # Change 'your_file.txt' to the path of your text file
word_to_find = 'KM'
occurrences = count_occurrences(filename, word_to_find)
print(f"The number of occurrences of '{word_to_find}' in the file is: {occurrences}")
