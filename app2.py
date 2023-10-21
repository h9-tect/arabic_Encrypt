import streamlit as st
import random

# Define the Arabic alphabet and additional letters
additional_letters = 'ايو'

# Function to generate a random word starting with a specified letter
def generate_random_word(start_letter):
    word_length = random.randint(3, 7)  # Random word length between 3 and 7 letters
    word = start_letter
    for _ in range(word_length - 1):
        word += random.choice(additional_letters)
    return word

def process_word(original_word):
    if not original_word:
        return ""
    new_word_1 = 'س' + original_word[1:]
    new_word_2 = generate_random_word(original_word[0])
    return f"{new_word_1}({new_word_2})"

def process_sentence(sentence):
    words = sentence.split()
    processed_words = [process_word(word) for word in words]
    processed_sentence = ' '.join(processed_words)
    return processed_sentence

# Streamlit UI
st.title("Arabic Linguistic Game")
user_input = st.text_input("Enter a sentence:", value="عاشت فلسطين حرة")
if st.button("Process Sentence"):
    result = process_sentence(user_input)
    st.write(result)
