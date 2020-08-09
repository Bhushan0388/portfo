from flask import Flask, render_template,request
import csv

app=Flask(__name__)

# ************** with out parammter **********************************
# @app.route('/')
# def hello_world():
#     # return 'Hello, Bhushan'
#     return render_template('index.html') # by default it looks into templates folder

#3 Optimization

@app.route('/')
def myhome():
    return render_template('index.html') # by default it looks into templates folder

# to redirect we dont have to define separate tags/ pages.
# we can use below code
@app.route('/<string:page_name>')
def html_page(page_name):
    print(page_name)
    return render_template(page_name) # by default it looks into templates folder



def write_in_file(data):
    with open('database.text',mode='a') as database:
        email= data["email"]
        subject = data["subject"]
        message = data["message"]
        file=database.write(f'\n {email}, {subject}, {message}')

def write_in_csv(data):
    with open('database.csv',mode='a') as database2:
        email= data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# Submit request from contact.html page
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data=request.form.to_dict()
            write_in_file(data) # it will save the dats in text file
            write_in_csv(data) # it will save the data in csv
            return render_template('/Thankyou.html')
        except:
            return 'did not saved in database'
    else:
        return 'please re-submit'
