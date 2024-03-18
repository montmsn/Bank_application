DELIMITER //

CREATE PROCEDURE `db_project`.`get_user_loans` (
  in_UID INT
)
BEGIN
 # SELECT 
#    l.*
 # FROM  
#    (	select ba.* 
#		from
#		`db_project`.`bank_user` as bu
#		JOIN 
#		`db_project`.`bank_account` as ba ON bu.`UID` = ba.`UID`
#       WHERE 
#		bu.`UID` = in_UID
#    ) as a
#  JOIN 
 #   `db_project`.`loan` as l on l.`ACCID`=a.`ACCID`;
  select * from loan
  where loan.ACCID in (select ACCID from bank_account where UID=in_UID);

END //

DELIMITER ;
