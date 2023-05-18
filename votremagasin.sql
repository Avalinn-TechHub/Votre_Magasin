-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 14, 2023 at 03:35 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `votremagasin`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_category`
--

CREATE TABLE `adminapp_category` (
  `id` bigint(20) NOT NULL,
  `Categry` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminapp_category`
--

INSERT INTO `adminapp_category` (`id`, `Categry`) VALUES
(1, 'Electronics'),
(2, 'Fashion'),
(3, 'Furniture'),
(4, 'Books');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_sub_category`
--

CREATE TABLE `adminapp_sub_category` (
  `id` bigint(20) NOT NULL,
  `Subcategory` varchar(30) NOT NULL,
  `Categry` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminapp_sub_category`
--

INSERT INTO `adminapp_sub_category` (`id`, `Subcategory`, `Categry`) VALUES
(1, 'Horror', 'Books'),
(2, 'Mobile', 'Electronics');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add sub_category', 8, 'add_sub_category'),
(30, 'Can change sub_category', 8, 'change_sub_category'),
(31, 'Can delete sub_category', 8, 'delete_sub_category'),
(32, 'Can view sub_category', 8, 'view_sub_category'),
(33, 'Can add auto_notification', 9, 'add_auto_notification'),
(34, 'Can change auto_notification', 9, 'change_auto_notification'),
(35, 'Can delete auto_notification', 9, 'delete_auto_notification'),
(36, 'Can view auto_notification', 9, 'view_auto_notification'),
(37, 'Can add auto_reg', 10, 'add_auto_reg'),
(38, 'Can change auto_reg', 10, 'change_auto_reg'),
(39, 'Can delete auto_reg', 10, 'delete_auto_reg'),
(40, 'Can view auto_reg', 10, 'view_auto_reg'),
(41, 'Can add auto_booking', 11, 'add_auto_booking'),
(42, 'Can change auto_booking', 11, 'change_auto_booking'),
(43, 'Can delete auto_booking', 11, 'delete_auto_booking'),
(44, 'Can view auto_booking', 11, 'view_auto_booking'),
(45, 'Can add cart', 12, 'add_cart'),
(46, 'Can change cart', 12, 'change_cart'),
(47, 'Can delete cart', 12, 'delete_cart'),
(48, 'Can view cart', 12, 'view_cart'),
(49, 'Can add customer_reg', 13, 'add_customer_reg'),
(50, 'Can change customer_reg', 13, 'change_customer_reg'),
(51, 'Can delete customer_reg', 13, 'delete_customer_reg'),
(52, 'Can view customer_reg', 13, 'view_customer_reg'),
(53, 'Can add purchase', 14, 'add_purchase'),
(54, 'Can change purchase', 14, 'change_purchase'),
(55, 'Can delete purchase', 14, 'delete_purchase'),
(56, 'Can view purchase', 14, 'view_purchase'),
(57, 'Can add product', 15, 'add_product'),
(58, 'Can change product', 15, 'change_product'),
(59, 'Can delete product', 15, 'delete_product'),
(60, 'Can view product', 15, 'view_product'),
(61, 'Can add shop_reg', 16, 'add_shop_reg'),
(62, 'Can change shop_reg', 16, 'change_shop_reg'),
(63, 'Can delete shop_reg', 16, 'delete_shop_reg'),
(64, 'Can view shop_reg', 16, 'view_shop_reg'),
(65, 'Can add auto_status', 17, 'add_auto_status'),
(66, 'Can change auto_status', 17, 'change_auto_status'),
(67, 'Can delete auto_status', 17, 'delete_auto_status'),
(68, 'Can view auto_status', 17, 'view_auto_status');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `autoapp_auto_notification`
--

