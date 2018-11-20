CREATE TABLE account
(user_id serial primary key,
user_name varchar(30) NOT NULL,
email text NOT NULL,
password text NOT NULL,
last_login timestamptz NOT NULL);