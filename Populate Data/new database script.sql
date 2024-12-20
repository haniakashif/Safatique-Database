USE [master]
GO
/****** Object:  Database [safatique]    Script Date: 17/12/2024 11:59:57 ******/
CREATE DATABASE [safatique]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'safatique', FILENAME = N'F:\sqlserver\MSSQL16.MSSQLSERVER\MSSQL\DATA\safatique.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'safatique_log', FILENAME = N'F:\sqlserver\MSSQL16.MSSQLSERVER\MSSQL\DATA\safatique_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [safatique] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [safatique].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [safatique] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [safatique] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [safatique] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [safatique] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [safatique] SET ARITHABORT OFF 
GO
ALTER DATABASE [safatique] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [safatique] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [safatique] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [safatique] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [safatique] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [safatique] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [safatique] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [safatique] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [safatique] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [safatique] SET  DISABLE_BROKER 
GO
ALTER DATABASE [safatique] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [safatique] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [safatique] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [safatique] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [safatique] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [safatique] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [safatique] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [safatique] SET RECOVERY FULL 
GO
ALTER DATABASE [safatique] SET  MULTI_USER 
GO
ALTER DATABASE [safatique] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [safatique] SET DB_CHAINING OFF 
GO
ALTER DATABASE [safatique] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [safatique] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [safatique] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [safatique] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'safatique', N'ON'
GO
ALTER DATABASE [safatique] SET QUERY_STORE = ON
GO
ALTER DATABASE [safatique] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [safatique]
GO
/****** Object:  Table [dbo].[Address]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Address](
	[address_id] [int] IDENTITY(1,1) NOT NULL,
	[address] [nvarchar](4000) NOT NULL,
	[city] [char](20) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[address_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Admin]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Admin](
	[employee_id] [int] IDENTITY(1,1) NOT NULL,
	[firstname] [nvarchar](4000) NOT NULL,
	[lastname] [nvarchar](4000) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[employee_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Cart]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cart](
	[customer_id] [int] IDENTITY(1,1) NOT NULL,
	[date_created] [date] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[customer_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CartItems]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CartItems](
	[customer_id] [int] NOT NULL,
	[prod_id] [char](20) NOT NULL,
	[quantity] [int] NOT NULL,
	[unit_price] [int] NOT NULL,
 CONSTRAINT [pk_cart_items] PRIMARY KEY CLUSTERED 
(
	[customer_id] ASC,
	[prod_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Company]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Company](
	[company_id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](4000) NOT NULL,
	[address] [nvarchar](4000) NOT NULL,
	[contact] [nvarchar](4000) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[company_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CompanyPromotion]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CompanyPromotion](
	[comany_id] [int] NOT NULL,
	[promotion_id] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CompanyUser]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CompanyUser](
	[company_id] [int] NOT NULL,
	[username] [char](10) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CompanyVistors]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CompanyVistors](
	[company_id] [int] NOT NULL,
	[date] [date] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Customer]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Customer](
	[customer_id] [int] IDENTITY(1,1) NOT NULL,
	[firstname] [nvarchar](4000) NOT NULL,
	[lastname] [nvarchar](4000) NULL,
	[email] [nvarchar](4000) NOT NULL,
	[phone] [nvarchar](4000) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[customer_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CustomerAddress]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CustomerAddress](
	[customer_id] [int] NOT NULL,
	[address_id] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CustomerPaymentInfo]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CustomerPaymentInfo](
	[customer_id] [int] NOT NULL,
	[payment_id] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[DeliveryCharges]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DeliveryCharges](
	[city_id] [int] IDENTITY(1,1) NOT NULL,
	[city] [nvarchar](20) NOT NULL,
	[cost] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[city_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[MaterialSupplier]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[MaterialSupplier](
	[mat_id] [int] NOT NULL,
	[supplier_id] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[OrderDetails]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[OrderDetails](
	[order_id] [int] NOT NULL,
	[prod_id] [char](20) NOT NULL,
	[quantity] [int] NOT NULL,
	[unit_price] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Orders]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Orders](
	[order_id] [int] IDENTITY(1,1) NOT NULL,
	[customer_id] [int] NOT NULL,
	[order_date] [date] NOT NULL,
	[payment_status] [nvarchar](4000) NOT NULL,
	[processing_status] [nvarchar](4000) NOT NULL,
	[delivery_method] [nvarchar](4000) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[order_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PaymentInfo]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PaymentInfo](
	[payment_id] [int] IDENTITY(1,1) NOT NULL,
	[cardnumber] [varchar](16) NOT NULL,
	[card_cvc] [int] NOT NULL,
	[card_expiry] [date] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[payment_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Product]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Product](
	[prod_id] [char](20) NOT NULL,
	[name] [nvarchar](4000) NOT NULL,
	[price] [float] NOT NULL,
	[category] [nvarchar](4000) NOT NULL,
	[description] [nvarchar](4000) NULL,
	[photo_path] [nvarchar](4000) NOT NULL,
	[in_stock] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[prod_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Promotions]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Promotions](
	[promo_id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](4000) NOT NULL,
	[description] [nvarchar](4000) NOT NULL,
	[discount] [float] NOT NULL,
	[start_date] [date] NOT NULL,
	[end_date] [date] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[promo_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[RawMaterial]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[RawMaterial](
	[mat_id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](4000) NOT NULL,
	[type] [nvarchar](4000) NOT NULL,
	[quantity] [int] NOT NULL,
	[cost] [float] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[mat_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Safatique data - Users]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Safatique data - Users](
	[Username] [varchar](50) NULL,
	[Password] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Supplier]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Supplier](
	[supplier_id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](4000) NOT NULL,
	[contact] [varchar](4000) NULL,
PRIMARY KEY CLUSTERED 
(
	[supplier_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[User]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[User](
	[username] [char](10) NOT NULL,
	[password] [varchar](16) NOT NULL,
	[role] [nvarchar](4000) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[UserAdmin]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[UserAdmin](
	[username] [char](10) NOT NULL,
	[employee_id] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[UserCustomer]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[UserCustomer](
	[username] [char](10) NOT NULL,
	[customer_id] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Visitors]    Script Date: 17/12/2024 11:59:58 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Visitors](
	[date] [date] NOT NULL,
	[count] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Address] ON 

INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (1, N'125/1 11th street khayaban e Rahat phase 6  Karachi  Pakistan', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (2, N'House no 978 Block B Satellite Town  Rawalpindi  Pakistan', N'Rawalpindi          ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (3, N'House no. 13 Set 7  Block E naval anchorage  Islamabad  Pakistan', N'Islamabad           ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (4, N'Near Dr Ziauddin road saddar opposite Suriya memorial hospit Apartment Pak city Tower 2nd Floor Flat no  20  Hyderabad  Pakistan', N'Hyderabad           ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (5, N'497-A Wapda city  Faisalabad  Pakistan', N'Faisalabad          ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (6, N'House 1  Street 8  Korang Town  Islamabad  Pakistan', N'Islamabad           ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (7, N'Qtr 20  Sector 51/B  Korangi no. 6  Karachi  Pakistan', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (8, N'House 3  Phase 2  Jeevan city  Sahiwal  Sahiwal  Pakistan', N'Sahiwal             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (9, N'Iron Squad Fitness Gym  Sector G-13/3  Islamabad  Pakistan', N'Islamabad           ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (10, N'Arbab Ghulam Ali Road  near passport office  joint road  Quetta  Pakistan', N'Quetta              ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (11, N'Quaid e azam road Multan cantt mall view house colony  Multan  Pakistan', N'Multan              ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (12, N'Awaisia Medical Pharmacy  Samanabad  Lahore  Punjab  54000  Lahore  Pakistan', N'Lahore              ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (13, N'Unit #b1010  Block B  10th floor  Rafi Premier Residency  Karachi  Pakistan', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (14, N'Habib University', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (15, N'12-B  7th East Street  DHA Phase 1  Karachi  Pakistan', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (16, N'Lane No. 03  Medical Colony  Girls Hostel  Quaid-e-Azam Medical College  Bahawalpur  Pakistan', N'Bahawalpur          ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (17, N'4B 1/7 Nazimabad No.4 opposite khair ul amal masjid  Karachi  Pakistan', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (18, N'House 447  Street 1  Block H  Phase 5  DHA  Lahore  Pakistan', N'Lahore              ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (19, N'Karachi malir cannt Askri 5  flat D floor 5 block 89 sector E  Karachi  Pakistan', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (20, N'House No. 64-B  PECHS Block 6  Karachi  Pakistan', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (21, N'D1  Shangrila Apartments  Dr. Ziauddin Road  Civil Lines  Karachi  Pakistan', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (22, N'Quetta town sector 18/A scheme 33 house B40 Karachi  Karachi  Pakistan', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (23, N'B93  Block 15 Gulshan e Iqbal  Karachi  Pakistan', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (24, N'Habib University', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (25, N'A 1/2 Gulistan-e-Johar  Block 16  in the lane of Al-Habib housing society  near PIA sports complex', N'Karachi             ')
INSERT [dbo].[Address] ([address_id], [address], [city]) VALUES (26, N'HelloWorld', N'Attock              ')
SET IDENTITY_INSERT [dbo].[Address] OFF
GO
SET IDENTITY_INSERT [dbo].[Admin] ON 

INSERT [dbo].[Admin] ([employee_id], [firstname], [lastname]) VALUES (1, N'Shaaf', N'Farooque')
INSERT [dbo].[Admin] ([employee_id], [firstname], [lastname]) VALUES (2, N'Sajal', N'Fatima')
INSERT [dbo].[Admin] ([employee_id], [firstname], [lastname]) VALUES (3, N'Hania', N'Kashif')
SET IDENTITY_INSERT [dbo].[Admin] OFF
GO
SET IDENTITY_INSERT [dbo].[Cart] ON 

INSERT [dbo].[Cart] ([customer_id], [date_created]) VALUES (13, CAST(N'2024-12-17' AS Date))
INSERT [dbo].[Cart] ([customer_id], [date_created]) VALUES (17, CAST(N'2024-12-17' AS Date))
INSERT [dbo].[Cart] ([customer_id], [date_created]) VALUES (19, CAST(N'2024-12-17' AS Date))
INSERT [dbo].[Cart] ([customer_id], [date_created]) VALUES (22, CAST(N'2024-12-17' AS Date))
SET IDENTITY_INSERT [dbo].[Cart] OFF
GO
INSERT [dbo].[CartItems] ([customer_id], [prod_id], [quantity], [unit_price]) VALUES (13, N'P13_red_____________', 1, 1300)
INSERT [dbo].[CartItems] ([customer_id], [prod_id], [quantity], [unit_price]) VALUES (17, N'P24_orange__________', 3, 700)
INSERT [dbo].[CartItems] ([customer_id], [prod_id], [quantity], [unit_price]) VALUES (19, N'P16_blue____________', 1, 700)
INSERT [dbo].[CartItems] ([customer_id], [prod_id], [quantity], [unit_price]) VALUES (19, N'P20_pink____________', 1, 600)
INSERT [dbo].[CartItems] ([customer_id], [prod_id], [quantity], [unit_price]) VALUES (22, N'P17_blue____________', 1, 1200)
GO
SET IDENTITY_INSERT [dbo].[Customer] ON 

INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (1, N'Maria', N'Imran', N'Marmi0778@gmail.com', N'92 345 8292336')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (2, N'Aqleema', N'Ahmed', N'aqleema.062@gmail.com', N'92 323 9969092')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (3, N'Areesha', N'Naqvi', N'Areeshab92@gmail.com', N'92 334 3809686')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (4, N'Muhammad', N'Hashemi', N'Asma.ateeq@gmail.com', N'92 300 5103726')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (5, N'Zobiya', N'Faizan', N'Zobiyafaizan@gmail.com', N'92 306 2131070')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (6, N'Ezzah', N'Farrukh', N'Ezzahfarrukh13@gmail.com', N'92 331 4954520')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (7, N'Sidra', N'Rana', N'Sidra.wooz170@gmail.com', N'92 334 0151468')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (8, N'Ahoor', N'Ali', N'Ahoor919@gmail.com', N'92 313 2076919')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (9, N'Bakhtiar', N'', N'Bakhtiara611@gmail.com', N'92 300 2807682')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (10, N'Rahimeen', N'Akram', N'Rahimeoww@gmail.com', N'92 331 4808459')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (11, N'Mariam', N'', N'Hams8716@gmail.com', N'92 333 7530963')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (12, N'Wania', N'Yasir', N'Waniasehgal741@gmail.com', N'92 301 1383076')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (13, N'Ahad', N'Shafeeq', N'Ahaddon98@gmail.com', N'92 316 1488075')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (14, N'Shahjahan', N'Masood', N'Murkabbasi56@gmail.com', N'92 343 5624581')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (15, N'Fatima', N'Aijaz', N'Fa08519@st.habib.edu.pk', N'92 335 2104413')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (16, N'Fatima', N'Amin', N'ff09248@st.habib.edu.pk', N'92 331 2345678')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (17, N'Mahnoor', N'', N'Mahnoor.taimur02@gmail.com', N'92 308 2598756')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (18, N'Noor', N'Bakht', N'Noorbakht2003@gmail.com', N'92 313 6327159')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (19, N'Syeda', N'Zareen', N'Bangbangbangtan706@gmail.com', N'92 321 7122961')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (20, N'Maziyah', N'Leghari', N'Maziyahleghari@gmail.com', N'92 323 5306154')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (21, N'Amna', N'Nawaz', N'Amnanawaz@yahoo.com', N'92 314 8251768')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (22, N'Alishba', N'Noman', N'Alishba.noman456@gmail.com', N'92 315 5964763')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (23, N'Zainab', N'Javed', N'zj06738@st.habib.edu.pk', N'92 335 7206651')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (24, N'Hareem', N'Taha', N'Hareemhehehe@gmail.com', N'92 323 2114115')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (25, N'Farwa', N'', N'zulqarnaingopang772@gmail.com', N'92 333 7079827')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (26, N'Musfirah', N'Kashif', N'musfirahmoon08@gmail.com', N'92 330 9416080')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (27, N'Hamdan', N'', N'dummy@dummy.com', N'00 000 0000000')
INSERT [dbo].[Customer] ([customer_id], [firstname], [lastname], [email], [phone]) VALUES (28, N'Fatima', N'', N'fatimaxxsiddiqui@gmail.com', N'92 341 1850450')
SET IDENTITY_INSERT [dbo].[Customer] OFF
GO
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (1, 1)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (2, 2)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (4, 3)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (5, 4)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (6, 5)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (7, 6)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (8, 7)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (9, 8)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (10, 9)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (11, 10)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (12, 11)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (13, 12)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (14, 13)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (15, 14)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (17, 15)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (18, 16)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (19, 17)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (20, 18)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (21, 19)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (23, 20)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (24, 21)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (25, 22)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (26, 23)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (27, 24)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (28, 25)
INSERT [dbo].[CustomerAddress] ([customer_id], [address_id]) VALUES (13, 26)
GO
INSERT [dbo].[CustomerPaymentInfo] ([customer_id], [payment_id]) VALUES (17, 1)
INSERT [dbo].[CustomerPaymentInfo] ([customer_id], [payment_id]) VALUES (15, 2)
INSERT [dbo].[CustomerPaymentInfo] ([customer_id], [payment_id]) VALUES (1, 3)
INSERT [dbo].[CustomerPaymentInfo] ([customer_id], [payment_id]) VALUES (19, 4)
INSERT [dbo].[CustomerPaymentInfo] ([customer_id], [payment_id]) VALUES (26, 5)
INSERT [dbo].[CustomerPaymentInfo] ([customer_id], [payment_id]) VALUES (10, 6)
INSERT [dbo].[CustomerPaymentInfo] ([customer_id], [payment_id]) VALUES (7, 7)
INSERT [dbo].[CustomerPaymentInfo] ([customer_id], [payment_id]) VALUES (13, 8)
INSERT [dbo].[CustomerPaymentInfo] ([customer_id], [payment_id]) VALUES (13, 12)
GO
SET IDENTITY_INSERT [dbo].[DeliveryCharges] ON 

INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (1, N'Karachi', 200)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (2, N'Lahore', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (3, N'Islamabad', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (4, N'Rawalpindi', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (5, N'Faisalabad', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (6, N'Peshawar', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (7, N'Quetta', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (8, N'Multan', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (9, N'Gujranwala', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (10, N'Sialkot', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (11, N'Hyderabad', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (12, N'Sukkur', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (13, N'Abbottabad', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (14, N'Bahawalpur', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (15, N'Sargodha', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (16, N'Jhelum', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (17, N'Mardan', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (18, N'Gujrat', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (19, N'Nawabshah', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (20, N'Mirpur (AJK)', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (21, N'Muzaffarabad', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (22, N'Rahim Yar Khan', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (23, N'Dera Ghazi Khan', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (24, N'Sheikhupura', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (25, N'Chiniot', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (26, N'Kasur', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (27, N'Okara', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (28, N'Sahiwal', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (29, N'Turbat', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (30, N'Gwadar', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (31, N'Mingora (Swat)', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (32, N'Vehari', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (33, N'Kamoke', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (34, N'Jhang', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (35, N'Larkana', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (36, N'Jacobabad', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (37, N'Khairpur', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (38, N'Shikarpur', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (39, N'Mansehra', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (40, N'Zhob', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (41, N'Dadu', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (42, N'Hafizabad', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (43, N'Kohat', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (44, N'Attock', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (45, N'Charsadda', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (46, N'Skardu', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (47, N'Gilgit', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (48, N'Hunza', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (49, N'Ghotki', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (50, N'Bannu', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (51, N'Chitral', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (52, N'Swabi', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (53, N'Tando Allahyar', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (54, N'Tando Muhammad Khan', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (55, N'Kotri', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (56, N'Nowshera', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (57, N'Dir', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (58, N'Thatta', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (59, N'Badin', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (60, N'Jamshoro', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (61, N'Khuzdar', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (62, N'Dera Ismail Khan', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (63, N'Bhakkar', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (64, N'Khanewal', 250)
INSERT [dbo].[DeliveryCharges] ([city_id], [city], [cost]) VALUES (65, N'Pakpattan', 250)
SET IDENTITY_INSERT [dbo].[DeliveryCharges] OFF
GO
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (1, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (2, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (3, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (4, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (5, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (6, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (7, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (8, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (9, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (10, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (11, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (12, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (13, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (14, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (15, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (16, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (17, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (18, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (19, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (20, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (21, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (22, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (23, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (24, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (25, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (26, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (27, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (28, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (29, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (30, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (31, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (32, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (33, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (34, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (35, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (36, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (37, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (38, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (39, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (40, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (41, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (42, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (43, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (44, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (45, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (46, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (47, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (48, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (49, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (50, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (51, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (52, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (53, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (54, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (55, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (56, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (57, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (58, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (59, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (60, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (61, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (62, 3)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (63, 1)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (64, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (65, 2)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (66, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (67, 4)
INSERT [dbo].[MaterialSupplier] ([mat_id], [supplier_id]) VALUES (68, 3)
GO
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (1, N'P1_purple___________', 2, 400)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (2, N'P23_green___________', 1, 200)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (3, N'P16_blue____________', 1, 700)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (4, N'P18_white___________', 1, 650)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (4, N'P11_black___________', 1, 600)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (5, N'P24_orange__________', 1, 700)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (5, N'P2_purple___________', 1, 550)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (6, N'P12_pearl___________', 2, 500)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (7, N'P2_purple___________', 2, 550)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (8, N'P20_pink____________', 1, 600)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (9, N'P24_pink____________', 1, 700)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (9, N'P22_cherry__________', 1, 500)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (10, N'P23_green___________', 2, 200)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (11, N'P4_red______________', 1, 600)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (12, N'P2_purple___________', 1, 550)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (13, N'P24_orange__________', 1, 700)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (14, N'P10_black___________', 1, 550)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (14, N'P13_red_____________', 1, 1300)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (14, N'P14_black___________', 1, 650)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (15, N'P3_purple___________', 1, 570)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (16, N'P10_black___________', 1, 550)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (16, N'P11_black___________', 1, 600)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (16, N'P20_pink____________', 1, 600)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (16, N'P21_pink____________', 1, 650)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (17, N'P22_cherry__________', 2, 500)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (18, N'P4_red______________', 1, 600)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (18, N'P5_black____________', 1, 570)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (18, N'P6_blue_____________', 1, 700)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (18, N'P11_black___________', 1, 600)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (19, N'P21_pink____________', 2, 650)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (20, N'P22_cherry__________', 1, 500)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (20, N'P2_purple___________', 1, 550)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (20, N'P11_black___________', 1, 600)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (20, N'P12_pearl___________', 1, 500)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (20, N'P3_purple___________', 1, 570)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (20, N'P10_black___________', 1, 550)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (21, N'P6_cherry___________', 1, 700)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (21, N'P20_pink____________', 3, 600)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (22, N'P11_black___________', 1, 600)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (23, N'P19_pink____________', 2, 650)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (24, N'P1_purple___________', 4, 400)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (25, N'P22_cherry__________', 2, 500)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (26, N'P11_black___________', 1, 600)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (27, N'P10_black___________', 1, 550)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (28, N'P23_green___________', 1, 200)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (28, N'P15_green___________', 1, 700)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (29, N'P24_pink____________', 1, 700)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (30, N'P20_pink____________', 2, 600)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (38, N'P14_black___________', 2, 650)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (38, N'P16_blue____________', 1, 700)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (39, N'P12_pearl___________', 1, 500)
INSERT [dbo].[OrderDetails] ([order_id], [prod_id], [quantity], [unit_price]) VALUES (40, N'P1_purple___________', 1, 400)
GO
SET IDENTITY_INSERT [dbo].[Orders] ON 

INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (1, 1, CAST(N'2024-05-31' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (2, 2, CAST(N'2024-05-31' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (3, 3, CAST(N'2024-06-01' AS Date), N'paid', N'delivered', N'self pickup')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (4, 4, CAST(N'2024-06-02' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (5, 5, CAST(N'2024-06-02' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (6, 6, CAST(N'2024-06-03' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (7, 7, CAST(N'2024-06-04' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (8, 8, CAST(N'2024-06-05' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (9, 9, CAST(N'2024-06-22' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (10, 10, CAST(N'2024-06-30' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (11, 11, CAST(N'2024-06-30' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (12, 12, CAST(N'2024-07-06' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (13, 13, CAST(N'2024-07-12' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (14, 14, CAST(N'2024-07-21' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (15, 15, CAST(N'2024-07-21' AS Date), N'paid', N'delivered', N'self pickup')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (16, 7, CAST(N'2024-07-21' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (17, 16, CAST(N'2024-07-21' AS Date), N'paid', N'delivered', N'self pickup')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (18, 17, CAST(N'2024-07-21' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (19, 18, CAST(N'2024-07-21' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (20, 19, CAST(N'2024-07-21' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (21, 20, CAST(N'2024-07-22' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (22, 21, CAST(N'2024-07-23' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (23, 22, CAST(N'2024-07-23' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (24, 23, CAST(N'2024-07-23' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (25, 24, CAST(N'2024-07-29' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (26, 25, CAST(N'2024-08-07' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (27, 26, CAST(N'2024-08-12' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (28, 27, CAST(N'2024-09-17' AS Date), N'paid', N'delivered', N'self pickup')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (29, 28, CAST(N'2024-09-13' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (30, 12, CAST(N'2024-09-14' AS Date), N'paid', N'delivered', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (38, 13, CAST(N'2024-12-17' AS Date), N'Awaiting Payment', N'Awaiting Processing', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (39, 13, CAST(N'2024-12-17' AS Date), N'Awaiting Payment', N'Awaiting Processing', N'shipping')
INSERT [dbo].[Orders] ([order_id], [customer_id], [order_date], [payment_status], [processing_status], [delivery_method]) VALUES (40, 13, CAST(N'2024-12-17' AS Date), N'Awaiting Payment', N'Awaiting Processing', N'shipping')
SET IDENTITY_INSERT [dbo].[Orders] OFF
GO
SET IDENTITY_INSERT [dbo].[PaymentInfo] ON 

INSERT [dbo].[PaymentInfo] ([payment_id], [cardnumber], [card_cvc], [card_expiry]) VALUES (1, N'1234567890156', 123, CAST(N'2029-04-15' AS Date))
INSERT [dbo].[PaymentInfo] ([payment_id], [cardnumber], [card_cvc], [card_expiry]) VALUES (2, N'9864656464664', 456, CAST(N'2028-07-01' AS Date))
INSERT [dbo].[PaymentInfo] ([payment_id], [cardnumber], [card_cvc], [card_expiry]) VALUES (3, N'5886468496484', 789, CAST(N'2030-05-04' AS Date))
INSERT [dbo].[PaymentInfo] ([payment_id], [cardnumber], [card_cvc], [card_expiry]) VALUES (4, N'9687674151781', 987, CAST(N'2029-01-14' AS Date))
INSERT [dbo].[PaymentInfo] ([payment_id], [cardnumber], [card_cvc], [card_expiry]) VALUES (5, N'7587588484944', 654, CAST(N'2027-08-21' AS Date))
INSERT [dbo].[PaymentInfo] ([payment_id], [cardnumber], [card_cvc], [card_expiry]) VALUES (6, N'4946777541659', 321, CAST(N'2029-11-12' AS Date))
INSERT [dbo].[PaymentInfo] ([payment_id], [cardnumber], [card_cvc], [card_expiry]) VALUES (7, N'6464489458514', 166, CAST(N'2032-03-18' AS Date))
INSERT [dbo].[PaymentInfo] ([payment_id], [cardnumber], [card_cvc], [card_expiry]) VALUES (8, N'1234569870156', 654, CAST(N'2028-12-06' AS Date))
INSERT [dbo].[PaymentInfo] ([payment_id], [cardnumber], [card_cvc], [card_expiry]) VALUES (12, N'13165132165', 132, CAST(N'2027-01-09' AS Date))
SET IDENTITY_INSERT [dbo].[PaymentInfo] OFF
GO
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P1_purple___________', N'Cinnamon Roll Elastic Bracelet', 400, N'Bracelets', N'Suitable for average women''s wrist', N'./images/cinnamoroll bracelet.jpg', 7)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P10_black___________', N'Simple Kuromi star Keychain', 550, N'Keychains', N'A dreamy Keychain that will go well with your bag', N'./images/kuromi keychains.jpg', 3)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P11_black___________', N'Kuromi in the garden star keychain', 600, N'Keychains', N'The better version of our simple kuromi star keychain', N'./images/kuromi keychains.jpg', 1)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P12_pearl___________', N'The Little Mermaid', 500, N'Bracelets', N'A romantic gift for your loved one', N'./images/little mermaid.jpg', 4)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P13_red_____________', N'A court of Thorns & Roses', 1300, N'Necklaces', N'This one''s for your inner villain.', N'./images/thornsnroses.jpg', 2)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P14_black___________', N'The Evil Queen', 650, N'Bracelets', N'Safatique''s unique best seller bracelet', N'./images/evil queen.jpg', 3)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P15_green___________', N'Green crystalline bracelet', 700, N'Bracelets', N'Part of our eid drop', N'./images/green crystalline.jpg', 4)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P16_blue____________', N'Winxed Bracelet', 700, N'Bracelets', N'Part of our eid drop', N'./images/winxed.jpg', 5)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P17_blue____________', N'Mermalidia Choker', 1200, N'Necklaces', N'Part of our eid drop', N'./images/mermalidia.jpg', 7)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P18_white___________', N'Whitney Bracelet', 650, N'Bracelets', N'Part of our eid drop', N'./images/whitney.jpg', 10)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P19_pink____________', N'Axolotl bracelet', 650, N'Bracelets', N'Part of our eid drop', N'./images/axolotl.jpg', 9)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P2_purple___________', N'Twiglight Metal Bracelet', 550, N'Bracelets', N'5.5 inches long with 5cm adjustability chain', N'./images/twilight metal.jpg', 1)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P20_pink____________', N'Tangled bracelet', 600, N'Bracelets', N'Elastic Bracelet with charm & rhinestones', N'./images/tangled.jpg', 5)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P21_pink____________', N'Tangled Metal Bracelet', 650, N'Bracelets', N'Safatique''s best seller inspired by tangled', N'./images/tangled metal.jpg', 8)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P22_cherry__________', N'Cherry n Tulip Bracelet', 500, N'Bracelets', N'Simple but cute', N'./images/cherry collection.jpg', 5)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P23_green___________', N'Tulip Earrings', 200, N'Earrings', N'Elegant', N'./images/cherry collection.jpg', 8)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P24_lightblue_______', N'Light Blue Winx Club Necklace', 700, N'Necklaces', N'Winx club inspired necklace with 50 cm stainless steel chain', N'./images/winx necklace.jpg', 4)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P24_orange__________', N'Orange Winx Club Necklace', 700, N'Necklaces', N'Winx club inspired necklace with 50 cm stainless steel chain', N'./images/winx necklace.jpg', 3)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P24_pink____________', N'Pink Winx Club Necklace', 700, N'Necklaces', N'Winx club inspired necklace with 50 cm stainless steel chain', N'./images/winx necklace.jpg', 10)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P3_purple___________', N'Mystic Lagoon Keychain', 570, N'Keychains', N'A cute bag charm for all the ocean core girlies', N'./images/mystic lagoon.jpg', 5)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P4_red______________', N'Aesthetic Red Heart Necklace', 600, N'Necklaces', N'45 cm long leather cord with 5 cm adjustability chain', N'./images/aesthetic red hear.jpg', 8)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P5_black____________', N'Midnight Whispers', 570, N'Necklaces', N'Fully handmade corpse bride necklace', N'./images/midnight whispers.jpg', 6)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P6_blue_____________', N'Blue Jade Natural Stone Necklace ', 700, N'Necklaces', N'45 cm long leather cord with 5 cm adjustability chain', N'./images/blue jade.jpg', 10)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P6_cherry___________', N'Cherry Quartz Natural Stone Necklace ', 700, N'Necklaces', N'45 cm long leather cord with 5 cm adjustability chain', N'./images/cherry quartz.jpg', 6)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P6_gold_____________', N'Goldstone Natural Stone Necklace', 700, N'Necklaces', N'45 cm long leather cord with 5 cm adjustability chain', N'./images/natural stone necklace general.jpg', 4)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P6_green____________', N'Malachite Natural Stone Necklace ', 700, N'Necklaces', N'45 cm long leather cord with 5 cm adjustability chain', N'./images/natural stone necklace general.jpg', 4)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P6_rainbow__________', N'Rainbow Calsilica Natural Stone Necklace', 700, N'Necklaces', N'45 cm long leather cord with 5 cm adjustability chain', N'./images/natural stone necklace general.jpg', 8)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P7_cherry___________', N'Cherry & tulip necklace', 1200, N'Necklaces', N'Handmade combo of cherry and tulips', N'./images/cherry collection.jpg', 9)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P8_cherry___________', N'Simple Cherry Necklace', 800, N'Necklaces', N'Classic cherry necklace', N'./images/simple cherry.jpg', 8)
INSERT [dbo].[Product] ([prod_id], [name], [price], [category], [description], [photo_path], [in_stock]) VALUES (N'P9_cherry___________', N'Cherry Phone Charm', 500, N'Phone Charms', N'A classic. Goes well with Cherry & Tulip necklace', N'./images/simple cherry.jpg', 1)
GO
SET IDENTITY_INSERT [dbo].[RawMaterial] ON 

INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (1, N'Dark Purple Beads', N'Glass Beads', 205, 0.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (2, N'Ferozi Beads', N'Glass Beads', 100, 0.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (3, N'Transparent Green', N'Glass Beads', 98, 0.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (4, N'Tiger Eye Bead', N'Natural Stone', 45, 5.3)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (5, N'Transparent Beads', N'Glass Beads', 195, 0.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (6, N'Pastel Pink Bead', N'Glass Beads', 420, 0.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (7, N'Dark Green Beads', N'Glass Beads', 94, 0.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (8, N'Milky White Beads', N'Glass Beads', 192, 0.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (9, N'Sky Blue Beads', N'Glass Beads', 195, 0.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (10, N'Dark Pastel Pink', N'Glass Beads', 296, 0.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (11, N'Pastel Blue Beads', N'Glass Beads', 187, 0.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (12, N'Blue Check Hearts', N'Charms', 15, 10)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (13, N'White rose', N'Beads', 183, 5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (14, N'White Shell', N'Beads', 44, 5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (15, N'Silver smiley sad face', N'Charms', 4, 40)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (16, N'Silver Chain pieces', N'Chains', 54, 10)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (17, N'Rainbow butterflies', N'Beads', 275, 1)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (18, N'White crystal beads', N'Crystal Beads', 73, 0.7)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (19, N'Light Pink Crystal Beads', N'Crystal Beads', 273, 0.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (20, N'Dark Pink Crystal Beads', N'Crystal Beads', 109, 0.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (21, N'Stainless steel charms', N'Charms', 11, 15)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (22, N'Stainless steel spacer', N'Beads', 31, 5.2)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (23, N'Black Crystal beads', N'Crystal Beads', 99, 0.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (24, N'Ink blue crystal beads', N'Crystal Beads', 44, 0.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (25, N'Light Purple Crystal Beads', N'Crystal Beads', 111, 0.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (26, N'red crystal beads', N'Crystal Beads', 108, 0.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (27, N'Transparent rectangle beads', N'Beads', 105, 1)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (28, N'Dark green crystal beads', N'Crystal Beads', 214, 0.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (29, N'Light blue crystal beads', N'Crystal Beads', 113, 0.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (30, N'Drop crystal', N'Czech Bead', 8, 13.55)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (31, N'Kuromi', N'Charms', 9, 54.7)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (32, N'Magnetic Hearts', N'Charms', 7, 43.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (33, N'Light green crystal beads', N'Crystal Beads', 58, 0.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (34, N'Dark Purple crystal beads', N'Crystal Beads', 72, 0.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (35, N'Black glass beads', N'Glass Beads', 48, 0.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (36, N'Yellow crystal beads', N'Crystal Beads', 252, 0.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (37, N'Brown crystal beads', N'Crystal Beads', 67, 0.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (38, N'Silver lobster hook', N'Charms', 70, 3)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (39, N'Phone charm string', N'Charms', 50, 17)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (40, N'Grey glass beads', N'Beads', 73, 0.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (41, N'Hollow Flower charm', N'Charms', 30, 8.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (42, N'Evil eye', N'Beads', 20, 5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (43, N'Stainless steel chain whole', N'chains', 282, 1)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (44, N'Angel wings charm', N'Charms', 59, 4.21)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (45, N'Star Keychain', N'Keychains', 6, 45.6)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (46, N'50 cm stainless steel chain', N'Chains', 7, 40.2)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (47, N'Pink cards', N'Packaging', 0, 5.05)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (48, N'Flower plastic bag', N'Packaging', 40, 5.41)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (49, N'Bubble mailers', N'Packaging', 14, 75.85)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (50, N'Leather Cord', N'Chains', 18, 26.5)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (51, N'pink czech lampwork flower', N'beads', 20, 12.55)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (52, N'purple blue czech leaf crystal', N'charms', 10, 23.7)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (53, N'czech glass transparent star', N'beads', 50, 6.76)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (54, N'blue czech lampwork fish', N'beads', 20, 18.08)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (55, N'Czech glass transparent heart', N'beads', 40, 9.53)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (56, N'Acryllic blue sea shell beads', N'beads', 20, 10.43)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (57, N'green czech lampwork flower', N'beads', 20, 22.39)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (58, N'Spider charm', N'charms', 30, 14.09)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (59, N'Acryllic butterfly transparent', N'beads', 20, 25.03)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (60, N'czech glass purple star', N'beads', 20, 14.46)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (61, N'Pearl Bowknot', N'beads', 50, 8.85)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (62, N'Cinnamoroll Resin', N'charms', 10, 39.78)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (63, N'My melody resin', N'charms', 10, 40.05)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (64, N'Hello Kitty Hollow', N'charms', 20, 26.15)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (65, N'Heart keychain', N'Keychains', 10, 50.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (66, N'Rhinestone spacer', N'beads', 200, 3.14)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (67, N'Metal hollow flower', N'beads', 60, 8.9)
INSERT [dbo].[RawMaterial] ([mat_id], [name], [type], [quantity], [cost]) VALUES (68, N'Pearl hearts', N'beads', 50, 7.07)
SET IDENTITY_INSERT [dbo].[RawMaterial] OFF
GO
SET IDENTITY_INSERT [dbo].[Supplier] ON 

INSERT [dbo].[Supplier] ([supplier_id], [name], [contact]) VALUES (1, N'saddar', N'923331234567')
INSERT [dbo].[Supplier] ([supplier_id], [name], [contact]) VALUES (2, N'beadify', N'923123345561')
INSERT [dbo].[Supplier] ([supplier_id], [name], [contact]) VALUES (3, N'daraz', N'923156489186')
INSERT [dbo].[Supplier] ([supplier_id], [name], [contact]) VALUES (4, N'aliexpress', N'923231654878')
SET IDENTITY_INSERT [dbo].[Supplier] OFF
GO
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Ahad001234', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Ahoor00890', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Alishba456', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Amna001234', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Aqleema002', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Areesha003', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Bakhtiar01', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Ezzah00678', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Farwa00912', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Fatima0012', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Fatima0023', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Fatima0091', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Hamdan0098', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Hania01234', N'Pass1234', N'admin')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Hareem0087', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Mahnoor012', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Maria00123', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Mariam0034', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Maziyah045', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Muhamma004', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Musfirah45', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Noor009123', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Rahimeen02', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Sajal01234', N'Pass1234', N'admin')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Shaaf01234', N'Pass1234', N'admin')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Shahj00123', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Sidra00789', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Syeda00123', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Wania00987', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Zainab0098', N'Pass1234', N'customer')
INSERT [dbo].[User] ([username], [password], [role]) VALUES (N'Zobiya0056', N'Pass1234', N'customer')
GO
INSERT [dbo].[UserAdmin] ([username], [employee_id]) VALUES (N'Shaaf01234', 2)
INSERT [dbo].[UserAdmin] ([username], [employee_id]) VALUES (N'Sajal01234', 1)
INSERT [dbo].[UserAdmin] ([username], [employee_id]) VALUES (N'Hania01234', 3)
GO
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Maria00123', 1)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Aqleema002', 2)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Areesha003', 3)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Muhamma004', 4)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Zobiya0056', 5)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Ezzah00678', 6)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Sidra00789', 7)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Ahoor00890', 8)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Bakhtiar01', 9)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Rahimeen02', 10)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Mariam0034', 11)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Wania00987', 12)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Ahad001234', 13)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Shahj00123', 14)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Fatima0012', 15)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Fatima0023', 16)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Mahnoor012', 17)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Noor009123', 18)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Syeda00123', 19)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Maziyah045', 20)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Amna001234', 21)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Alishba456', 22)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Zainab0098', 23)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Hareem0087', 24)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Farwa00912', 25)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Musfirah45', 26)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Hamdan0098', 27)
INSERT [dbo].[UserCustomer] ([username], [customer_id]) VALUES (N'Fatima0091', 28)
GO
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-01' AS Date), 50)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-02' AS Date), 60)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-03' AS Date), 45)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-04' AS Date), 30)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-05' AS Date), 70)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-06' AS Date), 80)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-07' AS Date), 55)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-08' AS Date), 65)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-09' AS Date), 75)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-10' AS Date), 40)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-11' AS Date), 90)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-12' AS Date), 95)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-13' AS Date), 100)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-14' AS Date), 85)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-15' AS Date), 120)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-16' AS Date), 130)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-17' AS Date), 110)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-18' AS Date), 60)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-19' AS Date), 45)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-20' AS Date), 55)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-21' AS Date), 150)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-22' AS Date), 135)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-23' AS Date), 125)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-24' AS Date), 140)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-25' AS Date), 80)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-26' AS Date), 70)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-27' AS Date), 60)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-28' AS Date), 55)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-29' AS Date), 65)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-30' AS Date), 85)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-01-31' AS Date), 100)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-01' AS Date), 50)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-02' AS Date), 75)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-03' AS Date), 90)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-04' AS Date), 60)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-05' AS Date), 40)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-06' AS Date), 70)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-07' AS Date), 55)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-08' AS Date), 85)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-09' AS Date), 95)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-10' AS Date), 110)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-11' AS Date), 120)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-12' AS Date), 65)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-13' AS Date), 45)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-14' AS Date), 70)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-15' AS Date), 55)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-16' AS Date), 75)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-17' AS Date), 85)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-18' AS Date), 60)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-19' AS Date), 65)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-20' AS Date), 80)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-21' AS Date), 95)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-22' AS Date), 100)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-23' AS Date), 105)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-24' AS Date), 110)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-25' AS Date), 115)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-26' AS Date), 120)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-27' AS Date), 85)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-28' AS Date), 90)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-02-29' AS Date), 95)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-01' AS Date), 130)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-02' AS Date), 140)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-03' AS Date), 150)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-04' AS Date), 160)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-05' AS Date), 170)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-06' AS Date), 180)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-07' AS Date), 190)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-08' AS Date), 200)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-09' AS Date), 210)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-10' AS Date), 220)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-11' AS Date), 230)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-12' AS Date), 240)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-13' AS Date), 250)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-14' AS Date), 260)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-15' AS Date), 270)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-16' AS Date), 280)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-17' AS Date), 290)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-18' AS Date), 300)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-19' AS Date), 310)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-20' AS Date), 320)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-21' AS Date), 330)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-22' AS Date), 340)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-23' AS Date), 350)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-24' AS Date), 360)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-25' AS Date), 370)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-26' AS Date), 380)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-27' AS Date), 390)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-28' AS Date), 400)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-29' AS Date), 410)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-30' AS Date), 420)
INSERT [dbo].[Visitors] ([date], [count]) VALUES (CAST(N'2024-03-31' AS Date), 430)
GO
/****** Object:  Index [UQ__Address__CAA247C9980F830A]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[Address] ADD UNIQUE NONCLUSTERED 
(
	[address_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__Admin__C52E0BA97816759F]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[Admin] ADD UNIQUE NONCLUSTERED 
(
	[employee_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__Cart__CD65CB84F3C1B5D0]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[Cart] ADD UNIQUE NONCLUSTERED 
(
	[customer_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__Company__3E2672347FFABC93]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[Company] ADD UNIQUE NONCLUSTERED 
(
	[company_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__Customer__CD65CB8433C0A3D8]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[Customer] ADD UNIQUE NONCLUSTERED 
(
	[customer_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__Delivery__031491A9A47C8886]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[DeliveryCharges] ADD UNIQUE NONCLUSTERED 
(
	[city_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__Orders__46596228B64E17EC]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[Orders] ADD UNIQUE NONCLUSTERED 
(
	[order_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__PaymentI__ED1FC9EBEBA23E2B]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[PaymentInfo] ADD UNIQUE NONCLUSTERED 
(
	[payment_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__Product__56958AB33749D36C]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[Product] ADD UNIQUE NONCLUSTERED 
(
	[prod_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__Promotio__84EB4CA4313540A7]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[Promotions] ADD UNIQUE NONCLUSTERED 
(
	[promo_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__RawMater__FCB3E526B9AB0863]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[RawMaterial] ADD UNIQUE NONCLUSTERED 
(
	[mat_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__Supplier__6EE594E98287AE09]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[Supplier] ADD UNIQUE NONCLUSTERED 
(
	[supplier_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__User__F3DBC57265F97DE7]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[User] ADD UNIQUE NONCLUSTERED 
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [UQ__Visitors__D9DE21FD41A77D53]    Script Date: 17/12/2024 11:59:58 ******/
ALTER TABLE [dbo].[Visitors] ADD UNIQUE NONCLUSTERED 
(
	[date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[CartItems]  WITH CHECK ADD  CONSTRAINT [CartItems_fk0] FOREIGN KEY([customer_id])
REFERENCES [dbo].[Cart] ([customer_id])
GO
ALTER TABLE [dbo].[CartItems] CHECK CONSTRAINT [CartItems_fk0]
GO
ALTER TABLE [dbo].[CartItems]  WITH CHECK ADD  CONSTRAINT [CartItems_fk1] FOREIGN KEY([prod_id])
REFERENCES [dbo].[Product] ([prod_id])
GO
ALTER TABLE [dbo].[CartItems] CHECK CONSTRAINT [CartItems_fk1]
GO
ALTER TABLE [dbo].[CompanyPromotion]  WITH CHECK ADD  CONSTRAINT [CompanyPromotion_fk0] FOREIGN KEY([comany_id])
REFERENCES [dbo].[Company] ([company_id])
GO
ALTER TABLE [dbo].[CompanyPromotion] CHECK CONSTRAINT [CompanyPromotion_fk0]
GO
ALTER TABLE [dbo].[CompanyPromotion]  WITH CHECK ADD  CONSTRAINT [CompanyPromotion_fk1] FOREIGN KEY([promotion_id])
REFERENCES [dbo].[Promotions] ([promo_id])
GO
ALTER TABLE [dbo].[CompanyPromotion] CHECK CONSTRAINT [CompanyPromotion_fk1]
GO
ALTER TABLE [dbo].[CompanyUser]  WITH CHECK ADD  CONSTRAINT [CompanyUser_fk0] FOREIGN KEY([company_id])
REFERENCES [dbo].[Company] ([company_id])
GO
ALTER TABLE [dbo].[CompanyUser] CHECK CONSTRAINT [CompanyUser_fk0]
GO
ALTER TABLE [dbo].[CompanyUser]  WITH CHECK ADD  CONSTRAINT [CompanyUser_fk1] FOREIGN KEY([username])
REFERENCES [dbo].[User] ([username])
GO
ALTER TABLE [dbo].[CompanyUser] CHECK CONSTRAINT [CompanyUser_fk1]
GO
ALTER TABLE [dbo].[CompanyVistors]  WITH CHECK ADD  CONSTRAINT [CompanyVistors_fk0] FOREIGN KEY([company_id])
REFERENCES [dbo].[Company] ([company_id])
GO
ALTER TABLE [dbo].[CompanyVistors] CHECK CONSTRAINT [CompanyVistors_fk0]
GO
ALTER TABLE [dbo].[CompanyVistors]  WITH CHECK ADD  CONSTRAINT [CompanyVistors_fk1] FOREIGN KEY([date])
REFERENCES [dbo].[Visitors] ([date])
GO
ALTER TABLE [dbo].[CompanyVistors] CHECK CONSTRAINT [CompanyVistors_fk1]
GO
ALTER TABLE [dbo].[CustomerAddress]  WITH NOCHECK ADD  CONSTRAINT [CustomerAddress_fk0] FOREIGN KEY([customer_id])
REFERENCES [dbo].[Customer] ([customer_id])
GO
ALTER TABLE [dbo].[CustomerAddress] CHECK CONSTRAINT [CustomerAddress_fk0]
GO
ALTER TABLE [dbo].[CustomerAddress]  WITH NOCHECK ADD  CONSTRAINT [CustomerAddress_fk1] FOREIGN KEY([address_id])
REFERENCES [dbo].[Address] ([address_id])
GO
ALTER TABLE [dbo].[CustomerAddress] CHECK CONSTRAINT [CustomerAddress_fk1]
GO
ALTER TABLE [dbo].[CustomerPaymentInfo]  WITH NOCHECK ADD  CONSTRAINT [CustomerPaymentInfo_fk0] FOREIGN KEY([customer_id])
REFERENCES [dbo].[Customer] ([customer_id])
GO
ALTER TABLE [dbo].[CustomerPaymentInfo] CHECK CONSTRAINT [CustomerPaymentInfo_fk0]
GO
ALTER TABLE [dbo].[CustomerPaymentInfo]  WITH NOCHECK ADD  CONSTRAINT [CustomerPaymentInfo_fk1] FOREIGN KEY([payment_id])
REFERENCES [dbo].[PaymentInfo] ([payment_id])
GO
ALTER TABLE [dbo].[CustomerPaymentInfo] CHECK CONSTRAINT [CustomerPaymentInfo_fk1]
GO
ALTER TABLE [dbo].[MaterialSupplier]  WITH NOCHECK ADD  CONSTRAINT [MaterialSupplier_fk0] FOREIGN KEY([mat_id])
REFERENCES [dbo].[RawMaterial] ([mat_id])
GO
ALTER TABLE [dbo].[MaterialSupplier] CHECK CONSTRAINT [MaterialSupplier_fk0]
GO
ALTER TABLE [dbo].[MaterialSupplier]  WITH NOCHECK ADD  CONSTRAINT [MaterialSupplier_fk1] FOREIGN KEY([supplier_id])
REFERENCES [dbo].[Supplier] ([supplier_id])
GO
ALTER TABLE [dbo].[MaterialSupplier] CHECK CONSTRAINT [MaterialSupplier_fk1]
GO
ALTER TABLE [dbo].[OrderDetails]  WITH NOCHECK ADD  CONSTRAINT [OrderDetails_fk0] FOREIGN KEY([order_id])
REFERENCES [dbo].[Orders] ([order_id])
GO
ALTER TABLE [dbo].[OrderDetails] CHECK CONSTRAINT [OrderDetails_fk0]
GO
ALTER TABLE [dbo].[OrderDetails]  WITH NOCHECK ADD  CONSTRAINT [OrderDetails_fk1] FOREIGN KEY([prod_id])
REFERENCES [dbo].[Product] ([prod_id])
GO
ALTER TABLE [dbo].[OrderDetails] CHECK CONSTRAINT [OrderDetails_fk1]
GO
ALTER TABLE [dbo].[Orders]  WITH NOCHECK ADD  CONSTRAINT [Orders_fk1] FOREIGN KEY([customer_id])
REFERENCES [dbo].[Customer] ([customer_id])
GO
ALTER TABLE [dbo].[Orders] CHECK CONSTRAINT [Orders_fk1]
GO
ALTER TABLE [dbo].[UserAdmin]  WITH NOCHECK ADD  CONSTRAINT [UserAdmin_fk0] FOREIGN KEY([username])
REFERENCES [dbo].[User] ([username])
GO
ALTER TABLE [dbo].[UserAdmin] CHECK CONSTRAINT [UserAdmin_fk0]
GO
ALTER TABLE [dbo].[UserAdmin]  WITH NOCHECK ADD  CONSTRAINT [UserAdmin_fk1] FOREIGN KEY([employee_id])
REFERENCES [dbo].[Admin] ([employee_id])
GO
ALTER TABLE [dbo].[UserAdmin] CHECK CONSTRAINT [UserAdmin_fk1]
GO
ALTER TABLE [dbo].[UserCustomer]  WITH NOCHECK ADD  CONSTRAINT [UserCustomer_fk0] FOREIGN KEY([username])
REFERENCES [dbo].[User] ([username])
GO
ALTER TABLE [dbo].[UserCustomer] CHECK CONSTRAINT [UserCustomer_fk0]
GO
ALTER TABLE [dbo].[UserCustomer]  WITH NOCHECK ADD  CONSTRAINT [UserCustomer_fk1] FOREIGN KEY([customer_id])
REFERENCES [dbo].[Customer] ([customer_id])
GO
ALTER TABLE [dbo].[UserCustomer] CHECK CONSTRAINT [UserCustomer_fk1]
GO
USE [master]
GO
ALTER DATABASE [safatique] SET  READ_WRITE 
GO
