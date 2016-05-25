select
    `coupon`.`account_id`
from
(select distinctrow
  `row_number`,
  `customer_orders`.`order_date`,
  `customer_orders`.`order_id`,
  `customer_orders`.`account_id`
  
from (
  select 
    @rn:=
    case
      when @account_id=account_id
        then @rn+1
      else 1
      end as `row_number`, 
    order_date as `order_date`,
    id as `order_id`,
    @account_id:=account_id as `account_id`
  from (
    select
      order_date,
      id,
      account_id
    from 
      orders,
      (select @rn:=0, @account_id:=0) as `r`
      where orders.status = 'completed'
      and orders.`type` = 'sale'
    order by account_id, order_date) t1
            ) `customer_orders`
    inner join (
      select
        o.id as `order_id`,
        o.account_id as `account_id`,
        o.order_date as `order_date`
      from
        orders o
      where
        o.coupon = 'GAUNTLET'
        and o.type = 'sale'
        and o.status != 'canceled'
        and o.status != 'cart'
      ) `coupon_orders` on `customer_orders`.`order_id` = `coupon_orders`.`order_id`) as `coupon`
    join (
        select distinctrow
            `row_number`,
            `customer_orders`.`order_date`,
            `customer_orders`.`order_id`,
            `customer_orders`.`account_id`
  
        from (
            select 
                @rn:=
                    case
                        when @account_id=account_id
                            then @rn+1
                        else 1
                    end as `row_number`, 
                order_date as `order_date`,
                id as `order_id`,
                @account_id:=account_id as `account_id`
            from (
                select
                    order_date,
                    id,
                    account_id
                from 
                    orders,
                   (select @rn:=0, @account_id:=0) as `r`
                    where orders.status = 'completed'
                    and orders.`type` = 'sale'
                order by account_id, order_date
               ) t1
            ) `customer_orders`
        inner join (
            select
                o.id as `order_id`,
                o.account_id as `account_id`,
                o.order_date as `order_date`
            from
                orders o
            where
                o.coupon = 'GAUNTLET'
                and o.type = 'sale'
                and o.status != 'canceled'
                and o.status != 'cart'
      ) `coupon_orders` on `customer_orders`.`account_id` = `coupon_orders`.`account_id`
    ) `previous_orders` on (`coupon`.`account_id` = `previous_orders`.`account_id` and `coupon`.`row_number` - 1 = `previous_orders`.`row_number`)
    where timestampdiff(day, `coupon`.`order_date`, `previous_orders`.`order_date`) <= -90
