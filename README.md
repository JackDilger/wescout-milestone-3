<h1 align="center">Wescout</h1>

![Wescout Home Page](wescout/static/images/readme/reponsive-site.JPG)

## About

***

[Wescout](https://github.com/JackDilger/wescout-milestone-3)  is player managment database built for professionals working in the Football industry. Users of the site can discover new talent by browsing and searching for existing players and learn key information, such as market value or read more in depth player analysis from other users. This app has a clean and itutitive interface which allows users to easily maintain player information, users can securely add,edit and delete player data once they register for an account. 


## Strategy and planning

***

Why football?

Football is the most popular sport in the world, with an estimated following of 4 billion fans. It is a global sport played by hundreds of millions people around the world. It's a game that breaks down social boundaries like no other sport and is inclusive
to everyone, connecting people of opposite cultures. The UK Sports Industry alone is worth £23.8 billion and holds nearly 1 million jobs, none more important than scouts. The biggest clubs have worldwide scouting networks, some full-time scouts can work up to 80 hours a week, watching many games in many different countries. With such a vast amount of data, its crucial that you have somewhere to securely maintain information on your players.


The Wescout app aims to be a hub for football scouts and professionals working in the industry, where by they can safely store player information and capture key data about them all in one place. Players information is always changing, whether they are moving clubs or their market value is fluctuating due to performance. This is why it is important you can update this information easily, or delete records of players you are no longer monitoring. The Wesout app allows users to seamlessly  manage all player data in this way with the ability to add, edit and delete player information on the go at any time on any device. 

It's normal to be maintaining information on hundreds of players at a time as a football scout, that is why it is important to be able to quickly locate player information without spending hours scrawling through lists of information. The Wescout app has an intuitively designed search index, you can find an individual player instantly by searching their name or filter the database to only display your own added players. 

We want to build a community of people in the football industry and develop the site in this direction of a collaborative approach towards scouting. Discovering new players can be challenging and costly and we wanted to offer a solution to this. That is why we wanted users to be able to collaborate by sharing player data. As well being able to maintain your own information you can browse the full list of players added by other Wescout professionals. 

One of our main aims with doing this, was to ensure though that your own information was kept secure. We understand the important of safely managing data online, which is why we used a multitude of defensive programming features in the app to ensure your information is safe.


## User Experience (UX)



-   ### User stories

    1. As a user, I want to understand the purpose of the website immediately upon opening the site.
    2. As a user, I want to be able to easily navigate the website. 
    3. As a user, I want to be able to quickly register a profile and be given confirmation of this action.
    4. As a user, I want to easily log out and be given confirmation of this action.
    5. As a user, I want to easily log in to my registered profile anytime I return and be given confirmation of this action.
    6. As a user, I want to easily add new players and be given confirmation of this action.
    7. As a user, I want to easily edit my player information and be given confirmation of this action.
    8. As a user, I want to easily delete my player information and be given confirmation of this action.
    9. As a user, I want to be able to view all players added to the database.
    10. As a user, I want to be able to search for an individual player by name.
    11. As a user, I want to be able to view only players I have added to the database.
    12. As a user, I want to be able to reset the player view after using searches.

-   ### Site Developer/Owner

    1. As the site developer/owner, I want to encourage the user to use the website as much as possible to grow the player base, I'll do this by offering future development that will benefit users to stay innovative.
    2. As the site developer/owner, I want to be the only user with access to edit/add/delete scouting regions.
    3. As the site developer/owner, I want to be able to add new scouting regions and be given confirmation of this action.
    4. As the site developer/owner, I want to be able to edit scouting regions and be given confirmation of this action.
    5. As the site developer/owner, I want to be able to delete scouting regions and be given confirmation of this action.
    6. As the site developer/owner, I only want users to have access to add players once they are registered and logged on.


## Layout

***

- I used Balsamiq to structure the layout of my website during the initial design phase.
- I used Materialize's built in grid system to make my site responsive across all devices.

### Home page (players) wireframe

![Home](wescout/static/images/readme/players-wireframe.JPG)

### Add Player wireframe

![Add Player](wescout/static/images/readme/add-player-wireframe.JPG)

### Edit Player wireframe

![Edit Player](wescout/static/images/readme/edit-player-wireframe.JPG)

### Add Region wireframe

![Add Region](wescout/static/images/readme/add-region-wireframe.JPG)

### View Regions wireframe

![Regions](wescout/static/images/readme/regions-wireframe.JPG)

### Login wireframe

![Login](wescout/static/images/readme/login-wireframe.JPG)

### Register wireframe

![Register](wescout/static/images/readme/register-wireframe.JPG)

### Profile wireframe

![Profile](wescout/static/images/readme/profile-wireframe.JPG)


## Existing Features and how they align to user stories

***

- __Logo-Links to user story 1 & 2__

  - The head of the page contains the 'Wescout' logo. The logo was designed to represent the websites target audience and purpose.
  - The text content of the logo 'Wescout', offers an indication to the user what the site offers and who it is built for. The player ID icon, also lends to this as a way to show it is a place for player information. 
  - The logo also serves as a clickable link, allowing users a simple way to navigate back to the home page at any time. The logo is consistently placed on each page of the website because of this.



![Logo](/assets/readme-files/logo.quiz.JPG)


- __Welcome Page- Links to user story 1__
  - The welcome page is displayed as soon as you load the website, it offers clear text content abouts its purpose and target audience and gives helpful tips on how to use the websites features.


  ![Welcome](/assets/readme-files/logo.quiz.JPG)

  
- __Search Bar- Links to user story 10, 11 & 12__
  - The search bar has a text index which searched the players database in MongoDB, it allows users to find individual players by name or view only players the user has added themselves. 
  - The reset button will allow you to reset the player view once you have finished with your search


  ![Search](/assets/readme-files/logo.quiz.JPG)


- __Player Collapsible- Links to user story 8__
  - The player collapsible shows a full list of all players added to the Wescout database.
  - You can see quick key information about the players name and club, and you can also expand each player section to view all the player data.


  ![View Players](/assets/readme-files/logo.quiz.JPG)


- __Register- Links to user story 2 & 3- Links to site owner goal 6__
  - Users can easily navigate to the register page using the nav bar link
  - In this screenshot you can see the flash message 'You must register to add players' which is triggered if a player
  tries to use the add player button without being signed in. 
  - Users can easily register here by filling out the required input fields on the form.
  - Once registered you are taking to the profile page and welcomed to the site to give confirmation of your registration.


  ![Register Form](/assets/readme-files/logo.quiz.JPG)



- __Log in- Links to user story 2 & 5__
  - Users can easily navigate to the register page using the nav bar link
  - Users can easily log in here by filling out the required input fields on the form.
  - Once logged you are taking to the profile page and welcomed to the site to give confirmation of your login.


  ![Login](/assets/readme-files/logo.quiz.JPG)


- __Log Out- Links to user story 2 & 4__
  - Users can easily log out but using the nav bar link
  - Once logged they will be taken to the log in page and a flash message will confirm they have successfully logged out.


  ![Logout](/assets/readme-files/logo.quiz.JPG)


- __User Profile- Links to user story 3 & 5- Links to site owner goal 1__
  - Anytime a user logs on ore registeres, they are taken to their profile page and a flash message welcoming them gives confirmation they are logged in. 
  - Another important reason they are taken here when logging in, is that here the site developer/owner keeps users up to date on future development and features users can look forward to. 


  ![Profile](/assets/readme-files/logo.quiz.JPG)


- __Add Players-Links to user story 2 & 6__
  - Users can easily navigate to the add players form using the nav bar link once logged in or using the add player button from the players page.
  - The add player form is easily completed by filling out all required input fields and is clear on what information is needed. 
  - Once the form is submitted, they are taken to the players page where  flash message will confirm their player has been added successfully. 


  ![Add-Player](/assets/readme-files/logo.quiz.JPG)


- __Edit Players- Links to user story 2 & 7__
  - Users can easily edit their added player information by using the edit button which takes them to the form. The form will have the preloaded player information and allow them to easily update any fields before submitting the new player data. 
  - Once the form is submitted, they are taken to the players page where a flash message will confirm their player has been updated successfully. 


  ![Edit-Player](/assets/readme-files/logo.quiz.JPG)


- __Delete Player- Links to user story 2 & 8__
  - Users can easily delete their added players by using the delete button. The Button will open a modal to confirm the deletion or give the option to cancel the request.
  - Once they confirm deletion on the modal pop up, they are taken to the players page where a flash message will confirm their player has been successfully deleted. 


  ![Delete-Player](/assets/readme-files/logo.quiz.JPG)


- __Manage Scouting Regions- Links to site owner goal 2__
  - The Regions page is hidden to all users except the admin.
  - Once logged in the admin user can easily navigate to the regions page using the nav bar link that will appear only to them
  - The regions page allows the admin to easily add/edit/delete regions using the required buttons.



  ![Manage Regions](/assets/readme-files/logo.quiz.JPG)



- __Add Region- Links to site owner goal 3__
  - The admin can easily add new regions by using the add region button which takes them to the form. The form is easily completed  by filling in the required input field.
  - Once the form is submitted, they are taken to the regions page where a flash message will confirm their region has been added successfully. 


  ![Add-Region](/assets/readme-files/logo.quiz.JPG)


- __Edit Region- Links to site owner goal 4__
  - The admin can easily edit regions by using the edit button which takes them to the form. The form will have the preloaded region name and allow them easily update the name by filling in the required input field.
  - Once the form is submitted, they are taken to the regions page where a flash message will confirm their region has been updated successfully.  


  ![Edit-Region](/assets/readme-files/logo.quiz.JPG)


- __Delete Region- Links to site owner goal 5__
  - The admin can easily delete a regions by using the delete button. The Button will open a modal to confirm the deletion or give the option to cancel the request.
  - Once they confirm deletion on the modal pop up, they are taken to the regions page where a flash message will confirm the region has been successfully deleted. 


  ![Delete-Region](/assets/readme-files/logo.quiz.JPG)










