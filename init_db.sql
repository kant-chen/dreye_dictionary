-- CREATE DATABASE dictionary;

CREATE TABLE vocabulary(
   name VARCHAR PRIMARY KEY NOT NULL,
   pronunciation VARCHAR,
   content_zh VARCHAR,
   content_en VARCHAR,
   variant VARCHAR,
   created_at TIMESTAMP,
   updated_at TIMESTAMP
);

