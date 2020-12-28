import pandas as pd


def data_ingestion(file_name):
    df = pd.read_csv(file_name)
    return df


def change_col_name(df):
    df.rename(columns={'jobId': 'jobID'}, inplace=True)
    return df


def merge_data(df1, df2):
    df = pd.merge(df1, df2, on="jobID")
    return df


if __name__ == '__main__':
    clicks = data_ingestion('job_clicks.csv')
    jobs = data_ingestion('jobs.csv')
    clicks = change_col_name(clicks)
    final_df = merge_data(clicks, jobs)
    final_df.to_csv('final_df.csv', index=False)
