"""
Exercise 2 — Extract Email-like Lines
Input: contacts.txt (one contact per line)
Task: Create emails_only.txt containing only lines that contain the character @.
Requirement: Preserve original line order.


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s)
"""


def extract_email_lines(input_txt, output_txt):
    try:
        with open(input_txt, "r") as infile, open(output_txt, "w") as outfile:
            for line in infile:
                if "@" in line:
                    outfile.write(line)
    except FileNotFoundError:
        print(f"Error: {input_txt} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


extract_email_lines("contacts.txt", "emails_only.txt")
