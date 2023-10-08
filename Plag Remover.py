#many help to make this code is taken from internet but nothing is entirely copied
import nltk
from nltk.corpus import wordnet
import matplotlib.pyplot as plt

def visualize_plagiarism_percent(percent):
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_axes([0,0,1,1])
    ax.bar(['Plagiarism Percentage'], [percent], color='green')
    ax.set_ylabel('Percentage')
    plt.show()



def visualizeplagiarismpercent(percent):
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_axes([0,0,1,1], projection='polar')
    ax.pie([100-percent, percent], labels=['Original', 'Plagiarized'], colors=['green', 'red'])
    plt.show()

def unplagiarize(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Input file not found at: {input_file}")
        return

    
    words = text.split()
    
    
    new_words = []
    
    for word in words:
        synonyms = wordnet.synsets(word)
        if synonyms:
            synonym = synonyms[0].lemmas()[0].name()
            new_words.append(synonym)
        else:
            new_words.append(word)
    
    new_text = " ".join(new_words)
    print ("your unplagarized version of text file is: ")
    print()
    print(new_text)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(new_text)
    except Exception as e:
        print(f"Failed to write to output file: {e}")
        

import nltk
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize

def check_plagiarism(text_file, reference_file):
    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Text file not found at: {text_file}")
        return

    try:
        with open(reference_file, 'r', encoding='utf-8') as file:
            reference_text = file.read()
    except FileNotFoundError:
        print(f"Reference file not found at: {reference_file}")
        return

    stop_words = set(stopwords.words("english"))

    text = word_tokenize(text)
    reference_text = word_tokenize(reference_text)

    text = [word.lower() for word in text if word.isalpha() and word.lower() not in stop_words]
    reference_text = [word.lower() for word in reference_text if word.isalpha() and word.lower() not in stop_words]

    match = 0
    for word in text:
        if word in reference_text:
            match += 1

    plagiarism_percent = (match / len(text)) * 100
    return plagiarism_percent








print("""press 1 if you want to have a unplagarized version of your text file
press 2 if you want to check plagarism percent of your file """)
n= int(input())
if n==1:
    a=input("enter file name: ")
    print("\n")
    print("\n")
    unplagiarize( a, 'output.txt')
    print("to get unplagarized code")
    print("open output.txt")
if n==2:
    a=input("enter first file name: ")
    b=input("enter second file name: ")

    percent = check_plagiarism(a,b)
    print(f"Plagiarism percent: {percent}%")
    visualizeplagiarismpercent(percent)
    visualize_plagiarism_percent(percent)
