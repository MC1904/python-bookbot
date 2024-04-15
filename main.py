def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count(text)
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

main()