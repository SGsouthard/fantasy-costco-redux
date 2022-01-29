# fantasy-costco-redux
Where all your dreams come true! Got a deal for you!

# TODO
    Establish backend information
        Heroku? Mongo?

# TODO
    User Story
        "As a User, I'd like to be able to contribute new items for DnD games"
        "As a User, I'd like to have access to the items I've made"
        "As a User, I'd like to be able to search for items by name, or by type"        

# TODO User Permissions
    [x]- Need to give blanket permission to Users to add items to the database
        - Need to figure out how to give permissions for people to update things they've uploaded
            - if statement? if <Logged-in-User> == User(field) then allow edit?
        - Need to figure out how to automatically update the User field in an item to the user that made it

# TODO Reset/Change password
    - Django has default forms for these, I just need to set up views for them