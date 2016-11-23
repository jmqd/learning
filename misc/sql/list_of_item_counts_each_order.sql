select
  `date`,
  group_concat(`items`) as `items`
from (
  select
    date(o.order_date) as `date`,
    sum(li.qty) as `items`
  from
    orders o
    inner join lineitems li on o.id = li.`order_id`
  where
    and o.status = "completed"
    and o.type = "sale"
    and o.is_pickup = 0
  group by o.id
) `order_groups`
group by `date`
