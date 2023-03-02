<a href="https://kb-watchit.herokuapp.com/"><h1>Watch It </h1></a>

## Contents

## Table of Contents
1. [Introduction](#introduction)
    1. [Demo](#demo)

2. [UX](#ux)
   1. [Colours](#colours)
   2. [Imagery](#imagery)

3. [Wireframes](#wireframes)

4. [Strategy](#strategy)
   1. [Aims](#aims)
   2. [Target Audience](#target-audience)
   3. [User Stories](#user-stories)

5. [Agile Methodology](#agile-methodology)

6. [Scope](#scope)

7. [Structure of Pages](#structure-of-pages)

8. [Features](#features)
   1. [Implemented Features](#implemented-features)

9. [Admin Panel and Superuser](#admin-panel-and-superuser)

10. [Technologies](#technologies)

11. [Frameworks and Tools and Programs Used](#frameworks-and-tools-and-programs-used)

12. [Creating the Django app](#creating-the-django-app)

   1. [Features Left To Implement](#features-left-to-implement)

8. [Deployment](#deployment)
   1. [Project Deployment](#project-deployment)

14. [Forking This Project](#forking-this-project)

15. [Cloning This Project](#cloning-this-project)

8. [Credits](#deployment)
   1. [Content](#content)
   2. [Code and Other Resources](#code-and-other-resources)
   3. [Acknowledgements](#acknowledgements)
## Introduction

Portfolio Project 4: Full Stack Frameworks - Code Institue - Deadline 28th January 2022

This is my sumission for CodeInstitue's Project Portfolio Four.<br/>It uses various technologies such as Python, HTML, CSS, Javascript aswell as Django and ElephantSQL which was recently changed as Heroku had changed their terms.<br/> I created this site as I was interested in movies as well as finding new ones to watch as sometimes browsing through the main providers take too long and have no ability to see if people have liked the movie or not.
<br>

[Back to Table of Contents](#contents)

### Demo
A live of the website can be found <a href="https://kb-watchit.herokuapp.com/"><strong>HERE</strong></a><br>
<br>

[Back to Table of Contents](#contents)

## UX

As many now rely on the internet to browse and access services, UX has become increasingly important than before.
<br>

[Back to Table of Contents](#contents)

### Design

### Colours
As many now rely on the internet to browse and access services, UX has become increasingly important than before.

<img src="readmeassets/extras/colorPalette.png">

The color scheme is kept simple by only having 3 colors. White (#FFFFFF), Black, (#000000) and Baby Blue (#34A5EB).<br>
I've opted for a combination of black text set on the white background, with the cta buttons being highlighted and underlined black.<br>
Along with this the baby blue is used to highlight the navbar, 3 main info points as well as the footer.
<br>

[Back to Table of Contents](#contents)

### Imagery

All imagery uploaded is related to movies, from the first image being a camera to the actual movie posters which have been uploaded by users.
<br>

[Back to Table of Contents](#contents)

## Wireframes

<details>
<summary>Home</summary>
<img src="readmeassets/wireframe_home.png">
</details>
<details>
<summary>Movie Details</summary>
<img src="readmeassets/wireframe_movie_details.png">
</details>
<details>
<summary>Edit Movie Recommendation</summary>
<img src="readmeassets/wireframe_movie_edit.png">
</details>
<details>
<summary>Register</summary>
<img src="readmeassets/wireframe_registration.png">
</details>
<br>

[Back to Table of Contents](#contents)


## Strategy

### Aims

<ol>
  <li>To allow the opportunity for users to create a post of a movie the completely recommend to others</li>
  <li>To allow un-logged in users to browse through posts and find a movie they may potentially watch</li>
  <li>To allow users logged in to like posts and visualise the amount of likes on a particular movie</li>
  <li>To allow users both logged in and out to create a comment on a post to mention why they particually liked the movie</li>
  <li>To allow users to create a profile to enable them to post a movie</li>
  <li>To allow users to create a profile page with social links and bio to make it more personable</li>
</ol>
<br>

[Back to Table of Contents](#contents)

### Target Audience

<ol>
  <li>Users who are interested in watching movies</li>
  <li>Users who like to read and would like to review a synopsis of a movie prior to watching</li>
</ol>
<br>

[Back to Table of Contents](#contents)

### User Stories
<ol>
    <li>As a user I can view the movies recently added whilst not needing to log in</li>
    <li>As a user I can view each movie more in depth by clicking on it as I may want to read the synopsis prior to committing to watch the movie</li>
    <li>As a user I can create a profile to be able to post movies I personally like for others to enjoy</li>
    <li>As a user I can create a profile page and include my social media links</li>
    <li>As a user I can comment on a post in order to tell other users if I like a movie or not</li>
    <li>As a user I can like a movie in order to let other users know that a particular movie was liked</li>
    <li>As a user I can delete my own posts in case I change my mind about a specific movie</li>
    <li>As a user I can edit my own posts in case I change my mind about a specific movie or perhaps have left out detail or want to upload a new movie poster</li>
    <li>As a user I can create an account</li>
    <li>As a user I can edit the settings on my account in case I need a password reset</li>
 </ol>
 <br>

[Back to Table of Contents](#contents)

 ## Agile Methodology
 All functionality and development of this project were managed using GitHub which Projects can be found
[here](https://github.com/KeithBautista/watch-it/issues)
<br>

[Back to Table of Contents](#contents)

 ## Scope
 It is sometimes more beneficial to develop a website based on the MMP (Minimum Marketable Product). Although unfortuantely as this project requires more advanced concepts aswell as possible time constrains, it may be the case that a MVP (Minimum Viable Product) be created instead. This will allow the basic functions of the website to be implemented whereby time can be more spent on the basics rather than features that our users may potentially never look at.

 Whilst using the MVP
 <ul>
    <li>We will create a clear and consise website that will have all the necessary features needed for such a site.</li>
    <li>We will create a site with minimum levels of UX whilst still being intuitive enough for our users.</li>
    <li>We will meet the requirements of our beloved users</li>
 </ul>
 <br>

[Back to Table of Contents](#contents)

 Whilst following the MVP model, to meet the user and business goals, our website will include:
 <ul>
    <li>A nav-bar that underlines the specific text currently on in order to enable users to identify where they are to be</li>
    <li>Links to the associated social media pages of the organization</li>
    <li>A registration form in order for users to sign up to the site.</li>
    <li>An add movie form in order for the users to provide their movie recommendations</li>
    <li>An edit movie form in case the user would like to edit anything in particular on the movie posted</li>
 </ul>
 <br>

[Back to Table of Contents](#contents)

## Structure of Pages
 
The page created is structured in a way which is easy recognizable to other web pages in the way it has a navigation bar on the top of the page and a footer at the bottom of the home.html. The navaigation bar is duplicated in each page so that it is easy to navigate to other pages from the main home page. On this, the site it divided up into multiple pages which each own having a function.

<ul>
    <li>Home: This is the main page where you will find the most recent posts that have been made/posted by other users. Here you will also find the nav bar and footer as well as the frequently asked questions.</li>
    <li>Registration: This is where users will find themselves creating an account to be able to post movie recommendations</li>
    <li>Add Movie: This, once user is logged in allows them to create movie recommendations with the ability to edit the synopsis as well as the image that will be see in the home page.</li>
    <li>Edit Movie: This, once user is logged in and is the correct user that has created the movie post, will be able to delete, edit the content as well as change the image shown in the home.html file</li>
    To add to this there are various files such as login, changepassword, edit-profile-page and more which enables the user to make their account their own and personalize.
</ul>
<br>

[Back to Table of Contents](#contents)

## Features
### Implemented Features

<details>
<summary>Registration Page: Allows users to create a user</summary>
<img src="readmeassets/registrationPage.png">
</details>
<details>
<summary>nav-bar: Enables users to navigate around the site easier and in an intuitive way</summary>
<img src="readmeassets/navbar.png">
</details>
<details>
<summary>Edit Movie Page: Allows logged in users to edit the post that they have made</summary>
<img src="readmeassets/editMovieRecommendation.png">
</details>
<details>
<summary>FAQ: Allows users a quick look into the frequently asked questions and their answers</summary>
<img src="readmeassets/faq.png">
</details>
<details>
<summary>Edit Profile Page: Allows users to create their own profile page which makes the experience more personable</summary>
<img src="readmeassets/editProfilePage.png">
</details>
<details>
<summary>Movie Detail Page: Allows users to view the movie as well as the synopsis written by the user who has posted said movie</summary>
<img src="readmeassets/movieDetailPage.png">
</details>
<details>
<summary>Comment, Like and Profile Page: Allows users to like, comment and view the profile page of the user that created the movie post</summary>
<img src="readmeassets/commentLikeAndProfilePage.png">
</details>
<br>

[Back to Table of Contents](#contents)

## Admin Panel and Superuser
On the Admin Panel, as an admin/superuser I have full access to CRUD functionality so I can view, create, edit and
delete the following ones:

<ol>
    <li>Users</li>
    <li>Categorys</li>
    <li>Comments</li>
    <li>Posts</li>
    <li>Profiles</li>
</ol>
<br>

[Back to Table of Contents](#contents)

## Technologies

- [HTML 5](https://en.wikipedia.org/wiki/HTML/)

- [CSS 3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://www.javascript.com/)

- [Django](https://www.python.org/)

- [Python](https://www.djangoproject.com/)
<br>

[Back to Table of Contents](#contents)


## Frameworks and Tools and Programs Used
- [Bootstrap](https://getbootstrap.com/)<br>
   Was used to style the website, add responsiveness and interactivity

- [Jquery](https://jquery.com/)<br>
   All the scripts were written using jquery library

- [Git](https://git-scm.com/)<br>
   Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub

- [GitHub](https://github.com/)<br>
   GitHub is used to store the project's code after being pushed from Git

- [Heroku](https://id.heroku.com)<br>
   Heroku was used to deploy the live project

- [PostgreSQL](https://www.elephantsql.com/)<br>
   Database used through heroku.

- [VSCode](https://code.visualstudio.com/)<br>
   VSCode was used to create and edit the website

- [Lucidchart](https://lucid.app/)<br>
   Lucidchart was used to create the database diagram

- [PEP8](http://pep8online.com/)<br>
   PEP8 was used to validate all the Python code

- [W3C - HTML](https://validator.w3.org/)<br>
   W3C- HTML was used to validate all the HTML code

- [W3C - CSS](https://jigsaw.w3.org/css-validator/)<br>
   W3C - CSS was used to validate the CSS code

- [Fontawesome](https://fontawesome.com/)<br>
   To add icons to the website

- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)<br>
   To check App responsiveness and debugging

- [Cloud Convert](https://cloudconvert.com/jpg-to-webp)<br>
   To change formatting of images to WEBP

- [Balsamiq](https://balsamiq.com/)<br>
   To build the wireframes for the project

- [Adobe Color Wheel](https://color.adobe.com/create/color-wheel)<br>
   To build the colour palette of the project
<br>

[Back to Table of Contents](#contents)

## Creating the Django app

<ol>
  <li>Go to the Code Institute Gitpod Full Template <a href="https://github.com/Code-Institute-Org/gitpod-full-template">Template</a>.</li>
  <li>Click on "Use This Template".</li>
  <li>Once the template is available in your repository, click on "Gitpod".</li>
  <li>When the image for the template and the Gitpod are ready, open a new terminal to start a new Django App.</li>
  <li>Install Django and gunicorn: <code>pip3 install django gunicorn</code>.</li>
  <li>Install supporting database libraries dj_database_url and psycopg2 library: <code>pip3 install dj_database_url psycopg2</code>.</li>
  <li>Create file for requirements: in the terminal window, type <code>pip freeze --local &gt; requirements.txt</code>.</li>
  <li>Create project: in the terminal window, type <code>django-admin startproject your_project_name</code>.</li>
  <li>Create app: in the terminal window, type <code>python3 manage.py startapp your_app_name</code>.</li>
  <li>Add app to the list of installed apps in settings.py file: <code>you_app_name</code>.</li>
  <li>Migrate changes: in the terminal window, type <code>python3 manage.py migrate</code>.</li>
  <li>Run the server to test if the app is installed, in the terminal window, type <code>python3 manage.py runserver</code>.</li>
  <li>If the app has been installed correctly, the window will display "The install worked successfully! Congratulations!".</li>
</ol>
<br>

[Back to Table of Contents](#contents)

### Features left to implement

<ul>

   <li>Categories for the Movies as they are currently bunched up in the home.html file</li>
   <li>Allow users to add favorites rather than browsing through the movies posts</li>
  
</ul>
<br>

[Back to Table of Contents](#contents)

## Deployment
A live demo of the website can be found <a href="https://kb-watchit.herokuapp.com/" target="_blank">**HERE**</a><br>

<ol>
    <li>A new repository was created using 'Code-Instutute-Org/gitpod-full-template'</li>
    <li>A meaningful name was given to the new repository and 'Create Repository' was selected</li>
    <li>The repository was then opened on GitHub by clicking the 'Gitpod' button to build the GitPod workspace which would allow me to build and edit the code used to make the <em>Project Name</em> website/application</li>
    <li>Version control was used throughout the project using the following commands in the terminal.
        <ul>
            <li>git add . <strong>OR</strong> git add "file name" - to stage the changes and get them ready for being committed to the local repo.</li> 
            <li>git commit -m "small description of update" - to save the change and commit the change to the local repo</li>
            <li>git push - to push all committed changes to the GitHub repo associated with the GitPod workspace</li>
        </ul>
    </li>
</ol>
<br>

[Back to Table of Contents](#contents)

### Project Deployment
This project was deployed via Heroku by carrying out the following:
<ol>
    <li>Create the gitpod repo from the template via the gitpod button in github.</li>
    <li>Log in to Heroku and create a new app. Or you can create new app within the terminal</li>
    <li>Create ElephantSQL Account and use url details to link app and database together</li>
    <li>Complete the config vars section</li>
    <li>Link Heroku and GitHub accounts together</li>
    <li>Select the repo (via Heroku) that you want to make an app of and give it a name in Heroku.</li>
    <li>Click on deploy.</li>
</ol>
<br>

[Back to Table of Contents](#contents)
## Forking This Project
Fork this project by following the steps:
<ol>
    <li>Open <a href="https://github.com/KeithBautista/watch-it" target="_blank">GitHub</a></li>
    <li>Find the 'Fork' button at the top right of the page</li>
    <li>Once you click the button the fork will be in your repository</li>
</ol>
<br>

[Back to Table of Contents](#contents)

## Cloning This Project
Clone this project by following the steps:
<ol>
    <li>Open <a href="https://github.com/KeithBautista/watch-it" target="_blank">GitHub</a></li>
    <li>You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order to copy the URL.</li>
    <li>Once you click the button, the fork will be in your repository.</li>
    <li>Open a new terminal.</li>
    <li>Change the current working directory to the location that you want the cloned directory.</li>
    <li>Type "git clone" and paste the URL copied in step 1.</li>
    <li>Press "Enter" and the project will be cloned.</li>
</ol>
<br>

[Back to Table of Contents](#contents)

## Credits

### Content
All Images and Appropriate descriptions were taken from <a href="https://www.wikipedia.org/" target="_blank">Wikipedia</a>
<br>

[Back to Table of Contents](#contents)

### Code and Other Resources
All code used in this project was taken from the Code Institute lessons, as well as Django's documentation.
[W3Schools - Python](https://www.w3schools.com/python/)
[Stack Overflow](https://stackoverflow.com/)
<br>

[Back to Table of Contents](#contents)

### Acknowledgements
This website, Watch It was designed and developed in conjunction with the Full Stack Developer Diploma course with specialty in ecommerce at Code Institute. I would like to thank Code Institute as well as the content creators in youtube for Django specifically for getting me through this! More Specifically John Elder with his Django course on Blog Posts.

<br>

[Back to Table of Contents](#contents)