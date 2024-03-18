DELIMITER //

CREATE PROCEDURE `db_project`.`do_transaction` (
  in_source_account VARCHAR(16),
  in_destination_account VARCHAR(16),
  in_amount INT,
  OUT out_result VARCHAR(20)
)
BEGIN
  DECLARE source_balance INT;
  DECLARE destination_balance INT;
  DECLARE success BOOLEAN DEFAULT FALSE;

  START TRANSACTION;

  -- current_balances:
  SELECT `balance` INTO source_balance
  FROM `db_project`.`bank_account`
  WHERE `card_number` = in_source_account;

  SELECT `balance` INTO destination_balance
  FROM `db_project`.`bank_account`
  WHERE `card_number` = in_destination_account;

  -- enough balance at sender:
  IF source_balance >= in_amount THEN
    -- update:
    UPDATE `db_project`.`bank_account`
    SET `balance` = source_balance - in_amount
    WHERE `card_number` = in_source_account;

    UPDATE `db_project`.`bank_account`
    SET `balance` = destination_balance + in_amount
    WHERE `card_number` = in_destination_account;

    SET success = TRUE;
    SET out_result = 'successful';

  
    INSERT INTO `transaction` (TID, date, amount, sender, reciever, success)
    SELECT (SELECT MAX(TID) + 1 FROM `transaction`), NOW(), in_amount, in_source_account, in_destination_account, 1;
  ELSE
 
        INSERT INTO `transaction` (TID, date, amount, sender, reciever, success)
    SELECT (SELECT MAX(TID) + 1 FROM `transaction`), NOW(), in_amount, in_source_account, in_destination_account, 0;

    SET out_result = 'unsuccessful';
  END IF;


  IF success THEN
    COMMIT;
  ELSE
    ROLLBACK;
  END IF;
END //

DELIMITER ;

