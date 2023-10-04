from collections import defaultdict

print("Reading file...")

with open("./data/file.txt", "r") as file:
    lines = file.read().split("\n")

print("Done reading file, counting words...")

words_dict = defaultdict(lambda: 0)

for line in lines:
    for word in line.split(" "):
        words_dict[word] += 1

print("Finished counting words, sorting results...")

result = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)

for res in result[:10]:
    print(res)
