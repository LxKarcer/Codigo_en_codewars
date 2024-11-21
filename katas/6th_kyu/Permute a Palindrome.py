def permute_a_palindrome(word):
    caracter_impar = ""
    
    for caracter in word:
        
        if word.count(caracter) %2 == 0:
            continue
            
        elif word.count(caracter) %2 != 0 and caracter_impar == "":
            caracter_impar = caracter
            continue

        elif caracter_impar == caracter: 
            continue
        
        elif caracter_impar != "":
            return False

    return True
