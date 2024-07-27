import pandas as pd

def main():
    # Read data from CSV file
    df = pd.read_csv('data.csv')

    # Display the first few rows of the dataframe
    print("First few rows of the data:")
    print(df.head())

    # Print some basic statistics
    print("\nBasic statistics:")
    print(df.describe())

if __name__ == "__main__":
    main()
