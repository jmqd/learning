<?php

class Pricer
{

    public function __construct()
    {
        $config = include('config.php');
        $this->prices = $config['prices_array'];
        $this->array_size = count($config['prices_array']);
        $this->breaks = $config['breaks'];
        $this->number_of_breaks = count($this->breaks);
    }

    public function conform()
    {
        // price conforming code here
    }

    public function step($price, $step)
    {
        $high_break = 199.99;
        $discrete_increment = 5.00;
        $high_discrete_increment = 10.00;

        if ($price >= $this->prices[$this->array_size - 1])
        {
            for ($i = 0; $i < $this->number_of_breaks; ++$i)
            {
                // the last break point
                if ($i + 1 == $this->number_of_breaks)
                {
                    $discrete_increment = $this->breaks[$i]['discrete_increment'];
                    break;
                }
                
                // this is the correct break point
                // iff price > break_price & price > next_break_price ||
                // break_price == max(break_prices)
                if ($price > $this->breaks[$i]['price']
                    and $price < $this->breaks[$i + 1]['price'])
                {
                    $discrete_increment = $this->breaks[$i]['discrete_increment'];
                    break;
                }
            }

            
            $remainder = fmod($price, $discrete_increment);
            if (!in_array($remainder + .01, [5.00, 10.00]))
            {
                $balanced_remainder = $remainder + 0.01;
                if ($balanced_remainder < ($discrete_increment / 2))
                {
                    $price -= $balanced_remainder;
                }

                elseif ($balanced_remainder > ($discrete_increment / 2))
                {
                    $price += $balanced_remainder;
                }

                elseif ($balanced_remainder === $discrete_increment / 2)
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
            if (($price - ($discrete_increment * $step)) < 49.99)
            {
                while ($price > 49.99)
                {
                    $price += $discrete_increment * -1;
                    ++$step;
                }

                $price = $this->prices[$this->array_size - 1 + $step];
                return $price;
            }

            $price += $discrete_increment * $step;
            return $price;
        }

        $price_key = array_search($price, $this->prices);

        if ($price_key === false)
        {
            $closest = null;
            foreach ($this->prices as $index => $price_step)
            {
                if ($closest === null 
                    or abs($price - $closest) > abs($price_step - $price))
                {
                    $closest = $price_step;
                    $price_key = $index;
                }
            }
        }
        
        if (($price_key + $step) > $this->array_size)
        {
            $extra_steps = $step - ($this->array_size - 1 - $price_key);
            $price = $this->prices[$this->array_size - 1];

        }

        return $this->prices[$price_key + $step];
    }


    public function unit_test()
    {
        function rng($min = 0, $max = 1)
        {
            return $min + mt_rand() / mt_getrandmax() * ($max - $min);
        }
        foreach ([49.99, 199.99, 5000] as $max)
        {
            for ($i = 0; $i < 10; ++$i)
            {
                $num = rng(0, $max);
                $step = mt_rand(-4, 4);
                $result = $this->step($num, $step);
                echo "\n$num going up $step steps: $result\n";
            }
        }
    }

}
?>
