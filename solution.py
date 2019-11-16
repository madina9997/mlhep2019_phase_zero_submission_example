#!/usr/bin/python
import sys
import pandas as pd
import numpy as np

def main():
    input_dir, output_dir = sys.argv[1:]
    # opening of initial data and converting it to dataframe structure
    # of numpy package and then into pandas in order to have names for columns
    df = np.loadtxt(input_dir + '/data.data')
    df = pd.DataFrame(df, columns=['column 1', 'column 2'])
    # creating new column where stored the sum of two previous columns
    df['result'] = df['column 1'] + df['column 2']
    # saving to file
    np.savetxt(output_dir + '/data.predict', np.array(df['result']))
    return 0

if __name__ == "__main__":
    main()