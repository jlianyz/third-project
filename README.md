# The Skincare Diaries
## Data Centric Development Milestone Project
### Introduction
The purpose of this site is for skincare aficionados to research more about top skincare products and also contribute their latest finds to the community. They are also able to update outdated information on products or delete products that are no longer relevant. The site can be found [here](https://jlyz-project3mongo.herokuapp.com/)

### User stories
##### As a newbie to skincare, I want to:
* Search for skincare products based on my skin concerns, type of product, or brands
* Know how much the product costs, how big the bottle is, where it is from and have a short description on it so that I can take all these into consideration when deciding to make a purchase

##### As a seasoned user of skincare, I want to: 
* Search for skincare products based on my skin concerns, type of product, or brands
* Add my latest finds to the products list to share with other skincare lovers
* Know how much the product costs, how big the bottle is, where it is from and have a short description on it so that I can take all these into consideration when deciding to make a purchase
* Ensure that product information is up to date
* Delete products that are no longer relevant

***

### UX
The site has a base html page with the navbar and all the other pages from the same layout and color scheme.
* **Content**: The headers are clearly larger than the rest of the text, and all text is in the same font for consistency. Images are of the same height so that the products page looks neat.
* **Dropdown list and buttons**: The buttons are colored and placed prominently to draw user attention to them. 
* **Color scheme and images used**: The images are all skincare related so that they are relevant to the site. The pages are in either pink or white to create a pastel and girly feel, suitable for a skincare website.
***

### UI and features
The site is mobile responsive on all forms of media (laptop, mobile and tablet).
#### Base page
* Contains the mobile responsive navigation bar that allows easy navigation to either (1) Add a new product or (2) Search through the existing products
#### Index page
* Skincare related jumbotron image with short description of what the site is about
#### Add product page
* Bootstrap divs, with left column having a short description on how their addition contributes to the website and right column having the form for them to submit the products
* Background is pastel pink and overlays a skincare related image
* Required input fields (all except image and description) are marked with a *
* Input fields that have unique values allow users to enter any text or number
* Input fields with standard attributes (country of origin, type and purpose) and a dropdown menu. The menu is created using a for loop to loop through the existing values 
* For pictures, users can upload any image file from their local drive
* Submit button for the user to add products
* Reminder to user to upload the corrrect image file types
* User is able to upload an image to the corresponding recipe
* Once the product is submitted, user will be redirected to product list where they can see the product that they have just added.
#### Products list page
* Users can search for their products based on country of origin, type or purpose using the dropdown lists
* Mobile responsive cards are used to display the product’s name, image and price. The selection will be updated when users filter with the above dropdown
* The cards contain images of a consistent height so they look neat
* On clicking on a product, users will be redirected to a product details page with more information about the product 
* Users can reset their search with a prominent reset button at the top
#### Product details page
* Contains detailed information about the product (name, brand, country of origin, type, price, quantity, description and larger image). 
* This page also allows users to edit the product info, delete it or go back to the main products listing page with color coded buttons
* When users choose to edit the product, they will be redirected to the edit products page
* When users choose to delete the product, a modal will pop up to confirm they really want to delete the product or not. If they click “yes”, they will be redirected to the main page. If they click “no” or outside of the modal, the modal will close and user remains on the product details page
* When users choose to go back, they will be redirected to the products listing page
#### Edit product page
* Contains bootstrap divs, with a left div explaining more about why keeping the information updated is important and a right div containing the form for them to update the product
* Similar to the add product form, it contains product information in either text, number or dropdown.
* If user does not make changes, the previous information will still be displayed.
* Reminder to user to upload the correct image file types


### Technologies used
* HTML
* CSS
* Python
* Bootstrap (4.4.1)
* Fontawesome
* bson to store and import files to MongoDB
* Flask with Jinja2
* Pymongo
* [MongoDB](https://www.mongodb.com/) as the noSQL database
***

### Features left to implement
In future, I would like to:
* To add a section allowing product reviews
* Include user authentication (Register/ Login/ Logout) to restrict access to who can delete, update or add products
***

### Testing

This site is tested to be responsive on the following devices:
* Iphone 5/6/7/8
* Ipad
* Ipad Pro (best viewed in landscape mode)
* Safari
* Chrome
* Firefox
* Edge
* IE

### Manual testing
#### Base page
* Navigation bar is mobile responsive and links to the correct pages.
* Logo is of appropriate size and toggle works for mobile
#### Index page
* Jumbotron image is displaying correctly and font size is appropriate for all mobile and laptop devices
* Text is easy to read despite background, due to semi opaque white overlay
#### Add product page
* Making sure that user is unable to submit a product if required fields are not filled in
* Dropdown list for loop is working and showing the right values for the right attributes
* User is unable to enter text into the number fields
* Submit button for the user to add new product is working
* Ensuring that user is redirected back to the main page after pressing the submit button
#### Products list page
* Ensuring that the dropdown searches work for each of the 3 attributes and that the right products are showing up for the searches
* When the product is clicked, users are redirected to the right product details page
* Products are listed in the right mobile responsive view and no images overlap
* Reset button works and clears the search
#### Product details page
* The right product attributes are showing up
* The image is displaying in the right size and does not overlap with the text regardless of device
* The text is easy to read
* The edit, delete and back buttons are working
* When clicking on the edit button, users are redirected to the correct product’s edit page
* When clicking on the delete button, the yes and no buttons in the modal work and redirect the user accordingly to the right page
* When clicking on the back button, the user is correctly redirected back to the products list page
#### Edit product page
* Input fields correctly display the existing information
* If user does not make any changes and presses the submit button, the same information is showing
* If user does not fill in or removes any of the required fields, they are unable to press the submit button
* The updated information is showing correctly in the products listing page
* The information is updated in MongoDB to reflected the edited details in the correct format (string, integer etc)
* Upon submission, the user is correctly redirected back to the index page.

### Interesting errors encountered and steps taken to fix them
1.	When editing product info, existing image not stored and not showing up if a new image is not added
* Solution: added if else statement in app.py to ensure that existing image will still show up

2.	Initially, I wanted product details to show up in a modal box but each time I clicked on an image for more info, the details of the first product in the list would show up in every box, regardless of which image I was clicking
* Solution: Create a separate product details page. Reason for the error was that the modal box was unable to link to the correct product id.
***

### Deployment
Heroku deployment - this is done as a last step to ensure that all installed packages are included in the requirements.txt file 
1.	Sign up for a [Heroku](https://www.heroku.com/) account
2.	Install Heroku using bash: `sudo snap install heroku --classic`
3.	Log into Heroku in bash: `heroku login` . This directs you to a link to log in on the Heroku site
4.	Create a new app in bash: `heroku create <app_name>`
5.	Check that the new remote has been added using bash: `git remote -v`
8.	Install gunicorn in bash: `pip3 install gunicorn`
9.	Create a file named "Procfile", add: `web gunicorn app:app` and save it
10.	Create the requirements.txt file using bash: `pip3 freeze --local > requirements.txt`
11.	Commit and push the project to heroku
* `git add .`
* `git commit -m "commit name"`
* `git push heroku master`
12. Enter your key and value in Heroku config in bash: `heroku config:set MONGO_URI=(input here)`


I deployed the site to Github with the following steps:
1. Go to this repository's github [link](https://github.com/jlianyz/third-project)
2. Click on settings --> Github Pages
3. Select "none" for the Source and then select "master branch"
4. Stored my MONGI URI as a key using bash

For my IDE, I used AWS Cloud9. My file architecture is as follows:
* A separate folder for templates containing html files
* A separate folder for static files containing css file and images folder
* An app.py file
* Procfile
* requirements.txt file

To deploy the page locally:
1.	Go to the github [link](https://github.com/jlianyz/third-project)
2.	Click on the Clone/download button and copy the URL 
3.	Set up a database with similar collections in MongoDB
4.	Set up your own MONGI URI key
4.	6.	To run the application locally, type `python3 app.py` in bash
***
### Credits
**Images**

The site images were taken from [Pexels](https://www.pexels.com/search/skincare/), while the product images and information were taken from [Amazon](https://www.amazon.com/)

**Inserting images into MongoDB**

I watched this [video](https://www.youtube.com/watch?v=DsgAuceHha4) for inspiration

**Typography**

The fonts were taken from [Google fonts](https://fonts.google.com/)