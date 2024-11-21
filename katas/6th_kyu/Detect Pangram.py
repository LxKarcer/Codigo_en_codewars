def is_pangram(st):
    abecdario = "abcdefghijklmnopqrstuvwxyz"
    for char in abecdario:
        if char not in st.lower():
            return False
    return True