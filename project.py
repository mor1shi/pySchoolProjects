import re
from collections import Counter 
from wordcloud import WordCloud
import matplotlib.pyplot as plt

textInput = []
while True:
    line = input()
    if line :
        textInput.append(line) 
    else:
        break
text = "\n".join(textInput)
words = re.split(r'[ ,.!?\n]+', text)
wordsLower = [word.lower() for word in words if word]

wordsCounts = Counter(wordsLower)

for word ,count in wordsCounts.most_common():
    print("Counter of words", f"{word}: {count}")

"""count = 0 
candidate = None

for i in words_upper:
    if count == 0:
        candidate = i
    count += 1 if candidate == i else + 0 """

print("All unique words ", len(wordsCounts))
print("Array of words", wordsLower)

word_freqs = dict(wordsCounts)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freqs)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

#pip install wordcloud matplotlib numpy pillow