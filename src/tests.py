from sklearn.feature_extraction.text import CountVectorizer

ex = ["Hello dear friend", "Friend can you give me some money", "What you up today"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(ex)

print("Sparse matrix:")
print(X)

print("\nDense matrix (cu numerele efectiv):")
print(X.toarray())

print("\nCuvintele (vocabulary):")
print(vectorizer.get_feature_names_out())

print("\nCorespondența cuvânt - număr:")
for word, idx in vectorizer.vocabulary_.items():
    print(f"{word}: index {idx}")

print("\nCuvintele sunt sortate alfabetic:")
print(vectorizer.get_feature_names_out())

print("\nStatistici globale (pentru toate textele):")
total_counts = X.toarray().sum(axis=0)  # sumează pe toate textele
feature_names = vectorizer.get_feature_names_out()
for word, count in zip(feature_names, total_counts):
    print(f"'{word}': {count} apariții în total")

print("\nPentru Naive Bayes ai nevoie de:")
print("- Frecvența cuvintelor PER CLASĂ (spam vs ham)")
print("- Nu doar frecvența totală")
print("- De ex: 'money' apare în 80% din spam, dar doar 5% din ham")
