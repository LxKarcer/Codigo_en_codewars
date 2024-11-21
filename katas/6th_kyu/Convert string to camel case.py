def to_camel_case(text):
    aux_text = text
    aux_text = aux_text.replace("_","-")
    aux_text = aux_text.split("-")
    
    for position, word in enumerate(aux_text):
        if position == 0:
            continue
        else:
            aux_text[position] = aux_text[position].capitalize()
            
    return ''.join(aux_text)


