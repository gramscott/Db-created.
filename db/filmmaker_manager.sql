DROP TABLE users;
DROP TABLE locations;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  job VARCHAR(255),
);

CREATE TABLE locations (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  set VARCHAR(255), 
  filmed BOOLEAN,
  user_id INT NOT NULL REFERENCES users(id) 
)






-- # tables tested. For now, I'm trying to be less complicated as possible. Would like to add in climate, i could add in a boolean but it would be good if there was a similar way like the datetime import and description but that might be uneeded. 