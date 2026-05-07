import re

with open("corpus.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

cleaned_text = raw_text.replace('\t', ' ')
cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
cleaned_text = re.sub(r'[^\u0D00-\u0D7F\s.]+', '', cleaned_text)


sentences = cleaned_text.split('.')


sentences = [s.strip() for s in sentences]


filtered_sentences = [s for s in sentences if len(s) >= 4]


with open("cleaned_corpus.txt", "w", encoding="utf-8") as file:
    for s in filtered_sentences:
        file.write(s + "\n")