from flask import Flask,render_template,request,flash
from ultralytics import YOLO
from flask_mail import Mail,Message
import cv2
import shutil
import os
app = Flask(__name__)
model=YOLO(r"best.pt")

names= {0: '0', 1: '1', 2: '2', 3: 'Fall-Detected', 4: 'Robber-Mask'}

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='t3754271@gmail.com'
app.config['MAIL_PASSWORD']='jjzskwoencqqzxsj'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.secret_key="secret"
mail=Mail(app)

allowed_extension=['jpg','mp4']

@app.route('/',methods=["POST","GET"])

def home():
	global model
	if request.method=="POST":	
		r=request.files["file"]
		file_name=str(r.filename)
		if file_name=="":
			flash("Please Upload a File")
			return render_template("index.html",nofileuploaded=True)
		extension=file_name.rsplit(".",1)[1].lower()
		if extension in allowed_extension:
			r.save('./upload/'+r.filename)
			if extension==allowed_extension[0]:
				if os.path.exists('./static/predict'):
					shutil.rmtree('./static/predict')
				result=model.predict('./upload/'+r.filename,save=True,project="./static/",show_labels=False)
				for r in result:
					boxes=r.boxes
					for box in boxes:
						if int(box.cls[0]) in names:
							message=Message(subject="ALERT!!",sender="t3754271@gmail.com",recipients=['t3754271@gmail.com'])
							message.body="Potential Security Issue Detected Kindly Look ASAP!!"
							with app.open_resource(f"/static/predict/{file_name}") as fp:
								message.attach("image.jpg","image/jpg",fp.read())
								mail.send(message)
							flash("User Got Alerted Potential Security Issue Detected Check ")
							return render_template("index.html",file_name=file_name,image=True)
					else:
						flash("No Thread Found")
						return render_template("index.html",file_name=file_name,image=False)
			elif extension==allowed_extension[1]:
				video=cv2.VideoCapture('./upload/'+file_name)
				fourcc = cv2.VideoWriter_fourcc(*'DIVX')
				width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
				height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
				out=cv2.VideoWriter("./static/prediction.avi",fourcc,20.0,(width,height))
				checklist=set()
				
				while (video.isOpened()):
					ret,frame=video.read()
					if ret==False:
						break
					if ret:
						result=model.predict(frame)
						for r in result:
							box=r.boxes
							for b in box:
								if int(box.cls[0]) in names:
									print("found")
									checklist.add(int(box.cls[0]))
								x1,y1,x2,y2=b.xyxy[0]
								x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
								cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,255),3)
								out.write(frame)
				video.release()
				out.release()

				for item in checklist:
					if item in names:
						checklist=True
						message=Message(subject="ALERT!!",sender="t3754271@gmail.com",recipients=['t3754271@gmail.com'])
						message.body="Potential Security Issue Detected Kindly Look ASAP!!"
						with app.open_resource("./static/prediction.avi") as fp:
							message.attach("video.avi","video/avi",fp.read())
						mail.send(message)
						break
				if checklist:
					
					flash("User Got Alerted Potential Security Issue Detected Check ")
					return render_template("index.html",file_name=file_name,video=True)

				else:

					flash("No Thread Found")
					return render_template("index.html",file_name=file_name,video=False)
	else:
		return render_template("index.html")
@app.route('/contact', methods=["POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        message2 = request.form["text"]
        if name != "" and message2 != "":
            message=Message(subject="Contact-Us-Topic-Mail",sender="t3754271@gmail.com",recipients=['t3754271@gmail.com'])
            message.body=f"User:{name}\nMessage:{message2}"
            mail.send(message)
            flash("Thank you for contacting us.", "success")
            return render_template("index.html",contact=True)
        else:
            flash("Please fill in both fields.", "error")
            return render_template("index.html",contact=False)
if __name__ == '__main__':
	app.run(debug=True)