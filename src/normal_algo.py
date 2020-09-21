file_way =
with (file_way, 'r') as file:
    word = file.readline()
    n = int(file.readline())
    word1 = [""] * n
    word2 = [""] * n
    last = [0] * n
for i in range(n):
    str = input()
    str = str.split(",")
    word1[i] = str[0]
    word2[i] = str[1]
    last[i] = int(str[2])
while i < n:
    if (word.find(word1) != -1) and (last[i] != 0):
        word = word.replace(word1[i], word2[i], 1)
        i = 0
    if last[i] == 0:
        word = word.replace(word1[i], word2[i], 1)
        break
print(word)
