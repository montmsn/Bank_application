DELIMITER //

CREATE FUNCTION `db_project`.`login_user` (
  in_username VARCHAR(45),
  in_password VARCHAR(45)
)
RETURNS BOOLEAN
READS SQL DATA
BEGIN
  DECLARE user_exists INT;
  
  SELECT COUNT(*) INTO user_exists
  FROM `db_project`.`bank_user`
  WHERE `username` = in_username AND `password` = in_password;
  
  RETURN user_exists > 0;
END //

DELIMITER ;
