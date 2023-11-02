from Flask import Flask ,render_templates,request
import request 

app=Flask(__name__)
app.static_folder='static'
@app.route('/templates',methods=['GET','POST','PUT','DELETE'])
def index():
    return