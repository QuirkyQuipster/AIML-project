from flask import *
import pandas as pd
from sklearn.linear_model import LinearRegression
#from sklearn.pipeline import Pipeline
#from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

app=Flask(__name__)


@app.route('/')       #### default route
def index():
    return render_template('index.html')
  


##################### DIAMONDS PRICE PREDICTION###############

url="https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/diamond.csv"
df1=pd.read_csv(url)
df1.drop('Unnamed: 0', axis=1, inplace=True)
df1.cut.replace(['Premium', 'Ideal','Good','Very Good','Fair'], [1, 2,3,4,5], inplace=True)
df1.color.replace(['D','E','F','G','H','I','J'], [1,2,3,4,5,6,7], inplace=True)
df1.clarity.replace(['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'], [1,2,3,4,5,6,7,8], inplace=True)

df1 = df1.drop(df1[df1["x"]==0].index)
df1 = df1.drop(df1[df1["y"]==0].index)
df1= df1.drop(df1[df1["z"]==0].index)


#Dropping the outliers.
df1 = df1[(df1["depth"]<75)&(df1["depth"]>45)]
df1 = df1[(df1["table"]<80)&(df1["table"]>40)]
df1 = df1[(df1["x"]<30)]
df1 = df1[(df1["y"]<30)]
df1 = df1[(df1["z"]<30)&(df1["z"]>2)]

X= df1.drop(["price"],axis =1)
Y= df1["price"]

model_1=RandomForestRegressor()
model_1.fit(X,Y)
#0.29	1	5	3	62.4	58.0	403	4.24	4.26	2.65
res_1=model_1.predict([[0.29,	1	,5,	3,	62.4	,58.0,4.24	,4.26	,2.65]])
op_1=str(round(res_1[0])) + ' $'
op_1
########################################################



@app.route("/dproject")
def dproject():
  return render_template("dform.html")

@app.route("/dpredict",methods=["POST"])
def dpredict():
  carat=float(request.form["carat"])
  cut=int(request.form["cut"])
  color=int(request.form["color"])
  clarity=int(request.form["clarity"])
  depth=float(request.form["depth"])
  table=float(request.form["table"])
  x=float(request.form["x"])
  y=float(request.form["y"])
  z=float(request.form["z"])
  res_1=model_1.predict([[carat,cut,color,clarity,depth,table,x,y,z]])
  op_1= "      Predicted Price: " +str(round(res_1[0]))+" $"
  return render_template("dform.html",result_1=op_1)

if __name__=="__main__":
  app.run()
  
  

  
  

  
  