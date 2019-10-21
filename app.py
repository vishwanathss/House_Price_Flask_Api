from flask import Flask,request,render_template, jsonify,url_for
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
	features=[int(x) for x in request.form.values()]
	print(features)
	feature_vals=[np.array(features)]
	
	prediction=model.predict(feature_vals)
	output=round(prediction[0],2)
	return render_template('result.html',prediction_text='Predicted house price is $ {}'.format(output))





if __name__ == '__main__':
 app.run(debug=True)