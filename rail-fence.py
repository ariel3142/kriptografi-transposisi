def rail_fence_encrypt(text, rails):
    
    text = text.replace(" ", "")
    
    fence = [""] * rails
    rail = 0
    direction = 1
    
    for char in text:
        fence[rail] += char
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
            
    return ''.join(fence)

text = "ariel ganteng banget"
rails = 3
encrypted_text = rail_fence_encrypt(text, rails)
print("Rail Fence Cipher:", encrypted_text)
