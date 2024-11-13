def columnar_transposition_encrypt(text, key):
    # Remove spaces
    text = text.replace(" ", "")
    
    # Sort key to determine column order
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    # Fill the text in columnar order
    cols = len(key)
    rows = (len(text) + cols - 1) // cols
    padded_text = text.ljust(rows * cols, "X")
    
    matrix = [padded_text[i:i + cols] for i in range(0, len(padded_text), cols)]
    
    # Read columns in key order
    encrypted_text = ''.join(''.join(row[i] for row in matrix) for i, _ in key_order)
    return encrypted_text

# Contoh penggunaan
text = "ariel ganteng banget"
key = "3142"
encrypted_text = columnar_transposition_encrypt(text, key)
print("Columnar Transposition:", encrypted_text)
