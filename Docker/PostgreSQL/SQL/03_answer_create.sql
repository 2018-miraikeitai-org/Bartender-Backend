CREATE TABLE IF NOT EXISTS answer(
    answer_id	    int	    NOT NULL,
    user_id	        int	    REFERENCES account(user_id),
    option_data	    text[],
    learning_data	text[],
    PRIMARY KEY(answer_id, user_id)
);