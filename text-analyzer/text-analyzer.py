import streamlit as st

st.set_page_config(page_title="Text-Analyzer")



st.title("Text Analyzer")
st.markdown("""
						## Welcome to text analyzer! """)

paragraph_input= st.text_area("Enter a pararaph to analyze:")

if paragraph_input:
 paragraph_input=str(paragraph_input)

words= paragraph_input.split()
word_count= len(words)
character_count= len(paragraph_input)

st.subheader("Total Words & Characters")
st.write(f"Total words in your paragraph are {word_count}")
st.write(f"Total characters in your paragraph are: {character_count}")

vowel_count=0
for character in paragraph_input:
	if character.lower() in ['a','e','i','o','u']:
					 vowel_count += 1
st.subheader("Vowel count")
st.write(f"Total vowels in your paragraph are {vowel_count}")

st.subheader("Search and replace!")
search_word=st.text_input("Search the word you want to find:")
replace_word=st.text_input("Enter the word you want to replace it with:")

if search_word and replace_word:
	updated_paragraph= paragraph_input.replace(search_word,replace_word)
	st.write("Updated Paragraph:")
	st.write(updated_paragraph)

st.subheader("Uppercase Conversion")
st.write(paragraph_input.upper())
st.subheader("Lowercase Conversion")
st.write(paragraph_input.lower())


st.subheader("Word Count into Strings")
word_count_str = str(word_count) 
vowel_count_str = str(vowel_count) 
st.write(f"Word count (as string): '{word_count_str}'")
st.write(f"Vowel count (as string): '{vowel_count_str}'")

average_word_length= character_count/word_count if word_count>0 else 0
st.write(f"The average word length of your paragraph is:{average_word_length:.2f}")

st.subheader("Presence of word 'Python'")

if paragraph_input:  
    if "python" in paragraph_input.lower():
        st.success("The word 'Python' is in the paragraph.")
    else:
        st.warning(" The word 'Python' is not in the paragraph!")
else:
    st.info(" Please enter a paragraph to check for the presence of 'Python'.")
