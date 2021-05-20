# TEAM-5

**Github Repository URL:** https://github.com/Brian1226/TEAM-5

**Team Members:** Brian Nguyen (Brian1226), Christy Nguyen (cnguyenth), Karan Sharma (Kar-Sha), Jin You Goh (jackedjin)

**Product Name:** Priority Queue


## Introduction
The to-do app Priority Queue allows users to collaborate on organizing and prioritzing tasks. The app organize their tasks from greater importance to least importance in a systemic checklist (aka note). After completing a task, the task would be removed and then the next task in queue would take its place. This continues until all tasks are completed. Then, the next checklist (note) in queue will take its place. This continues until all notes are completed.


## How to Use 
1. The home page is the login page. If a registration is needed, click on "Register", which will redirect to the register page.
2. After filling out the register form with a valid email, username, and password, it will redirect back to the login page.
3. Sign in with the correct username and password.
4. A successful login will redirect to the home page where the user can view their notes.
5. To create a note, enter the title of the Note and click "Add Note". The note will then be seen on the home page.
6. The user is able to customize the note by changing the color by clicking "Change Note Color" after entering the note ID and selecting their desire color.
7. To add tasks to the note, click on the title and/or id of the note, which will redirect to the task creation page.
8. On the task creation page, there is an option to enter a task and by clicking "Add Task", the task is added to the note.
9. After adding a task, the task will show up on the left-side and the user will be given the option to copy the task. 
10. To delete tasks, simply click on "Delete Task", this will clear all tasks then redirect the user back to the home page.
11. The user can also copy the note, delete the note, and invite other users to access the note. 
12. The user can clear their own home page by clicking "Clear Notes", which deletes all of the user's notes.
13. Click on the "log out" button to log out.


## Implemented Use Cases
1. **Sign In:** After filling out the login form with the valid username and password, clicking the "Sign in" button will redirect to the task page.
2. **Sign Up:** After filling out the register page with the valid email, username, and password, click the "Sign up" button will redirect to the login page.
3. **Log out:** Clicking the "log out" button will sign out and redirect back to the login page.
4. **View Note:** Displays all the created notes, otherwise prints the message "There's no notes to delete!"
5. **Add Note:** After filling out the "Note title", click "Add Note" to create the note.
6. **Invite:** After creating the note, clicking on "Invite" will share the note to the collaborator (enter their email).
7. **Delete Note:** Clicking on "Delete Note" will delete the selected note.
8. **Copy Note:** Clicking on "Copy Note" will create a duplicate of the selected note.
9. **Change Note Color:** Enter the id of the note you want to change color, select the desired color, then click on "Change Note Color."
10. **Clear Notes:** Clicking on "Clear Notes" will delete all notes.
11. **View Task:** After clicking on the title of the selected note, it displays all the created tasks for that note.
12. **Add Task:** After typing a task, click on "Add Task" to add the task to the respective note.
13. **Delete Task:** Clicking on "Delete Task" will delete the selected task from the note.
14. **Copy Task:** Clicking on "Copy Task" will create a duplicate of the selected task.
15. **Clear All Tasks:** Clicking on "Clear All Tasks" will delete all tasks within the respective note.
16. **Back to Notes:** Clicking on "Back to Notes" will redirect from task page to the notes page (Home).


## Image
**Login page:**
![Login](https://i.postimg.cc/X7ShtBnx/Screen-Shot-2021-05-07-at-4-33-53-PM.png)

**Register page:**
![Register](https://i.postimg.cc/MptFcsVr/Screen-Shot-2021-05-07-at-4-34-02-PM.png)

**View Notes page:**
![View Notes](https://i.postimg.cc/PqYC2j6z/Screen-Shot-2021-05-19-at-11-09-27-PM.png)

**View Tasks page**
![View Tasks](https://i.postimg.cc/6qMJz32P/Screen-Shot-2021-05-19-at-11-28-49-PM.png)


## Technologies Used
* HTML
* Python
* Flask
* SQLAlchemy


## Acknowledgements / References
* Professor Rojas's lectures and slides
* https://www.w3schools.com/html/default.asp
