# BookSwap
BookSwap is a project to connect readers through swapping books.

![Am I responsive image](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700683184/amiresponsive_vzoufb.png)

Link for the finished deployed site: https://book-swap-13f900a2d9c7.herokuapp.com/

# Table of Contents

- [BookSwap](#bookswap)
- [Table of Contents](#table-of-contents)
- [Site Goals](#site-goals)
- [Agile Methodology](#agile-methodology)
  - [Labels](#labels)
  - [Epics](#epics)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
- [Design](#design)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
- [Features](#features)
  - [Current Features](#current-features)
    - [Navbar](#navbar)
    - [Hero Section](#hero-section)
    - [Info Section](#info-section)
    - [Sign Up](#sign-up)
    - [Login](#login)
    - [Logout](#logout)
    - [Current Books](#current-books)
    - [Read Book Posts](#read-book-posts)
    - [Add Book](#add-book)
    - [Edit Book](#edit-book)
    - [Delete Book](#delete-book)
    - [Reserved Book](#reserved-book)
    - [Messaging](#messaging)
    - [Footer](#footer)
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


# Site Goals
The site's goals are to help connect readers and allow them to posts books they are willing to swap with each other.
Readers are able to see available books, and see the book's information such as genre and the book's condition to help them decide if they want to contact the book's owner and organise a swap.
This connects readers and is also a sustainable way of reading.
> Each year consumers waste more than 16,000 truckloads of books which have not been read once. [source](https://wordsrated.com/impact-of-book-publishing-on-environment/)

BookSwap has the potential to help make a positive impact on our environment by preventing wastage of unwanted books.

# Agile Methodology
This project was developed using agile methodologies by utilising Epics and User stories.
User storied were assigned to Epics. 
The Epics & User Stories were prioritised by labels. `must have`, `should have`, `could have`.
A kanban board in GitHub was used to track these, with a `not started`, `in progress`, `done`, `NINTH(not important, nice to have)` and `bug` sections.
When a user story is completed, it gets moved to the done section.
The full kanban board can be viewed here: https://github.com/users/saziosu/projects/4/views/1

## Labels
The labels are priorised as follows:

| must have | This feature/issue is required for the project to function                      |
| should have   | Important to implement but will not crash the project without but still key features |
| could have    | would like to have, but not essential to the project                                 |

These result in the following stats:

![label stats image](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700580861/Screenshot_2023-11-21_at_15.33.51_kfcvlu.png)
This can be viewed directly here: https://github.com/users/saziosu/projects/4/insights/1

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

**Epic**|**User Story**|**Label**
:-----:|:-----:|:-----:
 |As a Developer, I can deploy the website early so that I can avoid any technical issues or stress later in the project|must have
Remote Book Swap|As a User, I can create a book post so that I can other users can decide if they would like to swap|must have
Remote Book Swap|As a User, I can view other book posts so that I can decide which book I would like to swap with|must have
Remote Book Swap|As a User, I can edit my book post so that I can update my information|must have
Remote Book Swap|As a User, I can delete my book post so that I can manage my posts|must have
Account Management|As a User, I can create an account so that I can access features for authenticated users|must have
Account Management|As a User, I can reset my password so that I can access my account if I forget my password|could have
Account Management|As a User, I can update my contact details so that I can allow users to contact me for a swap|could have
Design & Experience|As a User, I can view a clean and attractive website so that I can have a positive experience|should have
Design & Experience|As a User, I can receive feedback messages so that I can gain feedback from the actions I have completed|could have

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

**All images were chosen to match the theme of the site**
The hero image was sourced from [Pexels](https://www.pexels.com/photo/books-on-shelves-2177482/)
The placeholder image was also sourced from [Pexels](https://www.pexels.com/photo/small-flowers-on-a-book-3696663/)
The example Book images were sourced from [Goodreads](https://www.goodreads.com/)

# Features 

## Current Features

### Navbar
![navbar image](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700764481/Screenshot_2023-11-23_at_18.34.37_brfec9.png)

The navbar was made with bootstrap.
The user is shown the user they are logged in as on the right of the navbar.
The navbar color was chosen based on the color palette selected for this project which is part of the user story [Styling & Layout](https://github.com/saziosu/book-swap/issues/17)

### Hero Section
![hero image](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700764505/Screenshot_2023-11-23_at_18.34.58_eeprk6.png)

The Hero image was chosen to match the theme of the website (books).
The mission statement overlaying the image was also chosen in line with the selected color palette to give a positive experience to the user.

### Info Section
![info section](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700764523/Screenshot_2023-11-23_at_18.35.18_zvupei.png)

The info section on was added to give more context into what the website's function and aims are.
Logged out users are encouraged to login and post their books. This information is not present for already logged in users so they are not seeing unnecessary information.

### Sign Up
![signup](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700765390/Screenshot_2023-11-23_at_18.49.44_xuxft2.png)

The link for the signup page can only be seen in the navbar for users that are logged out.
The signup page uses the base template from `django-allauth`.
Users are required to sign up for an account if they want to post books, or see the contact details of the users that own the books.
This is a part of the user story [Account Creation](https://github.com/saziosu/book-swap/issues/3)

### Login
![login](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700765375/Screenshot_2023-11-23_at_18.49.32_tgaaga.png)

The login page link is only viewable by users that are not logged in at the moment.
Users must be logged in to view the contact details of the users that own the posted books.
They must also be logged in to add their books that they would like to swap.
This is also part of the user story [Account Creation](https://github.com/saziosu/book-swap/issues/3)

### Logout
![logout](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700765361/Screenshot_2023-11-23_at_18.49.15_jskfcw.png)

The logout page link in the navbar is only seen by users that are already logged in.
The page asks the user to confirm that they are sure they want to log out of the account.
If they log out, they are then unable to add books or view the contact details of the book owners'
This feature is also a part of the user story [Account Creation](https://github.com/saziosu/book-swap/issues/3)

### Current Books
![current books](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700764548/Screenshot_2023-11-23_at_18.35.38_vvrrlg.png)

The currently posted books are viewable on the homepage.
There is a link to jump to this section of the page in the navbar.
On larger devices, this shows 4 books per row.
On smaller medium devices like tablets, this shows 3 books per row.
On mobile, this gives 1 book per row to ensure its fully viewable.
It includes the image of the book, the title, author and book's owner with the time posted.
The user that made the post (if logged in), can see the edit button and edit straight from the homepage.
This is part of the user story [View Books](https://github.com/saziosu/book-swap/issues/9)

### Read Book Posts
![book detail](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700771870/Screenshot_2023-11-23_at_20.37.44_n7igc7.png)

The detailed book post can be viewed by clicking on the card for the book post on the home page.
This shows more details of the book like it's current condition. Condition was added because someone may not want a book that is only of poor condition, so this helps them make an informed decision.
The genre is also included on this page, along with the book's blurb.
The slug for this is generated from the title. If a book with the same name is added, the title is still used but a number is added to the end of the slug to ensure it is unique.
This is also part of the user story [View Books](https://github.com/saziosu/book-swap/issues/9)

### Add Book
![add book](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700764578/Screenshot_2023-11-23_at_18.36.10_gvqalh.png)

The `add-book` can be accessed via the navbar for logged in users.
There is also a button at the top of the current books section, if this button is clicked and the user is logged out, they are brought to the login page. This encourages the user to log in to continue with this action.
The phone number field is set up to default to Irish numbers, but international dialling codes can also be used.
This is part of the user story [Create Book Post](https://github.com/saziosu/book-swap/issues/6)

### Edit Book
![edit book](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700764728/Screenshot_2023-11-23_at_18.38.44_b834sy.png)

The edit book page is only accessible by the user that made the book. They must be logged in to see this.
If a user that is logged in, but did not post that book manually enters the url to edit that book in their browser, they will reach an error page and not be allowed to complete that action.
The edit book page uses the same form as create book, so they are able to see all the previous information in that form so they can easily see what is currently there and edit it accordingly.
This feature is part of the user story [Edit Book Posts](https://github.com/saziosu/book-swap/issues/8)

### Delete Book
![delete book](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700764748/Screenshot_2023-11-23_at_18.39.01_efbpfa.png)
The delete page is only accessible by the user that made the book, they must be logged in to see the delete button.
If a user tried to reach the delete page for a book that they did not create they will get an error page and now be allowed to complete that action.
This feature is part of the user story [Delete Book Posts](https://github.com/saziosu/book-swap/issues/13)

### Reserved Book
![reserved book](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700771775/Screenshot_2023-11-23_at_20.36.08_kowb8k.png)
This is a boolean field in the database, it allows the user to confirm that the book has been reserved. A reserved book is pending a swap, so if the swap does not go ahead the user can edit it again and confirm that this book is available again.
If the book has been marked as reserved, all users cannot see the book owner's contact details.
This stops the owner from getting unnecessary contacts when their book is not available.

### Messaging
![messaging](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700765691/Screenshot_2023-11-23_at_18.54.40_q8l9fv.png)
Messaging is added for actions like posting books, editing books, deleting books, logging in and logging out.
This gives feedback to the user to give them feedback and show they have successfully completed their chosen action.T
This feature is part of the user story [Toast messages](https://github.com/saziosu/book-swap/issues/15)

### Footer
![footer](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700765412/Screenshot_2023-11-23_at_18.50.06_a8io79.png)
The footer is at the bottom of the page, Bootstrap flex was used to keep the footer at the bottom of all pages.
It includes links to Twitter, Facebook, Instagram and YouTube. These open in new tabs and include descriptive labels for accessibility.

## Future Features

* Password reset, currently the project does not require an email address. In future when I have furthered my skills I would like to add a password reset
* Update contact details, in future I would like to add a profile to the site so that users can track all the books they have posted. It would be nice if the contact details on the post pulled from the posting user's profile and they can easily update this from their profile.
* Books API - if I had more time and furthered my skills I would love to integrate this project with an API such as [Google Books](https://developers.google.com/books) or [Open Library](https://openlibrary.org/developers/api). This would allow the user to search for book and choose the correct one, rather than entering all of the book's information manually - this would also prevent human error such as entering the wrong details etc.
* Search - it would be a nice feature to add a search bar that allows you to search for your favourite author or genre, for example.
* Image optimisation - it would be great to add a method to auto upgrade uploaded to images to next gen format like webp. If I had more time and/or money I would love to implement this via django natively or via a CDN feature like CloudFlare's Polish feature.

## Accessibility

* Semantic HTML was used throughout the site as much as possible to ensure accessibility.
* Links to other pages and external websites in the footer were given `aria-label` attributes to ensure accessibility.

# Technology Used

## Languages

* HTML
* CSS
* Python
* JavaScript

## Frameworks, Libraries & Programs 

* BootStrap
* Django
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

* [Code Institute](https://github.com/Code-Institute-Solutions/Django3blog) -  I relied heavily on this resource to help set up the following:
  * Templates
  * Models.py
  * Urls.py
  * Messages - including timing them out with JavaScript
  * Views.py
  * Djang-allauth
  * Cloudinary Fields
  * Setting up django files (settings, admin etc)
* [Code Institute](https://github.com/ckz8780/ci-fsf-hello-django/) - I used this hello-django project for help with setting boolean field
* [Django Documentation](https://docs.djangoproject.com/en/4.2/ref/models/fields/#choices) - I used this resource to help set up the choice field in my model in models.py
* [Django Documentation](https://docs.djangoproject.com/en/4.2/ref/views/#error-views) -  I used this to help understand the error pages for django
* [Corey Schafer](https://www.youtube.com/watch?v=-s7e_Fy6NRU) - I used this resource to help set up the views for:
  * Creating posts
  * Editing posts
  * Deleting posts
* [ngangasn.com](https://ngangasn.com/what-is-get_absolute_url-in-django/) - I used this resource to help me set the absolute url on my model, to redirect the user to the book detail page after creating a post.
* [StackOverflow](https://stackoverflow.com/questions/65402719/updateview-and-preventing-users-from-editing-other-users-content) - I used this resource to help only allow the owner of the post to edit and/or delete it
* [CrispyForms Documentation](https://django-crispy-forms.readthedocs.io/en/latest/layouts.html) - I used this to help set up the crispforms helper, to help the submit button
* [StackOverflow](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown) - used this resource to help set up the messages on the deleteview
* [StackOverflow](https://stackoverflow.com/questions/24914637/show-a-successful-message-with-class-based-views) - I used this resource to help set up the messages on the other generic class based views
* [StackOverflow](https://stackoverflow.com/questions/28723266/django-display-message-after-post-form-submit) - I also used this resource to help set up messages on update and create views
* [StackOverflow](https://stackoverflow.com/questions/75495403/django-returns-templatedoesnotexist-when-using-crispy-forms) - I used this resource to help with an error with crispyforms package
* [Django Documentation](https://docs.djangoproject.com/en/4.2/ref/models/instances/#django.db.models.Model.get_FOO_display) - I used this resource to help resolve an issue with showing the model's choice data on the front end
* [AutoSlug](https://django-autoslug.readthedocs.io/en/latest/) - I used this resource to help set up unique slugs from the book title


## Media

* [Canva Logo Generator](https://www.canva.com/create/logos/) was used to create the favicon and site logo
  * [favicon.io](https://favicon.io/) was used to convert the logo into a favicon icon file
* The hero image on the homepage was sourced from [Pexels](https://www.pexels.com/photo/books-on-shelves-2177482/)
* The book post placeholder image was also sourced from [Pexels](https://www.pexels.com/photo/small-flowers-on-a-book-3696663/)
* The sample Book post images were sourced from [Goodreads](https://www.goodreads.com/)


## Content

* The information from the books were also sourced from [Goodreads](https://www.goodreads.com/)
  * I used this source to get the title, author, blurb/description and genre.

# Acknowledgements

* Graeme, my mentor, for all the help and advice throughout the project.
* Course Facilitator Alan for all the helpful tips and tricks, and great guidance throughout the project.
* My cohort classmates for feedback during our standups.

[Top](#bookswap)