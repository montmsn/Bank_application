CREATE SCHEMA `db_project` ;


CREATE TABLE `db_project`.`bank_user` (
  `UID` INT NOT NULL,
  `last_anme` VARCHAR(45) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `phone_number` VARCHAR(20) NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  UNIQUE INDEX `UID_UNIQUE` (`UID` ASC) VISIBLE,
  PRIMARY KEY (`UID`));

CREATE TABLE `db_project`.`card` (
  `card_number` VARCHAR(16) NOT NULL,
  `expire_date` DATE NOT NULL,
  `cvv2` INT NOT NULL,
  PRIMARY KEY (`card_number`),
  UNIQUE INDEX `card_number_UNIQUE` (`card_number` ASC) VISIBLE);

CREATE TABLE `db_project`.`bank_account` (
  `ACCID` INT NOT NULL,
  `UID` INT NOT NULL,
  `card_number` VARCHAR(16) NOT NULL,
  `balance` INT NOT NULL,
  PRIMARY KEY (`ACCID`),
  INDEX `UID_idx` (`UID` ASC) VISIBLE,
  INDEX `card_number_idx` (`card_number` ASC) VISIBLE,
  CONSTRAINT `UID`
    FOREIGN KEY (`UID`)
    REFERENCES `db_project`.`bank_user` (`UID`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `card_number`
    FOREIGN KEY (`card_number`)
    REFERENCES `db_project`.`card` (`card_number`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

CREATE TABLE `db_project`.`transaction` (
  `TID` INT NOT NULL,
  `date` DATE NOT NULL,
  `amount` INT NOT NULL,
  `sender` VARCHAR(16) NOT NULL,
  `reciever` VARCHAR(16) NOT NULL,
  `explain` TEXT NULL,
  `success` BINARY(1) NOT NULL,
  PRIMARY KEY (`TID`),
  INDEX `sender_idx` (`sender` ASC) VISIBLE,
  INDEX `reciever_idx` (`reciever` ASC) VISIBLE,
  UNIQUE INDEX `TID_UNIQUE` (`TID` ASC) VISIBLE,
  CONSTRAINT `sender`
    FOREIGN KEY (`sender`)
    REFERENCES `db_project`.`bank_account` (`card_number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `reciever`
    FOREIGN KEY (`reciever`)
    REFERENCES `db_project`.`bank_account` (`card_number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `db_project`.`loan` (
  `LID` INT NOT NULL,
  `ACCID` INT NOT NULL,
  `loan_score` INT NOT NULL,
  `loan_interest` INT NOT NULL,
  `settled` BINARY(1) NOT NULL,
  PRIMARY KEY (`LID`),
  INDEX `ACCID_idx` (`ACCID` ASC) VISIBLE,
  CONSTRAINT `ACCID`
    FOREIGN KEY (`ACCID`)
    REFERENCES `db_project`.`bank_account` (`ACCID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `db_project`.`loan_payment` (
  `payID` INT NOT NULL,
  `LID` INT NOT NULL,
  `payment_amount` INT NOT NULL,
  `settled` BINARY(1) NOT NULL,
  PRIMARY KEY (`payID`),
  UNIQUE INDEX `payID_UNIQUE` (`payID` ASC) VISIBLE,
  INDEX `LID_idx` (`LID` ASC) VISIBLE,
  CONSTRAINT `LID`
    FOREIGN KEY (`LID`)
    REFERENCES `db_project`.`loan` (`LID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


ALTER TABLE `db_project`.`bank_account` 
ADD COLUMN `suspended` BINARY(1) NOT NULL DEFAULT 0 AFTER `balance`;

ALTER TABLE `db_project`.`bank_user` 
ADD COLUMN `is_admin` BINARY(1) NOT NULL DEFAULT 0 AFTER `password`;

ALTER TABLE `db_project`.`card` 
ADD COLUMN `OTP` INT NULL DEFAULT NULL AFTER `cvv2`;

ALTER TABLE `db_project`.`bank_user` 
ADD UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE;

