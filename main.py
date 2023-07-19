from flask import Flask, render_template, request

import os
import subprocess


app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("index.html")



@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        if f:
            # Save the uploaded file in the 'NSE_data' folder
            file_path = os.path.join('NSE_data', f.filename)
            f.save(file_path)

            # Call the Python script to process the uploaded file (bhav copy)
            process_bhav_copy = subprocess.Popen(["python", "bhav_copy.py", file_path])
            process_bhav_copy.wait()

            # Call the Python script to perform technical analysis (abc.py)
            process_abc = subprocess.Popen(["python", "abc.py"])
            process_abc.wait()

            # Call the Python script to identify buy opportunities (ABC_BUYLIST.py)
            process_buylist = subprocess.Popen(["python", "ABC_BUYLIST.py"])
            process_buylist.wait()

            # Redirect the user back to the homepage with a success message
            return render_template('index.html', message="Data processed successfully!")

    return render_template('index.html', message="Failed to process data. Please try again.")


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
