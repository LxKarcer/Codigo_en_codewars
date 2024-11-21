def get_count(sentence):
    vocals = ["a", "e", "i", "o", "u"]
    counter = 0
    for vocal in vocals:
        for letter in sentence:
            if letter == vocal:
                counter += 1
            else: continue
    return counter
