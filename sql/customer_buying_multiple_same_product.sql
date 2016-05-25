select
  sum(li.qty) as `boxes`,
  `o`.`account_id`,
  `o`.`id` as `order_id`
from
  orders o
  inner join accounts ac on `o`.`account_id` = `ac`.`id`
  inner join lineitems li on `o`.`id` = `li`.`order_id`
where
  li.`product_id` = 206591
group by account_id
order by `boxes` desc
