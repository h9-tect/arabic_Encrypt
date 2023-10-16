import streamlit as st

def caesar_cipher(text, shift, direction='encrypt'):
    encrypted_text = ""
    for char in text:
        if '\u0600' <= char <= '\u06FF':  # Arabic Unicode range
            base = ord('\u0600')
            shifted = (ord(char) - base + shift) % 256 if direction == 'encrypt' else (ord(char) - base - shift) % 256
            encrypted_text += chr(base + shifted)
        else:
            encrypted_text += char
    return encrypted_text

st.title('تشفير اللغة العربية')

# Text input
text = st.text_area("Input Text", "")

# Mode selection
mode = st.radio("Choose a mode:", ["تشفير", "فك التشفير"])

# Process the text
if st.button("Process"):
    if mode == "Encrypt":
        result = caesar_cipher(text, 3, 'encrypt')
    else:
        result = caesar_cipher(text, 3, 'decrypt')
    st.text_area("Result", result, height=200)
