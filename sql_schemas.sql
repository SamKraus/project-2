CREATE TABLE superbowl (
	SB TEXT PRIMARY KEY,
	Attendance INT,
	Winner TEXT,
	Winning_Pts INT,
	Loser TEXT,
	Losing_Pts INT,
	MVP TEXT,
	Stadium TEXT,
	City_State TEXT
);

CREATE TABLE uscities (
	City_State TEXT,
	Lat INT,
	Lng INT
);

select * from superbowl;

select * from uscities;

SELECT Book.name, Price.price 
FROM Book
FULL OUTER JOIN Price 
ON Book.id = Price.id;

SELECT  superbowl.sb, superbowl.attendance, superbowl.winner,
superbowl.winning_pts, superbowl.loser, superbowl.losing_pts,
superbowl.mvp, superbowl.stadium, superbowl.city_state,
uscities.lat, uscities.lng
FROM superbowl
FULL OUTER JOIN uscities
ON superbowl.city_state=uscities.city_state;

CREATE VIEW combined_tables AS
SELECT  superbowl.sb, superbowl.attendance, superbowl.winner,
superbowl.winning_pts, superbowl.loser, superbowl.losing_pts,
superbowl.mvp, superbowl.stadium, superbowl.city_state,
uscities.lat, uscities.lng
FROM superbowl
FULL OUTER JOIN uscities
ON superbowl.city_state=uscities.city_state;

select * from combined_tables;