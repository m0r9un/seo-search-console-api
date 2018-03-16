# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: iskevych.lun.in.ua (MySQL 5.7.21-20)
# Database: sc
# Generation Time: 2018-03-16 10:46:53 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

# Dump of table category_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `category_data`;

CREATE TABLE `category_data` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(255) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AVG_ROW_LENGTH=152;

LOCK TABLES `category_data` WRITE;
/*!40000 ALTER TABLE `category_data` DISABLE KEYS */;

INSERT INTO `category_data` (`category_id`, `category_name`)
VALUES
	(1,'Default 1'),
	(2,'Default 2'),
	(3,'Default 3'),
	(4,'Default 4');

/*!40000 ALTER TABLE `category_data` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table search_console_calendar
# ------------------------------------------------------------

DROP TABLE IF EXISTS `search_console_calendar`;

CREATE TABLE `search_console_calendar` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` enum('not downloaded','downloaded','expired') DEFAULT NULL,
  PRIMARY KEY (`id`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AVG_ROW_LENGTH=84;

LOCK TABLES `search_console_calendar` WRITE;
/*!40000 ALTER TABLE `search_console_calendar` DISABLE KEYS */;

INSERT INTO `search_console_calendar` (`id`, `date`, `status`)
VALUES
	(1,'2017-03-16','not downloaded'),
	(2,'2017-03-15','not downloaded');

/*!40000 ALTER TABLE `search_console_calendar` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table search_console_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `search_console_data`;

CREATE TABLE `search_console_data` (
  `date` date NOT NULL,
  `url` varchar(255) NOT NULL,
  `query` varchar(255) NOT NULL,
  `clicks` int(11) DEFAULT NULL,
  `impressions` int(11) DEFAULT NULL,
  `ctr` double DEFAULT NULL,
  `position` double DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`date`,`url`,`query`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AVG_ROW_LENGTH=152;

LOCK TABLES `search_console_data` WRITE;
/*!40000 ALTER TABLE `search_console_data` DISABLE KEYS */;

INSERT INTO `search_console_data` (`date`, `url`, `query`, `clicks`, `impressions`, `ctr`, `position`, `category_id`)
VALUES
	('2017-07-07','/','lehola maxima',3,6,0.5,2,4),
	('2017-07-07','/','недвижимость лун',100,200,0.5,2,1),
	('2017-07-07','/amp/anda-uurile-tuba-elva','üürikorterid elvas otse omanikult',0,1,0,8,3),
	('2017-07-07','/amp/äripindade-muuk-kulitse','rait kuusik',0,1,0,30,3),
	('2017-07-07','/amp/buroo-muuk-vageva','unikivi',0,1,0,129,4),
	('2017-07-07','/amp/kinnisvara-luige','kinnisvara',1,1,1,9,4),
	('2017-07-07','/amp/kinnisvara-muuk-haapsalu','müüa maja haapsalus',0,1,0,1,3),
	('2017-07-07','/amp/kinnisvara-muuk-valga','valga kinnisvara müük',0,1,0,6,3),
	('2017-07-07','/amp/kinnisvara-randvere','randvere terviserada',0,1,0,8,3),
	('2017-07-07','/недвижимость-одесса','недвижимость одесса',0,1,0,7,2),
	('2017-07-07','/недвижимость-одесса-недорого','недорого недвижимость одесса',3,10,0.3,5,2),
	('2017-07-07','/недвижимость-одесса-элит','дорого купить квартиру',0,1,0,11,2),
	('2017-07-07','/продажа-квартир-киев','недвижимость киева квартиры',1,4,0.25,4.75,1),
	('2017-07-10','/','недвижимость лун',150,300,0.5,4,1),
	('2017-07-10','/amp/kinnisvara-kuivastu','lvm kinnisvara',0,1,0,24,3),
	('2017-07-10','/недвижимость-одесса','недвижимость одесса',5,10,0.5,5,2),
	('2017-07-10','/недвижимость-одесса-недорого','недорого недвижимость одесса',0,1,0,20,2),
	('2017-07-10','/продажа-квартир-киев','квартира в киеве',2,4,0.5,5,1),
	('2017-07-10','/продажа-квартир-киев-недорого','недорогие квартиры',1,1,1,52,1),
	('2017-07-11','/amp/kinnisvara-luige','kinnisvara',3,6,0.5,1,4),
	('2017-07-12','/','лун',80,100,0.8,1,1),
	('2017-07-12','/','недвижимость',2,2,1,1,1),
	('2017-07-12','/продажа-квартир-глеваха','квартира в глевахе',0,0,0,1,1);

/*!40000 ALTER TABLE `search_console_data` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table search_console_property
# ------------------------------------------------------------

DROP TABLE IF EXISTS `search_console_property`;

CREATE TABLE `search_console_property` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `property_uri` varchar(255) NOT NULL,
  `service_account` varchar(255) DEFAULT NULL,
  `key_file` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`,`property_uri`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AVG_ROW_LENGTH=442;



# Dump of table site_url_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `site_url_data`;

CREATE TABLE `site_url_data` (
  `page_id` int(11) NOT NULL,
  `url` varchar(255) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`page_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AVG_ROW_LENGTH=152;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
