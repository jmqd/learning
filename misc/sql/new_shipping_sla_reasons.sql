select
  t.id as `order_id`,
  `t`.`sla` as `reason`
  from
(select
    t3.id,
    t3.ready_on,
    t3.ship_date,
  case
    when date(t3.ready_on) = date(ship_date)
      and time(t3.ready_on) <= '12:00:00'
      and time(t3.ship_date) <= '16:00:00'
        then 1
    when date(t3.ready_on) = date(t3.ship_date)
      and time(t3.ready_on) between '12:00:01' and '17:00:00'
        then 1
    when time(t3.ready_on) > '17:00:00' 
      and ship_date <= date(ready_on) 
                         + interval 1 day 
                          + interval '16:00:00' hour_second
        then 1
    when time(t3.ready_on) <= '12:00:00' then concat('Morning order -- shipped ', round(timestampdiff(minute, date(ready_on)+interval '16:00:00' hour_second, ship_date)/60,1), ' hour(s) late (', time(ship_date), ')')
    when time(t3.ready_on) between '12:00:01' and '17:00:00' then concat('Afternoon order -- readied at ', t3.ready_on, '; shipped at ', t3.ship_date)
    when time(t3.ready_on) > '17:00:00' then concat('Evening order -- shipped ', round(timestampdiff(minute, date(ready_on)+interval 1 day + interval '16:00:00' hour_second, ship_date)/60,1), ' hour(s) late (', time(ship_date), ')')
    else "A logically impossible state has been reached."
    end as `sla`
from
(
  select
    id,
    ready_on,
    ship_date
  from  
    orders o
  where     
    date(o.`ship_date`) = date(curdate() - interval 1 day)
    and o.`is_selling`  = 0
    and o.ready_on is not null and o.ready_on > ''
    and o.is_pickup     = 0
    and o.status        = 'completed'
    and o.type         != 'transfer'
    and o.is_paid       = 1
    and o.account_id     != 182520
    and location_id     = 0
) as t3) as `t`
where `t`.`sla` != 1
order by `reason`
