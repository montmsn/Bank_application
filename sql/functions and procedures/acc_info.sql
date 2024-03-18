DELIMITER //

CREATE PROCEDURE `db_project`.`acc_info` (
  in_UID INT
)
BEGIN
  -- Retrieve account information for the given ACCID
  SELECT 
    ba.`ACCID`, 
    ba.`UID`, 
    bu.`last_anme` AS `last_name`, 
    bu.`first_name` AS `first_name`, 
    bu.`email`, 
    bu.`phone_number`, 
    bu.`username`, 
    ba.`card_number`, 
    ba.`balance`, 
    ba.`suspended`,
    c.`expire_date`,
    c.`cvv2`
  FROM 
    `db_project`.`bank_account` AS ba
  JOIN 
    `db_project`.`bank_user` AS bu
  ON 
    ba.`UID` = bu.`UID`
  join `db_project`.`card` as c
  on
	c.`card_number` = ba.`card_number`
  WHERE 
    ba.`UID` = in_UID;
END //

DELIMITER ;
