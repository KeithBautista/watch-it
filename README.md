<a href="https://kb-watchit.herokuapp.com/"><h1>Watch It </h1></a>

## Contents
<ul>
    <li>
        <a href="#Introduction"><strong>Introduction</strong></a>
    </li>
    <li>
        <a href="#UX"><strong>UX</strong></a>               
    </li>
    <li>
        <a href="#Technologies"><strong>Technologies</strong></a>
    </li>
    <li>
        <a href="#Features"><strong>Features</strong></a>
    </li>
    <li>
        <a href="#Testing"><strong>Testing</strong></a>   
    </li>
    <li>
        <a href="#Deployment"><strong>Deployment</strong></a>
    </li>
    <li>
       <a href="#Credits"><strong>Credits</strong></a> 
    </li>
    <li>
        <a href="#Screenshots"><strong>Screenshots</strong></a>
    </li>
    <li>
        <a href="#overall-thoughts"><strong>Overall Thoughts</strong></a>
    </li>
</ul>
<hr>

## Introduction

Portfolio Project 4: Full Stack Frameworks - Code Institue - Deadline 28th January 2022

This is my sumission for CodeInstitue's Project Portfolio Four.<br/>It uses various technologies such as Python, HTML, CSS, Javascript aswell as Django and ElephantSQL which was recently changed as Heroku had changed their terms.<br/> I created this site as I was interested in movies as well as finding new ones to watch as sometimes browsing through the main providers take too long and have no ability to see if people have liked the movie or not.

### Demo
A live of the website can be found <a href="https://kb-watchit.herokuapp.com/"><strong>HERE</strong></a><br>

## UX

As many now rely on the internet to browse and access services, UX has become increasingly important than before.

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

### Target Audience(s)

<ol>
  <li>Users who are interested in watching movies</li>
  <li>Users who like to read and would like to review a synopsis of a movie prior to watching</li>
</ol>

### User Stories
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

 ### Scope
 It is sometimes more beneficial to develop a website based on the MMP (Minimum Marketable Product). Although unfortuantely as this project requires more advanced concepts aswell as possible time constrains, it may be the case that a MVP (Minimum Viable Product) be created instead. This will allow the basic functions of the website to be implemented whereby time can be more spent on the basics rather than features that our users may potentially never look at.

 Whilst using the MVP
 <ul>
 <li>We will create a clear and consise website that will have all the necessary features needed for such a site.</li>
 <li>We will create a site with minimum levels of UX whilst still being intuitive enough for our users.</li>
 <li>We will meet the requirements of our beloved users</li>
 </ul>

 Whilst following the MVP model, to meet the user and business goals, our website will include:
 <ul>
 <li>A nav-bar that underlines the specific text currently on in order to enable users to identify where they are to be</li>
 <li>Links to the associated social media pages of the organization</li>
 <li>A registration form in order for users to sign up to the site.</li>
 <li>An add movie form in order for the users to provide their movie recommendations</li>
 <li>An edit movie form in case the user would like to edit anything in particular on the movie posted</li>
 </ul>

### Structure of Pages
 
The page created is structured in a way which is easy recognizable to other web pages in the way it has a navigation bar on the top of the page and a footer at the bottom of the home.html. The navaigation bar is duplicated in each page so that it is easy to navigate to other pages from the main home page. On this, the site it divided up into multiple pages which each own having a function.

<ul>
 <li>Home: This is the main page where you will find the most recent posts that have been made/posted by other users. Here you will also find the nav bar and footer as well as the frequently asked questions.</li>
 <li>Registration: This is where users will find themselves creating an account to be able to post movie recommendations</li>
 <li>Add Movie: This, once user is logged in allows them to create movie recommendations with the ability to edit the synopsis as well as the image that will be see in the home page.</li>
 <li>Edit Movie: This, once user is logged in and is the correct user that has created the movie post, will be able to delete, edit the content as well as change the image shown in the home.html file</li>
 To add to this there are various files such as login, changepassword, edit-profile-page and more which enables the user to make their account their own and personalize.
</ul>