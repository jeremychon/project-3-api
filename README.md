# Project 3 - Pain Point
by Sebastian Portuondo and Jeremy Chon

---

Pain Point is a full stack application that allows people to post pain points in an industry that need a solution or find existing pain points in an industry that may have a solution. In addition, people can post their own solutions to other people's pain points.

---

## User Stories

**User Login/Registration**
- As a user, I want to be able to enter my name and password in the login or registration page so that I can either log in to my account or register for an account.
- As a user, I should see that if I input an incorrect username or password in the login page, there will be a message telling me that the username and/or password was incorrect, so that I know that I typed in something wrong.
- As a user, I should see that if I input a username that already exists in the registration page, there will be a message telling me that the username is already taken, so that I know that I have to type in a different username.
- As a user, I want to be able to see the home page after logging in or registering, so that I can explore and use the app.

**User Profile**
- As a user, I can see a page that shows my name and all the pain points and solutions that I have come up with, so that I know that this is my profile page and that those are my pain points and solutions.

**Landing/Home Page**
- As a user, I want to be able to see all of the industry categories and be able to select one or more, so that I know what’s available and can filter the pain points based on my choices.

**Pain Points**
- As a user, I can browse a gallery of pain points listed on the pain points home page each pertaining to an industry or industries that fit the specifications I chose, so that I can find any pain points that I’m interested in with ease.
- As a user, I want to see the most highly voted pain points, so that I can see what is most relevant and necessary in the specific industry.
- As a user, I want to be able to upvote or downvote an pain point once.
- As a user, I want to be able to create my own pain point, so that people can create solutions to a pain point of mine.
- As a user, I want to be able to edit my own pain point, so that the problem is clearly defined, if not already done before.
- As a user, I want to be able to click on an pain point and see the title/head, the body/description of the pain point, the necessity rating, whether or not it has been solved, and, if there are any, the solutions to the pain point.
- As a user, I should get notified that someone has posted a solution to my pain point.

**Solutions**
- As a user, I can see a page with each solution name and owner who posted, but if I click on it, it expands and shows me the actual solution.
- As a user, I can upvote or downvote a solution once.
- As a user, I want to be able to create my own solutions to pain points.
- As a user, I want to be able to edit my solutions, so that the solution is as accurate as possible.


## Routes/Endpoints

#### USER
| 		     | HTTP VERB | URL            | DESCRIPTION	  	  		             |
| ---------- | :---------| :--------------| :------------------------------------|
| /user	     | POST		 | /register      | create user				             |
|		     | POST		 | /:login        | get login info and log user in       |
|		     | POST		 | /:logout       | destroy session and log user out     |
|		     | GET		 | /:id           | get info about user with :id         |
|		     | PUT		 | /:id        	  | updates user with :id		         |
| 		     | DELETE	 | /:id           | deletes user with :id		         |


#### CATEGORIES
| 		      | HTTP VERB | URL            | DESCRIPTION	  	   	   	          |
| ----------- | :---------| :--------------| :------------------------------------|
| /categories | GET	   	  | /			   |  get all industry categories 		  |
|		      | POST	  | /			   |  create new categories				  |


#### PAIN POINTS
| 		      | HTTP VERB | URL              | DESCRIPTION	  	  				 	          |
| ----------  | :---------| :----------------| :----------------------------------------------|
| /painpoints | GET		  | /                | get all of the newest pain points posted       |
| 		      | POST	  | /                | create pain point       				          |
| 		      | GET 	  | /< category_id > | get all pain points with specific categories   |
|		      | GET		  | /:id             | get info (solutions) about pain point with :id |
|		      | PUT		  | /:id             | updates pain point with :id			          |
|		      | POST	  | /:id/vote        | adds rating to pain point with :id		      |


#### SOLUTIONS
| 		     | HTTP VERB | URL            | DESCRIPTION	  	  				 	 |
| ---------- | :---------| :--------------| :------------------------------------|
| /solution  | POST		 | /  	     	  | create solution						 |
|		     | PUT		 | /:id      	  | updates solution with :id			 |
|		     | POST		 | /:id/vote   	  | adds rating to solution with :id	 |


<!-- ## How to run the app
1. After cloning this repo, run
> pip3 install -->
