-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: db_recruitment
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_candidate_resume`
--

DROP TABLE IF EXISTS `tbl_candidate_resume`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_candidate_resume` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Candidate_Name` varchar(70) NOT NULL,
  `Contact_Email` varchar(100) DEFAULT NULL,
  `Contact_phone` varchar(20) DEFAULT NULL,
  `Work_Experience` float DEFAULT NULL,
  `Skill_Set` varchar(1000) DEFAULT NULL,
  `Education` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_candidate_resume`
--

LOCK TABLES `tbl_candidate_resume` WRITE;
/*!40000 ALTER TABLE `tbl_candidate_resume` DISABLE KEYS */;
INSERT INTO `tbl_candidate_resume` VALUES (32,'KESHORE SURYANARAYANAN','keshore.suryanarayanan@gmail.com','9189397717',4.67,'[\'Excel\', \'Marketing\', \'Communication\', \'Reports\', \'Matlab\', \'Analysis\', \'Electronics\', \'Electrical\', \'Strategy\', \'Protocols\', \'C++\', \'Algorithms\', \'Tableau\', \'Visual\', \'Content\', \'Sql\', \'Quality standards\', \'International\', \'Automation\', \'Programming\', \'System\', \'Calculus\', \'Technical\', \'Mathematics\', \'English\', \'Mobile\', \'Facebook\', \'Website\', \'Iso\', \'Engineering\', \'Cloud\', \'Process\']','[\'Bachelor of Technology, Electrical & Electronics Engineering\']'),(33,'EDUCATION Sravani','sravani.thota@sjsu.edu','019 2018',0,'[\'Statistics\', \'Xgboost\', \'Shell\', \'Communication\', \'Mining\', \'Matlab\', \'Electronics\', \'Scripting\', \'Debugging\', \'C++\', \'C\', \'Java\', \'Sql\', \'Operating systems\', \'Research\', \'Health\', \'Automation\', \'Github\', \'Programming\', \'Jose\', \'Calculus\', \'Troubleshooting\', \'System\', \'Python\', \'Mobile\', \'Engineering\', \'R\', \'Testing\']','None'),(34,'K A','kloudor@email.com','456-7890',0,'[\'Numpy\', \'Statistics\', \'Ordering\', \'Marketing\', \'Flask\', \'Pandas\', \'Analysis\', \'Reporting\', \'Aws\', \'Tableau\', \'C\', \'Forecasting\', \'Analytical\', \'Sql\', \'Retention\', \'Github\', \'Python\', \'Mysql\', \'Budget\', \'Keras\', \'Scheduling\', \'R\', \'Segmentation\', \'Process\']','None'),(35,'Dhanasree Rajamani','dhanasree.rajamani@sjsu.edu','323-423-6501',4.17,'[\'Operations\', \'Shell\', \'Marketing\', \'Mining\', \'C#\', \'Reports\', \'Matlab\', \'Html\', \'Analytics\', \'Pandas\', \'Strategy\', \'C++\', \'Tableau\', \'C\', \'Java\', \'.net\', \'Word\', \'Sql\', \'Software engineering\', \'Ibm\', \'Brand\', \'Css\', \'Jose\', \'System\', \'Troubleshooting\', \'Logistics\', \'Python\', \'Mysql\', \'Android\', \'Sales\', \'Security\', \'Php\', \'Marketing strategy\', \'Linux\', \'Mobile\', \'Spark\', \'Javascript\', \'Controls\', \'Pharmaceutical\', \'Engineering\', \'Ansible\', \'R\', \'Cloud\', \'Oracle\', \'Inventory\']','[\'San Jose State University\', \'PSG College of Technology\', \'Master of Science in Software Engineering\', \'Master of Science (M.Sc.) in Software Engineering\']');
/*!40000 ALTER TABLE `tbl_candidate_resume` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_employees`
--

DROP TABLE IF EXISTS `tbl_employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_employees` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Employee_Name` varchar(70) NOT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Current_Role` varchar(100) DEFAULT NULL,
  `Work_Experience` int DEFAULT NULL,
  `Skill_Set` varchar(200) DEFAULT NULL,
  `Education` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_employees`
--

LOCK TABLES `tbl_employees` WRITE;
/*!40000 ALTER TABLE `tbl_employees` DISABLE KEYS */;
INSERT INTO `tbl_employees` VALUES (1,'Ben','Ben@company.com','Software Engineer',3,'Python, Java, C++, SQL, Ansible','BE'),(2,'Alex','Alex@company.com','Senior Software Engineer',4,'C++, .Net, Power BI, Shell script, Django','MS'),(3,'Alice','Alice@company.com','Recruiter',2,'CRM Tools, Zoom','MBA'),(4,'Sam','Sam@company.com','Project Manager',10,'Power BI, Tableau, Pandas, Django','MBA');
/*!40000 ALTER TABLE `tbl_employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_feedback`
--

DROP TABLE IF EXISTS `tbl_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_feedback` (
  `Candidate_Name` varchar(100) NOT NULL,
  `Feedback` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_feedback`
--

LOCK TABLES `tbl_feedback` WRITE;
/*!40000 ALTER TABLE `tbl_feedback` DISABLE KEYS */;
INSERT INTO `tbl_feedback` VALUES ('Dhanasree Rajamani','Good');
/*!40000 ALTER TABLE `tbl_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_open_roles`
--

DROP TABLE IF EXISTS `tbl_open_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_open_roles` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Role_name` varchar(100) NOT NULL,
  `Work_Experience` float DEFAULT NULL,
  `Skill_Set` varchar(200) DEFAULT NULL,
  `Open_flag` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_open_roles`
--

LOCK TABLES `tbl_open_roles` WRITE;
/*!40000 ALTER TABLE `tbl_open_roles` DISABLE KEYS */;
INSERT INTO `tbl_open_roles` VALUES (1,'Software Engineer',0,'Python, Java, SQL, C++',1),(2,'Project Manager',8,'Pandas, Power BI, Tableau',1),(5,'Support Engineer',2,'Ansible, Java, Python',1);
/*!40000 ALTER TABLE `tbl_open_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_resume_link`
--

DROP TABLE IF EXISTS `tbl_resume_link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_resume_link` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Resume_link` varchar(1000) NOT NULL,
  `Loaded_flag` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_resume_link`
--

LOCK TABLES `tbl_resume_link` WRITE;
/*!40000 ALTER TABLE `tbl_resume_link` DISABLE KEYS */;
INSERT INTO `tbl_resume_link` VALUES (24,'KESHORE SURYANARAYANAN.pdf',1),(25,'SravaniThota-SJSU-Resume.pdf',1),(26,'data-scientist-resume-example.pdf',1),(27,'dhanasree-sjsu-ds.pdf',1);
/*!40000 ALTER TABLE `tbl_resume_link` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_shortlisted_candidates`
--

DROP TABLE IF EXISTS `tbl_shortlisted_candidates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_shortlisted_candidates` (
  `Role_name` varchar(100) NOT NULL,
  `candidate_ID` int NOT NULL,
  `candidate_score` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_shortlisted_candidates`
--

LOCK TABLES `tbl_shortlisted_candidates` WRITE;
/*!40000 ALTER TABLE `tbl_shortlisted_candidates` DISABLE KEYS */;
INSERT INTO `tbl_shortlisted_candidates` VALUES ('Support Engineer',35,3);
/*!40000 ALTER TABLE `tbl_shortlisted_candidates` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-28 16:35:29