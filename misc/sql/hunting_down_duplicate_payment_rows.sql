select
  p_o.id as `id_of_row_with_account_id`,
  p_a.id as `id_of_row_with_order_id`,
  p_o.dt_rcvd,
  p_o.type,
  p_o.amount as `account_id_row_amnt`,
  p_a.amount as `order_id_row_amnt`,
  p_a.order_id,
  p_o.`account_id`
from
  payments p_o
inner join 
  payments p_a on (p_o.id = (p_a.id - 1) and 
    abs(p_o.amount) = abs(p_a.amount))
where
  p_o.dt_rcvd between '2016-06-21' and '2016-06-23' and
  p_o.type = 'storecredit' and (
  p_o.reason_code is null or 
  p_o.reason_code = '' or 
  p_a.reason_code is null or 
  p_a.reason_code = ''
    )

