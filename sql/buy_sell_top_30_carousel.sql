select
  `raw_data`.`id`,
  `raw_data`.`name`,
  `raw_data`.`resolved_qty`/`raw_data`.`threshold` as `resolved_equity`,
  `raw_data`.`resolved_qty`,
  `raw_data`.`threshold`
from (
    select
      `p`.`id`,
      `p`.`name`,
      `p`.`qty` - p.`qty_out` + p.`qty_in` as `resolved_qty`,
      `p`.`qty_out` + p.`qty_in` as `activity`,
      `p`.`threshold`
    from
      products `p`
    where
      p.`is_active` = 1
      and `p`.`is_template` = 0
      and `p`.`model` = 'mtg_card'
      and `p`.`qty_to_buy` > 0
      and `p`.`threshold` > 20
      and `p`.`price_buy` > 1
    ) as `raw_data`
where
  `raw_data`.`activity` > 10
order by `resolved_equity` asc
limit 30
