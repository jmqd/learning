select
  country_code,
  `lost_dollars`,
  `gross`,
  `lost_dollars` / `delivered_count` as `losses_averaged_per_parcel`,
  `lost_count`,
  `delivered_count`,
  `delivered_count`/(`delivered_count`+`lost_count`) as `shipping_success_rate`
from
(select
  country_code,
  sum(`gross`) as `gross`,
  sum(case when `notes` != 0 then gross else 0 end) as `lost_dollars`,
  sum(case when `notes` != 0 then 1 else 0 end) as `lost_count`,
  sum(case when `notes` = 0 then 1 else 0 end) as `delivered_count`
from
(select
  a.country_code,
  total as `gross`,
  case when lp.message like "%mia%" then 1 else 0 end as `notes`
from 
  orders o
    inner join addresses a on o.`ship_address_id` = a.`id`
    left join logposts lp on (o.id = lp.order_id and lp.message like "%mia%")
where
  o.`type` = "sale"
  and o.status = "completed"
  and year(o.ship_date) = year(curdate())) `tbl_1` 
group by country_code) as `tbl_2`
