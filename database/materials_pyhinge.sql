-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Jeu 15 Décembre 2016 à 15:47
-- Version du serveur :  5.7.16-0ubuntu0.16.04.1
-- Version de PHP :  7.0.8-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `PyHinge`
--

-- --------------------------------------------------------

--
-- Structure de la table `materials_pyhinge`
--

CREATE TABLE `materials_pyhinge` (
  `id` int(11) NOT NULL,
  `material` text COLLATE utf8mb4_bin NOT NULL,
  `class` text COLLATE utf8mb4_bin NOT NULL,
  `elastic_modulus` float(11) NOT NULL, /* MPa */
  `poisson_ratio` float(11) NOT NULL,   /* No unit */
  `shear_modulus` float(11) NOT NULL,    /* MPa */
  `shear_stress` float(11) NOT NULL     /* MPa */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Contenu de la table `materials_pyhinge`
--

INSERT INTO `materials_pyhinge` (`id`, `material`, `class`, `elastic_modulus`, `poisson_ratio`, `shear_modulus`, `shear_stress`) VALUES
(1, 'Aluminium', '1050-H18', 69000.0, 0.33, 26000.0, 83.0),
(2, 'Aluminium', '1110-H14', 68900.0, 0.33, 26000.0, 75.8),
(3, 'Aluminium', '1145-H18', 68000.0, 0.33, 26000.0, 85.0),
(4, 'Aluminium', '1199-H18', 67000.0, 0.33, 25000.0, 85.0),
(5, 'Aluminium', '1350-H12', 68900.0, 0.33, 26000.0, 62.1),
(6, 'Aluminium', '2011-T6', 70000.0, 0.33, 26000.0, 235.0),
(7, 'Aluminium', '2014-T4', 73100.0, 0.33, 28000.0, 262.0),
(8, 'Aluminium', '2024-T3', 73000.0, 0.33, 28000.0, 300.0),
(9, 'Aluminium', '2090-T83', 76000.0, 0.33, 28000.0, 320.0),
(10, 'Aluminium', '2218-T61', 74400.0, 0.33, 27500.0, 240.0),
(11, 'Aluminium', '3003-H12', 68900.0, 0.33, 25000.0, 82.7),
(12, 'Aluminium', '3004-H34', 68900.0, 0.33, 25000.0, 124.0),
(13, 'Aluminium', '3013-H14', 68900.0, 0.33, 25000.0, 90.0),
(14, 'Aluminium', '3104-H19', 69000.0, 0.34, 26000.0, 175.0),
(15, 'Aluminium', '3105-H25', 68900.0, 0.33, 25000.0, 103.0),
(16, 'Aluminium', '4032-T6', 78600.0, 0.34, 26000.0, 262.0),
(17, 'Aluminium', '5005-T38', 68900.0, 0.33, 25900.0, 110.0),
(18, 'Aluminium', '5042-H19', 70000.0, 0.33, 26000.0, 215.0),
(19, 'Aluminium', '5083-O', 71000.0, 0.33, 26400.0, 172.0),
(20, 'Aluminium', '5254-H32', 70300.0, 0.33, 26000.0, 152.0),
(21, 'Aluminium', '5754-H24', 70300.0, 0.33, 25900.0, 160.0),
(22, 'Chêne', 'D18', 9.5, 0.33, 0.59, 3.4), /* Ne pas trop compter sur les coefficients de poisson du bois */
(23, 'Chêne', 'D24', 10.0, 0.33, 0.62, 4.0),
(24, 'Chêne', 'D30', 11.0, 0.33, 0.96, 4.0),
(25, 'Sapin/Pin Maritime/Mélèze', 'C18', 9.0, 0.25, 0.56, 3.4),
(26, 'Epicea/Pin Noir/Mélèze', 'C24', 11.0, 0.3, 0.69, 4.0),
(27, 'Douglas/Pin Laricio', 'C30', 12.0, 0.41, 0.75, 4.0),
(28, 'Pin Sylvestre', 'C30', 7.0, 0.33, 0.44, 4.0),
(29, 'Mélèze', 'C27', 11.5, 0.33, 0.72, 4.0);

/*(7, 'Aluminium', '2014-T4', 73100.0, 0.33, 28000.0, 262.0),*/;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
