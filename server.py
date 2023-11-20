from flask import Flask,render_template,request,redirect
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from dotenv import load_dotenv
load_dotenv() 


pwd=os.getenv("password")
email="h85316085@gmail.com"
password = pwd
email_server = "smtp.gmail.com"
email_port = 587


def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = "hariprasaths21cs@psnacet.edu.in"
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    with smtplib.SMTP(email_server, email_port) as server:
        server.starttls()
        server.login(email, password)
        server.sendmail(email,"hariprasaths21cs@psnacet.edu.in", msg.as_string())

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<pagename>")
def any(pagename):
    return render_template(pagename)

@app.route("/submit",methods=['POST','GET'])
def submit():
    if request.method=="POST":
        data = request.form.to_dict()
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        subject = f"New Form Submission from {email}"
        body = f"Email: {email}\nMessage: {message}"
        send_email(subject, body)
        return redirect("/thanks.html")

if __name__ == "__main__":
    app.run()
