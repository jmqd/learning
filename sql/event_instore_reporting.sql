select
  date(ship_date) as `date`,
  `message_table`.`event_type`,
  count(*) as `order_count`,
  sum(o.total) as `total`,
  sum(case when p.type = 'paypal' then p.amount else 0 end) as `paypal`,
  sum(case when p.type = 'credit' then p.amount else 0 end) as `credit_card`,
  sum(case when p.type = 'storecredit' then p.amount else 0 end) as `storecredit`,
  sum(case when p.type = 'mocc' then p.amount else 0 end) as `mocc`
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
          when (message like "%LPS%" or message like "%Tuesday%") then 'Tuesday'
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
        and date(timestamp) between curdate() - interval 1 week and now()
    ) `message_table` on o.id = `message_table`.order_id
    inner join payments p on o.id = p.`order_id`
where
  o.status = 'completed'
  and o.type = 'sale'
  and o.is_pickup = 1
group by `event_type`, `date`
order by `date`
