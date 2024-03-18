DELIMITER //

CREATE PROCEDURE `db_project`.`change_password` (
  in_UID INT,
  in_previous_password VARCHAR(45),
  in_new_password VARCHAR(45)
)
BEGIN
  DECLARE user_exists INT;

  # is user valid:
  SELECT COUNT(*) INTO user_exists
  FROM `db_project`.`bank_user`
  WHERE `UID` = in_UID AND `password` = in_previous_password;

  # change:
  IF user_exists > 0 THEN
    UPDATE `db_project`.`bank_user`
    SET `password` = in_new_password
    WHERE `UID` = in_UID;
    
    SELECT 'successfull' AS `result`; # succesfull
  ELSE
    SELECT 'not successfull' AS `result`; # not changed
  END IF;
END //

DELIMITER ;
