import concurrent.futures
from collections import defaultdict

print("Reading file...")

with open("./data/file.txt", "r") as file:
    lines = file.read().split("\n")

print("Done reading file, counting words...")

words_dict = defaultdict(lambda: 0)


def count_words(lines_chunk):
    for line in lines_chunk:
        for word in line.split(" "):
            words_dict[word] += 1


num_lines = len(lines)
num_threads = 8
chunk_size = int(num_lines / num_threads)

with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    for chunk_start in range(0, num_lines, chunk_size):
        chunk_end = chunk_start + chunk_size
        executor.submit(count_words, lines[chunk_start:chunk_end])

print("Finished counting words, sorting results...")

result = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)

for res in result[:10]:
    print(res)
