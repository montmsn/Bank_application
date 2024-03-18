DELIMITER //

CREATE FUNCTION `db_project`.`calculate_loan_score` (
  in_ACCID INT
)
RETURNS INT
READS SQL DATA
BEGIN
  DECLARE min_balance INT;

  SELECT MIN(`balance`) INTO min_balance
  FROM (
    SELECT `balance`
    FROM `db_project`.`bank_account`
    WHERE `ACCID` = in_ACCID

    UNION ALL

    SELECT 
      CASE
        WHEN sender = (SELECT `card_number` FROM `db_project`.`bank_account` WHERE `ACCID` = in_ACCID) THEN
          (SELECT `balance` FROM `db_project`.`bank_account` WHERE `card_number` = reciever) - amount
        WHEN reciever = (SELECT `card_number` FROM `db_project`.`bank_account` WHERE `ACCID` = in_ACCID) THEN
          (SELECT `balance` FROM `db_project`.`bank_account` WHERE `card_number` = sender) + amount
      END AS `balance`
    FROM `db_project`.`transaction`
    WHERE (sender = (SELECT `card_number` FROM `db_project`.`bank_account` WHERE `ACCID` = in_ACCID)
           OR reciever = (SELECT `card_number` FROM `db_project`.`bank_account` WHERE `ACCID` = in_ACCID))
      AND `date` BETWEEN DATE_SUB(NOW(), INTERVAL 2 MONTH) AND NOW()
  ) AS subquery;

  RETURN COALESCE(min_balance, 0); 
END //

DELIMITER ;
