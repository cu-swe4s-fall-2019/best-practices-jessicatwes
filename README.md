# Assignment 1: Best-practices

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
Shell script to run tests on get_column_stats.
```
bash basics_test.sh
```