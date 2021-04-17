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
  
>Once clusters are created, we find the best model for each cluster. We are using two algorithms, "Random Forest" and "XGBoost". For each cluster, both the algorithms are passed with the best parameters derived from GridSearch. We calculate the AUC scores for both models and select the model with the best score. Similarly, the model is selected for each cluster. All the models for every cluster are saved for use in prediction. 

#### Steps For Prediction Files: 

> Same Steps are followed as per Training Files mentioned above.

#### Deployment:
 
> App been deployed in Pivotal Cloud Foundry Platform.
> Folder Structure:
> ![image](https://user-images.githubusercontent.com/62303495/115119827-03258c00-9fc8-11eb-82b7-51b001a1ee09.png)
> requirements.txt file consists of all the packages that you need to deploy the app in the cloud.
> ![image](https://user-images.githubusercontent.com/62303495/115119840-146e9880-9fc8-11eb-8e2b-166911d3a0a7.png)
> main.py is the entry point of our application, where the flask server starts. Here we will be decoding a base64 to an image, and then we will be making predictions.
> ![image](https://user-images.githubusercontent.com/62303495/115119866-294b2c00-9fc8-11eb-9930-28f8ca999599.png)
> This is the obj.py file where the predictions take place based on the image we are giving input to the model.
> ![image](https://user-images.githubusercontent.com/62303495/115119876-37994800-9fc8-11eb-85f2-fab69e4a5ee8.png)
>  manifest.yml:- This file contains the instance configuration, app name, and build pack language
>  ![image](https://user-images.githubusercontent.com/62303495/115119896-4e3f9f00-9fc8-11eb-8ced-0e5f10909b5f.png)
> ![image](https://user-images.githubusercontent.com/62303495/115119903-53045300-9fc8-11eb-9978-acf9c947a8f5.png)
> ![image](https://user-images.githubusercontent.com/62303495/115119930-77602f80-9fc8-11eb-9c92-654679142092.png)
> ![image](https://user-images.githubusercontent.com/62303495/115119935-7f1fd400-9fc8-11eb-8ea2-0922952c784f.png)
> ![image](https://user-images.githubusercontent.com/62303495/115119947-8c3cc300-9fc8-11eb-9228-60edc67adeee.png)
> ![image](https://user-images.githubusercontent.com/62303495/115119961-9232a400-9fc8-11eb-9ee1-a0d6e4f98f7e.png)
> After the app is successfully deployed in the cloud, you will see the screen below with the route.
> ![image](https://user-images.githubusercontent.com/62303495/115119974-a5de0a80-9fc8-11eb-8d8d-5968097a5467.png)
> Open Postman and see the result.
> ![image](https://user-images.githubusercontent.com/62303495/115119990-b3939000-9fc8-11eb-9cac-ddde3f1d6f8a.png)



   



