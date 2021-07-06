# ASCII Name Generator

**Designed and developed by Eduardo Aire**

The **ASCII Art Name Generator** is a simple program that helps you to have a practical Shell/Python workflow understanding, especially if visual outputs make more sense to you. The repository contains two python interactive files with pseudocode in almost every step so you can understand what's happening, the first file is a dictionary of objects defined by the class **Character**, and the second is the one that runs in the terminal giving a controlled result or a random one using the letterforms defined in the first file. The main features of the project are the following ones:

1. It takes an input string (hopefully your name)
2. It asks you if you want a random construction
3. It gives an output with the name stylized with ASCII characters
4. It creates a historic output file that feeds the repository dedicated website at https://eduairet.github.io/asciiArtName/

![Shell program preview](/docs/ims/shellinterface.png)

Before generating your names make sure to have installed the following modules (my advice is to [create a venv](https://docs.python.org/3/library/venv.html) for the project):

1. [Unidecode](https://pypi.org/project/Unidecode/) `pip3 install Unidecode`
2. [termcolor](https://pypi.org/project/termcolor/) `pip3 install termcolor`
3. The files `alphabetDict.py` and `nameGenerator.py` need to be inside the same folder which I've named `asciiNameGenerator` 

I encourage you to download the code, make your letters and create your own ASCII names, if you don't want to code but you want to use it, you just need to do the following steps:

1. Open a terminal in the folder that contains the python files by secondary click or via `cd path/of/directory`:

![Open the terminal](/docs/ims/openterminal.png)

2. Write the command `python3 nameGenerator.py`

![Run the file](/docs/ims/run.png)

3. And follow the instructions

4. If you are using a venv make sure to activate the environment before running the script using `source ./bin/activate` from your project's path 

If you have any inquiries or requests feel free to contact me at (hola@eduairet.com)
