-- string function

-- concat()
SELECT concat('my sql ', 'language ', 'is ', null, 'posgresql.');

-- position()
SELECT position('postgresql' in 'my sql language is postgresql.');

-- replace()
SELECT replace('my sql language is postgresql.', 'postgre', 'not My');