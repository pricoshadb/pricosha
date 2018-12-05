CREATE TABLE IF NOT EXISTS  `Person`(
   email VARCHAR(50) PRIMARY KEY,
   password_hash CHAR(64) NOT NULL,
   first_name VARCHAR(20) NOT NULL,
   last_name VARCHAR(20) NOT NULL,
   avatar VARCHAR(256));
CREATE TABLE IF NOT EXISTS  FriendGroup(
   fg_name VARCHAR(20),
   email VARCHAR(50),
   description VARCHAR(256),
   PRIMARY KEY(fg_name, email),
   FOREIGN KEY (email) REFERENCES Person(email) ON DELETE CASCADE);
CREATE TABLE IF NOT EXISTS  ContentItem(
   item_id INT PRIMARY KEY AUTO_INCREMENT,
   email VARCHAR(50),
   post_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
   item_name VARCHAR(24) NOT NULL,
   is_pub BOOL NOT NULL,
   file_path VARCHAR(128),
   FOREIGN KEY (email) REFERENCES Person(email) ON DELETE SET NULL);
CREATE TABLE IF NOT EXISTS Comments(
    item_id INT NOT NULL,
    email VARCHAR(50),
    post_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    content VARCHAR(2048),
    FOREIGN KEY(email) REFERENCES Person(email) ON DELETE SET NULL,
    FOREIGN KEY(item_id) REFERENCES ContentItem(item_id) ON DELETE CASCADE);
CREATE TABLE IF NOT EXISTS  Posted(
   email VARCHAR(50),
   item_id INT,
   rate_time DATETIME NOT NULL,
   emoji VARCHAR(1),
   PRIMARY KEY (email, item_id),
   FOREIGN KEY (email) REFERENCES Person(email) ON DELETE CASCADE ,
   FOREIGN KEY (item_id) REFERENCES ContentItem(item_id) ON DELETE CASCADE);
CREATE TABLE IF NOT EXISTS  Tag(
   email_tagger VARCHAR(50),
   email_tagged VARCHAR(50),
   item_id INT,
   tag_time DATETIME NOT NULL,
   status TINYINT,
   PRIMARY KEY (email_tagger, email_tagged, item_id),
   FOREIGN KEY (email_tagger) REFERENCES Person(email) ON DELETE CASCADE,
   FOREIGN KEY (email_tagged) REFERENCES Person(email) ON DELETE CASCADE,
   FOREIGN KEY (item_id) REFERENCES ContentItem(item_id) ON DELETE CASCADE);
CREATE TABLE IF NOT EXISTS  `Share`(
   email VARCHAR(50),
   fg_name VARCHAR(20),
   item_id INT,
   PRIMARY KEY (email, fg_name, item_id),
   FOREIGN KEY (email, fg_name) REFERENCES FriendGroup(email,fg_name) ON DELETE CASCADE,
   FOREIGN KEY (item_id) REFERENCES ContentItem(item_id) ON DELETE CASCADE);
CREATE TABLE IF NOT EXISTS  Belong(
   email_owner VARCHAR(50),
   email_member VARCHAR(50),
   fg_name VARCHAR(20),
   PRIMARY KEY (email_owner, email_member, fg_name),
   FOREIGN KEY (email_owner, fg_name) REFERENCES FriendGroup(email, fg_name) ON DELETE CASCADE,
   FOREIGN KEY (email_member) REFERENCES Person(email) ON DELETE CASCADE);
CREATE TABLE IF NOT EXISTS Saved (
    email VARCHAR(50),
    item_id INT,
    save_time DATETIME NOT NULL,
    FOREIGN KEY (email) REFERENCES Person(email),
    FOREIGN KEY (item_id) REFERENCES ContentItem(item_id)
)
