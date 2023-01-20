# Student Simulator
Coding link: https://drive.google.com/file/d/1kmhMQscMOC5lFkhbrVfwrDuc9QkjJkW4/view
## Function
My code is aimed to simulate (in text) the dramatized life of a student.
The user is offered a variety of choices leading to different impacts on their health statistics, different text, or often more choices. With each choice, the user receives an upgrade in their characters statistics mentioned at the beginning. The storyline covers 4 classes (2 breaks) and ends at the end of the day (except for one option ending in kidnapping/death). At the end of the day, the system grades the characters statistics/attributes and presents the user with their character's situation, for example: if there are over 3 happiness scores, there is a print statement saying that the student (user) is happy at the end of the day. In a Choose Your Own Adventure format, it asks the user to make decisions that impact their scores of smarts, friends, overall happiness, etc. Each choice either leads to separate choices or falls into the main storyline.
## Purpose/Who is this for
My project is aimed towards many trying to play a simple text based game. I tried to include challenging choices within the game - even some to test the skills of the user, like the sets of math questions I incorporated. Over the course of this class, my coding knowledge (across the different languages) has continued to build, but this final project put what I know to the test. I was able to use the knowledge I have of python, and search for specific functions that could benefit my project to create a final interactive product.
## Learned New Something New
A new coding function I learned was the time.sleep() function, which I successfully used across my code. While writing my coding script, I wanted to make the users’ experience as comprehensible as possible, so I searched up ways to change the timing of code or to erase lines of code after they have been written. Although I spent a lot of time trying different functions, I was only able to accomplish changing the time of my code, using time.sleep().
I also learned how to set up class structures and their variables, so I can easily call them in later code. Mr. Bowman helped me do this, and it helped make the code less repetitive and easier for me to edit.
![Screenshot 2023-01-21 012005](https://user-images.githubusercontent.com/112853185/213815494-49c24542-7b4b-4c57-af9b-62e7e175928e.jpg)
## Data Abstraction
Within my multiple choice questions (at the beginning of my code) I used array functions. This helped the code when there were multiple correct answers because it allowed multiple entries of data to be stored in one list. If the users' answer is within the array, their answer is correct. This allowed my code to be less repetitive because I didn't need to repeat a variable on multiple lines of code, mainly in cases when there was more than one correct answer or variations of the same answer.
![Screenshot 2023-01-21 013034](https://user-images.githubusercontent.com/112853185/213816860-7a313202-e831-4360-9fb9-fe41509b2f93.jpg)
## Procedural Abstraction
### Procedure
This is an example of my code taking an argument - when the user inputs their name, it is stored in the variable 'name' where it can be later called upon by another function, like the functions in the Player Class (the stats).
![Screenshot 2023-01-21 013657](https://user-images.githubusercontent.com/112853185/213817610-70615d63-5827-439d-96ce-3229b3920a23.jpg)
### Algorithm
Algorithm examples can be found in various points of sequencing, selection and iteration:
#### Sequencing
Code runs from top to bottom, so when mentioning variables within the players' class (friends, happiness, tardies, etc) I have to place the Players Class at the top of the code, above the main function, where it will later be called. This allows the code to call upon a variable in the players class because the Class was already introduced before being called on. This helps manage the complexity of my code because all the code is located in specific sequences, allowing it to run. Functions that are called in the main function are placed above the main function, so they can be called later on.
![Screenshot 2023-01-21 014631](https://user-images.githubusercontent.com/112853185/213818628-fb36414d-4b60-4e8d-a8ad-4c5a1c63a9bf.jpg)
#### Selection
![Screenshot 2023-01-21 013458](https://user-images.githubusercontent.com/112853185/213818526-f88a7a80-fd84-4070-9fc8-affd9c4570c7.jpg)
Selection can be found when I use IF statements in my code to allow a variety of options. These Conditional Statements fit into my code because they are only called upon when certain conditions are met - specifically when the user chooses a certain option - the code is being selected.
#### Iteration
My 'While' loop is an example of iteration because it will continue running the same code (the main function code) as long as the condition is met, which will always happen because the condition is simply that the code is True (always the case). The only way the code would stop iterating is if the user would chose to exit the code using sys.exit().

![Screenshot 2023-01-21 014946](https://user-images.githubusercontent.com/112853185/213819094-c1f9b0b7-0100-4426-84b9-3e5135309602.jpg)
