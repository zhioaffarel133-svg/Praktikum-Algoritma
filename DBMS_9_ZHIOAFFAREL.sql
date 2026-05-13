-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: praktikum_db
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ambil_mk`
--

DROP TABLE IF EXISTS `ambil_mk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ambil_mk` (
  `nim` int(11) NOT NULL,
  `kd_mk` varchar(10) NOT NULL,
  PRIMARY KEY (`nim`,`kd_mk`),
  KEY `kd_mk` (`kd_mk`),
  CONSTRAINT `ambil_mk_ibfk_1` FOREIGN KEY (`nim`) REFERENCES `mahasiswa` (`nim`),
  CONSTRAINT `ambil_mk_ibfk_2` FOREIGN KEY (`kd_mk`) REFERENCES `matakuliah` (`kd_mk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ambil_mk`
--

LOCK TABLES `ambil_mk` WRITE;
/*!40000 ALTER TABLE `ambil_mk` DISABLE KEYS */;
INSERT INTO `ambil_mk` VALUES (101,'PTI447'),(103,'TIK333'),(104,'PTI333'),(104,'PTI777'),(105,'PTI123'),(107,'PTI777');
/*!40000 ALTER TABLE `ambil_mk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dosen`
--

DROP TABLE IF EXISTS `dosen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dosen` (
  `kode_dos` int(11) NOT NULL,
  `nama_dos` varchar(50) DEFAULT NULL,
  `alamat_dos` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`kode_dos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dosen`
--

LOCK TABLES `dosen` WRITE;
/*!40000 ALTER TABLE `dosen` DISABLE KEYS */;
INSERT INTO `dosen` VALUES (10,'Suharto','Jl. Jombang'),(11,'Martono','Jl. Kalpataru'),(12,'Rahmawati','Jl. Jakarta'),(13,'Bambang','Jl. Bandung'),(14,'Nurul','Jl. Raya Tidar');
/*!40000 ALTER TABLE `dosen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jurusan`
--

DROP TABLE IF EXISTS `jurusan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jurusan` (
  `kode_jur` varchar(5) NOT NULL,
  `nama_jur` varchar(50) DEFAULT NULL,
  `kode_dos` int(11) DEFAULT NULL,
  PRIMARY KEY (`kode_jur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jurusan`
--

LOCK TABLES `jurusan` WRITE;
/*!40000 ALTER TABLE `jurusan` DISABLE KEYS */;
INSERT INTO `jurusan` VALUES ('TE','Teknik Elektro',10),('TM','Teknik Mesin',13),('TS','Teknik Sipil',23);
/*!40000 ALTER TABLE `jurusan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mahasiswa`
--

DROP TABLE IF EXISTS `mahasiswa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mahasiswa` (
  `nim` int(11) NOT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `jk` char(1) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`nim`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mahasiswa`
--

LOCK TABLES `mahasiswa` WRITE;
/*!40000 ALTER TABLE `mahasiswa` DISABLE KEYS */;
INSERT INTO `mahasiswa` VALUES (101,'Arif','L','Jl. Kenangan'),(102,'Budi','L','Jl. Jombang'),(103,'Wati','P','Jl. Surabaya'),(104,'Ika','P','Jl. Jombang'),(105,'Tono','L','Jl. Jakarta'),(106,'Iwan','L','JL. Bandung'),(107,'Sari','P','Jl. Malang');
/*!40000 ALTER TABLE `mahasiswa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matakuliah`
--

DROP TABLE IF EXISTS `matakuliah`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `matakuliah` (
  `kd_mk` varchar(10) NOT NULL,
  `nama_mk` varchar(50) DEFAULT NULL,
  `sks` int(11) DEFAULT NULL,
  `semester` int(11) DEFAULT NULL,
  `kode_dos` int(11) DEFAULT NULL,
  PRIMARY KEY (`kd_mk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matakuliah`
--

LOCK TABLES `matakuliah` WRITE;
/*!40000 ALTER TABLE `matakuliah` DISABLE KEYS */;
INSERT INTO `matakuliah` VALUES ('PTI123','Grafika Multimedia',3,5,12),('PTI333','Basis Data Terdistribusi',3,5,10),('PTI447','Praktikum Basis Data',1,3,11),('PTI777','Sistem Informasi',2,3,99),('TIK123','Jaringan Komputer',2,5,33),('TIK333','Sistem Operasi',3,5,10),('TIK342','Praktikum Basis Data',1,3,11);
/*!40000 ALTER TABLE `matakuliah` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-13 12:29:20
