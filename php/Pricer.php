<?php

function step($price, $step)
{
    $array =
    [
        0.25, 0.29, 0.35, 0.39, 0.49, 0.59, 0.69, 0.79, 0.99,
        1.29, 1.49, 1.79, 1.99,
        2.29, 2.49, 2.79, 2.99,
        3.49, 3.99,
        4.49, 4.99,
        5.49, 5.99,
        6.49, 6.99,
        7.49, 7.99,
        8.49, 8.99,
        9.49, 9.99,
        10.99, 11.99, 12.99, 13.99, 14.99, 15.99, 16.99, 17.99, 18.99, 19.99,
        20.99, 21.99, 22.99, 23.99, 24.99, 25.99, 26.99, 27.99, 28.99, 29.99,
        32.99, 34.99, 37.99, 39.99,
        44.99, 49.99,
    ];

    $array_size = count($array);
    $high_break = 199.99;
    $mult = 5.00;
    $high_mult = 10.00;

    if ($price >= $array[$array_size - 1])
    {
        $mult = 5.00;
 
        if ($price >= $high_break)
        {
            $mult = $high_mult;
        }
        
        $remainder = fmod($price, 5.00);
        if ($remainder !== 4.99
            and $price < $high_break)
        {
            $balanced_remainder = $remainder + 0.01;
            if ($balanced_remainder < ($mult / 2))
            {
                $price -= $balanced_remainder;
            }

            elseif ($balanced_remainder > ($mult / 2))
            {
                $price += $balanced_remainder;
            }

            elseif ($balanced_remainder === $mult / 2)
            {
                if ($tick >= 0)
                {
                    $price += $balanced_remainder;
                }

                if ($tick < 1)
                {
                    $price -= $balanced_remainder;
                }
            }
        }
        if (($price - ($mult * $step)) < 49.99)
        {
            while ($price > 49.99)
            {
                $price += $mult * -1;
                ++$step;
            }

            $price = $array[$array_size - 1 + $step];
            return $price;
        }

        $price += $mult * $step;
        return $price;
    }

    $price_key = array_search($price, $array);

    if ($price_key === false)
    {
        $closest = null;
        foreach ($array as $index => $price_step)
        {
            if ($closest === null 
                or abs($price - $closest) > abs($price_step - $price))
            {
                $closest = $price_step;
                $price_key = $index;
            }
        }
    }
    
    if (($price_key + $step) > $array_size)
    {
        $extra_steps = $step - ($array_size - 1 - $price_key);
        $price = $array[$array_size - 1];

    }

    return $array[$price_key + $step];
}

echo step(0.87, 1);

?>
