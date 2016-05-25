select
  distinct `o`.`account_id`
from 
  orders `o`
    inner join 
      `addresses` `ad` 
    on (
      (`o`.`ship_address_id` = `ad`.`id`
      or `o`.`bill_address_id` = `ad`.`id`)
      and ad.`state` in ('AE', 'AP', 'AA') -- these are the state designators for APO addresses
    )
