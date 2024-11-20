CREATE TABLE [Company] (
	[company_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[name] nvarchar(4000) NOT NULL,
	[address] nvarchar(4000) NOT NULL,
	[contact] nvarchar(4000) NOT NULL,
	PRIMARY KEY ([company_id])
);

CREATE TABLE [User] (
	[username] char(10) NOT NULL UNIQUE,
	[password] nvarchar(16) NOT NULL,
	[role] nvarchar(4000) NOT NULL,
	PRIMARY KEY ([username])
);

CREATE TABLE [CompanyUser] (
	[company_id] int NOT NULL,
	[username] char(10) NOT NULL
);

CREATE TABLE [Visitors] (
	[date] date NOT NULL UNIQUE,
	[count] int NOT NULL,
	PRIMARY KEY ([date])
);

CREATE TABLE [CompanyVistors] (
	[company_id] int NOT NULL,
	[date] date NOT NULL
);

CREATE TABLE [Customer] (
	[customer_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[firstname] nvarchar(4000) NOT NULL,
	[lastname] nvarchar(4000),
	[email] nvarchar(4000) NOT NULL,
	[phone] nvarchar(4000) NOT NULL,
	PRIMARY KEY ([customer_id])
);

CREATE TABLE [UserCustomer] (
	[username] char(10) NOT NULL,
	[customer_id] int NOT NULL
);

CREATE TABLE [Admin] (
	[employee_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[firstname] nvarchar(4000) NOT NULL,
	[lastname] nvarchar(4000) NOT NULL,
	PRIMARY KEY ([employee_id])
);

CREATE TABLE [UserAdmin] (
	[username] char(10) NOT NULL,
	[employee_id] int NOT NULL
);

CREATE TABLE [Cart] (
	[cart_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[username] char(10) NOT NULL,
	[date_created] date NOT NULL,
	PRIMARY KEY ([cart_id])
);

CREATE TABLE [CustomerCart] (
	[customer_id] int NOT NULL,
	[cart_id] int NOT NULL
);

CREATE TABLE [CartItems] (
	[cart_id] int NOT NULL,
	[prod_id] char(20) NOT NULL,
	[quantity] int NOT NULL,
	[unit_price] int NOT NULL
);

CREATE TABLE [Address] (
	[address_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[address] nvarchar(4000) NOT NULL,
	[city] char(20) NOT NULL,
	PRIMARY KEY ([address_id])
);

CREATE TABLE [CustomerAddress] (
	[customer_id] int NOT NULL,
	[address_id] int NOT NULL
);

CREATE TABLE [PaymentInfo] (
	[payment_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[cardnumber] int NOT NULL,
	[card_cvc] int NOT NULL,
	[card_expiry] date NOT NULL,
	PRIMARY KEY ([payment_id])
);

CREATE TABLE [CustomerPaymentInfo] (
	[customer_id] int NOT NULL,
	[payment_id] int NOT NULL
);

CREATE TABLE [Orders] (
	[order_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[customer_id] int NOT NULL,
	[order_date] date NOT NULL,
	[payment_status] nvarchar(4000) NOT NULL,
	[processing_status] nvarchar(4000) NOT NULL,
	[delivery_method] nvarchar(4000) NOT NULL,
	PRIMARY KEY ([order_id])
);

CREATE TABLE [OrderDetails] (
	[order_id] int NOT NULL,
	[prod_id] char(20) NOT NULL,
	[quantity] int NOT NULL,
	[unit_price] int NOT NULL,
	PRIMARY KEY ([order_id])
);

CREATE TABLE [Supplier] (
	[supplier_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[name] nvarchar(4000) NOT NULL,
	[contact] nvarchar(4000) NOT NULL,
	PRIMARY KEY ([supplier_id])
);

CREATE TABLE [RawMaterial] (
	[mat_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[name] nvarchar(4000) NOT NULL,
	[type] nvarchar(4000) NOT NULL,
	[quantity] int NOT NULL,
	[cost] float NOT NULL,
	PRIMARY KEY ([mat_id])
);

CREATE TABLE [MaterialSupplier] (
	[mat_id] int NOT NULL,
	[supplier_id] int NOT NULL
);

CREATE TABLE [Product] (
	[prod_id] char(20) NOT NULL UNIQUE,
	[name] nvarchar(4000) NOT NULL,
	[price] float NOT NULL,
	[category] nvarchar(4000) NOT NULL,
	[description] nvarchar(4000) NULL,
	[photo_path] nvarchar(4000) NOT NULL,
	PRIMARY KEY ([prod_id])
);

CREATE TABLE [DeliveryCharges] (
	[city_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[city] nvarchar(20) NOT NULL,
	[cost] int NOT NULL,
	PRIMARY KEY ([city_id])
);

CREATE TABLE [Promotions] (
	[promo_id] int IDENTITY(1,1) NOT NULL UNIQUE,
	[name] nvarchar(4000) NOT NULL,
	[description] nvarchar(4000) NOT NULL,
	[discount] float(53) NOT NULL,
	[start_date] date NOT NULL,
	[end_date] date NOT NULL,
	PRIMARY KEY ([promo_id])
);

CREATE TABLE [CompanyPromotion] (
	[comany_id] int NOT NULL,
	[promotion_id] int NOT NULL
);



ALTER TABLE [CompanyUser] ADD CONSTRAINT [CompanyUser_fk0] FOREIGN KEY ([company_id]) REFERENCES [Company]([company_id]);

ALTER TABLE [CompanyUser] ADD CONSTRAINT [CompanyUser_fk1] FOREIGN KEY ([username]) REFERENCES [User]([username]);

ALTER TABLE [CompanyVistors] ADD CONSTRAINT [CompanyVistors_fk0] FOREIGN KEY ([company_id]) REFERENCES [Company]([company_id]);

ALTER TABLE [CompanyVistors] ADD CONSTRAINT [CompanyVistors_fk1] FOREIGN KEY ([date]) REFERENCES [Visitors]([date]);

ALTER TABLE [UserCustomer] ADD CONSTRAINT [UserCustomer_fk0] FOREIGN KEY ([username]) REFERENCES [User]([username]);

ALTER TABLE [UserCustomer] ADD CONSTRAINT [UserCustomer_fk1] FOREIGN KEY ([customer_id]) REFERENCES [Customer]([customer_id]);

ALTER TABLE [UserAdmin] ADD CONSTRAINT [UserAdmin_fk0] FOREIGN KEY ([username]) REFERENCES [User]([username]);

ALTER TABLE [UserAdmin] ADD CONSTRAINT [UserAdmin_fk1] FOREIGN KEY ([employee_id]) REFERENCES [Admin]([employee_id]);

ALTER TABLE [CustomerCart] ADD CONSTRAINT [CustomerCart_fk0] FOREIGN KEY ([customer_id]) REFERENCES [Customer]([customer_id]);

ALTER TABLE [CustomerCart] ADD CONSTRAINT [CustomerCart_fk1] FOREIGN KEY ([cart_id]) REFERENCES [Cart]([cart_id]);
ALTER TABLE [CartItems] ADD CONSTRAINT [CartItems_fk0] FOREIGN KEY ([cart_id]) REFERENCES [Cart]([cart_id]);

ALTER TABLE [CartItems] ADD CONSTRAINT [CartItems_fk1] FOREIGN KEY ([prod_id]) REFERENCES [Product]([prod_id]);
ALTER TABLE [CustomerAddress] ADD CONSTRAINT [CustomerAddress_fk0] FOREIGN KEY ([customer_id]) REFERENCES [Customer]([customer_id]);

ALTER TABLE [CustomerAddress] ADD CONSTRAINT [CustomerAddress_fk1] FOREIGN KEY ([address_id]) REFERENCES [Address]([address_id]);

ALTER TABLE [CustomerPaymentInfo] ADD CONSTRAINT [CustomerPaymentInfo_fk0] FOREIGN KEY ([customer_id]) REFERENCES [Customer]([customer_id]);

ALTER TABLE [CustomerPaymentInfo] ADD CONSTRAINT [CustomerPaymentInfo_fk1] FOREIGN KEY ([payment_id]) REFERENCES [PaymentInfo]([payment_id]);
ALTER TABLE [Orders] ADD CONSTRAINT [Orders_fk1] FOREIGN KEY ([customer_id]) REFERENCES [Customer]([customer_id]);
ALTER TABLE [OrderDetails] ADD CONSTRAINT [OrderDetails_fk0] FOREIGN KEY ([order_id]) REFERENCES [Orders]([order_id]);

ALTER TABLE [OrderDetails] ADD CONSTRAINT [OrderDetails_fk1] FOREIGN KEY ([prod_id]) REFERENCES [Product]([prod_id]);


ALTER TABLE [MaterialSupplier] ADD CONSTRAINT [MaterialSupplier_fk0] FOREIGN KEY ([mat_id]) REFERENCES [RawMaterial]([mat_id]);

ALTER TABLE [MaterialSupplier] ADD CONSTRAINT [MaterialSupplier_fk1] FOREIGN KEY ([supplier_id]) REFERENCES [Supplier]([supplier_id]);


ALTER TABLE [CompanyPromotion] ADD CONSTRAINT [CompanyPromotion_fk0] FOREIGN KEY ([comany_id]) REFERENCES [Company]([company_id]);

ALTER TABLE [CompanyPromotion] ADD CONSTRAINT [CompanyPromotion_fk1] FOREIGN KEY ([promotion_id]) REFERENCES [Promotions]([promo_id]);
