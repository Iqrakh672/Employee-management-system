
use happy;
create table  employee(
e_id int not null,
e_name varchar(20),
e_salary int,
e_age int,
e_gender varchar(20),
e_dept varchar(20),
primary key(e_id)
);
insert into employee values(1,'iqra',200000,20,'f','cs');
insert into employee values(2,'samad',1000000,19,'m','it');
insert into employee values(3,'bilal',30000,21,'m','elec');
insert into employee values(4,'ibraheem',200000,20,'f','cs');
insert into employee values(5,'aamna',30000,20,'f','analytics');
insert into employee values(6,'sania',2000,28,'m','operations');
select distinct e_gender from employee;--removes duplicate 
update employee set e_salary=90000000 where  e_name='samad' and e_name ='iqra';
select * from employee
select avg(e_age) from employee;
select upper(e_name) from employee;
select lower(e_name) from employee;
select substring(e_name,2,2) from employee;
select e_name from employee order by e_salary desc; 
select avg(e_salary) , e_gender from employee group by e_gender;
--CRUD OPERATIONS
 create table test(
 name varchar(20),
 age int ,
 sex varchar(6));
 select * from test
 insert into test values('iqra',20,'f');
 insert into test values('aamna',20,'f');
 insert into test values('sara',21,'f');
 insert into test values('samad',19,'m');
 insert into test values('ibrahim',19,'m');
  update test set age=19 where name='iqra';
  delete from test where name='sara';

  select * into emptest from employee
  select * from emptest
  truncate table emptest
  insert all into emptest(e_name) values(e_name)
  -- if you want to delete entire table
  truncate table test
  select * from test
  drop database demo;