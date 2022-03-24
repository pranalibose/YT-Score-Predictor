<h2>Video Engagement Score Predictor</h2>

![YT Score Predictor Screenshot](https://user-images.githubusercontent.com/92683605/159986675-16860db8-11be-4c9a-b3c8-e655ea7cf751.PNG)

<h3>About the Project</h3>
This is an application that predicts the engagement score of a video based on certain parameters like the category to which it belongs or the age of the viewer.
This app can be used to determine whether a viewer will like a video, based on which perhaps it might be recommended to him/her. 
<p> This is a supervised Learning Problem where the target/label was provided. CatBoost algorithm has been used to train the regressor model. The frontend is built on Python's Flask framework.

<h3>Steps of app building:</h3>
<ol>
  <li> Reading the data from csv file (Kaggle Dataset)
  <li> Exploratory Data Analysis
  <li> Feature Engineering
  <li> Feature Selection
  <li> Model Building
  <li> Comparison of models and remodelling
  <li> Saving the final model as a pickle file
  <li> Building a flask app
</ol>  

<h3>Built With:</h3>
<ol>
  <li> Python 
  <li> Pandas 
  <li> Matplotlib
  <li> Seaborn
  <li> Numpy
  <li> Scikit-Learn
  <li> Flask
  <li> HTML
  <li> CSS
  <li> Bootstrap
</ol>

<h3>Steps to execute the app:</h3>
<ul>
  <li> Make a virtual environment using "conda create -n envname python=3.6 pip"
  <li> source activate envname (for mac/linux) | activate envname (for windows)
  <li> Download or clone this repo by git clone https://github.com/pranalibose/YT-Score-Predictor.git
  <li> pip install -r requirements.txt
  <li> Run the app using python `python app.py`
</ul>
