select 
  p.name, 
  sum(case when pq.style = 'NM' then pq.qty else 0 end) as `qty`,
  `incoming`.`qty` as `incoming_qty`
from 
  products p 
left outer join 
  products_qty pq on p.id = pq.`product_id`
left outer join (
  select
    l.product_id,
    sum(l.qty) as `qty`
  from
    lineitems l
      inner join orders od on l.`order_id` = od.`id`
  where 
      od.email = 'transfer@cardkingdom.com'
      and od.status not in ('completed', 'canceled')
      and l.style = 'NM'
  group by l.`product_id`  
    ) `incoming` on pq.product_id = `incoming`.product_id
  where
  (pq.location_id = 281854 or pq.location_id is null)
  and p.model = 'mtg_card'
group by p.id
order by qty desc
