import re

print("Welcome to Michael's Madlib")
print('''I need some words from you. I'll tell
You what type, and you enter a word. Ready or not, here we go
''')
print('''



''')
user_answers_list = []

def fill_user_answers_list(word_types):
  for i in word_types:
    #print(i)
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
  #print(string)
  inputed_string = string
  
  
  stripped = tuple(re.findall(r"\{(.*?)\}", inputed_string))

  string = re.sub(r"\{(.*?)\}", "{}", inputed_string)
  
  #print(string, stripped)
  
  
  return (string, stripped)
  
  
  #print(string)
  


def merge(bare_template, user_input_list):
  text = bare_template
  my_list = user_input_list
  print(my_list)
  regex = r"\{(.*?)\}"
  # iterate through evert word and if it has the regex, replace it with a new_word
  for word in text:
    new_word = user_input_list.pop()
    text = re.sub(regex, "hi", text, count=1)
      
  #print(text)


  
  #return final_string




stripped_contents = read_template("assets/madlibs-template.txt")
#print(stripped_contents)
empty_brackets = parse_template(stripped_contents)


#print(empty_brackets[0])
#print(empty_brackets[1])

fill_user_answers_list(empty_brackets[1])
print(user_answers_list)

merge(empty_brackets[0], user_answers_list)  