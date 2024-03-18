DELIMITER //

CREATE PROCEDURE `db_project`.`get_loan` (
  in_ACCID INT,
  OUT out_result VARCHAR(20)
)
BEGIN
  DECLARE loan_exists INT;
  DECLARE loan_score INT;
  DECLARE loan_interest INT;
  DECLARE new_loan_id INT;
  DECLARE new_pay_id INT;
  DECLARE i int;

  # check that if he has already a loan
  SELECT COUNT(*) INTO loan_exists
  FROM `db_project`.`loan`
  WHERE `ACCID` = in_ACCID AND `settled` = 0;

  IF loan_exists = 0 THEN
  # loan score:
    SET loan_score = (SELECT `db_project`.`calculate_loan_score`(in_ACCID));

    # loan interest
    SET loan_interest = FLOOR(0.20 * loan_score);


    SELECT max(LID) INTO new_loan_id FROM loan;
    if new_loan_id is NULL then set new_loan_id = 0; end if;
    if loan_score!=0 then
		INSERT INTO `db_project`.`loan` (LID,ACCID,loan_score,loan_interest,settled)
		VALUES (new_loan_id+1, in_ACCID, loan_score, loan_interest, 0);

		SET out_result = 'successful';
	else 
		SET out_result = 'unsuccessful';
    end if;
    
    if loan_score!=0 then
		set i =1;
		WHILE i<13 DO 
			SELECT max(payID) INTO new_pay_id FROM `db_project`.`loan_payment`;
			if new_pay_id is NULL then set new_pay_id = 1; else set new_pay_id=new_pay_id+1; end if;
			insert into loan_payment(payID,LID,payment_amount,settled) values(new_pay_id,new_loan_id+1,(loan_score+loan_interest)/12,0);
			set i = i+1;
		END WHILE;
    end if;
    
    
  ELSE
    SET out_result = 'unsuccessful';
  END IF;
END //

DELIMITER ;
