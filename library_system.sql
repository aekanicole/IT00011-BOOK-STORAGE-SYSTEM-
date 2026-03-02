/*M!999999\- enable the sandbox mode */
-- MariaDB dump 10.19-12.2.2-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: library_system
-- ------------------------------------------------------
-- Server version	12.2.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */
;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */
;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */
;
/*!40101 SET NAMES utf8mb4 */
;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */
;
/*!40103 SET TIME_ZONE='+00:00' */
;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */
;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */
;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */
;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */
;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */
;
/*!40101 SET character_set_client = utf8mb4 */
;
CREATE TABLE `books` (
    `book_id` int(11) NOT NULL AUTO_INCREMENT,
    `title` varchar(255) NOT NULL,
    `genre` varchar(100) NOT NULL,
    `author` varchar(255) DEFAULT NULL,
    `date_published` date DEFAULT NULL,
    `status` varchar(50) DEFAULT 'AVAILABLE',
    PRIMARY KEY (`book_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */
;

--
-- Dumping data for table `books`
--

SET @OLD_AUTOCOMMIT = @@AUTOCOMMIT, @@AUTOCOMMIT = 0;

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */
;
/*!40000 ALTER TABLE `books` ENABLE KEYS */
;
UNLOCK TABLES;

COMMIT;

SET AUTOCOMMIT = @OLD_AUTOCOMMIT;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */
;
/*!40101 SET character_set_client = utf8mb4 */
;
CREATE TABLE `members` (
    `member_id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) NOT NULL,
    `password` varchar(255) NOT NULL,
    `full_name` varchar(255) DEFAULT NULL,
    `age` int(11) DEFAULT NULL,
    `student_number` varchar(50) DEFAULT NULL,
    PRIMARY KEY (`member_id`),
    UNIQUE KEY `email` (`email`)
) ENGINE = InnoDB AUTO_INCREMENT = 2 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */
;

--
-- Dumping data for table `members`
--

SET @OLD_AUTOCOMMIT = @@AUTOCOMMIT, @@AUTOCOMMIT = 0;

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */
;
INSERT INTO
    `members`
VALUES (
        1,
        'test@gmail.com',
        'test',
        'test',
        20,
        '202412345'
    );
/*!40000 ALTER TABLE `members` ENABLE KEYS */
;
UNLOCK TABLES;

COMMIT;

SET AUTOCOMMIT = @OLD_AUTOCOMMIT;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */
;
/*!40101 SET character_set_client = utf8mb4 */
;
CREATE TABLE `transactions` (
    `trans_id` int(11) NOT NULL AUTO_INCREMENT,
    `member_id` int(11) DEFAULT NULL,
    `book_id` int(11) DEFAULT NULL,
    `borrow_date` date DEFAULT NULL,
    `duration` int(11) DEFAULT NULL,
    PRIMARY KEY (`trans_id`),
    KEY `member_id` (`member_id`),
    KEY `book_id` (`book_id`),
    CONSTRAINT `1` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`),
    CONSTRAINT `2` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */
;

--
-- Dumping data for table `transactions`
--

SET @OLD_AUTOCOMMIT = @@AUTOCOMMIT, @@AUTOCOMMIT = 0;

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */
;
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */
;
UNLOCK TABLES;

COMMIT;

SET AUTOCOMMIT = @OLD_AUTOCOMMIT;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */
;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */
;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */
;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */
;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */
;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */
;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */
;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */
;

-- Dump completed on 2026-03-01 23:22:31