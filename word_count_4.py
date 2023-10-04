import concurrent.futures
from collections import defaultdict

print("Reading file...")

with open("./data/file.txt", "r") as file:
    lines = file.read().split("\n")

print("Done reading file, counting words...")


def count_words(chunk_start, chunk_end):
    words_dict = {}

    for line in lines[chunk_start:chunk_end]:
        for word in line.split(" "):
            if word not in words_dict:
                words_dict[word] = 0

            words_dict[word] += 1

    return words_dict


num_lines = len(lines)
num_procs = 12
chunk_size = int(num_lines / num_procs)

futures = []

with concurrent.futures.ProcessPoolExecutor(max_workers=num_procs) as executor:
    for chunk_start in range(0, num_lines, chunk_size):
        chunk_end = chunk_start + chunk_size
        future = executor.submit(count_words, chunk_start, chunk_end)
        futures.append(future)

words_dict = defaultdict(lambda: 0)

for fut in futures:
    for word, count in fut.result().items():
        words_dict[word] += count


print("Finished counting words, sorting results...")

result = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)

for res in result[:10]:
    print(res)
