# PostgreSQL
Two ways to interact w/ postgres
- thru bash shell
- thru script

## Bash shell
init: `psql -U postgres -h localhost`

list all databois: `\l`

connect to a databoi: `\c database_name;`

make data table: `create table tablename`;

add data to table: `insert into tablename value(row_data, row_data....);`

drop table: `drop table tablename;`

check if table exists first: `drop table if exists tablename;`

add condition to query: `select * from studentTable where (gpa > 3.7 and sizeHS < 1000);`

only select certain attrs: `select sID, decision from Apply;`

order result: `select major, decision from Apply order by major;`

select unique values: `select distinct major, decision from Apply;`

making a table
```sql
create table Tablename (
    colName1  int,
    colName2  text,
    etc..
)
```

## SQL Script
Create file with `.sql` extension. Same syntax as bash terminal

Sample

```sql
-- comment
\echo "listing databois"
\list
\echo "connecting to potato databoi"
\c potato
\echo "*** SELECT * FROM foo ***"
SELECT * FROM foo
\quit
```

Execute using `psql -U postgres -f filename.sql`
Save to a file using `psql -U postgres -H -f filename.sql > filename.html`

## Joining
### Cross-join
```sql
-- join every row of Student to every row of Apply
select *
    from Student cross join Apply
    order by Student.sId;
```

### Inner-join
```sql
-- join every row of Student that has same sID as row from Apply
select *
    from Student
    inner join Apply using (sId);
```

OR 

```sql
-- join every row of Student that has same sID as row from Apply
select *
    from Student
    inner join Apply on Student.sID = Apply.sID;
```

```sql
-- join row of Student that has same sID as row from Apply
-- if row of Student satisfies conditions
select *
    from Student
    inner join Apply using (sId)
    where (sizeHs > 1000) and (major = 'CS') and (decision = false);
```

```sql
-- join row of Student that has same sID as row from Apply
-- then join to College that has same cName as row from Apply
select *
    from Student
    inner join Apply using (sId)
    inner join College using (cName)
```

### Natural-join
Combines rows from two tables when columns of common attrs have same values

### Left-join
Combines all rows from left table with matching rows from right, if any, else
only left values

```sql
select *
    from R
    left join S
    on R.A = S.B;
```