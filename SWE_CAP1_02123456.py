###################################
#https://github.com/UgayNobu/SWE_CAP1_Dzo_Spell_Checker.git

# Ugyen Norbu
# First Year SWE ' A '
# 02240369
###################################
# ChatGPT , YouTube , Goggle , W3 School
# https://chatgpt.com/ , https://www.youtube.com/watch?v=d-Eq6x1yssU, https://www.youtube.com/watch?v=_nkQd9SyEpw&t=4s , https://www.google.com/ , https://www.w3schools.com/ 
# Cleaning the english and dzongkha mixed dictionary the main problem comparing the .txt file with the dictionary file, few dzongkha words compare with 1000s of words in dictinary, Another problem we face is when i run the python code in mac it has many restrications such as i had to download the request modeule ealier
# https://www.youtube.com/watch?v=rjXeG0aT-7w
###################################

#Solution
###################################

#Converting the .dox dictionary to .txt dictionary
import docx2txt as d2t

Docxfile = "dictionary.docx"
txtfile = "dictionary.txt"

doc = d2t.process(Docxfile)

file = open(txtfile, 'w', encoding='utf-8')
file.write(doc)
file.close()

print("file converted")

#Read the input file 
import re
link = "https://csf101-server-cap1.onrender.com/get/input/369"
request_file = re.get(link)
with open('369.txt', 'wb') as file:
    data = file.write(request_file.content)
print('Downloaded: 369.txt')

#Cleaning the mixed dzongkha english dictionary to only dzongkha words
def clean_dictionary(input_file, output_file):
    cleaned_words = []
    with open(input_file, "r", encoding = "utf-8" ) as file:
        for line in file:
            words = line.split()
            if words:
                dzongkha_word = words[0]
                cleaned_words.append(dzongkha_word) 
    with open(output_file , "w", encoding = "utf-8")  as file:
        for word in cleaned_words:
            file.write(word + "\n") 
        print(f"cleaned words saved to {output_file}")
input_file = "dictionary.txt" 
output_file = "new_clear_dictionary.txt" 
clean_dictionary(input_file, output_file)

def mixeddictionary(files):
    with open(files, "r", encoding = "utf-8") as f:
        return set(word.strip().replace("།", "་") for word in f)

#Check spelling
def spellchecking(my_txt_file, dictionary):
    errors = []

    with open(my_txt_file, "r", encoding = "utf-8") as file:
        for line_number, line in enumerate(file, start = 1):
            words = re.split(r"[་\s]+", line)
            number_of_words= len(words)
            x = 0 
            while x < number_of_words:
                word = words[x].strip().replace("།", "་")
                if not word:
                    x += 1
                    continue
                y = i
                compound_word = word
                found = False
                next_word = words[j + 1].strip().replace("།", "")
                if not next_word:
                        y += 1
                        continue
                compound_word += "་" + next_word
                y += 1
                if compound_word in dictionary:
                        found = True
                        x = j
                        break 
                if not found and word not in dictionary:
                    errors.append((line_number, word))
                x += 1
    return errors

#Main spell checking function
import sys
def spell_checking_main_function():
    if len(sys.argv) !=2:
        print("Usage:python3 <SWE_CAP1_02123456>.py <input_369>.txt")
        sys.exit(1)
    files = "new_clear_dictionary.txt"
    my_txt_file = sys.argv[1]
    errors = spellchecking(my_txt_file, dictionary)
    dictionary = (files)   
    if errors:
        print("There is errors in your code,please change!!")
        for line, word in errors:
            print(f"line {line}: {word}")
    else:
        print("Awesome!! There is no errors found,keep it up")
if _name_ == "_main_":
    spell_checking_main_function()
    
