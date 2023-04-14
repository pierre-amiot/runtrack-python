def my_long_word(n, s):
    words = s.split()
    long_words = []
    for word in words:
        if len(word) > n:
            long_words.append(word)
    return " ".join(long_words)

# Exemple d'utilisation
sentence = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
long_words = my_long_word(3, sentence)
print(long_words)  # Output : "peur chemin vers côté obscur peur mène colère colère mène haine haine mène souffrance"