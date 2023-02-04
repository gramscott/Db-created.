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



