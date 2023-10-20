import streamlit as st


def caesar_cipher(text, shift, direction='encrypt'):
    encrypted_text = ""
    for char in text:
        # English and some German characters
        if '\u0020' <= char <= '\u007F' or '\u0080' <= char <= '\u00FF':
            base = ord('\u0020') if '\u0020' <= char <= '\u007F' else ord('\u0080')
            if direction == 'encrypt':
                shifted = (ord(char) - base + shift) % 128
            else:
                shifted = (ord(char) - base - shift) % 128
            encrypted_text += chr(base + shifted)

        # Russian characters
        elif '\u0400' <= char <= '\u04FF':
            base = ord('\u0400')
            if direction == 'encrypt':
                shifted = (ord(char) - base + shift) % 256
            else:
                shifted = (ord(char) - base - shift) % 256
            encrypted_text += chr(base + shifted)

        # Arabic Unicode range
        elif '\u0600' <= char <= '\u06FF':
            base = ord('\u0600')
            if direction == 'encrypt':
                shifted = (ord(char) - base + shift) % 256
            else:
                shifted = (ord(char) - base - shift) % 256
            encrypted_text += chr(base + shifted)

        else:
            encrypted_text += char
    return encrypted_text


st.title('Multilingual Caesar Cipher')

# Text input
text = st.text_area("Input Text", "")

# Mode selection
mode = st.radio("Choose a mode:", ["Encrypt", "Decrypt"])

# Process the text
if st.button("Process"):
    if mode == "Encrypt":
        result = caesar_cipher(text, 3, 'encrypt')
    else:
        result = caesar_cipher(text, 3, 'decrypt')
    st.text_area("Result", result, height=200)
