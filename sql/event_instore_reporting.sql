select
  date(ship_date) as `date`,
  `message_table`.`event_type`,
  count(*) as `order_count`,
  sum(o.total) as `total`,
  case when payment_type = 'paypal' then sum(o.total) end as `paypal`,
  case when payment_type = 'credit' then sum(o.total) end as `credit_card`,
  case when payment_type = 'check' then sum(o.total) end as `check`,
  case when payment_type = 'mocc' then sum(o.total) end as `mocc`,
  case when payment_type = 'storecredit' then sum(o.total) end as `storecredit`,
  case when payment_type not in ('paypal', 'credit', 'mocc', 'check') 
    then sum(o.total) end as `unknown_payment_type`
from
  orders o
    inner join (
      select distinct
        order_id,
        case
          when message like "%FNM%" then 'FNM'
          when message like "%Legacy%" then 'Legacy'
          when message like "%modern%" then 'Modern'
          when message like "%2DH%" then '2DH'
          when message like "%Marquee%" then 'Marquee'
          when message like "%LPS%" then 'LPS'
            end as `event_type`
      from
        logposts
      where 
        (
          message like "%FNM%" or 
          message like "%Legacy%" or 
          message like "%modern%" or
          message like "%2DH%" or 
          message like "%Marquee%" or
          message like "%LPS%"
        )
        and date(timestamp) between curdate()-interval 1 week and now()
    ) `message_table` on o.id = `message_table`.order_id
where 
  o.status = 'completed'
  and o.type = 'sale'
  and o.is_pickup = 1
group by `event_type`, `date`
