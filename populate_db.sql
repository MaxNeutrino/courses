INSERT INTO users(name, email, phone, mobile_phone, status) VALUES
  ('Fitz', 'firz@gmail.com', '111111111', '010101010101', TRUE),
  ('Bender', 'bender@gmail.com', '222222222', '0202020202', TRUE),
  ('Fibi', 'fibi@gmail.com', '333333333', '0303030303', TRUE),
  ('Sheldon', 'sheldon@gmail.com', '444444444', '0404040404', TRUE),
  ('Freddy', 'freddy@gmail.com', '555555555', '0505050505', TRUE);


INSERT INTO courses(name, code) VALUES
  ('Python beginner', 'qwerty'),
  ('Python advanced', 'ytrewq'),
  ('MySQL', '14253654'),
  ('Front-End for dummies', 'sda42313'),
  ('Reactive programming', 'fds45aas'),
  ('MongoDB', 'fds45315as'),
  ('Linux', 'fghff65153a'),
  ('Java beginner', 'fds533315as'),
  ('Spring 5(IoC, Data, WebFlux, Security)', 'fds5131aa'),
  ('Algorithms', '4531asda351');

INSERT INTO user_courses(user_id, course_id) VALUES
  (1000, 1000),
  (1000, 1001),
  (1000, 1002),
  (1000, 1003),
  (1001, 1007),
  (1001, 1008)