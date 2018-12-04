
-- Insert some users
INSERT INTO Person(email, password_hash, first_name, last_name) values('andrewhu@nyu.edu', SHA2('password', 256), 'Andrew', 'Hu')

-- Insert some public items
INSERT INTO ContentItem(email, post_time, item_name, is_pub, file_path) values('andrewhu@nyu.edu', NOW(), 'test public post', True, NULL);