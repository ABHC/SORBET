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
-- Structure de la table `k_constant`
--

CREATE TABLE `k_constant` (
  `wt_relation` float(11) NOT NULL,  /* mm */
  `k1` float(11) NOT NULL,   /* No unit */
  `k2` float(11) NOT NULL    /* No unit */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Contenu de la table `materials_pyhinge`
--

INSERT INTO `k_constant` (`wt_relation`, `k1`, `k2`) VALUES
(1, 0.208, 0.140),
(1.2, 0.216, 0.166),
(1.5, 0.231, 0.196),
(1.75, 0.239, 0.214),
(2, 0.246, 0.229),
(2.5, 0.258, 0.249),
(3, 0.267, 0.263),
(4, 0.282, 0.281),
(5, 0.291, 0.291),
(6, 0.299, 0.299),
(8, 0.307, 0.307),
(10, 0.313, 0.313),
(1000, 0.333333333, 0.333333333);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
