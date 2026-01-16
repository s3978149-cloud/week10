"""
Exercise 3 — Replace Words from a Mapping
Inputs: text.txt, mapping.txt
● mapping.txt format: each line is old_word,new_word (one pair per line)
Task: Create replaced.txt by replacing every occurrence of old_word with new_word
for all pairs in mapping.txt.
Requirement: Apply mappings in the order they appear in mapping.txt.


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s)
"""


def load_mappings(mapping_file):
    mappings = []
    try:
        with open(mapping_file, "r") as infile:
            for line in infile:
                old_word, new_word = line.strip().split(",")
                mappings.append((old_word, new_word))
    except FileNotFoundError:
        print(f"Error: {mapping_file} file not found.")
    except Exception as e:
        print(f"Error reading mappings: {e}")
    return mappings


def replace_words(input_txt, output_txt, mappings):
    try:
        with open(input_txt, "r") as infile:
            content = infile.read()
            for old_word, new_word in mappings:
                content = content.replace(old_word, new_word)
        with open(output_txt, "w") as outfile:
            outfile.write(content)
    except FileNotFoundError:
        print(f"Error: {input_txt} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


mappings = load_mappings("mapping.txt")
replace_words("text.txt", "replaced.txt", mappings)
