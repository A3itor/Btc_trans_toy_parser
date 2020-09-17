# Bitcoin

This small project is the result of the final assignment from "Programming for Data Science" from UOC.
It parses raw .json generated files that contain data from bitcoin blocks and transactions and extracts some information afterwards. It is a toy tool only meant to get comfortable programming and debugging with an IDE 


## Author
   Aitor \
  [Github](https://github.com/A3itor) \
  [Linkedin](https://www.linkedin.com/in/aitorjara/)


## Getting Started

These instructions will get us a copy of the project up and running on our local machine.
First of all the repository has been tested with a virtual machine with roughly ~5MBs of RAM and 2 CPUS, to be able to fit in memory the txs.json and store it into a dictionary. Even though the file needs 1.1GByte for storage it requires significantly more memory to perform operations on it. It might work with less memory.  
First of all, if we are not using an IDE like Pycharm, that automatically sets up a virtual environment for us, we will need to open a terminal and make a virtual environment by ourselves by typing the following command:
```
python3 -m venv Bitcoin
```
This will create a virtual environment called "Bitcoin" on our local machine, in the current directory.
Next we will activate the virtual environment, with the following command:
```
source Bitcoin/bin/activate
```
Because we just created this virtual environment, it is empty and we need to install the dependencies (libraries) that the software needs to run correctly.
To do that we just run the following command:
```
pip install -r requirements.txt
```
Because Pycharm can show the following error message: "Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  plt.show()
"
it is recommended to install tkinter running the following command:
```
 sudo apt-get install python3.6-tk
```

Now, in order to run this package we simply need to run the main.py file with the following command:
```
python3 main.py
```

Now, the main.py file has some options based on preferences:
We can assign different variables to the parameters PATH, TRANSACTIONS, BLOCKS, CONTROL_TIME,
based on where we have the source files or if we want to display additional information about
the time it takes to parse those files.

### Static method:
We might have the files in our Desktop rather than in the ./Downloads folder. Thus, we would assign
```os.path.join(os.path.expanduser('~'), 'Desktop')``` to PATH.\
We might even have a different .json called ```random.json``` with transactions data. Then, we would assign
```os.path.join(PATH, 'random.json')``` to TRANSACTIONS.\
We might want to control the execution time of the parsing of this file. Then, we would assign
```True``` to CONTROL_TIME

### Dynamic method:
This is a more advanced method, more convenient, that allows us to change those parameters in-the-run when we execute the file, without changing any line of the original code, for example:

We can run ```python3 main.py --path /home/datasci/Desktop``` or a simplified command: ```python3 main.py -p /home/datasci/Desktop``` if we have the .json files there\

We can also run ```python3 main.py --transactions /home/datasci/Downloads/random.json``` or a simplified command: ```python3 main.py -t /home/datasci/Downloads/random.json```
to tell the program we have a file called ```random.json``` instead of ```txs.json```.\

Or we can run ```python3 main.py --control_time True``` or a simplified command: ```python3 main.py -ctrl True```
to display the execution time of the parsing of the .json file

Or we might run two of them with the simplified version:\
```python3 main.py -p /home/datasci/Downloads -ctrl True```

The program should take around ~20 seconds to execute using an average laptop


## Structure of the repository
As we have already mentioned, the main goal of this mini-project is to parse and extract information from raw .json files that contain data about bitcoin blocks and transactions.
The package data contains a script that parses the .json files and extracts information from them, as well as draws some interactive plots (THERE IS ONLY ONE AT THE MOMENT). The module _tests_ must be run from the same module and makes sure all the functions contained in the module data.dataset work fine (THERE IS ONLY ONE AT THE MOMENT). Last but not least, the module main.py puts everything together and allows us to use different values for the parameters in order to display the information that we want. For example, we could decide that we want to display or to not display the execution time for the loading part of the dataset, by passing True or False to the parameter CTRL_TIME. If we don't want to use this parameter it will display the execution time by default.



## The dataset
The dataset consists of two .json files containing a subset of bitcoin transactions and blocks
