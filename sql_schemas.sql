CREATE TABLE superbowl (
	SB TEXT PRIMARY KEY,
	Attendance INT,
	Winner TEXT,
	Winning_Pts INT,
	Loser TEXT,
	Losing_Pts INT,
	MVP TEXT,
	Stadium TEXT,
	City_State TEXT,
	Lat FLOAT,
	Lng FLOAT
);

select * from superbowl;