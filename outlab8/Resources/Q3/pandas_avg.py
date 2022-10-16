import pandas as pd

def read_data(file_name):
    r"""
        This function reads the contents from the file,
        specified by the file_name into a pandas DataFrame.
    """
    df = pd.read_csv(file_name)
    return df

def compute_avg(data_frame):
    r"""
        This function takes in a DataFrame and returns another 
        DataFrame with the computed averages
    """
    # btech_total = 0
    # btech_count = 0
    # ms_total = 0
    # ms_count = 0
    # phd_count = 0
    # phd_total = 0
    # for i in range(0,len(data_frame.index)):
    #     if data_frame["programme"][i] == "BTech":
    #         btech_total += data_frame["cgpa"][i]
    #         btech_count +=1
    #     elif data_frame["programme"][i] == "MS":
    #         ms_total += data_frame["cgpa"][i]
    #         ms_count +=1
    #     elif data_frame["programme"][i] == "PhD":
    #         phd_total += data_frame["cgpa"][i]
    #         phd_count +=1
    # btech_avg = btech_total/btech_count
    # ms_avg = ms_total/ms_count
    # phd_avg = phd_total/phd_count
    # data = {"programme":["BTech","MS","PhD"],"cgpa":[btech_avg,ms_avg,phd_avg]}
    # df = pd.DataFrame(data)
    # return df.to_string(index=False)
    return df.groupby("programme").mean(numeric_only=True).to_string()

if __name__ == '__main__':
    df = read_data('example_input.csv')
    print('\n=============INPUT DF=============\n')
    print(df)
    print('\n=============EXPECTED OUTPUT=============\n')
    print(compute_avg(df))