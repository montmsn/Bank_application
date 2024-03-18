DELIMITER //

CREATE PROCEDURE `db_project`.`suspend_acc` (
  in_ACCID INT
)
BEGIN
  -- Suspend the account by setting the 'suspended' flag to 1
  UPDATE `db_project`.`bank_account`
  SET `suspended` = 1
  WHERE `ACCID` = in_ACCID;
END //

DELIMITER ;
