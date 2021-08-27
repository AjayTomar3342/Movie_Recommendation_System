# Movie Recommendation System
Data Science project based on Movie Data for Movie Recommendation procedure in Machine Learning using Python. 

A personal project made for practising and learning Data Science and Machine Learning Techniques. 

### Requirements to run and test the project:

To run this project, you will need Python3+, pip and Git installed on the system. 

The reference links are provided below.

> **Python:**
  https://www.python.org/downloads/
  
> **pip:**
  https://pypi.org/project/pip/

> **Git:**
  https://git-scm.com/downloads
	
The necessary libraries and packages are specified in the **requirements.txt** file and will be validated in the below steps


## Process for acquiring the results: 

  * **Step 1:**
  Create a local directory in your machine where you want to pull the git project and clone the project by running the below command from cmd 
  (Make sure that you are in the newly created directory first!):
  
  	```git clone https://github.com/AjayTomar3342/Movie_Recommendation_System```

  * **Step 2:**
  From cmd, move into the main folder of the cloned project
  
 	 ```cd Movie_Recommendation_System```

  * **Step 3:**
  Execute the below commands to meet the pre-requisites to execute the code
  
  ```  	
      Unix/macOS
      python -m pip install -r requirements.txt

      Windows
      py -m pip install -r requirements.txt
  ```

  
  * **Step 4:**
  Execute the below commands to run the code from cmd
  
  ``` 
      Unix/macOS
      python main.py

      Windows
      %run main.py
  ```
  
  
## Alternative Process for acquiring the results(Backup):

For quick running of program, PyCharm use is suggested as it has good controls for removing manual steps to pull a repository and get it running.

Steps are:

  * **Step 1:**
  Make sure one is signed in on Github in Pycharm
  
  * **Step 2:**
  Open a new project
  
  * **Step 3:**
  Go to VCS Option on the Top Horizontal Options Bar
  
  * **Step 4:**
  Select Enable Version Control Integration Control inside VCS if not done already
  
  * **Step 5:**
  After checking the previous option on, select Checkout from Version Control and select Git
  
  * **Step 6:**
  In the new pop up window, include the link of the github repository you are trying to pull.
  Subsequently in the same pop up window, select an appropriate directory where the  project will be pulled.
  
  * **Step 7:**
  Select clone option to start the pulling process.
  
  * **Step 8:**
  Select option to start the pulled project in New Window or This window as per your personal preference.
  
  * **Step 9:**
  After this the project will be up and running and requirements.txt file will automatically install required libraries. Run the file main.py from Root Folder to get the results

This is a quick process to start the testing of GitHub project taken from the Official Jet Brains Website. We have tried this with several PC’s and are confident that this will not give any errors.

> **Link to Above Process Video:**
  https://www.youtube.com/watch?v=ukbvdF5wqPQ&feature=emb_title
  
  
  **NOTE:** 
Since, the libraries used in the project are updated by the original developers regularly, some function/functions may not run as expected. This project will be regularly updated as per the updated libraries requirement, but if project does not run at any give time when you pull the project, it may be due to the library change, rather than a coding issue. This repository is last updated as per latest libraries on 10/07/2021

## Procedure followed in the Project:

   * **Step 1:**
   Movie data is taken from Kaggle in .dat format. Data is ingested from three files. movies.dat, 	        ratings.dat, users.dat provide movie data, their respective ratings data and users rating data. These        three are then merged in a suitable way for further processing. Input file is above 50 mb(GitHub limit) 	so a zipped version of it is unzipped for furthe procedure to avoid GitHub heavy file limit. 
   
   * **Step 2:**
   Then using Matrix Factorization Collaborative Filtering is done on the input data. This is a mathematical 	approach for Movie Recommendation using data about Users and Movies both. A user-movie matrix is made as    it's important for the matrix factorization step. In this user-movie matrix NA values can be filled          either by mean or by median. This mean/median is taken with respect to the movie rating from the user        movie matrix. Both options are available for us to use and witness difference in the recommendations as      the project output.  
  
   * **Step 3:**
   Movie prediction can be done using two ways:
   1. Finding similar users to the user we are recommending movies for and then recommending the similar 	users movies. 
   2. Finding similar movies as per the user interests(for which we are finding movies). 

   To select the first option above, one must uncomment Line No. 30 and 39 and comment Line No. 33 and 36 in 	file named main.py in the Root Folder of the repository. 
   
   To select the second option above, one must uncomment Line No. 33 and 36 and comment Line No. 30 and 39      in file named main.py in the Root Folder of the repository. 
   

  **NOTE:** 
All .dat files mentioned in the above steps are present in the input_data folder. Power BI file is present in the Root Folder. 

## Results:

When recommendations are made on basis of finding similar users, first similar users are shown in the console(in decreasing order of similarity) and then recommended movies are shown. 

In case of finding similar movies as per user interests, recommended movies are shown directly. 

In both cases, good recommendations were made as observed by 3-4 peers of mine. 
