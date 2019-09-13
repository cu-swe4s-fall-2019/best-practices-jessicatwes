#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

echo Test PEP8 style guide via pycodestyle
run style_check_style pycodestyle style.py
assert_no_stdout

run style_check_getcol pycodestyle get_column_stats.py
assert_no_stdout

# Test code with random
(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt
run random_pass python3 get_column_stats.py --input_file data.txt --col_num 2
assert_exit_code 0

echo Test exit code and error message
(for i in `seq 1 100`; do 
    echo -e "$RANDOM,$RANDOM,$RANDOM,$RANDOM,$RANDOM";
done )> data.txt
run random_bad_comma python3 get_column_stats.py --input_file data.txt --col_num 2
assert_in_stdout "Input file has incorrect formatting resulting in no rows; Exiting"
assert_exit_code 1

(for i in `seq 1 100`; do 
    echo -e "$RANDOM $RANDOM $RANDOM $RANDOM $RANDOM";
done )> data.txt
run random_bad_space python3 get_column_stats.py --input_file data.txt --col_num 2
assert_in_stdout "Input file has incorrect formatting resulting in no rows; Exiting"
assert_exit_code 1


# Additional parameter errors
run para_bad_nofile python3 get_column_stats.py --input_file --col_num 2
assert_in_stderr "usage: get_column_stats [-h] --input_file INPUT_FILE --col_num COL_NUM"
assert_exit_code 2

run para_bad_badfilename python3 get_column_stats.py --input_file no_data.txt --col_num 2
assert_in_stdout "Input file does not exist; Exiting"
assert_exit_code 1

run para_bad_nofile python3 get_column_stats.py --input_file data.txt --col_num
assert_in_stderr "usage: get_column_stats [-h] --input_file INPUT_FILE --col_num COL_NUM"
assert_exit_code 2

run para_bad_colbig python3 get_column_stats.py --input_file data.txt --col_num 8
assert_in_stdout "Input file has incorrect formatting resulting in no rows; Exiting"
assert_exit_code 1

run para_bad_col0 python3 get_column_stats.py --input_file data.txt --col_num 0
assert_in_stdout "Input file has incorrect formatting resulting in no rows; Exiting"
assert_exit_code 1

# Test code of expected value
V=1
(for i in `seq 1 100`; do
     echo -e "$V\t$V\t$V\t$V";
 done)> data.txt
run expected_good python3 get_column_stats.py --input_file data.txt --col_num 2
assert_in_stdout "mean: 1.0"
assert_in_stdout "standard deviation: 0.0"

