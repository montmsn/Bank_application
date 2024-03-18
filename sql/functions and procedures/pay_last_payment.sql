DELIMITER //

CREATE PROCEDURE `db_project`.`pay_last_payment` (
  in_LID INT,
  OUT out_result VARCHAR(20)
)
BEGIN
  DECLARE not_payeds_count INT;
  DECLARE balance_amount INT;
  DECLARE acc_id_value INT;
  DECLARE avg_payment_amount INT;
  DECLARE min_not_payed_id INT;

  START TRANSACTION;

  SELECT COUNT(*) INTO not_payeds_count
  FROM `loan_payment`
  WHERE `LID` = in_LID AND `settled` = 0;

  SELECT `balance` INTO balance_amount
  FROM `bank_account`
  WHERE `ACCID` = (SELECT `ACCID` FROM `loan` WHERE `LID` = in_LID);

  SELECT `ACCID` INTO acc_id_value
  FROM `bank_account`
  WHERE `ACCID` = (SELECT `ACCID` FROM `loan` WHERE `LID` = in_LID);

  SELECT AVG(`payment_amount`) INTO avg_payment_amount
  FROM `loan_payment`
  WHERE `LID` = in_LID;

  IF not_payeds_count = 0 OR balance_amount < avg_payment_amount THEN
    SET out_result = 'unsuccessful';
  ELSE
    SELECT MIN(`payID`) INTO min_not_payed_id
    FROM `loan_payment`
    WHERE `LID` = in_LID AND `settled` = 0;

    UPDATE `loan_payment` SET `settled` = 1 WHERE `payID` = min_not_payed_id;
    UPDATE `bank_account` SET `balance` = `balance` - avg_payment_amount WHERE `ACCID` = acc_id_value;

    SET out_result = 'successful';
    
    SELECT COUNT(*) INTO not_payeds_count
	FROM `loan_payment`
	WHERE `LID` = in_LID AND `settled` = 0;
    IF not_payeds_count = 0 then
		update loan set settled=1 where 'LID'=in_LID;
    end if;
  END IF;

  IF out_result = 'successful' THEN
    COMMIT;
  ELSE
    ROLLBACK;
  END IF;
END //

DELIMITER ;
