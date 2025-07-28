  CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        );

 INSERT INTO users (name, email) values
 ('itay', 'itay@gmail.com'),
 ('rina', 'rina@walla.co.il');

 UPDATE users
 set name='rina', email='rina@walla.com'
 where name='rina';

 DELETE from users
 where id = 3;