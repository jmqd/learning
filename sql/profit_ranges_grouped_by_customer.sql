select
  case 
    when `profit` < 0 then '<0'
    when `profit` between 0 and 4.99 then '0 - 4.99'
    when `profit` between 5 and 19.99 then '5 - 19.99'
    when `profit` between 20 and 49.99 then '20 - 49.99'
    when `profit` between 50 and 99.99 then '50 - 99.99'
    when `profit` between 100 and 499.99 then '100 - 499.99'
    when `profit` > 500 then '500 +' 
  end as `range`,
  count(*) as `count`,
  avg(`gross`) as `average_gross`,
  avg(`profit`) as `average_profit`,
  max(`gross`) as `max_gross`
from (
  select 
    sum(ls.price - ls.cost) as `profit`,
    sum(ls.price) as `gross`
  from 
    lifo_stack ls 
  where 
    out_on between '2015-12-01' and '2016-06-07' and 
    out_account_id not in (0) 
  group by 
    out_account_id
  ) as `rows`
group by `range`
order by `profit`
