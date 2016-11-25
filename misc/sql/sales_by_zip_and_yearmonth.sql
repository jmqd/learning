select
  concat(month(o.order_date), '/', year(o.order_date)) as `monthyear`,
  ad.`zip` as `zip`,
  sum(li.qty*li.price) as `sales`,
  sum(case when p.model in ('mtg_card', 'mtg_foil') then li.qty*li.price else 0 end) as `singles`,
  sum(case when p.model = 'game' then li.qty*li.price else 0 end) as `games`,
  sum(case when p.model = 'product' then li.qty*li.price else 0 end) as `product`,
  count(distinct o.id) as `orders`,
  count(distinct o.account_id) as `customers`
from
  orders o
  inner join addresses ad on o.`ship_address_id` = ad.id
  inner join lineitems li on o.id = li.`order_id`
  inner join products p on li.`product_id` = p.id
where 
  ad.state = 'WA'
  and o.`status` = 'completed'
  and o.type = 'sale'
  and o.`location_id` = 0
  and order_date > '2011-01-01'
group by `monthyear`, `zip`
order by order_date desc
