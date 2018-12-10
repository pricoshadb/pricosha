
-- Insert some users
INSERT INTO Person(email, password_hash, first_name, last_name) values('andrewhu@nyu.edu', SHA2('password', 256), 'Andrew', 'Hu');

-- Insert some public items
INSERT INTO ContentItem(email, post_time, item_name, is_pub) values('andrewhu@nyu.edu', NOW(), 'test public post', true);

-- Insert duplicate users
INSERT INTO Person(email, password_hash, first_name, last_name) VALUES ('AA2@nyu.edu', SHA2('AA2',256), 'Ann', 'Anderson');

-- Create profile
INSERT INTO Profile(email,bio) VALUES ('AA@nyu.edu', 'Welcome to my profile');