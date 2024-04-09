def main():
    PATH_TO_FILE = "books/frankenstein.txt"
    text = get_book_text(PATH_TO_FILE)
    words_num = count_words(text)
    letters_counted = count_letters(text)
    print(letters_counted)
   
def get_book_text(path): 
    with open(path) as f:
        return f.read()

def count_words(input_text):
    words = input_text.split()
    counted_num = len(words)
    return counted_num

def count_letters(input_text):
    chars = {}
    report = []
    for c in input_text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    for i, k in chars.items():
        if i.isalpha():
            report.append({"name": i, "num": k})

    def sort_on(dict):
        return dict["name"]
    report.sort(reverse=False, key=sort_on)
    report_text = "--- Begin report of books/frankenstein.txt ---\n"
    report_text += str(count_words(input_text)) + " words found in the document\n"
    for i in report:
        report_text += "For the letter " + str(i["name"]) + " there have been " + str(i["num"]) + " amount of letters found" + "\n"
    report_text += "--- END OF REPORT ---"
    return report_text


main()