/*
  Initialize the dynamic aspects of the query.
*/
set
  @edition_name := 'Eldritch Moon',
  @rarity = 'R',
  @status = 'completed';
/*
  Top-level query that returns the result set.
*/
select
  `product_id`,
  `name`,
  `qty` + `total_sold` - `total_bought` as `initial`,
  `qty` as `current_nm_qty`,
  `total_sold`,
  `total_bought`
from
(
/*
  Inner query from which the outer query pulls its values.
*/
  select
    `p`.`name`,
    `p`.`id` as `product_id`,
    sum(case when li.is_selling = 1 then li.qty else 0 end) as `total_bought`,
    sum(case when li.is_selling = 0 then li.qty else 0 end) as `total_sold`,
    pq.qty
  from
    lineitems `li`
  inner join
    products `p` on `li`.`product_id` = `p`.`id`
  inner join
    products_qty pq on p.id = pq.product_id and pq.style = 'NM'
  inner join
    cfields `cf` on `p`.`id` = `cf`.`product_id`
  inner join
    orders `o` on
      `li`.`order_id` = `o`.`id`
      and o.`status` = @status
  where
    `p`.`primary_category_id` = (select id from categories where name = @edition_name)
    and `cf`.`rarity` = @rarity
    and li.`style` = 'NM'
    and pq.location_id = 0
    and p.model = 'mtg_card'
    and o.`email` not in ('zerocost@cardkingdom.com',
                          'collections@cardkingdom.com',
                          'inventory@cardkingdom.com',
                          'conversion@cardkingdom.com')
  group by `p`.`id`
) as `raw_data`
