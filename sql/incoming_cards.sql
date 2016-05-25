select
  date(`lineitems_table`.`added_on`) as `added_on`,
  sum(case when `product_id` not in (203744, 203741) and `category` = 'customer' then `lineitems_table`.`qty` end) as `customer_cards`,
  sum(case when `product_id` not in (203744, 203741) and `category` = 'internal' then `lineitems_table`.`qty` end) as `internal_cards`,
  sum(case when `product_id` in (203744, 203741) then `lineitems_table`.`qty` end) as `bulk_received`
from (
select
  li.product_id as `product_id`,
  li.qty as `qty`,
  date(o.ship_date) as `added_on`,
  case when o.account_id in (0, 309421, 206187, 182520) then 'internal' else 'customer' end as `category`
from
  lineitems li
    join orders o on li.order_id = o.id
where
  o.type = 'purchase'
  and date(o.ship_date) between curdate() - interval 15 month and curdate() - interval 1 day
) as `lineitems_table`
group by `added_on`
