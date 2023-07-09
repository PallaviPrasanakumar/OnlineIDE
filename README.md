# OnlineIDE

This is simple online IDE backend using Django.<br>
1)Created a Submission service which does the following:<br>
     &ensp* Initially it should add a status as Pending as soon as user submits the code<br>
     &ensp* It should create a file with the code with proper extension "py"<br>
     &ensp* It should compile and run the code and change the status to "Pending" or "Error" accordingly<br>
     &ensp* It should save the code in the database for retrieval <br>
    
2)Implemented Authentication Layer using Token Authentication<br>
    &ensp* User must be able to register and login via Token Authentication and can see the history of codes submitted by the user
3)Implemented Long Polling method using Multiprocessing<br>
