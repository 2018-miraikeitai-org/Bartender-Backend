CREATE TABLE IF NOT EXISTS account(
    user_id	    int	NOT NULL,
    user_name	varchar(20)	NOT NULL,
    mailaddress	text NOT NULL,
    login_pw	varchar(20)	NOT NULL,
    PRIMARY KEY(user_id)
);