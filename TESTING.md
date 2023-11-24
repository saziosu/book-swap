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



# Manual Testing

A range of devices were used to test the site.

* OnePlus 7T Pro (Firefox, chrome, opera)
* MAC: MacBook Pro 14-inch 2021 (Mac OS Ventura 13.6.2) (Chrome, Safari, Firefox)
* LENOVO Tab P11 11.5" Tablet (Chrome, Firefox)

[Browserstack](https://www.browserstack.com/) was also used to test on the following devices:

* iPhone 14 (Chrome, Safari)
* iPhone 12 mini (Chrome, Safari)
* Samsung s23 (Chrome, Firefox)
* iPad 10th (Chrome, Safari)

MANUAL TESTING DETAILS

# Bugs

## Known Bugs

KNOWN BUGS TABLE

## Fixed bugs

FIXED BUGS TABLE