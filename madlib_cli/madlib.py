import re
print(
'''
Welcome to Michael's Madlib

I need some words from you. I'll tell
You what type, and you enter a word. Ready or not, here we go




'''
)
user_answers_list = []

def fill_user_answers_list(word_types):
  for i in word_types:
    user_answers_list.append(input(f"Please enter a/an {i} > "))
  
  return user_answers_list

def read_template(file_path):
  try:
    with open (file_path)as template:
      contents = template.read()

    stripped_contents = contents.strip()
    return stripped_contents
  
  except FileNotFoundError:
    raise

def parse_template(string):
  inputed_string = string
  
  stripped = tuple(re.findall(r"\{(.*?)\}", inputed_string))

  string = re.sub(r"\{(.*?)\}", "{}", inputed_string)
  
  return (string, stripped)
  
  
def merge(bare_template, user_input_list):
  text = bare_template.split()
  my_list = user_input_list
  
  for i in range(len(text)):
    brackets = re.match(r"\{(.*?)\}", text[i])
    if brackets and len(my_list) > 0:
      new_word = my_list.pop(0)
      text[i] = new_word
    
    final_string = ' '.join(text)
  
  print (final_string)




stripped_contents = read_template("assets/madlibs-template.txt")
empty_brackets = parse_template(stripped_contents)

fill_user_answers_list(empty_brackets[1])

merge(empty_brackets[0], user_answers_list)  