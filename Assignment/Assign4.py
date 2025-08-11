
=====================================================

	~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~

=====================================================

<--- Functions You Didn’t Know You Needed --->
     -------------------------------------

rev_spell     → Reverse a String
freq_potion   → Character Frequency Counter
cleanse_list  → Remove Duplicates from List
shared_runes  → Find Common Elements
dict_fuse     → Merge Dictionaries
calc_charm    → Simple Calculator
sort_glyphs   → Sort Tuples by Second Element
unfold_scroll → Flatten Nested List
lost_number   → Find Missing Number
mirror_words  → Check if Strings are Anagrams
exit_spell    → Exit the Spellbook

Type your magic key: rev_spell
Program: Reverse a String (Without [::-1] or reversed())

def reverse_str(s):
    result = ''
    for char in s:
        result = char + result
    return result
    
Test Case 1: reverse_str('hello') → 'olleh'
Test Case 2: reverse_str('abc') → 'cba'
Explanation: Characters are prepended one by one to reverse the string.


=====================================================

	~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~

=====================================================

<--- Functions You Didn’t Know You Needed --->
     -------------------------------------

rev_spell     → Reverse a String
freq_potion   → Character Frequency Counter
cleanse_list  → Remove Duplicates from List
shared_runes  → Find Common Elements
dict_fuse     → Merge Dictionaries
calc_charm    → Simple Calculator
sort_glyphs   → Sort Tuples by Second Element
unfold_scroll → Flatten Nested List
lost_number   → Find Missing Number
mirror_words  → Check if Strings are Anagrams
exit_spell    → Exit the Spellbook

Type your magic key: fre_potion
Unknown spell. Try again!

=====================================================

	~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~

=====================================================

<--- Functions You Didn’t Know You Needed --->
     -------------------------------------

rev_spell     → Reverse a String
freq_potion   → Character Frequency Counter
cleanse_list  → Remove Duplicates from List
shared_runes  → Find Common Elements
dict_fuse     → Merge Dictionaries
calc_charm    → Simple Calculator
sort_glyphs   → Sort Tuples by Second Element
unfold_scroll → Flatten Nested List
lost_number   → Find Missing Number
mirror_words  → Check if Strings are Anagrams
exit_spell    → Exit the Spellbook

Type your magic key: cleanse_list
Program: Remove Duplicates from List (Without set())

