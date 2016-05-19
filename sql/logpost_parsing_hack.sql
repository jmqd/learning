-- If there were an obfuscated SQL contest... I might submit this. :P

select
(select name from products where id = `product_id_new_price`.`new_id`) as `product_id`,
(select rarity from cfields where product_id = `product_id_new_price`.`new_id`) as `rarity`,
`product_id_new_price`.`new_price`,
`previous_price`.`prev_price`,
round(`product_id_new_price`.`new_price` - `previous_price`.`prev_price`,2) as `absolute_change_in_price`,
round(((`product_id_new_price`.`new_price` - `previous_price`.`prev_price`)  / `product_id_new_price`.`new_price`)*100,2) as `pct_change_in_price`,
`product_id_new_price`.`repricer` as `repriced_by`
from
(select 
  product_id as `new_id`,
  user as `repricer`,
  timestamp as `reprice_date`,
  substring_index(group_concat(cast(substring_index(
                                    message, 'Repriced to ', -1) 
                               as decimal(10,2)) 
                  order by timestamp asc),
    ',', -1) as `new_price`
from logposts lp
where 
  lp.product_id in (
  (
    select
      id
    from 
      products p
    where 
      is_active = 1 and 
      is_template = 0 and 
      p.model in ('mtg_card') and 
      p.primary_category_id != 2833 and 
      repriced_on is not null and 
      repriced_on >= curdate() - interval 7 day
  )
) and 
  timestamp >= curdate() - interval 7 day and 
  access_point = "admin/products/browse" and 
  message like "Repriced%"
group by product_id
  ) as `product_id_new_price`,
(
  select 
    product_id as `prev_id`,
    max(timestamp) as `max_ts`,
    cast(substring_index(message, 'Repriced to ', -1) 
        as decimal(10,2)) 
          as `prev_price`
  from
    logposts lp
where 
  lp.product_id in (
  (
    select
      id
    from 
      products p
    where 
      is_active = 1 and 
      is_template = 0 and 
      p.model in ('mtg_card') and 
      p.primary_category_id != 2833 and
      repriced_on is not null and 
      repriced_on >= curdate() - interval 7 day
  )
) and 
  timestamp < curdate() - interval 7 day and 
  access_point = "admin/products/browse" and 
  message like "Repriced%" and
  timestamp = (select max(timestamp) 
               from logposts 
               where 
                  product_id = lp.product_id and 
                  timestamp < curdate() - interval 7 day and 
                  access_point = "admin/products/browse" and 
                  message like "Repriced%"
                )
group by product_id
    ) as `previous_price`
where `prev_id` = `new_id`
group by `product_id`
