import pandas as pd
import json


def data_ingestion(file_name):
    df = pd.read_csv(file_name)
    return df


def recommend_jobs(userid):
    response_dict = {}
    df = data_ingestion("user_final_clicks.csv")
    with open("job_dict.json") as j:
        job_dict = json.load(j)
    var = df.iloc[int(userid)].sort_values(ascending=False)[0:5]
    job_id = var.index.to_list()
    for i in job_id:
        if i in job_dict.keys():
            response_dict[i] = job_dict[i]
    job_recommend = pd.Series(response_dict).to_frame().reset_index()
    job_recommend.columns = ['Job ID', 'Job Category']
    return job_recommend


if __name__ == '__main__':
    r = recommend_jobs(101)
    print(r)