def remove_dups(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
    
Test Case 1: remove_dups([1, 2, 2, 3]) → [1, 2, 3]
Test Case 2: remove_dups(['a', 'a', 'b']) → ['a', 'b']
Explanation: Only add elements to result if not already present.


=====================================================

	~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~

=====================================================

<--- Functions You Didn’t Know You Needed --->
     -------------------------------------

rev_spell     → Reverse a String
freq_potion   → Character Frequency Counter
cleanse_list  → Remove Duplicates from List
shared_runes  → Find Common Elements
dict_fuse     → Merge Dictionaries
calc_charm    → Simple Calculator
sort_glyphs   → Sort Tuples by Second Element
unfold_scroll → Flatten Nested List
lost_number   → Find Missing Number
mirror_words  → Check if Strings are Anagrams
exit_spell    → Exit the Spellbook

Type your magic key: shared_runes
Program: Find Common Elements in Two Lists

def common(lst1, lst2):
    return [item for item in lst1 if item in lst2]
    
Test Case 1: common([1,2,3], [2,3,4]) → [2,3]
Test Case 2: common(['a','b'], ['b','c']) → ['b']
Explanation: We use list comprehension to filter elements in both lists.


=====================================================

	~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~

=====================================================

<--- Functions You Didn’t Know You Needed --->
     -------------------------------------

rev_spell     → Reverse a String
freq_potion   → Character Frequency Counter
cleanse_list  → Remove Duplicates from List
shared_runes  → Find Common Elements
dict_fuse     → Merge Dictionaries
calc_charm    → Simple Calculator
sort_glyphs   → Sort Tuples by Second Element
unfold_scroll → Flatten Nested List
lost_number   → Find Missing Number
mirror_words  → Check if Strings are Anagrams
exit_spell    → Exit the Spellbook

Type your magic key: dict_fuse
Program: Merge Two Dictionaries

def merge_dicts(d1, d2):
    return {**d1, **d2}
    
Test Case 1: merge_dicts({'a':1}, {'b':2}) → {'a':1, 'b':2}
Test Case 2: merge_dicts({'x':10}, {'x':20, 'y':30}) → {'x':20, 'y':30}
Explanation: Dictionary unpacking merges the contents, with latter keys overwriting.


=====================================================

	~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~

=====================================================

<--- Functions You Didn’t Know You Needed --->
     -------------------------------------

rev_spell     → Reverse a String
freq_potion   → Character Frequency Counter
cleanse_list  → Remove Duplicates from List
shared_runes  → Find Common Elements
dict_fuse     → Merge Dictionaries
calc_charm    → Simple Calculator
sort_glyphs   → Sort Tuples by Second Element
unfold_scroll → Flatten Nested List
lost_number   → Find Missing Number
mirror_words  → Check if Strings are Anagrams
exit_spell    → Exit the Spellbook

Type your magic key: calc_charm
Program: Simple Calculator Using Functions

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return 'Invalid operator'
    
Test Case 1: calculate(10, 5, '+') → 15
Test Case 2: calculate(6, 2, '*') → 12
Explanation: Use conditional statements to handle operator-based arithmetic.


=====================================================

	~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~

=====================================================

<--- Functions You Didn’t Know You Needed --->
     -------------------------------------

rev_spell     → Reverse a String
freq_potion   → Character Frequency Counter
cleanse_list  → Remove Duplicates from List
shared_runes  → Find Common Elements
dict_fuse     → Merge Dictionaries
calc_charm    → Simple Calculator
sort_glyphs   → Sort Tuples by Second Element
unfold_scroll → Flatten Nested List
lost_number   → Find Missing Number
mirror_words  → Check if Strings are Anagrams
exit_spell    → Exit the Spellbook

Type your magic key: sort_glyphs
Program: Sort List of Tuples by Second Element

def sort_by_second(lst):
    return sorted(lst, key=lambda x: x[1])
    
Test Case 1: sort_by_second([(1,3), (2,2), (3,1)]) → [(3,1), (2,2), (1,3)]
Test Case 2: sort_by_second([('a',5), ('b',3)]) → [('b',3), ('a',5)]
Explanation: We use `sorted()` with key as the second item in each tuple.


=====================================================

	~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~

=====================================================

<--- Functions You Didn’t Know You Needed --->
     -------------------------------------

rev_spell     → Reverse a String
freq_potion   → Character Frequency Counter
cleanse_list  → Remove Duplicates from List
shared_runes  → Find Common Elements
dict_fuse     → Merge Dictionaries
calc_charm    → Simple Calculator
sort_glyphs   → Sort Tuples by Second Element
unfold_scroll → Flatten Nested List
lost_number   → Find Missing Number
mirror_words  → Check if Strings are Anagrams
exit_spell    → Exit the Spellbook

Type your magic key: unfold_scroll
Program: Flatten a Nested List

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
    
Test Case 1: flatten([[1, 2], [3, [4]]]) → [1, 2, 3, 4]
Test Case 2: flatten([1, [2, [3, [4]]]]) → [1, 2, 3, 4]
Explanation: Recursively flatten sublists and append to result list.


=====================================================

	~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~

=====================================================

<--- Functions You Didn’t Know You Needed --->
     -------------------------------------

rev_spell     → Reverse a String
freq_potion   → Character Frequency Counter
cleanse_list  → Remove Duplicates from List
shared_runes  → Find Common Elements
dict_fuse     → Merge Dictionaries
calc_charm    → Simple Calculator
sort_glyphs   → Sort Tuples by Second Element
unfold_scroll → Flatten Nested List
lost_number   → Find Missing Number
mirror_words  → Check if Strings are Anagrams
exit_spell    → Exit the Spellbook

Type your magic key: lost_number
Program: Find the Missing Number in a List

def find_missing(lst, n):
    total = n * (n + 1) // 2
    return total - sum(lst)
    
Test Case 1: find_missing([1,2,4,5], 5) → 3
Test Case 2: find_missing([1,3], 3) → 2
Explanation: Use sum formula of 1 to N and subtract actual sum of list.


=====================================================

	~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~

=====================================================

<--- Functions You Didn’t Know You Needed --->
     -------------------------------------

rev_spell     → Reverse a String
freq_potion   → Character Frequency Counter
cleanse_list  → Remove Duplicates from List
shared_runes  → Find Common Elements
dict_fuse     → Merge Dictionaries
calc_charm    → Simple Calculator
sort_glyphs   → Sort Tuples by Second Element
unfold_scroll → Flatten Nested List
lost_number   → Find Missing Number
mirror_words  → Check if Strings are Anagrams
exit_spell    → Exit the Spellbook

Type your magic key: mirror_words
Program: Check if Two Strings are Anagrams

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
    
Test Case 1: is_anagram('listen', 'silent') → True
Test Case 2: is_anagram('hello', 'world') → False
Explanation: Sort both strings and compare equality to check anagram.


=====================================================

	~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~

=====================================================

<--- Functions You Didn’t Know You Needed --->
     -------------------------------------

rev_spell     → Reverse a String
freq_potion   → Character Frequency Counter
cleanse_list  → Remove Duplicates from List
shared_runes  → Find Common Elements
dict_fuse     → Merge Dictionaries
calc_charm    → Simple Calculator
sort_glyphs   → Sort Tuples by Second Element
unfold_scroll → Flatten Nested List
lost_number   → Find Missing Number
mirror_words  → Check if Strings are Anagrams
exit_spell    → Exit the Spellbook

Type your magic key: exit_spell
The spellbook closes... Farewell, wizard!
