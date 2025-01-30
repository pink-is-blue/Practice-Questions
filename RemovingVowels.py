def remove_vowels(input_string): #checking for vowels in given input if there is vowel skip it and add it to a new string and print
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result
input_str = "Hello, World!"
output_str = remove_vowels(input_str)
print(output_str)
