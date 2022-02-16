Modelo EER do banco Mysql (workbench) 
![image](https://user-images.githubusercontent.com/74442630/154342417-b41ccec1-4488-4fee-811c-63f65309d9a4.png)

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`perguntas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`perguntas` (
  `idperguntas` INT NOT NULL AUTO_INCREMENT,
  `conteudo_pergunta` VARCHAR(200) NULL,
  PRIMARY KEY (`idperguntas`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = cp1256;


-- -----------------------------------------------------
-- Table `mydb`.`alternativas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`alternativas` (
  `idalternativas` INT NOT NULL AUTO_INCREMENT,
  `conteudo_alternativa` VARCHAR(45) NULL,
  `resposta_certa` VARCHAR(45) NULL,
  `perguntas_idperguntas` INT NOT NULL,
  PRIMARY KEY (`idalternativas`),
  INDEX `fk_alternativas_perguntas_idx` (`perguntas_idperguntas` ASC) VISIBLE,
  CONSTRAINT `fk_alternativas_perguntas`
    FOREIGN KEY (`perguntas_idperguntas`)
    REFERENCES `mydb`.`perguntas` (`idperguntas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


