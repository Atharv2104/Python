
text = input("Enter a paragraph:\n")

words = text.split()
total_words = len(words)


word_freq = {}
for word in words:
    word = word.lower().strip(".!,?")
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1


sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
top_3 = sorted_words[:3]


vowel_count = 0
for char in text.lower():
    if char in 'aeiou':
        vowel_count += 1


print("\nTotal number of words:", total_words)

print("\nWord frequencies:")
for word, count in word_freq.items():
    print(word, ":", count)

print("\nTop 3 most frequent words:")
for word, count in top_3:
    print(word, ":", count)

print("\nTotal number of vowels:", vowel_count)
