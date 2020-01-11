-- Create Table
CREATE TABLE superbowl (
	SB TEXT PRIMARY KEY,
	Attendance INT,
	Winner TEXT,
	Winning_Pts INT,
	Loser TEXT,
	Losing_Pts INT,
	MVP TEXT,
	Stadium TEXT,
	City TEXT,
	State TEXT
);



select * from superbowl;


DELETE from superbowl;