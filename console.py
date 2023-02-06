from models.user import User
from models.location import Location 

import repositories.location_repository as location_repository
import repositories.user_repository as user_repository 

location_repository.delete_all()
user_repository.delete_all()

# user_repository.select_all()

user1 = User("Susan", "Tv Producer")
user_repository.save(user1)
user2 = User("Greg", "Assistant Director")
user_repository.save(user2)


location1 = Location("Glasgow", user1, "River City", True, False)
location_repository.save(location1)
location2 = Location("Edinburgh", user2, "Avengers: Infinity War", False, False)
location_repository.save(location2)


location_repository.select_all()

