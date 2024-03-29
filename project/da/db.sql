create database mft;

create table mft.person(
    id int primary key auto_increment,
    name varchar(30),
    family varchar(30)
);

create table mft.book(
    id int primary key auto_increment,
    name varchar(30),
    writer varchar(30)
);

create table mft.borrow(
    id int primary key auto_increment,
    person_id int,
    book_id int,
    borrow_date date,
    return_date date
);