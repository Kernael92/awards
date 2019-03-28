# Kernael92's Awards
# https://kernelawards.herokuapp.com/

* Profile API endpoint
## http://127.0.0.1:8000/api/profile

* Project API endpoint
## http://127.0.0.1:8000/api/project


## Built By [Kernael Apuko](https://github.com/kernael92/)

## Description
This is an application that allows authenticated users to view projects, submit their own projects and have them reviewed. The admin is responsible for posting, editing or deleting projects and profiles.

## User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* Sign in to the application to start using.
* View posted projects and their details.
* Post a project to be rated/reviewed.
* Rate/ review other users' projects
* Search for projects
* View projects overall score
* View their profile page

## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Create a profile and post projects.
* Delete projects
* Update project post details.
* Comment and rate/review projects.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display all projects | **Home page** | Clickable links to view a site and rate/review the project |
| Comment and review on a users posted project| **On  click** | average of ratings based on the design, usability and content|
| To post a project  | **Through Admin dashboard** | Add the title, image, description and link of the project|
| To edit profile | **Through Admin dashboard** | Redirected to the  profile settings and edit the profile picture as well as the bio|
| To delete a profile,comment,rating or project  | **Through Admin dashboard** | click on any of the  objects and confirm by delete button|
| To search  | **Enter text in search bar** | Users can search by title of the project|


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt
* Django authentication

### Cloning
* In your terminal:

        $ git clone https://github.com/kernael92/kernel-awards
        $ cd kernel-awards

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.6 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test awards

## Technologies Used
* Python3.6
* Django and postgresql

## License

Copyright (c) 2018 Kernael92

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
