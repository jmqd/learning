/*
  Generates a report on the sales of presale items, and post-release sales.
  Of course, this could be generalized as a 90-day sales report of any given
  category of products, but it is tailored specifically for MTG releases.
*/

/*
  Set dynamic aspects of query.
*/
set
  @release := '2014-06-06 00:00:00',
  @cat_id := (select id from categories where name = 'Conspiracy');
/*
  Main query which returns the result set.
*/
select
  p.model,
  sum(li.qty) as `qty_sold`,
  sum(li.qty * li.price) as `gross`,
  case
    when o.order_date between @release - interval 30 day and @release then 'presale (-30 days - 0 days)'
    when o.order_date between @release and @release + interval 30 day then '1st month (0 days - 30 days)'
    when o.order_date between @release + interval 30 day and @release + interval 60 day then '2nd month (30 days - 60 days)'
  end as `period`
from
  lineitems li
inner join
  products p on li.product_id = p.id
inner join
  orders o on li.order_id = o.id
where
  o.order_date between @release - interval 30 day and @release + interval 60 day
  and o.status = 'completed'
  and o.type = 'sale'
  and p.primary_category_id = @cat_id
group by p.model, period

