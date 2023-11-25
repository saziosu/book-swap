# BookSwap | Testing

Link for the finished deployed site: https://book-swap-13f900a2d9c7.herokuapp.com/

![Am I responsive image](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700683184/amiresponsive_vzoufb.png)

# Table of Contents

- [BookSwap | Testing](#bookswap--testing)
- [Table of Contents](#table-of-contents)
- [Testing Tools](#testing-tools)
  - [W3C Validator](#w3c-validator)
  - [CSS Validator](#css-validator)
    - [JavaScript Validator](#javascript-validator)
    - [Python Validator](#python-validator)
    - [Lighthouse Report](#lighthouse-report)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
  - [Known Bugs](#known-bugs)
  - [Fixed bugs](#fixed-bugs)

# Testing Tools

## W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML code across all pages of the website.
Due to the django templating, pasting directly from the code was not possible.
Instead the source code via the browser was used to test these and directly input into the validator.

**Page**|**Pass/Fail**
:-----:|:-----:
Homepage|Pass
Book Detail|Pass
Add Book|Pass
Edit|Pass
Delete|Pass
Logout|Pass
Login|Pass

## CSS Validator

[Jigsaw](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code across all possible pages of the website.

**Page**|**Pass/Fail**
:-----:|:-----:
Homepage|Pass
Book Detail|Pass

All other pages required login which was not handled by the validator via the url
Most of the pages are utilising Bootstrap for styling, however the custom css from style.css was input manually and passed with no errors:
![css validator](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700852774/Screenshot_2023-11-24_at_19.05.46_qsyebj.png)

### JavaScript Validator

[JShint](https://jshint.com/) was used to validate the JavaScript on the site.
The project only has a small amount of JS in the footer for helping to time out the toast messages on the front end.
There was one error about bootstrap not being a defined variable. This is fine however, as that is not seen in the validator.

### Python Validator

The [Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code written on the project
All python files passed the validation without issue, with the exception of settings.py which only has some line too long errors.

### Lighthouse Report

**Homepage**
![homepage lighthouse](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700856068/Screenshot_2023-11-24_at_20.00.41_zne78a.png)
The performance is not as high as it ideally should be. This is mainly due to the images that are uploaded, and the cache policy within Cloudinary. Unfortuantely there was not much more I could do to resolve this.

**Book Detail**
![book detail lighthouse](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700857152/Screenshot_2023-11-24_at_20.19.06_tnutrl.png)

**Add Book**
![add book](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700858146/Screenshot_2023-11-24_at_20.35.41_jrrlsc.png)

**Edit Book**
![edit book](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700858257/Screenshot_2023-11-24_at_20.37.31_dakflb.png)

**Delete Book**
![delete book](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700858377/Screenshot_2023-11-24_at_20.39.31_ozrnvi.png)

**Login**
![login page](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700858725/Screenshot_2023-11-24_at_20.45.18_tqloes.png)

**Logout**
![Logout](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700858377/Screenshot_2023-11-24_at_20.39.31_ozrnvi.png)

**Sign up**
![signup page](https://res.cloudinary.com/dygj0wxf0/image/upload/v1700858725/Screenshot_2023-11-24_at_20.45.18_tqloes.png)

# Manual Testing

A range of devices were used to test the site.

* OnePlus 7T Pro (Firefox, chrome, opera)
* MAC: MacBook Pro 14-inch 2021 (Mac OS Ventura 13.6.2) (Chrome, Safari, Firefox)
* LENOVO Tab P11 11.5" Tablet (Chrome, Firefox)

[Browserstack](https://www.browserstack.com/) was also used to test on the following devices:

* iPhone 15 (Chrome, Safari)
* iPhone 12 mini (Chrome, Safari)
* Samsung s23 (Chrome, Firefox)
* iPad 10th (Chrome, Safari)

Some css styling issues such as the hero image section being too large for the image on smaller devices and the orientation of the text on the info section were found through testing and tweaked accordingly.

**Feature**|**Expected**|**Pass/fail**
:-----:|:-----:|:-----:
Navbar|All links should redirect to the correct page|Pass
Navbar|Logout and Add Book should only be viewable to logged in users|Pass
Navbar|Signup and login should only be seen by users not logged in|Pass
Navbar|The navbar should show the username of the logged in user to show|Pass
Navbar|The navbar should only show the link to add a book to users that are logged in|Pass
Hero image section|The mission statement overlaying the hero image should change to fit smaller screen sizes|Pass
Sign up|Users must enter a username and password to sign up to the website|Pass
Login|Users must enter the correct username and password to log into the website|Pass
Logout|Users must be asked if they are sure they want to log out of the website|Pass
Logout|Users must be logged out after confirming they want to log out|Pass
Current books|The section listing the current books should change to fit the book posts on different screen sizes|Pass
Current books|The edit and delete buttons should only be seen by the users that made the post|Pass
Current books|Clicking on a post, should bring the user to the post detail|Pass
Current books|Logged out user: clicking on the `add book` button should  bring the user to the log in page|Pass
Current books|Logged in user: Clicking on the `add book` button should bring the user to the add-book page|Pass
Add Book|The user must fill out all the required fields to submit their book post|Pass
Add Book|Submitting the post should bring the user to the post detail page of the book post they just created|Pass
Edit Book|The edit button should only be visible to the user that created that post|Pass
Edit Book|Users that did not create the post, or logged out users should not be permitted to edit a book via direct url|Pass
Edit Book|The form should show the current data in the book post|Pass
Delete Book|The delete button should only be visible to the user that created that post|Pass
Delete Book|Users that did not create the post, or logged out users should not be permitted to edit a book via direct url|Pass
Delete Book|The user should be asked to confirm if they want to delete the post they selected|Pass
Delete Book|Confirming deletion should remove the post from the website|Pass
Delete Book|Cancelling the deletion should bring the user back to the previous page they were viewing|Pass
Reserved Book|The reserved book should display that it is reserved on the homepage/current books section|Pass
Reserved Book|The reserved book should hide the user's contact details on the Book detail page|Pass
Messaging|Messages should be seen at the top of the page for adding, editing, deleting, logging in and logging out|Pass
Messaging|Messages should be dismissable|Pass
Messaging|Messages should time out after 3 seconds|Pass
Footer|All links to external websites should open in new tabs|Pass

# Bugs

## Known Bugs

To my knowledge there are no further known bugs on this project

## Fixed bugs

All resolved bugs are listed on the [kanban board for the project](https://github.com/users/saziosu/projects/4)