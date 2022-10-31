from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect
app = Flask(__name__,static_folder= "static", template_folder= "tenmplates")
import sys
import os

@app. route('/', methods=['GET','POST'])
def Menu_func ():
    import os
    
    return render_template('Frontpage.html')


if __name__ == "__main_":
    app.run(debug=True,host='localhost', port=8001)
