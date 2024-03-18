DELIMITER //

CREATE PROCEDURE `db_project`.`unsuspend_acc` (
  in_ACCID INT
)
BEGIN
  -- Suspend the account by setting the 'suspended' flag to 1
  UPDATE `db_project`.`bank_account`
  SET `suspended` = 0
  WHERE `ACCID` = in_ACCID;
END //

DELIMITER ;
