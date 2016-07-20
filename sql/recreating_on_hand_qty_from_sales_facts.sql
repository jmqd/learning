set @product_id := 190603;
set @current_on_hand := 114;
set @on_hand := @current_on_hand;
set @push_ct := 0;
select
  `date`,
  `date_of_order`,
  @on_hand := @on_hand - @push_ct as `on_hand`,
  @push_ct := `delta` as `delta`
from (
  select
    o.ship_date as `date`,
    o.order_date as `date_of_order`,
    case
      when li.is_selling = 0 then -li.qty
      when li.is_selling = 1 then li.qty
    end as `delta`
  from
    lineitems li
  inner join
    orders o on li.order_id = o.id
  where
    product_id = @product_id
    and qty <> 0
    and o.status = 'completed'
  order by `date` desc
  ) as `sub_table`
