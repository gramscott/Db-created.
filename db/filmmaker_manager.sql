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


INSERT INTO users (name, job) VALUES ('Susan', 'TV Producer') RETURNING *;
INSERT INTO users (name, job) VALUES ('Greg', 'Assistant Director') RETURNING *;

INSERT INTO locations (name, set, filmed, good_climate, user_id) VALUES ('Glasgow', 'River City', 'True', 'False', 1) RETURNING *;
INSERT INTO locations (name, set, filmed, good_climate, user_id) VALUES('Edinburgh', 'Avengers: Infinity War', 'False', 'False', 2) RETURNING *;

