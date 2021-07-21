# Running Instructions
Once cloned the directory, open command line and go to the path of the directory where the cloned repository is, follow the following instructions:

> First install all the requirements.
* pip install -r requirements.txt or pip install -r requirements.txt --user   
If the first one displays a permission error. 
> Open and run the files, the Api.py file is the one that responds to the test.py file. To pass in a number to validate, open the test.py file and input the number into this URL : response = requests.get(TARGET_URL + "Validate/ Input-Number-Here") 

# Decisions made

>I decided to make only one resource and a single endpoint not two seperated resources and endpoints for BBC-V1 and BBC-V2 because to reduce code duplication and to reduce wastage of resources.

>String was used as an input, this was because using int removed the leading zero in the number which caused problems during the calculations of BBC-V1. The lenght of the full number was affected and the muliplication by its own position was also affected if integer was used.

> The check digit was seperated from the number, this was done to compare the calculations to the check digit if they matched it meant validated.

# Additional Comments

> I would recommend using visual studio code for this project. This is because the test.py file can be run in an interactive window, and the Api.py can be run in the terminal both side by side to get a better view.