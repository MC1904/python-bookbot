def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count(text)
  print(letter_count(text))
  # textile = text.split()
  # print(len(text.split()))

def get_book_text(path):
  with open(path) as f:
    return f.read()

def word_count(text):
  count = 0
  # new_text = text.replace("-"," ")
  new_text = text.replace("\n"," ")
  list = new_text.split(" ")
  list_length = len(list)
  for i in range(list_length):
    if list[i] == "" or list[i] == "***":
      count += 1
  print(len(list)-count)
  return len(list)

def letter_count(text):
  letter_dict = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
  text_lower = text.lower()
  for i in range(len(text_lower)):
    if text_lower[i] in letter_dict:
      letter_dict[text_lower[i]] += 1
  return letter_dict

main()