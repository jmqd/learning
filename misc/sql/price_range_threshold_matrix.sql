select 
  price_range,  
  concat(sum(case when qty <= 0.25*threshold                          then 1 else 0 end)/count(*)*100,'%') as '< 25%',
  concat(sum(case when qty <= 0.55*threshold and qty > 0.25*threshold then 1 else 0 end)/count(*)*100,'%') as '25%-55%',
  concat(sum(case when qty <= 0.95*threshold and qty > 0.55*threshold then 1 else 0 end)/count(*)*100,'%') as '55%-95%',
  concat(sum(case when qty <= 1.25*threshold and qty > 0.95*threshold then 1 else 0 end)/count(*)*100,'%') as '95%-125%',
  concat(sum(case when qty <= 1.50*threshold and qty > 1.25*threshold then 1 else 0 end)/count(*)*100,'%') as '125%-150%',
  concat(sum(case when qty >  1.50*threshold                          then 1 else 0 end)/count(*)*100,'%') as '> 150%'
from
(select case 
  when p.price > 0      and p.price <= 0.25   then '0-0.25'
  when p.price > 0.25   and p.price <= 0.75   then '0.25-0.75'
  when p.price > 0.75   and p.price <= 1.00   then '0.75-1.00'
  when p.price > 1.00   and p.price <= 2.00   then '1.00-2.00'
  when p.price > 2.00   and p.price <= 3.00   then '2.00-3.00'
  when p.price > 3.00   and p.price <= 4.00   then '3.00-4.00'
  when p.price > 4.00   and p.price <= 5.00   then '4.00-5.00'
  when p.price > 5.00   and p.price <= 6.00   then '5.00-6.00'
  when p.price > 6.00   and p.price <= 7.00   then '6.00-7.00'
  when p.price > 7.00   and p.price <= 8.00   then '7.00-8.00'
  when p.price > 8.00   and p.price <= 9.00   then '8.00-9.00'
  when p.price > 9.00   and p.price <= 10.00  then '9.00-10.00'
  when p.price > 10.00  and p.price <= 12.00  then '10.00-12.00'
  when p.price > 12.00  and p.price <= 15.00  then '12.00-15.00'
  when p.price > 15.00  and p.price <= 20.00  then '15.00-20.00'
  when p.price > 20.00  and p.price <= 40.00  then '20.00-40.00'
  when p.price > 40.00  and p.price <= 100.00 then '40.00-100.00'
  when p.price > 100.00 and p.price <= 250.00 then '100.00-250.00'
  when p.price > 250.00                       then '> 250.00'
  end as price_range,
threshold,
qty,
price

from products p
  join cfields cf on p.id = cf.product_id
where 1 and 
  is_active = 1                         -- filters out inactive items
  and is_template = 0                   -- filters out template items 
  and primary_category_id != 2833       -- filters out promotional items
  and model = "mtg_card"                -- filters out foils and any other rogue non-singles
  and p.price > 0
    ) as price_summaries
group by price_range
order by price
