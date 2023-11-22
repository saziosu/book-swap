# BookSwap
BookSwap is a project to connect readers through swapping books.

![Am I responsive image](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700683184/amiresponsive_vzoufb.png)

Link for the finished deployed site: https://book-swap-13f900a2d9c7.herokuapp.com/

# Table of Contents

- [BookSwap](#bookswap)
- [Table of Contents](#table-of-contents)
- [Agile Planning](#agile-planning)
  - [Site Goals](#site-goals)
  - [Epics](#epics)
  - [User Stories](#user-stories)
  - [Labels](#labels)
  - [Wireframes](#wireframes)
- [Design](#design)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
- [Features](#features)
  - [Current Features](#current-features)
    - [Feature One](#feature-one)
    - [Feature Two](#feature-two)
    - [FEATURE THREE](#feature-three)
    - [FEATURE FOUR](#feature-four)
  - [Future Features](#future-features)
  - [Accessibility](#accessibility)
- [Technology Used](#technology-used)
  - [Languages](#languages)
  - [Frameworks, Libraries \& Programs](#frameworks-libraries--programs)
- [Deployment \& Development](#deployment--development)
  - [Forking the Repository](#forking-the-repository)
  - [Deploy to Heroku](#deploy-to-heroku)
- [Testing](#testing)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Content](#content)
- [Acknowledgements](#acknowledgements)

# Agile Planning

## Site Goals
The site's goals are to help connect readers and allow them to posts books they are willing to swap.
Readers are able to see available books, and see the book's information such as genre and the book's condition to help them decide if they want to contact the book's owner and organise a swap.

## Epics
There are three Epics within this project:

**EPIC: Account Management**
This epic focuses on the account management portion of the project.
It involves creating accounts, signing in and logging out.

**EPIC: Remote Book Swap**
This epic focuses on the features that allow the users to use the book swap functionality so that they can trade their books.
The user must be logged in/authenticated to generate the post.
The user should be logged in/authenticated to view the other user's contact details.
If they are not logged in when they view the post, the contact details should be replaced with a request to log in to view them.

**EPIC: Design & Experience**
This epic focuses on the overall styling of the website.
The overall design and colour scheme of the website should be attractive and fitting with the theme of the project.
Toast messages should give feedback to the user.
Custom error pages should redirect the user back to the appropriate area of the site.

## User Stories
Majority of User stories are linked to Epics. Labels are applied for prioritisation, such as `must have`, `should have` and `could have`.

* As a Developer, I can deploy the website early so that I can avoid any technical issues or stress later in the project

| **Epic**            | **User Story**                                                                                      | **Priority Label** |
|---------------------|-----------------------------------------------------------------------------------------------------|--------------------|
| Account Management  | As a User, I can create an account so that I can access features for authenticated users            | must have          |
| Account Management  | As a User, I can reset my password so that I can access my account if I forget my password          | could have         |
| Account Management  | As a User, I can update my contact details so that I can allow users to contact me for a swap       | could have         |
| Remote Book Swap    | As a User, I can create a book post so that I can other users can decide if they would like to swap | must have          |
| Remote Book Swap    | As a User, I can edit my book post so that I can update my information                              | must have          |
| Remote Book Swap    | As a User, I can view other book posts so that I can decide which book I would like to swap with    | must have          |
| Remote Book Swap    | As a User, I can edelete my book post so that I can manage my posts                                 | must have          |
| Design & Experience | As a User, I can feedback messages so that I can see feedback from the actions I have completed     | could have         |
| Design & Experience | As a User, I can view a clean and attractive website so that I can have a positive experience       | should have        |


## Labels
The labels are priorised as follows:

| **must have** | **This feature/issue is required for the project to function**                       |
|---------------|--------------------------------------------------------------------------------------|
| should have   | Important to implement but will not crash the project without but still key features |
| could have    | would like to have, but not essential to the project                                 |
| bug           | Something isn't working                                                              |

These result in the following stats:

![label stats image](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700580861/Screenshot_2023-11-21_at_15.33.51_kfcvlu.png)

## Wireframes

The following wireframes were used to plan the look of the site:
![wireframes image](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700581232/Screenshot_2023-11-21_at_15.40.18_b3dhdj.png)

# Design

## Color Scheme

For the colorscheme, [this palette from Canva](https://www.canva.com/colors/color-palettes/pastel-dreams/) was used for inspiriation:
![canva image](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700581475/Screenshot_2023-11-21_at_15.44.28_slnhyv.png)

These were adjusted to ensure there was enough contrast on the site.
The final colors used (made with [coolers](https://coolors.co/)):

![Coolers image](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700683581/coolers_n4umdo.png)

## Typography

Fonts were chosen from GoogleFonts

* [Syne](https://fonts.google.com/specimen/Syne) was used for header fonts
* [Inter](https://fonts.google.com/specimen/Inter) was used for all other fonts
* San-serif was used as the fallback font

## Imagery

The hero image was sourced from [Pexels](https://www.pexels.com/photo/books-on-shelves-2177482/)
The placeholder image was also sourced from [Pexels](https://www.pexels.com/photo/small-flowers-on-a-book-3696663/)

# Features 

## Current Features

### Feature One

FEATURE ONE
IMAGE

### Feature Two

FEATURE TWO
IMAGE

### FEATURE THREE

IMAGE
FEATURE

### FEATURE FOUR

IMAGE
FEATURE

## Future Features

* A few
* Future
* Features

## Accessibility

* Accessibility
* Considerations
* Here

# Technology Used

## Languages

* HTML
* CSS
* BootStrap
* Python
* Django
* JavaScript

## Frameworks, Libraries & Programs 

* AutoSlug
* Cloudinary & dj3-cloudinary-storage
* CrispyForms & crispy-bootstrap4
* django-allauth
* django-phonenumber-field & phonenumbers
* gunicorn
* psycopg2
* requests-oauthlib
* sqlparse
* urllib3
* whitenoise

# Deployment & Development

## Forking the Repository

1. Log in or Sign up to [GitHub](https://github.com/)
2. Navigate to https://github.com/saziosu/book-swap.
3. Click the 'fork' button in the top right corner.
4. Feel free to customize your repo name, this is not required.
5. Click the Create Fork button.

## Deploy to Heroku
Heroku was used to deploy this site:

1. Run pip3 freeze > requirements.txt in the console to set up the requirements.txt file. This command will create the file if it does not already exist.
2. Commit any changes and push to GitHub.
3. Navigate to Heroku's website and log in to the dashboard.
4. Click on "Create new app" in the top right.
5. Enter the "App name" and select your region, then click "Create App". 
6. Head to the Settings tab in the new app.
7. Go to "Config Vars" under the Settings tab.
8. Click on "Reveals Config Vars".
9. Add the "CLOUDINARY_URL", "DATABASE_URL", and "SECRET_KEY" values generated for the project
10. Add "PORT" key and "8000" value to the config vars.
11. Move to the "deploy" tab on the app, and scroll down to the deployment method section.
12. Select "GitHub" and connect to GitHub.
13. Search for the appropriate GitHub repo and Connect.
14. Select "Automatic deploys" or "Manual deploys" to deploy the application.


# Testing

[TESTING.md](TESTING.md)

# Credits

## Code

* Code
* Credits
* Here

## Media

* Media
* Credits
* Here

## Content

* Content details

# Acknowledgements

* Thanks y'all!