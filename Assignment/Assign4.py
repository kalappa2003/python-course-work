# ==============================================
#   Wizard's Spellbook of Functions 🧙‍♂️✨
# ==============================================

def reverse_str(s):
    result = ''
    for char in s:
        result = char + result
    return result

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def remove_dups(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

def common(lst1, lst2):
    return [item for item in lst1 if item in lst2]

def merge_dicts(d1, d2):
    return {**d1, **d2}

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

def sort_by_second(lst):
    return sorted(lst, key=lambda x: x[1])

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def find_missing(lst, n):
    total = n * (n + 1) // 2
    return total - sum(lst)

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


# ==============================================
# Menu
# ==============================================
def spellbook_menu():
    print("\n=====================================================")
    print("\t~*~*~*~*~  Wizard's Spellbook of Functions  ~*~*~*~*~")
    print("=====================================================")
    print("\n<--- Functions You Didn’t Know You Needed --->")
    print("     -------------------------------------")
    print("rev_spell     → Reverse a String")
    print("freq_potion   → Character Frequency Counter")
    print("cleanse_list  → Remove Duplicates from List")
    print("shared_runes  → Find Common Elements")
    print("dict_fuse     → Merge Dictionaries")
    print("calc_charm    → Simple Calculator")
    print("sort_glyphs   → Sort Tuples by Second Element")
    print("unfold_scroll → Flatten Nested List")
    print("lost_number   → Find Missing Number")
    print("mirror_words  → Check if Strings are Anagrams")
    print("exit_spell    → Exit the Spellbook")


# ==============================================
# Main Interactive Loop
# ==============================================
while True:
    spellbook_menu()
    choice = input("\nType your magic key: ").strip()

    if choice == "rev_spell":
        print("Result:", reverse_str("hello"))

    elif choice == "freq_potion":
        print("Result:", char_frequency("abracadabra"))

    elif choice == "cleanse_list":
        print("Result:", remove_dups([1, 2, 2, 3, 4, 4, 5]))

    elif choice == "shared_runes":
        print("Result:", common([1, 2, 3], [2, 3, 4]))

    elif choice == "dict_fuse":
        print("Result:", merge_dicts({'a': 1}, {'b': 2, 'a': 10}))

    elif choice == "calc_charm":
        print("Result:", calculate(6, 2, '*'))

    elif choice == "sort_glyphs":
        print("Result:", sort_by_second([(1, 3), (2, 2), (3, 1)]))

    elif choice == "unfold_scroll":
        print("Result:", flatten([1, [2, [3, [4]]]]))

    elif choice == "lost_number":
        print("Result:", find_missing([1, 2, 4, 5], 5))

    elif choice == "mirror_words":
        print("Result:", is_anagram("listen", "silent"))

    elif choice == "exit_spell":
        print("The spellbook closes... Farewell, wizard! 🧙‍♂️✨")
        break

    else:
        print("Unknown spell. Try again!")
