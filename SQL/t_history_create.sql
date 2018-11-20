CREATE TABLE history
(history_id serial primary key,
user_id int NOT NULL,
alco_name varchar(20) NOT NULL,
data_joined timestamptz NOT NULL,
review int);