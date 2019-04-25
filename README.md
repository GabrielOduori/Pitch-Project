# Pichers Zone

###  By Gabriel Oduori

## Description
Pichers Zone  is a web application that that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

The pitches are organized by category. You can have different categories eg Technology, Government, Hospitality and Social Comunity.

The pitches are organized by category with the new posts should be displayed first

You can view the site at: http://location.com

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See the pitches other people have posted.
* Vote on the pitch they liked and give it a downvote or upvote
* Be signed in for me to leave a comment.
* Receive a welcoming email once I sign up.
* View the different categories.
* Comment on different pitches and leave feedback.
*  View pitches I have created in my profile page.

## SetUp / Installation Requirements
### Prerequisites
* python3.7
* Flask 1.0
* virtualenv

### Cloning
* In your terminal:
        
        $ git clone https://github.com/GabrielOduori/Pitch-Project
        $ cd News-Highlight

## Running the Application
* Creating the virtual environment

        $ python3 -m pip install --user virtualenv ( on a Mac)
        $ python3 -m virtualenv env
        $ source env/bin/activate
        $(For other operating systems, see https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
        
* Installing Flask and other Modules
- While in the virtalenvironment install all the requirements by running 
$ pip install -r requirements.txt

        
* Setting up the API Key

        
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh
        
## Testing the Application
* To run the tests for the class files:

        $ python3.7 manage.py tests
        
## Technologies Used
* Python3.7
* Flask

## License information

Pichers Zone is Copyright 2019 Gabriel Oduori licensed under GNU avaliable at http://www.gnu.org/licenses.

## Contact

gabriel.oduori@gmail.com

