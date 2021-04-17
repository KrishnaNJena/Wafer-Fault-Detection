import os
from flask import Flask,request,render_template,Response
from wsgiref import simple_server
from flask_cors import CORS,cross_origin
import json
import  flask_monitoringdashboard as dashboard
from trainingModel import trainModel
from training_Validation_Insertion import train_validation
from prediction_Validation_Insertion import pred_validation
from predictFromModel import prediction

os.putenv('LANG','en_US.UTF-8')
os.putenv('LANG','en_US.UTF-8')

app = Flask(__name__)
dashboard.bind(app)
CORS(app)

@app.route("/",methods=["GET"])
@cross_origin()
def home():
    return render_template('home.html')

@app.route("/train", methods=['GET'])
@cross_origin()
def trainRouteClient():

    try:
        # if request.json['folderPath'] is not None:
            # path = request.json['folderPath']
        path = 'Training_Batch_Files'
        train_valObj = train_validation(path) #object initialization

        train_valObj.train_validation()#calling the training_validation function


        trainModelObj = trainModel() #object initialization
        trainModelObj.trainingModel() #training the model for the files in the table


    except ValueError:

        return Response("Error Occurred! %s" % ValueError)

    except KeyError:

        return Response("Error Occurred! %s" % KeyError)

    except Exception as e:

        return Response("Error Occurred! %s" % e)
    return Response("Training successfull!!")

@app.route("/predict",methods=["POST"])
@cross_origin()
def predictRouteClient():
    try:
        if request.json is not None:
            path=request.json["filepath"]
            pred_val=pred_validation(path) # Object Initialisation
            pred_val.prediction_validation() #calling the prediction_validation function
            pred = prediction(path) #object initialization
        
        # predicting for dataset present in database
            path,json_predictions = pred.predictionFromModel()
            return Response("Prediction File created at !!!"  +str(path) +'and few of the predictions are '+str(json.loads(json_predictions) ))
        elif request.form is not None:

            path = request.form['filepath']

            pred_val = pred_validation(path) #object initialization

            pred_val.prediction_validation() #calling the prediction_validation function

            pred = prediction(path) #object initialization

            # predicting for dataset present in database
            path,json_predictions = pred.predictionFromModel()
            return Response("Prediction File created at !!!"  +str(path) +'and few of the predictions are '+str(json.loads(json_predictions) ))
        else:
            print('Nothing Matched')
    except ValueError:
        return Response("Error Occurred! %s" %ValueError)
    except KeyError:
        return Response("Error Occurred! %s" %KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" %e)


if __name__ == '__main__':
    host='0.0.0.0'
    port=8000 # Port Number
    httpd=simple_server.make_server(host,port, app)
    httpd.serve_forever()