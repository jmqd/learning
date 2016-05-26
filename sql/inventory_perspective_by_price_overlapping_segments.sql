select -- info on $0.25 or less cards
  '<= 0.25' as `price_range`, 
  count(*) as `number_of_titles`, 
  sum(p.price) as `cost_to_buy_one_of_each`, 
  sum(case when qty_to_buy > 0 then 1 else 0 end) as `count_on_buylist`, 
  sum(qty_to_buy) as `buying_up_to` 
from 
  products p 
where 
  p.primary_category_id not in (2395, 2430, 2720) 
  and p.model = 'mtg_card' 
  and p.`is_active` = 1 
  and p.`is_template` = 0 
  and p.price <= 0.25 
union all
select -- info on >$0.25 cards
  '>0.25' as `price_range`, 
  count(*) as `number_of_titles`, 
  sum(p.price) as `cost_to_buy_one_of_each`, 
  sum(case when qty_to_buy > 0 then 1 else 0 end) as `count_on_buylist`, 
  sum(qty_to_buy) as `buying_up_to` 
from 
  products p 
where 
  p.primary_category_id not in (2395, 2430, 2720) 
  and p.model = 'mtg_card' 
  and p.`is_active` = 1 
  and p.`is_template` = 0 
  and p.price > 0.25 
union all
select -- info on >$1.00 cards
  '>1.00' as `price_range`, 
  count(*) as `number_of_titles`, 
  sum(p.price) as `cost_to_buy_one_of_each`, 
  sum(case when qty_to_buy > 0 then 1 else 0 end) as `count_on_buylist`, 
  sum(qty_to_buy) as `buying_up_to` 
from 
  products p 
where 
  p.primary_category_id not in (2395, 2430, 2720) 
  and p.model = 'mtg_card' 
  and p.`is_active` = 1 
  and p.`is_template` = 0 
  and p.price > 1.00 
union all
select -- info on >$5.00 cards
  '>5.00' as `price_range`, 
  count(*) as `number_of_titles`, 
  sum(p.price) as `cost_to_buy_one_of_each`, 
  sum(case when qty_to_buy > 0 then 1 else 0 end) as `count_on_buylist`, 
  sum(qty_to_buy) as `buying_up_to` 
from 
  products p 
where 
  p.primary_category_id not in (2395, 2430, 2720) 
  and p.model = 'mtg_card' 
  and p.`is_active` = 1 
  and p.`is_template` = 0 
  and p.price > 5.00 
union all
select -- info on >$10.00 cards
  '>10.00' as `price_range`, 
  count(*) as `number_of_titles`, 
  sum(p.price) as `cost_to_buy_one_of_each`, 
  sum(case when qty_to_buy > 0 then 1 else 0 end) as `count_on_buylist`, 
  sum(qty_to_buy) as `buying_up_to` 
from 
  products p 
where 
  p.primary_category_id not in (2395, 2430, 2720) 
  and p.model = 'mtg_card' 
  and p.`is_active` = 1 
  and p.`is_template` = 0 
  and p.price > 10.00 
union all
select -- info on >$20.00 cards
  '>20.00' as `price_range`, 
  count(*) as `number_of_titles`, 
  sum(p.price) as `cost_to_buy_one_of_each`, 
  sum(case when qty_to_buy > 0 then 1 else 0 end) as `count_on_buylist`, 
  sum(qty_to_buy) as `buying_up_to` 
from 
  products p 
where 
  p.primary_category_id not in (2395, 2430, 2720) 
  and p.model = 'mtg_card' 
  and p.`is_active` = 1 
  and p.`is_template` = 0 
  and p.price > 20.00 
union all
select -- info on >$100.00 cards
  '>50.00' as `price_range`, 
  count(*) as `number_of_titles`, 
  sum(p.price) as `cost_to_buy_one_of_each`, 
  sum(case when qty_to_buy > 0 then 1 else 0 end) as `count_on_buylist`, 
  sum(qty_to_buy) as `buying_up_to` 
from 
  products p 
where 
  p.primary_category_id not in (2395, 2430, 2720) 
  and p.model = 'mtg_card' 
  and p.`is_active` = 1 
  and p.`is_template` = 0 
  and p.price > 50.00
