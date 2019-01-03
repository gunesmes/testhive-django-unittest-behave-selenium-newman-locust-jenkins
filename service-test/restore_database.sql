
# * * * * * *   RESTORE DATA STARTED  * * * * * *

# DELETE ALL THE RECORDS IN THE FOLLOWING TABLE
TRUNCATE src_users CASCADE;
ALTER SEQUENCE src_users_id_seq RESTART WITH 1


# ADD TWO TEST USER TO src_users
INSERT INTO src_users ("username","email","address","birthday") VALUES('testusername1','test1@test.com','Turkey İstanbul Bakırköy 344252','2001-09-03');
INSERT INTO src_users ("username","email","address","birthday") VALUES('testusername2','test2@test.com','Studio 103 Wellfield Road Roath Cardiff','2000-09-03');


# * * * * * *   RESTORE DATA FINISHED  * * * * * *