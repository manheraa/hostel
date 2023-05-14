create database manu;
use manu;
create table student(
Email varchar(30) not null,
passwd varchar(300) not null,
student_id varchar(30),
fname varchar(30) not null ,lname varchar(30) not null,
phone varchar(30) not null,sex varchar(30) not null,
age int not null,address varchar(30) not null,
course varchar(30) not null,primary key(student_id,Email)
);
create table fees(
student_id varchar(30) not null,
mess_fees int null,
room_fees int null,
arrival_date DATE null,
departure_date DATE null,mess_validity int null,
foreign key(student_id) references student(student_id));
select * from fees;
create table mess(student_id varchar(30) not null,bulding_id varchar(30) not null
,foreign key(student_id) references student(student_id));

create table rooms(ROOM_ID varchar(30) not null,no_of_students int,gender varchar(30),primary key(ROOM_ID));
create table bulding(bulding_id int,room_id varchar(30),no_of_students int,foreign key(room_id) references rooms(ROOM_ID));
create table hostel(bulding_id varchar(30) primary key,building_name varchar(30),no_of_rooms int);
create table booked(student_id varchar(30),room_id varchar(30),
foreign key(student_id) references student(student_id),foreign key(room_id) references rooms(ROOM_ID));
insert into bulding values('01','01',0);
insert into bulding values('01','02',0);
insert into bulding values('01','03',0);
insert into bulding values('01','04',0);
insert into bulding values('01','05',0);
insert into bulding values('01','06',0);
insert into bulding values('01','07',0);
insert into bulding values('01','08',0);
insert into bulding values('01','09',0);
insert into bulding values('01','10',0);
insert into bulding values('02','11',0);
insert into bulding values('02','12',0);
insert into bulding values('02','13',0);
insert into bulding values('02','14',0);
insert into bulding values('02','15',0);
insert into bulding values('02','16',0);
insert into bulding values('02','17',0);
insert into bulding values('02','18',0);
insert into bulding values('02','19',0);
insert into bulding values('02','20',0);
select * from bulding;
insert into rooms values('01','0','M');
insert into rooms values('02','0','M');
insert into rooms values('03','0','M');
insert into rooms values('04','0','M');
insert into rooms values('05','0','M');
insert into rooms values('06','0','M');
insert into rooms values('07','0','M');
insert into rooms values('08','0','M');
insert into rooms values('09','0','M');
insert into rooms values('10','0','M');
insert into rooms values('11','0','F');
insert into rooms values('12','0','F');
insert into rooms values('13','0','F');
insert into rooms values('14','0','F');
insert into rooms values('15','0','F');
insert into rooms values('16','0','F');
insert into rooms values('17','0','F');
insert into rooms values('18','0','F');
insert into rooms values('19','0','F');
insert into rooms values('20','0','F');
select * from rooms;
insert into hostel values('01','mens_hostel',10);
insert into hostel values('02','womens_hostel',10);