print("Welcome to Michael's Madlib")
print('''I need some words from you. I'll tell
You what type, and you enter a word. Ready or not, here we go
''')
print('''



''')
def read_template(file_path):

  with open (file_path)as template:
    contents = template.read()

  #print(contents)
  stripped_contents = contents.strip()
  return (stripped_contents)

def parse_template():
  print("hi")

def merge():
  print("bye")

read_template("assets/madlibs-template.txt")
