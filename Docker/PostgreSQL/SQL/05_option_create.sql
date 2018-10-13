CREATE TABLE IF NOT EXISTS option(
    option_id	        int	        NOT NULL,
    ques_id	            int	        REFERENCES question(ques_id),
    option_contents1	varchar(30) NOT NULL,
    option_contents2	varchar(30) NOT NULL,
    option_contents3	varchar(30),
    option_contents4	varchar(30),
    PRIMARY KEY(option_id)
);