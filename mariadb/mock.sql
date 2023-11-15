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
    `id` INT NOT NULL,
    `city_id` VARCHAR(10) NOT NULL,
    `status_id` INT NOT NULL,
    `geometry` VARCHAR(150) NOT NULL,

    PRIMARY KEY (`id`)
);

INSERT INTO `bike`
    (`id`, `city_id`, `status_id`, `geometry`)
VALUES
    (1, 2, 1, '...'),
    (2, 2, 1, '...'),
    (3, 2, 1, '...'),
    (4, 2, 1, '...'),
    (5, 2, 1, '...')
;
