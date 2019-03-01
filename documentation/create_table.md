# CREATE TABLE -lauseet
## Drink
```SQL
CREATE TABLE drink (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  name VARCHAR(20),
  price INTEGER,
  PRIMARY KEY (id)
)
```
## Organization
```SQL
CREATE TABLE organization (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
)
```

## User
```SQL
CREATE TABLE account (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  username VARCHAR(144) NOT NULL,
  password VARCHAR(144) NOT NULL,
  admin BOOLEAN NOT NULL,
  PRIMARY KEY (id),
  CHECK (admin IN (0,1))
)
```

## Customer
```SQL
CREATE TABLE customer (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  organization_id INTEGER NOT NULL, 
  first_name VARCHAR(50) NOT NULL, 
  last_name VARCHAR(50) NOT NULL, 
  birthday INTEGER NOT NULL, 
  balance INTEGER NOT NULL, 
  PRIMARY KEY (id), 
  FOREIGN KEY(organization_id) REFERENCES organization (id)
)
```

## Order
```SQL
CREATE TABLE purchase (
  id INTEGER NOT NULL, 
  date_created DATETIME, 
  date_modified DATETIME, 
  customer_id INTEGER, 
  user_id INTEGER, 
  total INTEGER, 
  deposit INTEGER, 
  PRIMARY KEY (id), 
  FOREIGN KEY(customer_id) REFERENCES customer (id), 
  FOREIGN KEY(user_id) REFERENCES account (id)
)
```

## Block
```SQL
CREATE TABLE block (
  id INTEGER NOT NULL, 
  customer_id INTEGER NOT NULL, 
  date_start DATETIME, 
  date_end DATETIME NOT NULL, 
  PRIMARY KEY (id), 
  FOREIGN KEY(customer_id) REFERENCES customer (id)
)
```