DELIMITER //

CREATE PROCEDURE `db_project`.`loan_payments` (
  in_LID INT
)
BEGIN
  SELECT
    `payID`,
    `LID`,
    `payment_amount`,
    `settled`
  FROM
    `db_project`.`loan_payment`
  WHERE
    `LID` = in_LID;
END //

DELIMITER ;
