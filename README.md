# ----------------THIS CODE IS TO CHECK AND VIEW THE WEBSITES NETWORK STATUS AND SAVE IT IN DATA BASE.----------------------

{
BACKEND:PYTHON FLASK.
FRONTEND:HTML,CSS,JAVASCRIPT.
DATABASE:DB browser sqlite.
}

# <-------------------HOW TO INSTALL AND RUN THE CODE----------------->

# ---->STEP-1: Open terminal and navigate to the project path.
# ---->Step 2: Create a Virtual Environment to isolate project dependencies: To create virtual env run the following commands in terminal.
# On Windows
python -m venv env name

# On macOS/Linux
python3 -m venv env name

# -->Step 3: Activate the Virtual Environment:To activate the virtual environment run this command:
# On Windows
env name\Scripts\activate

# On macOS/Linux
source env name/bin/activate

# -->Step 4: Install the required dependencies using pip: run this command
pip install Flask Flask-SQLAlchemy requests

# --->Step 5: Run the Flask Application: Run this command
# python app.py
If everything is set up correctly, you should see output indicating that the development server is running. By default, the application will be accessible at http://127.0.0.1:5000/ in your web browser.

Step 6: Access the Application
Open your web browser and go to http://127.0.0.1:5000/ to access the website.

# NOW YOU CAN SEE THE WEBSITE STATUS CHECKER PAGE 
 IN THAT PAGE A TABLE TO DISPLAY THE WEBSITES AND ITS STATUS 
 AND ALSO WE CAN CHECK THESE WEBSITES STATUS DYNAMICALLY BY SEARCHING THE WEBSITE NAME Eg:Amazon
 WHEN EVER WE RELOAD THE PAGE OR CHECK ANY WEBSITE FROM THE LIST THEN THE DATA IS STORED IN DATABASE.

