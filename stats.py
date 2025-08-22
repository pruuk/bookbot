def get_word_count(text):
    words = text.split()
    return len(words)

def create_dict_of_char_counts(text):
    char_count = {}
    for char in text:
        char = char.lower()  # Normalize to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_dict_by_value(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

def produce_book_report(word_count, sorted_char_dict, file_path):
    """
    Sample Report:
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
    """
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {file_path}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {word_count} total words\n"
    report += "--------- Character Count -------\n"
    
    for char, count in sorted_char_dict.items():
        report += f"{char}: {count}\n"
    
    report += "============= END ==============="
    
    return report
