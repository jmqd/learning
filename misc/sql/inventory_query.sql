select
  edition,
  rarity,
  case when qty_to_buy > 0 then concat(trim(title), '*') else title end as `title`,
  case 
    when rarity = 'M' then 'all'
    when rarity = 'R' and price > 1.5 then 'all'
    when rarity = 'R' and price between 1.00 and 1.49 then 'all NM/EX'
    when rarity = 'R' and price between 0.79 and 0.99 then 'all NM'
    when rarity in ('C', 'U') and price between 0.40 and 0.49 then 'all NM'
    when rarity in ('C', 'U') and price between 0.50 and 0.99 then 'all NM/EX'
    when rarity in ('C', 'U') and price > 0.99 then 'all'
    when keep + nm > 100 and nm < 100 then 'all NM'
    else keep
    end as `keep`,
  nm as 'NM qty',
  price,
  qty_180,
  qty_30,
  qty_7,
  shortRunIDV,
  longRunIDV,
  qty_in,
  qty_out,
  qty_to_buy,
  repriced_on
from
(select 
    cf.edition,
    cf.rarity, 
    concat_ws(' ', cf.title, cf.variation) as title,    -- concatenate with seperator :: (%s, a, b) -> a ++ %s ++ b
    -- takes the greatest of: weighted short-run IDV stock of 180 days, long-run IDV stock of 180 days, minimum quantitity of 12, qty_180 - 135
    round(greatest((qty_30/30/3)+(qty_7/7/3)*4*p.price*180-p.qty-(p.qty_in*3/5),
           (((p.qty_30/30)/2)+((p.qty_180)/180)/2)*4*p.price*180-p.qty-(p.qty_in*3/5),
           20-p.qty,0, 100-pq.qty),0) as keep,
    p.qty,
    p.is_buying,
    pq.qty as 'nm',
    p.price,
    p.qty_180,
    p.threshold,
    p.qty_30, 
    p.qty_7,
    (qty_30/30)/2 + (qty_7/7)/2 as shortRunIDV,         -- IDV: iterpolated daily velocity
    (qty_30/30)/2+(qty_180/180)/2 as longRunIDV,
    p.qty_in,
    p.qty_out,
    qty_to_buy,
    repriced_on,
    color,
    p.id,
    p.model
  from products p
    inner join cfields cf
      on p.id = cf.product_id
      inner join products_qty pq
      on (p.id = pq.product_id and pq.location_id = 0 and pq.style = 'NM')
  where is_active = 1 and                   -- filters out inactive items
        is_template = 0 and                 -- filters out template items
        primary_category_id != 2833 and     -- filters out promotional items
        model in ('mtg_card')   -- filters out foils and any other rogue non-singles
  order by 
    p.model,
    cf.edition,
    cf.rarity,
    cf.title,
    cf.variation) t1
