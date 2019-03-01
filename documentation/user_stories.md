# User Stories
## What is a user story?

> User stories are short, simple descriptions of a feature told 
> from the perspective of the person who desires the new capability, 
> usually a user or customer of the system.
>
> https://www.mountaingoatsoftware.com/agile/user-stories

<br />


| # | As | I want | So that |
|-|-|-|-|
| 1 | User | add a new purchase to a customer | I can log their balance |
| 2 | User | deposit euros to customer's account | they can pay their debt
| 3 | User | search for a customer | I can inform a customer about his/her balance |
| 4 | Admin | add a new organization | only the organization that I approve can have customers |
| 5 | Admin | add a new customer | only the customers that I approve can have an account |
| 6 | Admin | block users | customers will not misbehave |
| 7 | Admin | view customers purchase history | we can examine unclear situations |

## SQL

### #1
```SQL
INSERT INTO purchase (customer_id, user_id, total, deposit) VALUES (?, ?, ?, ?)
```
### #2
```SQL
UPDATE customer
SET customer.balance = ?
WHERE customer.id = ?;
```
### #3
```SQL
SELECT * FROM customer
WHERE customer.first_name LIKE '%?%' AND
WHERE customer.last_name LIKE '%?%';
```
### #4
```SQL
INSERT INTO organizaton (name, limit) VALUES (?, ?);
```
### #5
```SQL
INSERT INTO customer (first_name, last_name, birthday, balance, organization_id)
VALUES (?, ?, ?, ?, ?);
```
### #6
```SQL
INSERT INTO block (customer_id, date_end) VALUES (?, ?);
```
### #7
```SQL
SELECT purchase.date_created, purchase.total, purchase.deposit FROM customer
INNER JOIN purchase ON purchase.customer_id = customer.id
WHERE customer.id = ?;
```
