from flask import Flask
from flask import render_template
import socket
import mysql.connector
import os
import boto3
s3 = boto3.client('s3')

app = Flask(__name__)

DB_Host = os.environ.get('MYSQL_SERVICE_HOST') or "localhost"
DB_Database = os.environ.get('DB_Database') or "mysql"
DB_User = os.environ.get('DB_User') or "root"
DB_Password = os.environ.get('DB_Password') or "paswrd"
IMAGE_URL = os.environ.get('IMAGE_URL') or "static"
USER_NAME = os.environ.get('USER_NAME') or ""


@app.route("/")
def main():
    db_connect_result = False
    err_message = ""
    try:
        mysql.connector.connect(
            host=DB_Host, database=DB_Database, user=DB_User, password=DB_Password)
        color = '#39b54b'
        db_connect_result = True
        if IMAGE_URL != 'static':
            s3.download_file(IMAGE_URL, './static/')
    except Exception as e:
        color = '#ff3f3f'
        err_message = str(e)

    return render_template('hello.html', debug="Environment Variables: DB_Host=" + (os.environ.get('MYSQL_SERVICE_HOST') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database') or "Not Set") + "; DB_User=" + (os.environ.get('DB_User') or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password') or "Not Set") + "; " + err_message, db_connect_result=db_connect_result, name=socket.gethostname(), color=color, image_url=IMAGE_URL, user_name=USER_NAME)


@app.route("/debug")
def debug():
    color = '#2196f3'
    return render_template('hello.html', debug="Environment Variables: DB_Host=" + (os.environ.get('MYSQL_SERVICE_HOST') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database') or "Not Set") + "; DB_User=" + (os.environ.get('DB_User') or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password') or "Not Set"), color=color, image_url=IMAGE_URL, user_name=USER_NAME)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
