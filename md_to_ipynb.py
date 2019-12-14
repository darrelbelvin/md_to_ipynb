import sys
import json
import subprocess
import re

regex = r"(^[#]+ )|(^\d[\\]?[\.]?)"

def convert(file_in, file_out):
    with open(file_in, 'r') as filehandle:
        lines = filehandle.readlines()
    
    lines = ''.join(lines)
    matches = re.finditer(regex, lines, re.MULTILINE)
    indices = [match.span()[0] for match in list(matches)]
    if indices[0] != 0:
        indices.insert(0,0)
    indices.append(len(lines))
    cells = [lines[indices[i]:indices[i+1]] for i in range(len(indices)-1)]
    js = {
        "cells":[{
                 "cell_type":"markdown",
                 "metadata":{},
                 "source":cell
                 } for cell in cells],
        "metadata":{},
        "nbformat":4,
        "nbformat_minor":2
    }
    
    with open(file_out, 'w') as filehandle:
        filehandle.writelines(json.dumps(js,indent=4, separators=(',', ': ')))

if __name__ == "__main__":
    try:
        args = sys.argv[1:]
        h = False
        o = False
        f1 = ""
        f2 = ""
        for arg in args:
            if arg == '-h':
                h = True
            elif arg == '-o':
                o = True
            elif arg[0] == '-':
                print("Unrecognized flag: {}".format(arg))
            elif f1 == "":
                f1 = arg
            elif f2 == "":
                f2 = arg

        if h:
            print("""python md_to_ipynb.py -o -h <markdown file> <file to output>
This command takes in a markdown file and converts it into a Jupyter Notebook.
If the output file is not specified the name of the markdown file will be used
with a .ipynb extension.

Arguments:
  -h   help
  -o   attempts to open the converted file after conversion (using xdg-open)""")
        elif f1 == "":
            print("Missing filename argument")
        else:
            if f2 == "":
                if(f1.endswith(".md")):
                    f2 = f1[:-3] + ".ipynb"
                else:
                    f2 = f1 + ".ipynb"
            
            convert(f1, f2)

        if o:
            bashCommand = f"xdg-open {f2}"
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()

    
    except IOError:
        print("File not accessible")