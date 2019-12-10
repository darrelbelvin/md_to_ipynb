# md_to_ipynb
Converts markdown files into Jupyter Notebooks.

md_to_ipynb takes in a markdown file and converts it into a Jupyter Notebook.
If the output file is not specified the name of the markdown file will be used
with a .ipynb extension.

## Usage:
```
python md_to_ipynb.py (-o -h) <markdown file> <file to output>
```
Arguments:
- markdown file : the file to be converted
- output file : (optional) name of converted file
- -h   help
- -o   attempts to open the converted file after conversion (using xdg-open)

## Hints:
I suggest placing the script in '~/bin/' then run 
```
echo 'alias md_to_python='python ~/bin/md_to_python.py' >> .bash_aliases
```
You can then run it from the terminal in any folder by simply calling md_to_python

In order for the -o flag to work, your os needs to know how to directly open .ipynb files. For this purpose I reccomend installing [nbopen](https://github.com/takluyver/nbopen) and following the instructions in the readme to integrate with your file manager.