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

    public function conform($price, $step = 0)
    {
        $this->restart();
        $price = round($price, 2);
        if ($price >= $this->prices[$this->array_size - 1])
        {
            for ($i = 0; $i < $this->number_of_breaks; ++$i)
            {
                // the last break point
                if ($i + 1 == $this->number_of_breaks)
                {
                    $this->discrete_increment = $this->breaks[$i]['discrete_increment'];
                    break;
                }
                
                // this is the correct break point
                // iff price > break_price & price > next_break_price ||
                // break_price == max(break_prices)
                if ($price > $this->breaks[$i]['price']
                    and $price < $this->breaks[$i + 1]['price'])
                {
                    $this->discrete_increment = $this->breaks[$i]['discrete_increment'];
                    break;
                }
            }

            $remainder = fmod($price, $this->discrete_increment);
            if ($remainder + .01 !== $this->discrete_increment)
            {
                $balanced_remainder = $remainder + 0.01;
                if ($balanced_remainder < ($this->discrete_increment / 2))
                {
                    $price -= $balanced_remainder;
                }

                elseif ($balanced_remainder > ($this->discrete_increment / 2))
                {
                    $price += ($this->discrete_increment - $balanced_remainder);
                }

                elseif ($balanced_remainder === $this->discrete_increment / 2)
                {
                    if ($tick >= 1)
                    {
                        $price += ($this->discrete_increment - $balanced_remainder);
                    }

                    if ($tick <= 0)
                    {
                        $price -= $balanced_remainder;
                    }
                }
            }
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
        return $this->prices[$price_key];
    }


    private function restart()
    {
        $this->discrete_increment = null;
    }


    public function suggest($product)
    {
        $price = $product->price;
        $price = $this->conform($price);

        // price suggestion algorithm code here ...

        return $price;
    }


    public function reprice($price, $step)
    {
        $this->restart();
        $price = $this->conform($price, $step);

        if ($price > $this->prices[$this->array_size - 1]
            and $step < 0 
            and $price + $this->discrete_increment * $step 
            < $this->prices[$this->array_size - 1])
        {
            while ($price > $this->prices[$this->array_size - 1])
            {
                $price += $this->discrete_increment * -1;
                ++$step;
            }

            $price = $this->prices[$this->array_size - 1 + $step];
            return $price;
        }
        
        if ($price > $this->prices[$this->array_size - 1])
        {
            $price += $this->discrete_increment * $step;
            return $price;
        }

        $price_key = array_search($price, $this->prices);
        
        if (($price_key + $step) > $this->array_size - 1)
        {
            $extra_steps = $step - ($this->array_size - 1 - $price_key);
            $price = $this->prices[$this->array_size - 1];
            return $price + $extra_steps * $this->breaks[0]['discrete_increment'];
        }

        if ($price_key + $step < 0)
        {
            return $this->prices[0];
        }

        return $this->prices[$price_key + $step];
    }


    public function unit_test()
    {
        function rng($min = 0, $max = 1)
        {
            return $min + mt_rand() / mt_getrandmax() * ($max - $min);
        }
        echo "<pre>\n";
        echo "<h3>This is the unit test module for Pricer.php.\n"
            . " Shows input of price and step, and resulting output price.\n"
            . " Inputs are randomly generated along ranges of known test cases.</h3>";

        foreach ([1.00, 49.99, 199.99, 5000] as $max)
        {
            for ($i = 0; $i < 5; ++$i)
            {
                $num = round(rng(0, $max), 2);
                $step = mt_rand(-4, 4);
                $result = $this->reprice($num, $step);
                echo "\n$num going $step steps: $result";
            }
        }
        echo "\n</pre>";
    }

}
?>