CREATE TABLE `autoapp_auto_notification` (
  `id` bigint(20) NOT NULL,
  `sname` varchar(30) NOT NULL,
  `splace` varchar(50) NOT NULL,
  `uname` varchar(30) NOT NULL,
  `cname` varchar(30) NOT NULL,
  `items` varchar(30) NOT NULL,
  `categry` varchar(30) NOT NULL,
  `price` varchar(30) NOT NULL,
  `total` varchar(30) NOT NULL,
  `datetime` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `autoapp_auto_notification`
--

INSERT INTO `autoapp_auto_notification` (`id`, `sname`, `splace`, `uname`, `cname`, `items`, `categry`, `price`, `total`, `datetime`, `status`) VALUES
(1, 'annamart', 'Anna Mart, Mandhiram,Puthuppally P.O Kottayam-11', 'Anoop Nair', 'AMAAL', 'A history of fear', 'Books', '280', '280', '2023-02-09', 'Delivered');

-- --------------------------------------------------------

--
-- Table structure for table `autoapp_auto_reg`
--

CREATE TABLE `autoapp_auto_reg` (
  `id` bigint(20) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Vehicleno` varchar(30) NOT NULL,
  `Phonenum` varchar(13) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Latitude` varchar(30) NOT NULL,
  `Longitude` varchar(30) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `autoapp_auto_reg`
--

INSERT INTO `autoapp_auto_reg` (`id`, `Name`, `Vehicleno`, `Phonenum`, `Address`, `Latitude`, `Longitude`, `Username`, `Password`, `Status`) VALUES
(1, 'Anoop Nair', 'KL05AD6876', '9496874532', 'Green Villa, Puthuppally P.O Kottayam-11', '9°33\'33.4\"N', '76°34\'20.9\"E', 'anoopnair', 'anoop3', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `autoapp_auto_status`
--

CREATE TABLE `autoapp_auto_status` (
  `id` bigint(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `autoapp_auto_status`
--

INSERT INTO `autoapp_auto_status` (`id`, `name`, `status`) VALUES
(1, 'anoopnair', 'Available');

-- --------------------------------------------------------

--
-- Table structure for table `customerapp_auto_booking`
--

CREATE TABLE `customerapp_auto_booking` (
  `id` bigint(20) NOT NULL,
  `Cname` varchar(30) NOT NULL,
  `Cusername` varchar(30) NOT NULL,
  `Cphone` varchar(13) NOT NULL,
  `Cplace` varchar(30) NOT NULL,
  `Aname` varchar(30) NOT NULL,
  `Ausername` varchar(30) NOT NULL,
  `Avehicleno` varchar(30) NOT NULL,
  `Aphone` varchar(13) NOT NULL,
  `Date` date NOT NULL,
  `Status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customerapp_auto_booking`
--

INSERT INTO `customerapp_auto_booking` (`id`, `Cname`, `Cusername`, `Cphone`, `Cplace`, `Aname`, `Ausername`, `Avehicleno`, `Aphone`, `Date`, `Status`) VALUES
(1, 'AMAAL', 'amaal', '9678453278', 'Rosevilla, Mandhiram,Puthuppal', 'Anoop Nair', 'anoopnair', 'KL05AD6876', '9496874532', '2023-02-14', 'Accepted');

-- --------------------------------------------------------

--
-- Table structure for table `customerapp_cart`
--

CREATE TABLE `customerapp_cart` (
  `id` bigint(20) NOT NULL,
  `Shopname` varchar(30) NOT NULL,
  `Userid` varchar(30) NOT NULL,
  `Itemid` varchar(30) NOT NULL,
  `Product` varchar(30) NOT NULL,
  `Image` varchar(30) NOT NULL,
  `Catgry` varchar(30) NOT NULL,
  `Price` varchar(30) NOT NULL,
  `Quantity` int(5) NOT NULL,
  `Total` int(30) NOT NULL,
  `Status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customerapp_customer_reg`
--

CREATE TABLE `customerapp_customer_reg` (
  `id` bigint(20) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Phonenum` varchar(13) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customerapp_customer_reg`
--

INSERT INTO `customerapp_customer_reg` (`id`, `Name`, `Email`, `Phonenum`, `Address`, `Username`, `Password`) VALUES
(1, 'AMAAL', 'amaal304@gmail.com', '9678453278', 'Rosevilla, Mandhiram,Puthuppally P.O Kottayam-11', 'amaal', 'amaal4'),
(2, 'MIDHUN', 'midhun95@gmail.com', '9847665430', 'Chakkalakal , Puthuppally P.O Kottayam-11', 'midhun', 'midhun1'),
(3, 'ANN LIN', 'annlin02@gmail.com', '8289975423', 'Plapparambil , Puthuppally P.O Kottayam-11', 'annlin', 'annlin02');

-- --------------------------------------------------------

--
-- Table structure for table `customerapp_purchase`
--

CREATE TABLE `customerapp_purchase` (
  `id` bigint(20) NOT NULL,
  `shopname` varchar(30) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `items` varchar(30) NOT NULL,
  `catgry` varchar(30) NOT NULL,
  `price` varchar(30) NOT NULL,
  `total` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `Autoname` varchar(30) NOT NULL,
  `Status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customerapp_purchase`
--

INSERT INTO `customerapp_purchase` (`id`, `shopname`, `Username`, `items`, `catgry`, `price`, `total`, `date`, `Autoname`, `Status`) VALUES
(14, 'annamart', 'amaal', 'A history of fear', 'Books', '280', '280', '2023-02-09', 'Anoop Nair', 'Delivered');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'adminapp', 'category'),
(8, 'adminapp', 'sub_category'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(9, 'autoapp', 'auto_notification'),
(10, 'autoapp', 'auto_reg'),
(17, 'autoapp', 'auto_status'),
(5, 'contenttypes', 'contenttype'),
(11, 'customerapp', 'auto_booking'),
(12, 'customerapp', 'cart'),
(13, 'customerapp', 'customer_reg'),
(14, 'customerapp', 'purchase'),
(6, 'sessions', 'session'),
(15, 'shopapp', 'product'),
(16, 'shopapp', 'shop_reg');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-01-23 11:22:46.207268'),
(2, 'auth', '0001_initial', '2023-01-23 11:22:46.654968'),
(3, 'admin', '0001_initial', '2023-01-23 11:22:46.765048'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-01-23 11:22:46.774992'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-01-23 11:22:46.784563'),
(6, 'adminapp', '0001_initial', '2023-01-23 11:22:46.814477'),
(7, 'contenttypes', '0002_remove_content_type_name', '2023-01-23 11:22:46.895020'),
(8, 'auth', '0002_alter_permission_name_max_length', '2023-01-23 11:22:46.947539'),
(9, 'auth', '0003_alter_user_email_max_length', '2023-01-23 11:22:46.964787'),
(10, 'auth', '0004_alter_user_username_opts', '2023-01-23 11:22:46.972450'),
(11, 'auth', '0005_alter_user_last_login_null', '2023-01-23 11:22:47.018025'),
(12, 'auth', '0006_require_contenttypes_0002', '2023-01-23 11:22:47.022012'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2023-01-23 11:22:47.030956'),
(14, 'auth', '0008_alter_user_username_max_length', '2023-01-23 11:22:47.048769'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2023-01-23 11:22:47.063657'),
(16, 'auth', '0010_alter_group_name_max_length', '2023-01-23 11:22:47.083103'),
(17, 'auth', '0011_update_proxy_permissions', '2023-01-23 11:22:47.090789'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2023-01-23 11:22:47.105883'),
(19, 'autoapp', '0001_initial', '2023-01-23 11:22:47.130755'),
(20, 'customerapp', '0001_initial', '2023-01-23 11:22:47.178877'),
(21, 'sessions', '0001_initial', '2023-01-23 11:22:47.205119'),
(22, 'shopapp', '0001_initial', '2023-01-23 11:22:47.228684'),
(23, 'shopapp', '0002_alter_product_image', '2023-01-27 08:09:35.855836'),
(24, 'customerapp', '0002_cart', '2023-01-31 07:53:37.912763'),
(25, 'autoapp', '0002_auto_status', '2023-02-10 13:58:44.449257');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('qwsq2e3cvg9ud5jk00ni37gx6556qu5m', 'e30:1pRvAr:I5cMD9kxO8tH9dYeO5tbeUjW8mk6e3ij1bErKNDBS7o', '2023-02-28 13:16:45.283008');

-- --------------------------------------------------------

--
-- Table structure for table `shopapp_product`
--

CREATE TABLE `shopapp_product` (
  `id` bigint(20) NOT NULL,
  `Pname` varchar(30) NOT NULL,
  `Categry` varchar(30) NOT NULL,
  `Subcat` varchar(30) NOT NULL,
  `Price` varchar(10) NOT NULL,
  `Info` varchar(200) NOT NULL,
  `Stock` int(10) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `Username` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `shopapp_product`
--

INSERT INTO `shopapp_product` (`id`, `Pname`, `Categry`, `Subcat`, `Price`, `Info`, `Stock`, `Image`, `Username`) VALUES
(1, 'Night Of Terror', 'Books', 'Horror', '300', ' How do you explain something that you can\'t prove? That you can\'t touch, but you know it\'s there? Follow this novella and discover what happens. Based on a true story, it\'s the stuff of nightmares . ', 9, 'uploads/book1_JKinFhq.jpg', 'annamart'),
(2, 'Black Forest', 'Books', 'Horror', '460', 'Inspired by the dark labyrinthine narration of Shirley Jackson’s Hangsaman: a young gay man battles with reality as it seemingly dissolves around him, forcing him to fight a series of ever-more fright', 11, 'uploads/book2.jpg', 'annamart'),
(3, 'Into the Dark', 'Books', 'Horror', '260', ' A new home. A new town. And a (terrifying) new start.Ella Tickles is certain that the new house she and her family are about to move into is haunted. Her parents and brother try to convince her that ', 6, 'uploads/book3.jpg', 'annamart'),
(4, 'The Last Chance Hotel', 'Books', 'Horror', '400', 'It\'s \'Poirot meets Potter\' in a locked-room murder mystery that\'s full of magic and intrigue. Be prepared for non-stop reading as you try to solve clues in this who-dunnit, a surefire winner that\'s at', 9, 'uploads/book4.jpg', 'annamart'),
(5, ' House Of Furies', 'Books', 'Horror', '340', 'Seventeen-year-old Louisa escapes her school and finds a job as a maid at a boarding house owned by Mr. Morningside.  At Coldthistle House, she finds her master and the rest of the staff mysterious as', 15, 'uploads/book5.jpg', 'annamart'),
(6, 'A history of fear', 'Books', 'Horror', '280', 'A History of Fear is a propulsive foray into the darkness of the human psyche, marrying dread-inducing atmosphere and heart-palpitating storytelling.', 2, 'uploads/book6.jpg', 'annamart'),
(12, 'The Haunting of Hill House', 'Books', 'Horror', '360', 'The Haunting of Hill House is a 1959 gothic horror novel by American author Shirley Jackson.', 4, 'uploads/book7.jpg', 'annamart');

-- --------------------------------------------------------

--
-- Table structure for table `shopapp_shop_reg`
--

CREATE TABLE `shopapp_shop_reg` (
  `id` bigint(20) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Phonenum` varchar(13) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Latitude` varchar(30) NOT NULL,
  `Longitude` varchar(30) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `shopapp_shop_reg`
--

INSERT INTO `shopapp_shop_reg` (`id`, `Name`, `Email`, `Phonenum`, `Address`, `Latitude`, `Longitude`, `Username`, `Password`, `Status`) VALUES
(1, 'ANNA MART', 'annamart@gmail.com', '9496283452', 'Anna Mart, Mandhiram,Puthuppally P.O Kottayam-11', '9°34\'07.2\"N', '76°33\'57.0\"E', 'annamart', 'annamart8', 'Active'),
(2, 'Best Bakers', 'bestbaker@gmail.com', '9447642594', 'Best Bakers,Puthuppally P.O Kottayam-11', '9°33\'33.7\"N', '76°34\'22.0\"E', 'bestbakers', 'bestbakers4', 'Active');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminapp_category`
--
ALTER TABLE `adminapp_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `adminapp_sub_category`
--
ALTER TABLE `adminapp_sub_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `autoapp_auto_notification`
--
ALTER TABLE `autoapp_auto_notification`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `autoapp_auto_reg`
--
ALTER TABLE `autoapp_auto_reg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `autoapp_auto_status`
--
ALTER TABLE `autoapp_auto_status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customerapp_auto_booking`
--
ALTER TABLE `customerapp_auto_booking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customerapp_cart`
--
ALTER TABLE `customerapp_cart`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customerapp_customer_reg`
--
ALTER TABLE `customerapp_customer_reg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customerapp_purchase`
--
ALTER TABLE `customerapp_purchase`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `shopapp_product`
--
ALTER TABLE `shopapp_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `shopapp_shop_reg`
--
ALTER TABLE `shopapp_shop_reg`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminapp_category`
--
ALTER TABLE `adminapp_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `adminapp_sub_category`
--
ALTER TABLE `adminapp_sub_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `autoapp_auto_notification`
--
ALTER TABLE `autoapp_auto_notification`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `autoapp_auto_reg`
--
ALTER TABLE `autoapp_auto_reg`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `autoapp_auto_status`
--
ALTER TABLE `autoapp_auto_status`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `customerapp_auto_booking`
--
ALTER TABLE `customerapp_auto_booking`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `customerapp_cart`
--
ALTER TABLE `customerapp_cart`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `customerapp_customer_reg`
--
ALTER TABLE `customerapp_customer_reg`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `customerapp_purchase`
--
ALTER TABLE `customerapp_purchase`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `shopapp_product`
--
ALTER TABLE `shopapp_product`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `shopapp_shop_reg`
--
ALTER TABLE `shopapp_shop_reg`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
