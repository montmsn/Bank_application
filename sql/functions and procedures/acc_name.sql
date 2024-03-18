DELIMITER //

CREATE FUNCTION `db_project`.`acc_name` (
  in_ACCID INT
)
RETURNS VARCHAR(100)
READS SQL DATA
BEGIN
  DECLARE full_name VARCHAR(100);

  -- Retrieve complete name for the given ACCID
  SELECT CONCAT(`first_name`, ' ', `last_anme`) INTO full_name
  FROM `db_project`.`bank_user` AS bu
  JOIN `db_project`.`bank_account` AS ba ON bu.`UID` = ba.`UID`
  WHERE ba.`ACCID` = in_ACCID;

  RETURN full_name;
END //

DELIMITER ;
