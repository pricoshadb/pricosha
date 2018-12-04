-- Clear tables
DELETE FROM Person;
DELETE FROM FriendGroup;
DELETE FROM ContentItem;
DELETE FROM Posted;
DELETE FROM Tag;
DELETE FROM `Share`;
DELETE FROM Belong;
-- Insert people
INSERT INTO Person (email, password_hash, first_name, last_name)
VALUES
('AA@nyu.edu', SHA2('AA', 256), 'Ann', 'Anderson'),
('BB@nyu.edu', SHA2('BB', 256), 'Bob', 'Baker'),
('CC@nyu.edu', SHA2('CC', 256), 'Cathy', 'Chang'),
('DD@nyu.edu', SHA2('DD', 256), 'David', 'Davidson'),
('EE@nyu.edu', SHA2('EE', 256), 'Ellen', 'Ellenberg'),
('FF@nyu.edu', SHA2('FF', 256), 'Fred', 'Fox'),
('GG@nyu.edu', SHA2('GG', 256), 'Gina', 'Gupta'),
('HH@nyu.edu', SHA2('HH', 256), 'Helen', 'Harper');

INSERT INTO FriendGroup(fg_name, email, description)
VALUES('family', 'AA@nyu.edu', 'Ann, Cathy, David, and Ellen');

INSERT INTO Belong(email_owner, email_member, fg_name)
VALUES
('AA@nyu.edu', 'AA@nyu.edu', 'family'),
('AA@nyu.edu', 'CC@nyu.edu', 'family'),
('AA@nyu.edu', 'DD@nyu.edu', 'family'),
('AA@nyu.edu', 'EE@nyu.edu', 'family');

-- Bob owns FriendGroup called “family” with users Bob, Fred, and Ellen.

INSERT INTO FriendGroup(fg_name, email, description)
VALUES('family', 'BB@nyu.edu', 'Bob, Fred, and Ellen');

INSERT INTO Belong(email_owner, email_member, fg_name)
VALUES
('BB@nyu.edu', 'BB@nyu.edu', 'family'),
('BB@nyu.edu', 'FF@nyu.edu', 'family'),
('BB@nyu.edu', 'EE@nyu.edu', 'family');

-- Ann owns FriendGroup called “roommates” with users Ann, Gina, and Helen.

INSERT INTO FriendGroup(fg_name, email, description)
VALUES('roommates', 'AA@nyu.edu', 'Ann, Gina, and Helen');

INSERT INTO Belong(email_owner, email_member, fg_name)
VALUES
('AA@nyu.edu', 'AA@nyu.edu', 'roommates'),
('AA@nyu.edu', 'GG@nyu.edu', 'roommates'),
('AA@nyu.edu', 'HH@nyu.edu', 'roommates');

-- Ann posted a content item with item_ID=1, item_name = “Whiskers”, is pub = False, and shared it with her “family” FriendGroup.

INSERT INTO ContentItem(item_id, email, item_name, is_pub, file_path)
VALUES
(1, 'AA@nyu.edu', 'Whiskers', False, NULL);

INSERT INTO `Share`(email, fg_name, item_id)
VALUES('AA@nyu.edu', 'family',1);
-- Ann posted a content item with item_ID=2, item_name = “leftovers in fridge”, is pub = False, and shared it with her “roommates” FriendGroup.

INSERT INTO ContentItem(item_id, email, post_time, item_name, is_pub, file_path)
VALUES
(2, 'AA@nyu.edu', NOW(), 'leftovers in fridge', False, NULL);

INSERT INTO `Share`(email, fg_name, item_id)
VALUES('AA@nyu.edu', 'roommates', 2);

-- Bob posted a content item with item_ID=3, item_name = “Rover”, is pub = False, and shared it with his “family” FriendGroup.

INSERT INTO ContentItem(item_id, email, post_time, item_name, is_pub, file_path)
VALUES
(3, 'BB@nyu.edu', NOW(), 'Rover', False, NULL);

INSERT INTO Share(email, fg_name, item_id)
VALUES('BB@nyu.edu', 'family', 3);


