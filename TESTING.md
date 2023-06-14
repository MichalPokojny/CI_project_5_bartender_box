# Testing

## Code Validation

Python

* Python code was tested using PEP8 Code Institute [Python Linter Validator](https://pep8ci.herokuapp.com/)

<details>

<Summary> Validation Output</Summary>

**Bag app**

apps.py
<p align="center">
<img src="./assets/test/bag-app.jpg">
</p>

contexts.py
<p align="center">
<img src="./assets/test/bag-contexts.jpg">
</p>

urls.py
<p align="center">
<img src="./assets/test/bag-urls.jpg">
</p>

views.py
<p align="center">
<img src="./assets/test/bag-vies.jpg">
</p>

**Bartender box app**

context_processors.py
<p align="center">
<img src="./assets/test/bartender_box-context-processors.jpg">
</p>

urls.py
<p align="center">
<img src="./assets/test/bartender_box-urls.jpg">
</p>

views.py
<p align="center">
<img src="./assets/test/bartender_box-views.jpg">
</p>

**Checkout app**

admin.py
<p align="center">
<img src="./assets/test/checkout-admin.jpg">
</p>

apps.py
<p align="center">
<img src="./assets/test/checkout-apps.jpg">
</p>

forms.py
<p align="center">
<img src="./assets/test/checkout-forms.jpg">
</p>

models.py
<p align="center">
<img src="./assets/test/checkout-models.jpg">
</p>

signals.py
<p align="center">
<img src="./assets/test/checkout-signals.jpg">
</p>

urls.py
<p align="center">
<img src="./assets/test/checkout-urls.jpg">
</p>

views.py
<p align="center">
<img src="./assets/test/checkout-views.jpg">
</p>

webhook_handler.py
<p align="center">
<img src="./assets/test/checkout-webhook-handler.jpg">
</p>

webhooks.py
<p align="center">
<img src="./assets/test/checkout-webhook.jpg">
</p>

**Home app**

apps.py
<p align="center">
<img src="./assets/test/home-apps.jpg">
</p>

urls.py
<p align="center">
<img src="./assets/test/home-urls.jpg">
</p>

views.py
<p align="center">
<img src="./assets/test/home-views.jpg">
</p>

**Products app**

admin.py
<p align="center">
<img src="./assets/test/products-admin.jpg">
</p>

apps.py
<p align="center">
<img src="./assets/test/products-apps.jpg">
</p>

forms.py
<p align="center">
<img src="./assets/test/products-forms.jpg">
</p>

models.py
<p align="center">
<img src="./assets/test/products-models.jpg">
</p>

urls.py
<p align="center">
<img src="./assets/test/products-urls.jpg">
</p>

views.py
<p align="center">
<img src="./assets/test/products-views.jpg">
</p>

widgets.py
<p align="center">
<img src="./assets/test/products-widgets.jpg">
</p>

**Profiles app**

apps.py
<p align="center">
<img src="./assets/test/profiles-apps.jpg">
</p>

forms.py
<p align="center">
<img src="./assets/test/profiles-forms.jpg">
</p>

models.py
<p align="center">
<img src="./assets/test/profiles-models.jpg">
</p>

urls.py
<p align="center">
<img src="./assets/test/profiles-urls.jpg">
</p>

views.py
<p align="center">
<img src="./assets/test/profiles-views.jpg">
</p>

**Rating app**

apps.py
<p align="center">
<img src="./assets/test/rating-apps.jpg">
</p>

models.py
<p align="center">
<img src="./assets/test/rating-models.jpg">
</p>

urls.py
<p align="center">
<img src="./assets/test/rating-urls.jpg">
</p>

views.py
<p align="center">
<img src="./assets/test/rating-views.jpg">
</p>

**Wishlist app**

apps.py
<p align="center">
<img src="./assets/test/wishlist-apps.jpg">
</p>

models.py
<p align="center">
<img src="./assets/test/wishlist-models.jpg">
</p>

urls.py
<p align="center">
<img src="./assets/test/wishlist-urls.jpg">
</p>

views.py
<p align="center">
<img src="./assets/test/wishlist-views.jpg">
</p>

</details>

HTML

* HTML code was tested using [W3 Validator](https://validator.w3.org/)

Every page has passed the W3 validator

<p align="center">
<img src="./assets/test/html_validator.jpg">
</p>

CSS

* CSS code was tested using [Jigsaw W3 Validator](https://jigsaw.w3.org/)

<p align="center">
<img src="./assets/test/css-validator.jpg">
</p>

JavaScript

* Javascript code was tested using [JSHint](https://jshint.com/)

main.js
<p align="center">
<img src="./assets/test/mainjs.jpg">
</p>

stripe_elements.js
<p align="center">
<img src="./assets/test/stripejs.jpg">
</p>

## Browser Testing

The website has been tested thoroughly on several different browsers.

* Google Chrome
* Mozilla Firefox
* Microsoft Edge
* Safari
* Opera

### Google Chrome Lighthouse

Lighthouse was used to test performance, Accesibility, Best Practices and SEO of the website.

Desktop Results:

<p align="center">
<img src="./assets/test/lighthouse.jpg">
</p>

Mobile Results:

<p align="center">
<img src="./assets/test/lighthouse-mobile.jpg">
</p>

## User Story testing

**EPIC** - Wishlist Management

**USER STORY**: Add Product to Wishlist
Acceptance Criteria: A user should be able to add a product to their wishlist.

**Summary**:

- As a user, when viewing a product, I can click on the "Add to Wishlist" button to add the product to my wishlist.
The website should validate that the product is successfully added to my wishlist.
I can view my wishlist to see the added product.

**Status**: Pass

**EPIC** - Product Review

**USER STORY**: Review a Product
Acceptance Criteria: A logged in user should be able to review a product.

**Summary**:

- As a logged in user, I can navigate to a product detail page and find a "Write a Review" section.
I can enter my review and submit it.
The website should then display the review on the product page.

**Status**: Pass

**EPIC** - Product Rating

**USER STORY**: Rating products
Acceptance Criteria: A logged in user should be able to rate a product.

**Summary**:

- As a  logged in user, I can navigate to a product page and find a rating system (e.g., stars) to rate the product.
I can select the desired rating and submit it.
The website should validate the rating submission and update the product's average rating.

**Status**: Pass

**EPIC** - Privacy and Terms

**USER STORY**: Privacy policy and Terms & Conditions
Acceptance Criteria: Users should be able the website privacy policy and terms & conditions.

**Summary**:

- As a user, I can find links to the privacy policy and terms & conditions in the footer or navigation menu.
Clicking on these links should open the respective pages with the relevant information.

**Status**: Pass

**EPIC** - Management

**USER STORY**: Manage registered users 
Acceptance Criteria: Administrators should be able to manage registered user accounts.

**Summary**:

- As an administrator, I can access a user management section with a list of registered users.
I can view user details, including their username, email, registration date and also all order history details.
I can perform actions such as suspending or deleting user accounts, manage their orders.

**Status**: Pass

**USER STORY**: Delete products
Acceptance Criteria: Administrators should be able to delete existing products.

**Summary**:

- As an administrator, I can access a product management section with a list of existing products.
I can select a product and choose the option to delete it.
The system should prompt for confirmation before deleting the product.

**Status**: Pass

**USER STORY**: Add and update products
Acceptance Criteria: Administrators should be able to add and update product information.

**Summary**:

- As an administrator, I can access a product management section to add new products.
I can provide product details such as name, description, price, and image.
I can submit the form to add the product to the system.
As an administrator, I can also update existing product information.

**Status**: Pass

**USER STORY**: Check out
Acceptance Criteria: Users should be able to proceed with the checkout process.

**Summary**:

- As a user, when viewing my shopping cart, I can proceed to the checkout process.
I should be prompted to provide shipping and billing information.
I can review the order Summary and confirm the purchase.
The system should process the payment and display a confirmation message.

**Status**: Pass

**USER STORY**: Confirmation email
Acceptance Criteria: Users should receive a confirmation email after placing an order.

**Summary**:

- As a user, after successfully placing an order, I should receive a confirmation email.
The email should contain order details such as the products purchased, total amount, and shipping address.
The email should be sent to the email address provided during the order process.

**Status**: Pass

**EPIC** - User Profile

**USER STORY**: User profile
Acceptance Criteria: Users should be able to view and edit their delivery information.

**Summary**:

- As a user, I can access my profile page to view my delivery information.
I can edit and update delivery details.
The system should validate and save the changes made to my profile.

**Status**: Pass

**EPIC** - Communication

**USER STORY**: Newsletter
Acceptance Criteria: Users should be able to subscribe to a newsletter.

**Summary**:

- As a user, I can find an option to subscribe to a newsletter.
I can provide my email address and choose to subscribe.
The system should validate the email address and add it to the newsletter subscription list.

**Status**: Pass

**EPIC** - Authentication

**USER STORY**: Login and Log out
Acceptance Criteria: Users should be able to log in and log out of their accounts.

**Summary**:

- As a user, I can access the login page and enter my credentials (username/email and password).
Upon successful authentication, I should be redirected to the home page as a logged-in user.
I can log out by selecting the "Log out" option, which should invalidate the session and redirect me to the login page.

**Status**: Pass

**USER STORY**: Registration
Acceptance Criteria: Users should be able to create new account.

**Summary**:

- As a user, I can access the registration page and provide the required information (username, email, password, etc.).
After submitting the registration form, the system should validate the information and create a new user account.
Upon successful registration, I should receive a confirmation email with further instructions.

**Status**: Pass

**EPIC** - Shopping Cart

**USER STORY**: Shopping bag
Acceptance Criteria: Users should be able to add and manage items in their shopping cart.

**Summary**:

- As a user, I can add products to my shopping cart by selecting the "Add to Cart" button.
The system should display the updated cart **Summary**, including the total number of items and the total price.
I can view and manage the items in my shopping cart, including removing or updating quantities.

**Status**: Pass

**EPIC** - Product Sorting and Searching

**USER STORY**: Sorting products
Acceptance Criteria: Users should be able to sort products based on different criteria.

**Summary**:

- As a user, when viewing a list of products, I can select sorting options such as "Price Low to High" or "Rating High to Low".
The system should update the product list according to the selected sorting criteria.

**Status**: Pass

**USER STORY**: Search products
Acceptance Criteria: Users should be able to search for specific products.

**Summary**:

- As a user, I can enter a search query in a search bar.
The system should display relevant products matching the search query.
The search results should include product names, descriptions, and other relevant details.

**Status**: Pass

**USER STORY**: Open a product
Acceptance Criteria: Users should be able to view detailed information about a product.

**Summary**:

- As a user, I can click on a product to view its detailed page.
The product page should display information such as name, description, price, and reviews.
Users can navigate back to the product list or continue with other actions like adding to the cart.

**Status**: Pass

## Black box features manual testing

<details>

<Summary>TEST PLAN</Summary>

<p align="center">
<img src="./assets/test/test_plan_1.png">
</p>

<p align="center">
<img src="./assets/test/test_plan_2.png">
</p>

<p align="center">
<img src="./assets/test/test_plan_3.png">
</p>

<p align="center">
<img src="./assets/test/test_plan_4.png">
</p>

</details>

<details>

<Summary>TEST DATA</Summary>

<p align="center">
<img src="./assets/test/test_data_1.png">
</p>

<p align="center">
<img src="./assets/test/test_data_2.png">
</p>

<p align="center">
<img src="./assets/test/test_data_3.png">
</p>

<p align="center">
<img src="./assets/test/test_data_4.png">
</p>

<p align="center">
<img src="./assets/test/test_data_5.png">
</p>

<p align="center">
<img src="./assets/test/test_data_6.png">
</p>

</details>

<details>

<Summary>TEST LOG</Summary>

<p align="center">
<img src="./assets/test/test_log_1.png">
</p>

<p align="center">
<img src="./assets/test/test_log_2.png">
</p>

<p align="center">
<img src="./assets/test/test_log_3.png">
</p>

</details>


## Unsolved Bugs


[Back to README.](./README.md)