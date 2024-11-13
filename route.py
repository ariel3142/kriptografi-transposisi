import numpy as np

def route_cipher_encrypt(text, rows, cols):
    # Remove spaces and pad with X if necessary
    text = text.replace(" ", "")
    while len(text) < rows * cols:
        text += "X"
    
    # Convert text to a matrix
    matrix = np.array(list(text)).reshape(rows, cols)
    
    # Route cipher: spiral read
    encrypted_text = []
    for layer in range((min(rows, cols) + 1) // 2):
        for i in range(layer, cols - layer):
            encrypted_text.append(matrix[layer][i])
        for i in range(layer + 1, rows - layer):
            encrypted_text.append(matrix[i][cols - layer - 1])
        for i in range(cols - layer - 2, layer - 1, -1):
            encrypted_text.append(matrix[rows - layer - 1][i])
        for i in range(rows - layer - 2, layer, -1):
            encrypted_text.append(matrix[i][layer])
            
    return ''.join(encrypted_text)

# Contoh penggunaan
text = "ariel ganteng banget"
rows, cols = 4, 5
encrypted_text = route_cipher_encrypt(text, rows, cols)
print("Route Cipher:", encrypted_text)
