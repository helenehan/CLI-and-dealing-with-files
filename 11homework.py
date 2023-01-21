
# first step, to see if changing file works, this works



# import argparse

# parser = argparse.ArgumentParser(description="write the sentence in capital letters") 

# parser.add_argument('--input', help='an input file', required=True)

# args = parser.parse_args()

# def changeupper(input):
#     "this function changes a whole text to capital letters"
#     with open(input, encoding='utf-8') as poem_file:
#         content = poem_file.read()
#         print(content.upper())

# changeupper(args.input)





# second step, doesn't work (I tried many variations), 
# so my terminal says "Unsupported Operation: not readable", however the output file has the upper letter text in it, which is interesting

import argparse

parser = argparse.ArgumentParser(description="input und output file") 

parser.add_argument('--input', help='an input file', required=True)
parser.add_argument('--output', help='changes will be saved to output file', required=True)
parser.add_argument("--indent", action="store_true", help=("name will be indented by 2 spaces"))

args = parser.parse_args()

def changeupper(input, output, indent=False):
    with open(input,'r', encoding='utf8') as input_file:
        text = input_file.read()
    with open(output, 'w', encoding='utf8') as output_file:
        output_file.write(text.upper())
        if indent:
            print("  ", end="")
            print(output_file.read())
        else :
            print(output_file.read())
            
    

changeupper(args.input, args.output, args.indent)



# --> terminal: python3 11homework.py --input 11hwtext.txt --output 11hwoutput.txt


