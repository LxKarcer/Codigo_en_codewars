def duplicate_encode(word):
    word_lowercase = word.lower()
    string_codificado = ""
    for caracter in word_lowercase:
        if word_lowercase.count(caracter) == 1:
            string_codificado += "("
        else:
             string_codificado += ")"
    return string_codificado
