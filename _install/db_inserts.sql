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

