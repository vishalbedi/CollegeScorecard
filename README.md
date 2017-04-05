# CollegeScorecard
This application performs analysis over the college scorecard dataset and shows results within angular client web application.
The choice of server is Flask framework over python. 
Python is chosen because it has an array of data-analytics and machine learning toolkits. 


# Setup
#### Setting Server
 ```bash
 git clone git@github.com:vishalbedi/CollegeScorecard.git
 cd server
 pip install -r requirements.txt
 python run.py
 ```
 
 You will need python installed on your machine to run above commands
 #### Setting Client
 > Make sure you have node ver 6.10.x and npm 3.x.x installed
 ```
 cd client
 npm install karma-cli protractor typescript webpack-dev-server rimraf webpack -g
 npm install
 npm run server
 ```
 
 You can find more information related to angular client from webpack-angular2-starter repo
 
 
