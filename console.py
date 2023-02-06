from models.user import User
from models.location import Location 

import repositories.location_repository as location_repository
import repositories.user_repository as user_repository 

# user_repository.delete_all()
user_repository.select_all()

user1 = User("Susan", "Tv Producer")
user_repository.save(user1)
user2 = User("Greg", "Assistant Director")
user_repository.save(user2)


# location1 = Location("Glasgow", "River City", True, False, user1.id)
# location_repository.save(location1)
# location2 = Location("Edinburgh", "Avengers: Infinity War", False, False, user2.id)
# location_repository.save(location2)

# location_repository.delete_all()
# location_repository.select_all()

