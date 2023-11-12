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
    ('GOGOGO', 2, 1, '...'),
    ('REG123', 2, 1, '...'),
    ('123REG', 2, 1, '...'),
    ('HEJHEJ', 2, 1, '...'),
    ('TEST12', 2, 1, '...')
;
