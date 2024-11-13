def double_columnar_transposition_encrypt(text, key1, key2):
    # First transposition
    encrypted_once = columnar_transposition_encrypt(text, key1)
    
    # Second transposition
    encrypted_twice = columnar_transposition_encrypt(encrypted_once, key2)
    
    return encrypted_twice

# Contoh penggunaan
text = "ariel ganteng banget"
key1 = "3142"
key2 = "2413"
encrypted_text = double_columnar_transposition_encrypt(text, key1, key2)
print("Double Columnar Transposition:", encrypted_text)
