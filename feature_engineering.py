import pandas as pd
import json

final_df = pd.read_csv("final_df.csv")

final_df.job_category.replace('Retial', 'Retail', inplace=True)

job_dict = dict(zip(final_df.jobID, final_df.job_category))

with open("job_dict.json", "w") as d:
    json.dump(job_dict, d, indent=4)


if __name__ == '__main__':
    pass


