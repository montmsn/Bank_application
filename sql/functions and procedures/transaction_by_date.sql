DELIMITER //

CREATE PROCEDURE `db_project`.`transaction_by_date` (
  in_ACCID INT,
  in_start_date DATE,
  in_end_date DATE
)
BEGIN
  SELECT *
  FROM `db_project`.`transaction`
  WHERE (`sender` = (SELECT `card_number` FROM `db_project`.`bank_account` WHERE `ACCID` = in_ACCID)
         OR `reciever` = (SELECT `card_number` FROM `db_project`.`bank_account` WHERE `ACCID` = in_ACCID))
    AND `date` BETWEEN in_start_date AND in_end_date
  ORDER BY `date` DESC;
END //

DELIMITER ;
