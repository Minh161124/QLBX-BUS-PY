-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th2 20, 2025 lúc 06:51 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlns_bx_bus`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `login`
--

CREATE TABLE `login` (
  `USER` varchar(10) NOT NULL,
  `PASSWORD` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `login`
--

INSERT INTO `login` (`USER`, `PASSWORD`) VALUES
('1', '1'),
('1234', '2'),
('2', '1');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `qlccvlt`
--

CREATE TABLE `qlccvlt` (
  `MCC` char(10) NOT NULL,
  `MNS` char(10) NOT NULL,
  `NCC` date NOT NULL,
  `CALAM` int(11) NOT NULL,
  `TTLV` text NOT NULL,
  `LUONGCB` decimal(10,3) NOT NULL,
  `SONGAYCONG` int(11) NOT NULL,
  `PHUCAP` decimal(10,3) NOT NULL,
  `THUONG` decimal(10,3) NOT NULL,
  `PHAT` decimal(10,3) NOT NULL,
  `TONGLUONG` decimal(10,3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `qlhdld`
--

CREATE TABLE `qlhdld` (
  `MHD` char(10) NOT NULL,
  `MNS` char(10) NOT NULL,
  `LHD` text NOT NULL,
  `VITRI` varchar(45) NOT NULL,
  `NGAYKY` date NOT NULL,
  `NGAYKT` date NOT NULL,
  `THOIHANHD` varchar(10) NOT NULL,
  `LUONGCB` decimal(10,3) NOT NULL,
  `PHUCAP` decimal(10,3) NOT NULL,
  `BAOHIEM` text NOT NULL,
  `DKKL` varchar(100) NOT NULL,
  `DKKTHD` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `qlhsns`
--

CREATE TABLE `qlhsns` (
  `MNS` char(10) NOT NULL,
  `USER` varchar(10) NOT NULL,
  `TENNS` text NOT NULL,
  `GIOITINH` int(11) NOT NULL,
  `NAMSINH` year(4) NOT NULL,
  `DIACHI` varchar(100) NOT NULL,
  `SDT` text NOT NULL,
  `EMAIL` varchar(100) NOT NULL,
  `PHONGBAN` varchar(10) NOT NULL,
  `LUONG` decimal(10,3) NOT NULL,
  `THUONG` decimal(10,3) NOT NULL,
  `TRINHDO` varchar(20) NOT NULL,
  `NSQUANLY` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `qlpc`
--

CREATE TABLE `qlpc` (
  `MPC` char(10) NOT NULL,
  `MNS` char(10) NOT NULL,
  `TENNS` text NOT NULL,
  `NAMSINH` date NOT NULL,
  `VITRI` text NOT NULL,
  `TUYENXE` int(11) DEFAULT NULL,
  `CALAM` int(11) NOT NULL,
  `NGAYLAM` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `qltd`
--

CREATE TABLE `qltd` (
  `MUV` char(10) NOT NULL,
  `HOTENUV` text NOT NULL,
  `GIOTINHUV` text NOT NULL,
  `SDTUV` int(10) NOT NULL,
  `VITRIUV` text NOT NULL,
  `TRINHDO` text NOT NULL,
  `TRANGTHAITD` text NOT NULL,
  `NGAYLAMVIEC` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`USER`);

--
-- Chỉ mục cho bảng `qlccvlt`
--
ALTER TABLE `qlccvlt`
  ADD PRIMARY KEY (`MCC`),
  ADD UNIQUE KEY `MCC` (`MCC`),
  ADD KEY `MNS` (`MNS`);

--
-- Chỉ mục cho bảng `qlhdld`
--
ALTER TABLE `qlhdld`
  ADD PRIMARY KEY (`MHD`),
  ADD UNIQUE KEY `MHD` (`MHD`),
  ADD UNIQUE KEY `MNS` (`MNS`);

--
-- Chỉ mục cho bảng `qlhsns`
--
ALTER TABLE `qlhsns`
  ADD PRIMARY KEY (`MNS`),
  ADD UNIQUE KEY `MNS` (`MNS`),
  ADD KEY `USER` (`USER`);

--
-- Chỉ mục cho bảng `qlpc`
--
ALTER TABLE `qlpc`
  ADD PRIMARY KEY (`MPC`),
  ADD UNIQUE KEY `MPC` (`MPC`),
  ADD KEY `MNS` (`MNS`);

--
-- Chỉ mục cho bảng `qltd`
--
ALTER TABLE `qltd`
  ADD PRIMARY KEY (`MUV`),
  ADD UNIQUE KEY `MUV` (`MUV`),
  ADD UNIQUE KEY `SDTUV` (`SDTUV`);

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `qlccvlt`
--
ALTER TABLE `qlccvlt`
  ADD CONSTRAINT `qlccvlt_ibfk_1` FOREIGN KEY (`MNS`) REFERENCES `qlhsns` (`MNS`);

--
-- Các ràng buộc cho bảng `qlhdld`
--
ALTER TABLE `qlhdld`
  ADD CONSTRAINT `qlhdld_ibfk_1` FOREIGN KEY (`MNS`) REFERENCES `qlhsns` (`MNS`);

--
-- Các ràng buộc cho bảng `qlhsns`
--
ALTER TABLE `qlhsns`
  ADD CONSTRAINT `qlhsns_ibfk_1` FOREIGN KEY (`USER`) REFERENCES `login` (`USER`);

--
-- Các ràng buộc cho bảng `qlpc`
--
ALTER TABLE `qlpc`
  ADD CONSTRAINT `qlpc_ibfk_1` FOREIGN KEY (`MNS`) REFERENCES `qlhsns` (`MNS`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
