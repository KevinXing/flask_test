drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  ext time not null default current_timestamp,
  amount integer not null,
  price integer not null
);

