def name_number(func):
    def wrapper(arg):
        name_file = arg.replace('.txt','')
        words = (arg.replace('.txt','')).count("_") + 1
        print(name_file)
        print(words)

def read_print_text (text_file):
    if text_file.endswith('.txt'):
        text_file.read()
        print(text_file)
    else :
        pass