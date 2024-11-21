def spin_words(sentence):
    word_list = sentence.split(" ") #enlista el valor sentence (string a lista) separados por cada espacio//
    KEY = 5
    aux_list = []
    
    for word in word_list:
        if len(word) < KEY:
            aux_list.append(word)
        elif len(word) >= KEY:
            aux_list.append(word[::-1])
            
    return ' '.join(aux_list)