DROP TABLE locations;
DROP TABLE users;


CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  job VARCHAR(255)
);

CREATE TABLE locations (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  set VARCHAR(255), 
  filmed BOOLEAN,
  good_climate BOOLEAN,
  user_id INT NOT NULL REFERENCES users(id) 
);







