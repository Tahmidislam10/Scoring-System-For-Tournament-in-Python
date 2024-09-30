**Competition Scoring Program**

This Python Application is designed to automate the scoring process for a multi-event competition involving individuals and teams. The program allows for input of points for various events and calculates rankings for participants.

**Course Information**

Course: BTEC Level 3 Extended Diploma in IT
Unit: Programming
Term: Spring 2021

**Libraries Used**

sys: Used for handling system-related functions, such as safely exiting the program.
The program doesn't require any external libraries, so no additional installations are needed beyond the Python standard library.

**Features**

Supports scoring for multiple events, including:
Art
English
Science
Maths
Sports
Allows input for up to 20 participants.
Supports both team and individual competitions.
Dynamically updates rankings after each event.
Simple error handling to ensure proper input.
How to Use
Run the Script:
Ensure Python is installed on your system.
Execute the script using the following command:
python competition_scoring.py

**Choose Scoring Mode:**

The program will prompt you to choose between teams or individual mode.
Follow the prompts to input participant names and their respective scores for each event.
Input Points:

Points are entered based on rankings, where the 1st place gets the highest points and so on.
Ensure to input points between 1 and 20 as specified by the program.
View Results:

Once all events are scored, the program displays the ranking of each participant based on their accumulated points.
Code Structure
Event Functions:
There are specific functions for each event (singleart(), singlemaths(), singlescience(), etc.).
Each function asks for participant names and points.
Error Handling:
Input validation ensures that the entered points are numbers within the accepted range (1-20).


**Example Output**

![image](https://github.com/user-attachments/assets/71dbab41-31f3-428e-b403-f5e90ce645d2)


**Contributing**

Feel free to fork the repository and submit pull requests for any improvements or new features.

**License**

This project is licensed under the MIT License.
