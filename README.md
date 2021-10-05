# Quiz Navigus

> Developed by :Alabhya Singh, [Abhyudaya Bora](https://github.com/codeluna99)

---

## Funtionalities Added As Per The Assignment(Level-0)

- [x] Each Course can have one quiz
- [x] Teacher can add, delete and edit questions.
- [x] Each question can have multiple correct answers, **but** can select any one correct answer.
- [x] Teacher can allot maximum of 10 marks to one question.
- [x] Teacher can also specify the passing marks, and the passing marks will appear on the view marks page.
- [x] Teacher can add course.
- [ ] Teacher can edit and delete course.
- [ ] Student will be given a choice to leave the quiz, when the passing marks have already been achieved.
- [x] Deploy the project on Heroku([Link To The Deployed Project](https://project-navigus-quizzer.herokuapp.com/ "deployed project"))

##### Deployed Project: https://project-navigus-quizzer.herokuapp.com/

## Functions

### Admin

- Default Admin Account - user and Password is - user.
- After Login, can see Total Number Of Student, Teacher, Course, Questions are there in system on Dashboard.
- Can View, Update, Delete, Approve Teacher.
- Can View, Update, Delete Student.
- Can Also See Student Marks.
- Can Add, View, Delete Course.
- Can Add Questions To Respective Courses With Options, Correct Answer, And Marks.
- Can View And Delete Questions Too.

### Teacher

- Can Sign-up for the platform. Then Login (Approval required by system admin, Then only teacher can login).
- Default account - Teacher and Password -Teacher
- After Login, can see Total Number Of Student, Course, Questions are there in system on Dashboard.
- Can Add, View, Delete Course.
- Can Add Questions To Respective Courses With Options, Correct Answers, Marks and Passing Marks.
- Can View And Delete Questions Too.
  > Basically Admin Will Hire Teachers To Manage Courses and Questions.

### Student

- Create account. Default Account - Student and Password - Student.
- After Login, Can See How Many Courses/Exam And Questions Are There In System On Dashboard.
- Can Give Exam Any Time, There Is No Limit On Number Of Attempt.
- Can View Marks Of Each Attempt Of Each Exam.
- Question Pattern Is MCQ With 4 Options And 1 Correct Answer.

---

## HOW TO RUN THIS PROJECT

- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Download This Project Zip Folder and Extract it
- Open Terminal and Execute Following Commands :

```
python -m pip install -r requirements. txt
```

- Move to project folder in Terminal. Then run following Commands :

```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

- Now enter following URL in Your Browser Installed On Your Pc

```
http://127.0.0.1:8000/
```
