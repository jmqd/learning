<?php

// ........................................
// Mathematical functions, etc
// Jordan McQueen, 04-29-2016
// ........................................

class Mathematics 
{
    // ................................
    // median($array) -> int(median)
    // ................................
    function median($array)
    {
    sort($array);
    $count = count($array);
    $middleval = floor(($count-1)/2);
    if($count & 1) 
    { // odd number, middle is the median
        $median = $array[$middleval];
    } 
    else 
    { // even number, calculate avg of 2 medians
        $low = $array[$middleval];
        $high = $array[$middleval+1];
        $median = (($low+$high)/2);
    }
    return $median; 
    }
}
