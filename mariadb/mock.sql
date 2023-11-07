--
-- SETUP
--
DROP DATABASE IF EXISTS `test`;
CREATE DATABASE `test`;
USE `test`;

--
-- DDL
--

DROP TABLE IF EXISTS `bike`;

CREATE TABLE `bike`(
    `id` INT NOT NULL AUTO_INCREMENT,
    `city_id` VARCHAR(10) NOT NULL,
    `geometry` VARCHAR(100) NOT NULL,

    PRIMARY KEY (`id`)
);
