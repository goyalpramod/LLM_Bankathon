# def separate_text(text, separator):
#     # Find the index of the separator word in the text
#     separator_index = text.find(separator)
#
#     if separator_index == -1:
#         # Separator word not found in the text
#         print("Separator word not found in the text.")
#         return None, None
#
#     # Extract the two words before and after the separator word
#     word1 = text[:separator_index]
#     word2 = text[separator_index + len(separator):]
#
#     return word1, word2
#
#
# # Example usage:
# if __name__ == "__main__":
#     input_text = "Python-is_awesome"
#     separator_word = "-is_"
#
#     word1, word2 = separate_text(input_text, separator_word)
#     print(f"Word 1: {word1}")
#     print(f"Word 2: {word2}")


text_body="""HI
lfnhsdn
sdnjsnb
sdjss
Final Job Description
ffnh
fcnjsdjnc
sadcjs

"""
a = text_body.split("Final Job Description")
print(f"initial text: \n {text_body}")
print("separated:")
print(a)