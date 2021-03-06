-- MySQL dump 10.13  Distrib 5.5.55, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ip_pool
-- ------------------------------------------------------
-- Server version	5.5.55-0ubuntu0.14.04.1

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
-- Table structure for table `ip_pool`
--

DROP TABLE IF EXISTS `ip_pool`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ip_pool` (
  `ip` varchar(25) NOT NULL,
  `origin` varchar(100) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `failed_count` int(11) DEFAULT NULL,
  `response_speed` int(11) DEFAULT NULL,
  `validity` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip_pool`
--

LOCK TABLES `ip_pool` WRITE;
/*!40000 ALTER TABLE `ip_pool` DISABLE KEYS */;
INSERT INTO `ip_pool` VALUES ('221.201.81.248:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:47',0,4579,1),('122.72.32.73:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('113.128.105.53:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('144.255.233.100:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('175.23.39.212:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('122.72.32.74:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('122.188.187.202:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('36.249.192.179:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('175.42.102.252:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('182.90.120.104:8123','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('110.72.32.106:8123','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('182.88.163.205:8123','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('119.135.234.155:8888','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('153.36.191.155:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('123.14.42.199:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('112.114.93.168:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('49.69.175.53:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('175.2.250.70:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('123.232.141.244:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('58.243.227.97:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('183.186.59.59:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('36.102.68.88:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('115.212.243.17:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('182.90.191.77:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('122.235.154.46:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('119.5.177.144:6979','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('119.5.177.4:6979','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('58.243.226.33:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('223.240.239.37:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('125.122.171.142:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('175.165.106.106:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('175.154.80.110:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('119.35.150.25:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('1.85.135.194:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('119.50.15.36:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('114.226.174.151:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('117.90.64.177:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('27.185.48.167:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('61.160.6.158:81','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('49.81.122.165:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('123.8.42.134:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('110.73.9.85:8123','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('182.90.20.155:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('112.227.85.55:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('1.87.211.197:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('113.121.145.220:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('219.159.89.28:8998','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('182.122.244.176:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('42.4.215.69:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('27.202.113.168:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('27.152.54.56:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('139.208.197.214:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('101.249.36.34:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('175.30.86.20:8998','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('175.163.91.113:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('220.161.239.75:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('113.120.131.147:8998','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('180.118.241.46:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('58.243.226.188:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('121.42.154.207:3128','xicidaili','2017-08-08 10:59:02','2017-08-08 11:04:47',1,-1,0),('180.117.101.245:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:04:47',1,-1,0),('144.255.122.110:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:04:47',1,-1,0),('218.86.200.11:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:04:52',1,-1,0),('121.31.101.3:8123','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('60.163.130.238:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('113.121.47.126:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('42.224.117.99:8888','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('116.196.5.150:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('106.44.81.113:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('223.155.204.217:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('110.73.6.8:8123','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('183.151.41.255:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('1.26.56.203:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('182.242.172.136:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('125.37.175.233:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('112.114.94.141:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('115.215.51.74:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('112.114.94.121:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('119.114.245.28:80','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('180.118.243.228:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('112.114.97.143:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('112.114.94.231:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('115.208.82.89:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('112.114.97.51:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('112.114.99.131:8118','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('58.243.227.108:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('58.243.227.236:808','xicidaili','2017-08-08 10:59:02','2017-08-08 11:02:21',0,-1,0),('175.155.79.107:808','xicidaili','2017-08-08 10:59:03','2017-08-08 11:02:21',0,-1,0),('113.121.37.87:808','xicidaili','2017-08-08 10:59:03','2017-08-08 11:02:21',0,-1,0),('180.104.37.113:808','xicidaili','2017-08-08 10:59:03','2017-08-08 11:02:21',0,-1,0),('220.198.116.101:80','xicidaili','2017-08-08 10:59:03','2017-08-08 11:02:21',0,-1,0),('114.235.119.190:8118','xicidaili','2017-08-08 10:59:03','2017-08-08 11:02:21',0,-1,0),('110.77.88.63:80','xicidaili','2017-08-08 10:59:03','2017-08-08 11:02:21',0,-1,0),('58.243.227.187:808','xicidaili','2017-08-08 10:59:03','2017-08-08 11:02:21',0,-1,0),('182.90.20.38:80','xicidaili','2017-08-08 10:59:03','2017-08-08 11:02:21',0,-1,0);
/*!40000 ALTER TABLE `ip_pool` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-08-27  4:32:50
