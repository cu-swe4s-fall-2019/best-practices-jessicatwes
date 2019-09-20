# Assignment 1 and 2: Best-practices and Unit Testing, respectively
Part 1 of this assignment (assignment 1) adheres to Best Practices as layout in PEP8 style guide for Python. The python scripts were written in Python 3.0 release 3.6. Development environment set-up includes conda environment managment and installing pycodestyle.

Part 2 of this assignment (assignment 2) adds unit testing.

## Software requirement
### Update and configure Conda done in terminal
```
conda update --yes conda
conda config --add channels bioconda
echo ". HOME/miniconda3/etc/profile.d/conda.sh" >> HOME/.bashrc
```
### Create swe4s environment (require only once)
```
conda create --yes -n swe4s
conda install --yes python=3.6
```
### Starting conda (required each time you log in)
```
conda activate swe4s
```
### Install pycodestyle library with pip or conda, respectively
```
pip install pycodestyle
```
```
conda install -y pycodestyle
```

## style.py
### Updates
* Fixed style errors adhering to PEP8 and based on pycodestyle output

## get_column_stats.py
### Updates
* Fixed style errors adhering to PEP8 and based on pycodestyle output
* Added exception handling to detect bad input
* Modularizing code with usage of function

### Usage
Purpose of code is to get the mean and standard deviation for column specified by user within the input file. 
```
python3 get_column_stats.py --input_file <input_file> --col_num <column_number>
```

## basics_test.sh
### Updates
* Add line to use ssshtest
* Add tests to test the parameter validation
* Include test for expected values and random values

### Usage
Shell script to run functional tests on get_column_stats.
```
bash basics_test.sh
```

Python script to run unit tests on get_column_stats.
```
python basics_test.py
```
