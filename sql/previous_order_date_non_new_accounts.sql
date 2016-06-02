select
  o.account_id,
  `previous`.`order_date`
from
  orders o
  inner join accounts ac on o.`account_id` = ac.id
  inner join orders `previous` on (
    o.`account_id` = `previous`.`account_id`
    and o.order_date > `previous`.`order_date`
  )
where
  o.status = 'completed'
  and o.`type` = 'sale'
  and o.`is_pickup` = 0
  and o.`order_date` > curdate() - interval 2 day
  and o.`email` <> 'transfer@cardkingdom.com'
  and o.account_id != 0
  and `previous`.`order_date` = (
    select 
      max(`order_date`)
    from
      orders
    where
      order_date < o.`order_date`
      and account_id = `previous`.`account_id`
      and o.`type` = 'sale'
      and o.`status` = 'completed'
      and o.`is_pickup` = 0
      and o.`email` <> 'transfer@cardkingdom.com'
  )
