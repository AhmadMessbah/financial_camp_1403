create DATABASE Acc;
#--------------------***etelaat personel dar in table zakhire mishe***--------------------------
    create table acc.__person__
    (
        id int primary key auto_increment,
            name varchar (30),
        family       varchar(30)
    );

#--------------------***etelaat tarakonesh ha dar in table zakhire mishe***--------------------------
    create table acc.__transaction__
    (
        id int primary key auto_increment,
        pid int(20),
        type int (10),
        datetime datetime
    );
#--------------------***in dastor yek fk ba table personel ejad mikone ***--------------------------
alter table acc.__transaction__
    add constraint __person_____transaction____fk
        foreign key (pid) references __person__ (id);

#--------------------***etelaat login dar in table zakhire mishe***--------------------------
create table acc.__pusers__
    (
        id int primary key auto_increment,
        pid int(20),
        username varchar (50),
        password varchar(50)
    );
#--------------------***in dastor yek fk ba table personel ejad mikone ***--------------------------
alter table acc.__pusers__
    add constraint __person_____pusers____fk
        foreign key (pid) references __person__ (id);

#--------------------------------------------------------------------
CREATE PROCEDURE `sp_Insert_person_in_pusers_nf`()
BEGIN

insert into Acc.__pusers__( pid, username, password)
    select id
	    ,family
	    ,family
    from acc.__person__ ;
end;
#--------------------------------------------------------------------
insert into Acc.__pusers__
value(1,1,"admin","admin")