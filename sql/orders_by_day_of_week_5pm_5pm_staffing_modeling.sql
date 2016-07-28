/*
  Historical fulfillment work volume. Used for staffing
  modeling. 5pm to 5pm model, for reasonable shipping SLA
  expectations (i.e. orders before 5pm are considered part of
  that day's workload, and any after 5pm are considered part of
  the following day's workload). Provides distribution of 
  fulfillment work load across day of week.
*/
set
  @from_date := '2016-02-01 17:00:00',
  @to_date := '2016-07-25 17:00:00';
select
  `weekday`,
  avg(`orders`) as `avg_orders`,
  avg(`lineitems`) as `avg_lineitems`
from 
(
  select
    case
      when weekday(ready_on + interval 7 hour) = 0 then 'Monday'
      when weekday(ready_on + interval 7 hour) = 1 then 'Tuesday'
      when weekday(ready_on + interval 7 hour) = 2 then 'Wednesday'
      when weekday(ready_on + interval 7 hour) = 3 then 'Thursday'
      when weekday(ready_on + interval 7 hour) = 4 then 'Friday'
      when weekday(ready_on + interval 7 hour) = 5 then 'Saturday'
      when weekday(ready_on + interval 7 hour) = 6 then 'Sunday'
      end as `weekday`,
    count(distinct o.id) as `orders`,
    sum(li.qty) as `lineitems`  
  from
    orders o
  inner join
    lineitems li on o.id = li.order_id
  where
    o.type = 'sale'
    and o.`status` = 'completed'
    and o.`ready_on` between @from_date and @to_date
  group by date(o.ready_on + interval 7 hour)
) as `raw_data`
group by `weekday`
order by field(`weekday`,
               'Monday',
               'Tuesday',
               'Wednesday',
               'Thursday',
               'Friday',
               'Saturday',
               'Sunday')
