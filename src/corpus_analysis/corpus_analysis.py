import re
from collections import Counter
import csv


with open("cleaned_corpus.txt", "r", encoding="utf-8") as f:
    text = f.read()


pattern = r'[\u0D00-\u0D7F]+'


words = re.findall(pattern, text)


freq = Counter(words)


for word, count in freq.most_common(50):
    print(word, ":", count)


with open("word_frequency.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["word", "length", "frequency"])

    for w, c in freq.items():
        writer.writerow([w, len(w), c])

print("\nSaved frequency data to word_frequency.csv")
