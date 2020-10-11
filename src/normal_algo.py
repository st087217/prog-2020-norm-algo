import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
file = args.file
with (file, 'r') as file:
    word = file.readline()
    n = int(file.readline())
    word_before = [""] * n
    word_after = [""] * n
    last_string = [0] * n
    for i in range(n):
        string = input()
        string = string.split(",")
        word_before[i] = string[0]
        word_after[i] = string[1]
        last_string[i] = int(string[2])
while i < n:
    if (word.find(word1) != -1) and (last[i] != 0)
        if (word.find(word_before) != -1) and (last_string[i] != 0):
        word = word.replace(word_before[i], word_after[i], 1)
        i = 0
        if last_string[i] == 0:
        word = word.replace(word_before[i], word_after[i], 1)
        break

print(word)
