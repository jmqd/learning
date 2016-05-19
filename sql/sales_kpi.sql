select
   date(o.order_date) as `date`,
   sum(o.total) as `sales`,
   count(distinct o.id) as `orders`,
   sum(ls.`profit`) as `profit`,
   sum(ls.`profit`)/sum(o.total) as `margin`,
   count(distinct o.account_id) as `customers`,
   round(avg(o.subtotal),2) as `subtotal_avg`,
   round(avg(o.shipping),2) as `avg_shipping`,
   round(sum(case
     when a.country_code = "US" then 0 else 1 end)/count(*)*100,2) as `intl_pct`
 from
   orders o
     inner join addresses a on o.ship_address_id = a.id
     inner join (
       select
         out_order_id,
         sum(price-cost) as `profit`
       from 
         lifo_stack
       group by out_order_id
         ) ls 
    on o.id = ls.out_order_id
 where
   o.status in ("completed", "queue", "ready")
   and o.type = "sale"
   and o.order_date between curdate() - interval 91 day and curdate() - interval 1 day
   and o.is_pickup = 0
group by `date`
