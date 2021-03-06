select "hello world";
select 1+2;

-- 한줄 주석
 
/* 여러줄 주석시작
여러줄 주석 끝 */




-- 가장 기본: select 칼럼명 from 테이블
select id, name, CountryCode from city;

-- 파이썬에서의 head와 같은 기능: limit
select code, name from country limit 5; 

-- 정렬 기능: order by
select id, name, CountryCode from city order by name, id; 

-- 범위 선택: offset x = x부터 가져오겠다
select id, name, CountryCode from city limit 10 offset 10; 

-- 행의 개수 새기 count (*)
select count(*) from city;

-- 이름 바꿔서 가져오기 (원본 유지): 칼럼명 as 변경이름
select id,name, CountryCode as code from city;

-- limit 제한을 두기 전에 order by 가 앞으로 와야 함
select * from city order by name limit 5;

/* 칼럼을 불러올 때 바로 숫자 연산해서 단위를 바꿀 수 있음
   그리고 order by 칼럼명 desc 로 내림차순 정렬도 가능함  */
select id, name, Population / 1000 as pop from city order by pop desc; 

-- 조건검색: where
select name, population as p  from country
where p < 1000 and p>5000 
order by p desc;
-- 위에 조건과 같은 조건: 몇과 몇 사이에는 bwtween 사용 가능
select name, population as p  from country
where p between 5000 and 10000
order by p desc;

-- 퀴즈1: 인구가 천명에서 5천명 사이의 도시는?
select name, population as p from city
where p between 1000 and 5000
order by p;

-- 문자열 조건 검색: %를 조건 기점으로 함
-- island로 끝나는 것
select * from country where name like '%island';

-- 두번째 글자가 a 인것
select * from country where name like '_a%';

-- 특정 칼럼내에 값에 속하는 것 
select * from country where continent in ('Asia','Europe');

-- 퀴즈: 지역코드 'AIA','ABG'인 도시를 인구 내림차순으로 5개를 알고싶어요
select Name, Population, CountryCode as code from city
where code in ('AIA','ARG')
order by Population desc limit 5; 

-- 중복제거: distinct
select distinct CountryCode from city;

-- 서브쿼리
select count(*) from (select code, name, continent from country);

select count(name) 
from (select code, name, continent from country where continent in ('Asia'));




/********** 테이블 생성 **********/
create table test(
    a INT,
    b TEXT,
    c TEXT
);

--sqlite에서 테이블 확인하는 쿼리
select * from sqlite_master where type = 'table';
select * from sqlite_master;

-- 데이터 (행) 추가
insert into test values(1,'aaa','bbb');
select * from test;

insert into test values(2,'ann','hyun');
select * from test;

insert into test (b,c) values ('cccc','dddd');
select * from test;

-- 데이터(행) 삭제 : 꼭 임시테이블 작업을 해야 함
delete from test2 where a is null;

--테이블 함부로 변경하거나 지우지 말것
create table test2(a INT, b TEXT, c TEXT);

--데이터(행) 추가: 한번에 다른 table을 추가
insert into test2 (a,b,c) select a,b,c from test;
select * from test2;

--테이블 삭제
drop table test2;

--데이터 갱신
update test2 set a = 0 ,b = '000' where a is not null;



/********** 쿼리 실습 **********/
drop table user;
create table user (
    id integer primary key autoincrement, --autoincrement: 자동으로 1씩증가
    name varchar(50) not null, --varchar는 가변 문자열: 입력문자열에따라 먹는 메모리가 달라짐
    adress varchar(255),
    email varchar(255) not null
);

drop table product;
create table product (
    id integer primary key autoincrement,
    name varchar(50) not null,
    price integer not null default 0,
    desc varchar(255)
);

-- 테이블 칼럼 추가 또는 속성 변경 : alter table
ALTER TABLE product ADD COLUMN star int default 0;

--Foreign KEY 는 일종의 방어책이다. 
drop table order_product;
create table order_product(
    id             integer primary key autoincrement,
    product_id     integer,
    user_id        integer,
    count          integer,
    created_date   text,
    FOREIGN KEY(product_id) REFERENCES product(id),
    FOREIGN KEY(user_id) REFERENCES user(id)
);

--시간 
select datetime('now');

insert into product (name, desc) values ('땅콩','....');
insert into product (name, desc) values ('오징어땅콩','....');
select  * from product;

insert into order_product (product_id, count, created_date)
values (1,1,date('now'));
select * from order_product;

-- join기능
select * from product, order_product;
select * from product, order_product where product.id = order_product.product_id;

insert into user (name, email) values ('Park','a@a.com');
insert into user (name, email) values ('kim','b@a.com');
insert into user (name, email) values ('lee','c@a.com');
select * from user;

insert into order_product (product_id, user_id, count, created_date)
values(1 ,1 ,2 ,date('now'));

-- 퀴즈: 구매자가 어느날 구매했는지?
select name, created_date from user, order_product
where user.id = order_product.user_id;
select * from user, order_product as op where user.id=op.user_id;

--아래 두개가 같은 표현이라고 볼 수 있음
select * from city, country where city.Countrycode = country.Code;
select name, name, population from city, country where city.Countrycode = country.Code;
select city.name, country.name, population from city, country where city.Countrycode = country.Code;

-- 퀴즈: 언제 주문자가 어떤 제품을 몇 개 주문 했는가?
select created_date, user.name, product.name, order_product.count
from user, product, order_product
where order_product.user_id = user.id and product.id = order_product.product_id;

-- View 생성
CREATE VIEW VIEW1 AS select created_date, user.name as uname, product.name as pname, order_product.count
from user, product, order_product
where order_product.user_id = user.id and product.id = order_product.product_id;
--View 생성
select created_date, uname, pname, count from view1;

--관계 테이블에서 갱신과 삭제 오류
delete from product where id=1;
--업데이트로 바꾸는 것은 에러가 일어나지 않음
update product set name = '뉴땅콩' where name = '땅콩';
select * from product;

--join: SQLLite 는 Right join, Full outer join을 지원하지 않음
select * from order_product as op
inner join product on op.product_id = product.id;

/* 기타 연산 함수 */
select date('now');
select 1+2+4;
select date('now'), 1+2+4;
select time('now');
select strftime('%m월 %d일','now');
select min(population), max(population) from city;
select upper(name), lower(name) from city;
