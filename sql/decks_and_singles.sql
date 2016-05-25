select
  (select name from decks where id = `t0`.`deck_id`) as `deck_name`,
  greatest(min(floor((`t0`.`qty_available` - 4)/`t0`.`qty_in_decklist`)),0) as `able_to_make`,
  group_concat(`limiting_factor`) as `limiting_factors`
from
  (select
    `card_title`,
    `deck_id`,
    `qty_available`,
    `qty_in_decklist`,
    case when (`inventory`.`qty_available` - 4) / `inventory`.`qty_in_decklist` <= 10 then `card_title` end as `limiting_factor`

from
  (select 
    cf.title as `card_title`,
    dp.deck_id as `deck_id`,
    sum(p.qty) as `qty_available`,
    dp.qty as `qty_in_decklist`
  from 
    decks_products dp
      join cfields cf_one on dp.product_id = cf_one.product_id
      join cfields cf on cf_one.title = cf.title
      join products p on cf.product_id = p.id
  where 
    dp.deck_id in (select id from decks where name like "Battle Deck%") 
    and cf.rarity != 'L'
    and p.model = "mtg_card"
    and p.is_active = 1
    and p.is_template = 0
    and cf.title not in ('Forest', 'Mountain', 'Plains', 'Swamp', 'Island')
    and p.primary_category_id not in (2833, 2630)
  group by `deck_id`, cf.title) as `inventory`
  group by `deck_id`, `card_title`
  ) as `t0`
group by deck_id
order by `deck_name`
