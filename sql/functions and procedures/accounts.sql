DELIMITER //

CREATE PROCEDURE `db_project`.`get_accounts` (
  in_UID INT
)
BEGIN
  SELECT *
  FROM `db_project`.`bank_account`
  WHERE `UID` = in_UID;
END //

DELIMITER ;
