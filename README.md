# Job-Recommender-System
Data Description: Using a data set with columns as jobId, userId, job_category and number of clicks to build a recommender system model.
Domain: Online recruitment consultancy
Dataset: https://drive.google.com/drive/folders/1Pz-5NfqoiQRcXx8gqlfz--ZVSugb0MMe

Problem statement: XYZ .Inc. is similar to naukri.com/indeed.com, where people upload their resumes and check what are the other jobs available to them, The CEO of the company wants to take this further and wants to introduce a premium feature called Personalized Job recommendation system. The CEO has gathered some data ( around 466 Users ) and is looking for a candidate to build this recommender system.

Attribute Information: ● userId : Every user identified with a unique id ● jobId : Every job identified with a unique id ● Clicks : Number of clicks for the corresponding job by the corresponding user ● job_category: Different categories like IT, Retail, Marketing, etc.

Learning Outcomes: ● Exploratory Data Analysis ● Creating a Recommendation system using real data 

Objective: Build a recommendation system to recommend jobs to customers based on the their previous clicks for other jobs.

Steps and tasks:

Read and explore the given dataset. Joined the dataset and cleaned the dataset by replacing few values
Split the data randomly into train and test dataset. 
Built User-based similarity model. 
Built Item-based similarity model.
Evaluated both the models. 
After the model is trained on the training data, it is used to compute the error (RMSE) on predictions made on the test data.
A final data set is created with userIds as columns and top 15 job ids to recommend to the user as rows.
