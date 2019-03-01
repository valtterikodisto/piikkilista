# User Stories
## What is a user story?

> User stories are short, simple descriptions of a feature told 
> from the perspective of the person who desires the new capability, 
> usually a user or customer of the system.
>
> https://www.mountaingoatsoftware.com/agile/user-stories

<br />


| As | I want | So that |
|----|--------|---------|
| User | add a new purchase to a customer | I can log their balance |
| User | deposit euros to customer's account | they can pay their debt
| User | search for a customer | I can inform a customer about his/her balance |
| Admin | add a new organization | only the organization that I approve can have customers |
| Admin | add a new customer | only the customers that I approve can have an account |
| Admin | block users | customers will not misbehave |
| Admin | view customers purchase history | we can examine unclear situations |

## SQL
```SQL
SELECT drink.name, SUM(drink_amount.amount) AS amount FROM customer
INNER JOIN purchase ON purchase.customer_id = customer.id
INNER JOIN drink_amount ON drink_amount.order_id = purchase.id
INNER JOIN drink ON drink.id = drink_amount.drink_id
WHERE customer.id = :[ID HERE]
GROUP BY drink.name
ORDER BY amount DESC
```
```SQL
SELECT AVG(purchase.total) AS average FROM organization
INNER JOIN customer ON customer.organization_id = organization.id
INNER JOIN purchase ON purchase.customer_id = customer.id
WHERE organization_id = [ID HERE]
```
