DELIMITER //

CREATE PROCEDURE `db_project`.`last_n_transactions` (
  in_ACCID INT,
  in_number INT
)
BEGIN
  SELECT *
  FROM `db_project`.`transaction`
  WHERE `sender` = (SELECT `card_number` FROM `db_project`.`bank_account` WHERE `ACCID` = in_ACCID)
     OR `reciever` = (SELECT `card_number` FROM `db_project`.`bank_account` WHERE `ACCID` = in_ACCID)
  ORDER BY `date` DESC
  LIMIT in_number;
END //

DELIMITER ;
