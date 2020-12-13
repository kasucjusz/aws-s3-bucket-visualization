import boto3 as boto3
from flask import Flask, render_template

app = Flask(__name__)
s3 = boto3.resource(
    service_name='s3',
)
bucket = s3.Bucket('ka-app-069436461438')


@app.route("/")
def index():
    keylist = []
    for obj in bucket.objects.filter(Prefix='data/'):
        spl = obj.key.split('/')
        try:
            keylist.append((spl[1], spl[2]))
        except Exception as e:
            pass
    return render_template("index.html", context={'keylist': keylist}, len=len(keylist))


if __name__ == '__main__':
    app.run()
