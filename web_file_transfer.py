
from flask import Flask,render_template,request,redirect
from flask.ext.script import Manager
from werkzeug import secure_filename
import os

app=Flask(__name__)
UPLOAD_FOLDER='/home/zjc/Downloads'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
manager=Manager(app)


@app.route('/')
def index():
	return render_template('UI.html') 
@app.route('/user/' ,methods=['GET','POST'])
def user():
	if request.method =='POST':
		file=request.files['file']
		if file :
			filename=secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			return '<h1> finished ,please close the web </>'
		else:
			return "wrong !!!!!"
	
		

		

if __name__=='__main__':
	manager.run()
