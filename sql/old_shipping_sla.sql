select  
  yearweek(adddate(curdate(), -7), 3) as 'yearweek',
  t2.`total`                                      as 'total',
  t1.`within24hrsReady`/t2.`total`    as 'within24hrsReadyPercent',
  t1.`within24hrsReady`                     as 'within24hrsReadyCount',
  t3.`within24hrsPlaced`/t2.`total`   as 'within24hrsPlacedPercent',
  t3.`within24hrsPlaced`                      as 'within24hrsPlacedCount'
from
(
  select count(*) as `within24hrsReady`
    from    
      orders o
    where   
      yearweek(o.`ship_date`, 3)           = yearweek(adddate(curdate(), -7), 3)
      and   o.`is_selling`                 = 0
      and   o.status                         = 'completed'
      and o.is_paid                      = 1
      and   o.is_pickup                    = 0
      and   o.account_id                    != 182520
      and   ceil(time_to_sec(timediff(
            ship_date, ready_on))/3600) <= 24
      and location_id                    = 0
) as t1,
(
  select count(*) as `total`
  from  
    orders o
  where     
    yearweek(o.`ship_date`, 3) = yearweek(adddate(curdate(), -7), 3)
    and o.`is_selling`        = 0
    and o.is_pickup             = 0
    and o.status              = 'completed'
    and o.is_paid             = 1
    and o.account_id           != 182520
    and o.location_id         = 0
) as t2,
(
  select count(*) as `within24hrsPlaced`
  from  
    orders o
  where     
    yearweek(o.`ship_date`, 3)            = yearweek(adddate(curdate(), -7), 3)
    and o.`is_selling`                    = 0
    and o.is_pickup                       = 0
    and o.status                          = 'completed'
    and o.is_paid                         = 1
    and ceil(time_to_sec(timediff(
          ship_date, order_date))/3600)  <= 24
    and o.account_id                       != 182520
    and location_id                       = 0
) as t3;
