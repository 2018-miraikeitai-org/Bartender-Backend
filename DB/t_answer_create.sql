CREATE TABLE answer
(answer_id	int	NOT NULL,
user_id	int	REFERENCES account(user_id),
ques_id	int REFERENCES question(ques_id),
learning_data	varchar[],
PRIMARY KEY(answer_id, user_id, ques_id));