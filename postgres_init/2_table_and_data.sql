\connect foo
CREATE TABLE bar (group_id int, name text);
INSERT INTO bar (group_id, name) VALUES
  (1, 'one'),
  (2, 'two'),
  (3, 'three'),
  (4, 'four'),
  (5, 'five')
;
ALTER TABLE bar OWNER TO foo;

