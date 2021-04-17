# Wafer-Fault-Detection

#### Description: 

---

The inputs of various sensors for different wafers have been provided. In electronics, a wafer (also called a slice or substrate) is a thin slice of semiconductor used for the fabrication of integrated circuits. The goal is to build a machine learning model which predicts whether a wafer needs to be replaced or not (i.e., whether it is working or not) based on the inputs from various sensors. 



![image](https://user-images.githubusercontent.com/62303495/115117581-f6e80180-9fbc-11eb-975f-cf31b8830d14.png)


There are 590 sensor columns & having more than 41 number of files. There are two classes: +1 and -1. 
+1 means that the wafer is in a working condition and it doesn’t need to be replaced.
-1 means that the wafer is faulty and it needs to be replaced.


#### Architecture: 

---

![image](https://user-images.githubusercontent.com/62303495/115117717-a3c27e80-9fbd-11eb-9be8-e935458ca0e7.png)

We have training files, we need to have a DSA agreement which is been provided to the Client. We have Schema file from Client contain information about training files:

Name of the files, Length of Date value in FileName, Length of Time value in FileName, Number of Columns, Name of the Columns, and their datatype.

#### Steps For Training Files: 


> Data Validation:
 - Name Validation
 - Number Of Columns
 - Name Of Columns
 - Data Type of columns
 - Null Value in Columns
      
> Data Insertion in Database
 - Database Create & Connect
 - Table Creation in the Database
 - Data Inserted in the tab;e

All the Steps are done for validating data based on Schema File. If it matches Criteria it   moved to Good Data or else Bad Data Folder 

> Model Training
 - Data Exported from Database
 - Data Preprocessing
 - Cluster the data using K-Means
     
     ![image](https://user-images.githubusercontent.com/62303495/115118888-23068100-9fc3-11eb-9600-c6f836656374.png)

> Model Selection
  
        Once clusters are created, we find the best model for each cluster. We are using two algorithms, "Random Forest" and "XGBoost". For each cluster, both the algorithms are passed with the best parameters derived from GridSearch. We calculate the AUC scores for both models and select the model with the best score. Similarly, the model is selected for each cluster. All the models for every cluster are saved for use in prediction. 
     
    
   



