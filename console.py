import pdb
from models.user import User
from models.location import Location 

import repositories.user_repository as user_repository 
import repositories.location_repository as location_repository

user1 = User("Susan", "Tv Producer")
user_repository.save(user1)
user2 = User("Greg", "Assistant Director")
user_repository.save(user1)


location1 = Location("Glasgow", "River City", True)
location_repository.save(location1)
location2 = Location("Edinburgh", "Avengers: Infinity War", False)
location_repository.save(location2)



