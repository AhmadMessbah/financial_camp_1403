create database Acc;

USE [Acc]
GO

/****** Object:  Table [dbo].[__Person__]    Script Date: 3/29/2024 5:59:05 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[__Person__](
	[id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[Name] [nchar](50) NOT NULL,
	[Family] [nchar](50) NOT NULL,
 CONSTRAINT [PK___Person__] PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

USE [mft]
GO

/****** Object:  Table [dbo].[__transaction__]    Script Date: 3/29/2024 6:01:07 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[__transaction__](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[prnid] [int] NOT NULL,
	[Date] [datetime] NOT NULL,
	[type] [int] NOT NULL,
 CONSTRAINT [PK___transaction__] PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

Create TABLE [dbo].[__transaction__]  WITH CHECK ADD  CONSTRAINT [FK___transaction_____Person__] FOREIGN KEY([prnid])
REFERENCES [dbo].[__Person__] ([id])
GO

ALTER TABLE [dbo].[__transaction__] CHECK CONSTRAINT [FK___transaction_____Person__]
GO







