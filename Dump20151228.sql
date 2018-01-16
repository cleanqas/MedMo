-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: medmo
-- ------------------------------------------------------
-- Server version	5.7.9-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `campaigndetails`
--

DROP TABLE IF EXISTS `campaigndetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `campaigndetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campaign_id` int(11) DEFAULT NULL,
  `station_id` int(11) DEFAULT NULL,
  `schedule_dates` varchar(750) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_CampaignDetails_campaign_id` (`campaign_id`),
  KEY `ix_CampaignDetails_station_id` (`station_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaigndetails`
--

LOCK TABLES `campaigndetails` WRITE;
/*!40000 ALTER TABLE `campaigndetails` DISABLE KEYS */;
INSERT INTO `campaigndetails` VALUES (1,1,1,'24-12-2015, 25-12-2015'),(2,1,2,'24-12-2015, 25-12-2015'),(3,2,1,'24-12-2015, 27-12-2015'),(4,3,1,'25-12-2015'),(8,1,3,'12-02-2016, 06-07-2013'),(9,7,1,'29-12-2015,30-12-2015,31-12-2015,01-01-2016,02-01-2016,03-01-2016'),(10,7,2,'29-12-2015, 30-12-2015, 31-12-2015, 10-01-2016, 11-01-2016, 12-01-2016, 13-01-2016, 14-02-2016, 15-02-2016, 16-02-2016, 17-02-2016, 12-04-2016');
/*!40000 ALTER TABLE `campaigndetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campaigns`
--

DROP TABLE IF EXISTS `campaigns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `campaigns` (
  `campaign_id` int(11) NOT NULL AUTO_INCREMENT,
  `createdby_user_id` int(11) DEFAULT NULL,
  `product` varchar(120) DEFAULT NULL,
  `campaign_name` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`campaign_id`),
  KEY `ix_Campaigns_createdby_user_id` (`createdby_user_id`),
  KEY `ix_Campaigns_product` (`product`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campaigns`
--

LOCK TABLES `campaigns` WRITE;
/*!40000 ALTER TABLE `campaigns` DISABLE KEYS */;
INSERT INTO `campaigns` VALUES (1,1,'Mamador','Xmas Give Away'),(2,1,'Chivta','100% Juice'),(3,1,'CloseUp','Get Closed Up'),(4,1,'Konga','konga.com'),(6,1,'Javago','Hotels'),(7,1,'Carlo Rossi','midnight blue');
/*!40000 ALTER TABLE `campaigns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `companies` (
  `company_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(120) DEFAULT NULL,
  `company_address` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
INSERT INTO `companies` VALUES (1,'Media Perspective','Ikeja'),(2,'MediaReach OMD','Ikeja');
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stations`
--

DROP TABLE IF EXISTS `stations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stations` (
  `station_id` int(11) NOT NULL AUTO_INCREMENT,
  `station_name` varchar(120) DEFAULT NULL,
  `station_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`station_id`),
  KEY `ix_Stations_station_type_id` (`station_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stations`
--

LOCK TABLES `stations` WRITE;
/*!40000 ALTER TABLE `stations` DISABLE KEYS */;
INSERT INTO `stations` VALUES (1,'NTA Network',1),(2,'Cool FM',2),(3,'AIT',1);
/*!40000 ALTER TABLE `stations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stationtypes`
--

DROP TABLE IF EXISTS `stationtypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stationtypes` (
  `station_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `station_type_desc` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`station_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stationtypes`
--

LOCK TABLES `stationtypes` WRITE;
/*!40000 ALTER TABLE `stationtypes` DISABLE KEYS */;
INSERT INTO `stationtypes` VALUES (1,'Local Station'),(2,'Radio'),(3,'DSTV');
/*!40000 ALTER TABLE `stationtypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(120) DEFAULT NULL,
  `email` varchar(120) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `registered_on` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `ix_Users_username` (`username`),
  UNIQUE KEY `ix_Users_email` (`email`),
  KEY `ix_Users_company_id` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'qasimokuneye','qasim.okuneye@gmail.com','python01',1,'2015-12-24 00:00:00'),(2,'mariam','abolanle.kassim@gmail.com','python01',1,'2015-12-26 00:00:00');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-12-28 22:41:56
