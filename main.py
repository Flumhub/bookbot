def main():
    PATH_TO_FILE = "books/frankenstein.txt"
    text = get_book_text(PATH_TO_FILE)
    print(text)
   
def get_book_text(path): 
    with open(path) as f:
        return f.read()
main()