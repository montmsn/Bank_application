
SET GLOBAL event_scheduler = ON;

ALTER EVENT set_otp_null
ON SCHEDULE EVERY 2 MINUTE -- Adjust the interval as needed
DO
  UPDATE card SET otp = NULL;