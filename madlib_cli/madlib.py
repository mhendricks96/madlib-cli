# Imported modules

import re #regex
print(
'''
Welcome to Michael's Madlib

I need some words from you. I'll tell
You what type, and you enter a word. Ready or not, here we go




'''
)
# Global variables
user_answers_list = []

#Functions

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
  my_list = list(user_input_list)
  
  for i in range(len(text)):
    brackets = re.match(r"\{(.*?)\}", text[i])
    if brackets and len(my_list) > 0:
      new_word = my_list.pop(0)
      text[i] = new_word
    
    final_string = ' '.join(text)
    
  
  print('''
  **************
  Thank You! 
  Here is your completed Madgab!
  **************
  ''')

  print (final_string)
  return (final_string)



# Running Code

if __name__ == "__main__":
  stripped_content = read_template("assets/madlibs-template.txt")
  empty_brackets = parse_template(stripped_content)

  fill_user_answers_list(empty_brackets[1])

  fill_template = merge(empty_brackets[0], user_answers_list) 

  with open('assets/new-madlibs-answer.txt', 'w') as filled_madlib:
    filled_madlib.write(fill_template)
