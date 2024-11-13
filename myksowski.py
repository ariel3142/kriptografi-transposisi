def myszkowski_transposition_encrypt(text, key):
    # Remove spaces and prepare key structure
    text = text.replace(" ", "")
    unique_key = sorted(set(key), key=key.index)
    cols = len(key)
    rows = (len(text) + cols - 1) // cols
    padded_text = text.ljust(rows * cols, "X")
    
    # Fill the matrix row-wise
    matrix = [padded_text[i:i + cols] for i in range(0, len(padded_text), cols)]
    
    # Extract columns based on the order of unique_key
    encrypted_text = []
    for k in unique_key:
        for i in range(len(key)):
            if key[i] == k:
                encrypted_text.extend(row[i] for row in matrix)
    
    return ''.join(encrypted_text)

# Contoh penggunaan
text = "ariel ganteng banget"
key = "BALLOON"
encrypted_text = myszkowski_transposition_encrypt(text, key)
print("Myszkowski Transposition:", encrypted_text)
