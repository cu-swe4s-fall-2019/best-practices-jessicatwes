import sys
import math
import argparse as ap


# Function to calculate mean
def calc_mean(col_values):
    return (sum(col_values)/len(col_values))


# Function to calculate standard deviation
def calc_stdev(col_values, mean_val):
    return math.sqrt(sum([(mean_val-x)**2 for x in col_values])
                     / (len(col_values)-1))


# Functional testing using argparse to pass in parameters.
def parseArgs():
    parser = ap.ArgumentParser(
        description="Passing in file name and number of columns argument",
        prog='get_column_stats')

    parser.add_argument(
        '--input_file',
        type=str,
        help='Name of Input file',
        required=True)

    parser.add_argument(
        '--col_num',
        type=int,
        help='The number of columns in the input file',
        required=True)

    args = parser.parse_args()
    return args


def main():
    args = parseArgs()
    file_name = args.input_file
    ncol = args.col_num
    col_values = []
    mean = None
    stdev = None

    # Check if valid input file
    try:
        input_file = open(file_name, 'r')
    except FileNotFoundError:
        print("Input file does not exist; Exiting.")
        sys.exit(1)
    except IOError:
        print("Could not read file; Exiting.")
        sys.exit()
    except PermissionError:
        print("Permission denied while reading file; Exiting.")

    # Check number of columns
    try:
        ncol = int(ncol)
    except ValueError:
        print("--col_num must be an integer greater than 0; Exiting")

    if ncol < 0:
        print("--col_num must be an integer greater than 0; Exiting")
        sys.exit(1)

    # Collecting values in column col_num and converting into integers
    for line in input_file:
        try:
            row_values = [int(x) for x in line.split('\t')]
            col_values.append(row_values[ncol])
        except ValueError:
            print("Input file has incorrect formatting " +
                  "resulting in no rows; Exiting")
            sys.exit(1)

    # Calculate mean and standard deviation
    mean = calc_mean(col_values)
    stdev = calc_stdev(col_values, mean)

    print('mean:', mean)
    print('standard deviation:', stdev)


if __name__ == "__main__":
    main()
