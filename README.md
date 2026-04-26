# OBJ-Group-Project
Programming assignment for object orientating programming

Group Members: Daniel Episcopo, Troy Naill, Atahan Ors

Description of assiament: This is a database driven application that uses the U.S Social Security baby name data in order to provide the statistical insights about names. Data is loaded into a SQLite database and can be accessed through both a console based application and a FastAPI web API. Users can search for a name and retrive info for example the year it was most popular, the top 10 most poular years, and estimated age.

How to run application + the API below:
First go to this website: https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-data and download the SSA baby name dataset. Then extract the files and place all txt files into the api_app folder. Example of a txt: yob2019.txt 
Then after that load the the database by going to tha api_app and run load_data.py and wait until you see this message: "Database loaded successfully." 

Then in the terminal type: "python -m uvicor api_app.main:app --reload" to run the api. After open up your browser and enter this http://127.0.0.1:8000. If everthing is working should pop up with "Baby Name API is running"

To run the cosole application go to the project root folder and run: console_app/consolap.py and then you can use the menu to do the following things below:
-Add records
- Search names
- Update records
- Delete records
- View sample data
