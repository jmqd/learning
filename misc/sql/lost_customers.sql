select distinct 
  `accounts_active_week_of_six_months_ago`.account_id
from 
  orders `accounts_active_week_of_six_months_ago` 
  left outer join (
    select distinct 
      o.account_id 
    from 
      orders o
    where 
      yearweek(o.order_date) between yearweek(curdate() - interval 6 month) and yearweek(curdate()) 
      and o.type = 'sale' 
      and o.status = 'completed'
      and o.`is_pickup` = 0
        ) `accounts_ordered_since`
   on `accounts_active_week_of_six_months_ago`.`account_id` = `accounts_ordered_since`.account_id
where
  yearweek(`accounts_active_week_of_six_months_ago`.order_date) = yearweek(curdate() - interval 6 month - interval 1 week)
  and `accounts_active_week_of_six_months_ago`.type = 'sale' 
  and `accounts_active_week_of_six_months_ago`.status = 'completed'
  and `accounts_active_week_of_six_months_ago`.`is_pickup` = 0
  and `accounts_ordered_since`.account_id is null
