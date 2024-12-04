from pprint import pprint
import os

def solution(filename):
    #Open the file in reading text mode
    with open(filename, "rt") as text:
        data = text.read()
    words = data.split()
    number_of_words = len(words)
    number_of_lines = 1

    #Initialize dictionaries and lists
    letter_dict = {}
    sorted_dict = {}
    longest_word = ""
    longest_words = []
    shortest_word = ""
    shortest_words = []
    symbol_dict = {}

    #A dictionary that will store all data we gather
    return_dict = {}

    #Count lines
    for line in data:
        if "\n" in line:
            number_of_lines += 1


    #Checks for the longest word, the starting point is just ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word.replace(".", "")
    #Checks if there are more words that are as long as the longest found 
    #if so add them to list
    for word in words:
        if word in longest_words:
            continue
        elif len(word.replace(".", "")) == len(longest_word):
            longest_words.append(word.replace(".", ""))

    #Copy words list and sort it by length of elements
    shortest_words = sorted(words, key=len)
    shortest_word = shortest_words[0]

    #Remove words if longer than the shortest
    for word in words:
        if len(word) > len(shortest_word):
            shortest_words.pop()

    #Add all letters to a dictionary as keys and count the occurences of the
    #letter and add the count as value
    for letter in data:
        letter_dict[letter] = data.count(letter)

    #Sort the keys alphabetically
    #If not a letter go next iteration
    for key, value in sorted(letter_dict.items()):
        if str.isalpha(key) == False:
            if key == "\n":
                continue
            elif key == " ":
                symbol_dict["(Whitespace)"] = value
            else:
                symbol_dict[key] = value
        else:
            sorted_dict[key] = value

    #Removes path and keeps filename
    filename = os.path.basename(filename)
    #Removes extension from filename
    filename = os.path.splitext(filename)[0]

    print(f"This is {filename}:s submission")

    print(f" \nLongest words their length is: {len(longest_word)} characters\n")
    pprint(longest_words, indent=2)
    
    print(f"\nShortest words their length is: {len(shortest_word)} characters\n")
    pprint(shortest_words, indent=2)

    print(f"\nAmount of words in submission: {number_of_words}")

    print(f"Amount of lines(including empty) in submission: {number_of_lines}\n")

    print(f"Here comes a list of all letters used and their number of occurences:\n")

    pprint(sorted_dict, indent=2)

    print("Symbols:")
    pprint(symbol_dict, indent=2)

    #Add all data to dictionary that will be returned.
    return_dict = sorted_dict.copy()
    return_dict["Longest words:"] = longest_words
    return_dict["Shortest words:"] = shortest_words
    return_dict["Number of words:"] = number_of_words
    return_dict["Number of lines(including empty lines):"] = number_of_lines


    return return_dict
