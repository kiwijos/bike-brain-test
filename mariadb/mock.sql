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
    `id` VARCHAR(6) NOT NULL,
    `city_id` VARCHAR(10) NOT NULL,
    `status_id` INT NOT NULL,
    `geometry` VARCHAR(150) NOT NULL,

    PRIMARY KEY (`id`)
);

INSERT INTO `bike`
    (`id`, `city_id`, `status_id`, `geometry`)
VALUES
    ('GOGOGO', 2, 1, '[18.02393, 59.33854]')
;
