#insert into bank_user(UID,last_anme,first_name,email,phone_number,username,password) values 
#(1071071077,'Hazard','Eden','e_hazard@gmail.com','09127777777','hazard','injury');
#insert into card(card_number,expire_date,cvv2) values ('6037603760371077','2025-12-31',123);
#insert into bank_account(ACCID,UID,card_number,balance) values (5,1071071077,'6037603760371077',10000000);
# insert into card(card_number,expire_date,cvv2) values ('6037603760371111','2025-11-11',122);
# insert into bank_account(ACCID,UID,card_number,balance) values (2,1111111111,'6037603760371111',10000);
-- insert into transaction(TID,date,amount,sender,reciever,success) values 
-- (1,'2023-11-11',10000,'6037603760376037','6037603760371111',1)
-- ,(2,'2022-10-11',10000,'6037603760371111','6037603760376037',1)
-- ,(3,'2022-11-11',10000,'6037603760376037','6037603760371111',1)
-- ,(4,'2023-9-11',10000,'6037603760376037','6037603760371111',1);
# insert into card(card_number,expire_date,cvv2) values ('1111222233334444','2026-11-12',225);
# insert into bank_account(ACCID,UID,card_number,balance) values (3,1111111112,'1111222233334444',20000);
-- insert into transaction(TID,date,amount,sender,reciever,success) values 
-- (5,'2019-11-11',14000,'1111222233334444','6037603760371111',1)bank_account
# insert into card(card_number,expire_date,cvv2) values ('1212121211111112','2025-12-10',547);
# insert into bank_account(ACCID,UID,card_number,balance) values (4,1111111112,'1212121211111112',23400);
# SELECT MIN(LID) FROM `db_project`.`loan`;
#delete from loan;