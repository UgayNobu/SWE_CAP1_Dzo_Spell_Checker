# SWE_CAP1_Dzo_Spell_Checker
# Dzongkha Spell Checker

## Project Overview
THis particular project is a small task i did to check if the Dzongkha text in the .txt has any spelling errors comparing to a set of mixture of dzongkha and enlish dictionary.First we have to obatain the .txt using import request functions and then clean all the enlish words in the dictionary.Then we link the two fies and implement them to check if there is any errors.This task uses functions as input files and checking against a cleaned Dzongkha dictionary.

## Table of Contents
- [Usage](#usage)
- [Implementation Detail](#implementation-details)
- [Data Structures](#data-structures)
- [Algorithms](#algorithms)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Improvements](#future-improvements)
- [References](#references)

## Usage
In order to use my dzongkha spell checker, follow the following steps:
1. Command-Line Argument: My spell checker requires a argumnet to check the spelling.
Eg-python3 <SWE_CAP1_02123456>.py <input_369>.txt

2. Input: The input file should it simple and easy in the form of .txt that has the text whcich has to be checked if there is any spelling errors or not.

3. Output: If there is any spelling errors in the .txt file, the output should show the line number that contains error and the spelling errors.
If error : Line <line_number>: <misspelled_word>
If no error : Awesome!! There is no errors found,keep it up.

4. Dictionary: The .txt file should be compared with the new_clear_dictionary.txt which contains correct words.

5. Example : To see if here is a error in a file named input_369.txt, use the code: 
python3 SWE_CAP1_02240369.py input_369.txt 

```bash
python3 SWE_CAP1_02123456.py input_369.txt
```

## Implementations Details
Only Dzo Dictionary: We remove all the eng words from the mixed dictionary and keep only the dzongkha words to simplify the task and reduce the difficuility focusing only on the dzongkha words.

Compounds Handling:The code are made to identity the main dzongkha words and other characthers present in the file.

Dectecting Errors: Finds the errors in the words and gives clear feed back to us.

Code Breadown: The task are broken down into smaller sub parts like convertion of .dox to .txt , Rquest the .txt , clean dictionary , check spelling in the file.

## Data Structures
Set: The dictionary is stored in a set to allow efficient O(1) word lookups.
List: The input file’s words are stored in a list for sequential processing.
Tuple: Errors are recorded as (line number, word) tuples.

## Algorithms
Dictionary Cleaning: This algorithm strips the mixed Dzongkha-English dictionary to retain only valid Dzongkha words, ensuring consistency in spell checking.
Spell Checking: This algorithm splits each input line into individual words and checks if they exist in the dictionary. It handles compound words by joining components with "་".

## Performance Analysis
Time Complexity:
Dictionary Cleaning: O(n), where n is the number of lines in the dictionary file.
Spell Checking: O(m * k), where m is the number of lines in the input file and k is the number of words per line. The set-based dictionary lookup has O(1) complexity.
Space Complexity:
O(n), where n is the number of words in the dictionary. Dictionary words are stored in a set, and the input text is processed line by line to minimize memory usage.

## Challenges and Solutions
Unicode Handling:The use of Dzongkha-specific Unicode characters required consistent handling. The code ensures that "།" is replaced by "་" uniformly in both the dictionary and the input file.
Efficient Dictionary Lookup:By using a set for the dictionary, the spell checker achieves O(1) lookup time, optimizing performance for large files.
Compound Word Detection:Dzongkha compound words are joined by "་", which posed a challenge. The algorithm was adapted to check combinations of words for compound word detection.

## Future Improvements
Context-Aware Checking: The spell checker could be enhanced to check for context-based errors, ensuring words are used correctly in context, not just as isolated words.
UI Implementation: A graphical user interface (GUI) or web-based interface could be developed to make the tool more accessible.
Multilingual Support: Expanding the tool to support other languages, allowing multilingual dictionary cleaning and spell checking.

## References
[References1-ChatGPT1](https://chatgpt.com/)
[References2-Youtube](https://www.youtube.com/watch?v=IYIJmZhEiOc)
[References3-TextbookPagew](https://openbookproject.net/courses/python4fun/spellcheck.html)