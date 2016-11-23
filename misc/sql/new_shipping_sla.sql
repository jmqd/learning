select  
  case 
      when time(t3.ready_on) <= '12:00:00' then 'Morning'
      when time(t3.ready_on) between '12:00:01' and '17:00:00' then 'Afternoon'
      when time(t3.ready_on) > '17:00:00' then 'Evening'
  end as `readied_during`,
  count(*) as `total`,
  sum(
    case
      when 
        date(t3.ready_on) = date(ship_date)
        and time(t3.ready_on) <= '12:00:00'
        and time(t3.ship_date) <= '16:00:00'
          then 1
      when 
        date(t3.ready_on) = date(t3.ship_date)
        and time(t3.ready_on) between '12:00:01' and '17:00:00'
          then 1
      when
        time(t3.ready_on) > '17:00:00' 
        and ship_date <= date(ready_on) + interval 1 day + interval '16:00:00' hour_second
          then 1
      else 0 
    end
  ) as `met_sla`
from
(
  select
    id,
    ready_on,
    ship_date
  from  
    orders o
  where
    o.ready_on is not null and
    o.ready_on != '' and
    date(o.`ship_date`) = date(curdate() - interval 1 day)
    and o.`is_selling`  = 0
    and o.is_pickup     = 0
    and o.status        = 'completed'
    and o.is_paid       = 1
    and o.account_id    not in (182520, 0)
    and location_id     = 0
) as t3
group by `readied_during`
order by field(`readied_during`, 'Morning','Afternoon','Evening')
