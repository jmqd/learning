function search(list, value, start = null, stop = null)
{
    if (start == null || stop == null)
    {
        start = 0;
        stop = list.length
    }

    index = start + Math.floor((stop - start) / 2)

    if (index < 0 || index > list.length - 1)
    {
        console.log('value not in array');
        return false;
    }

    if (list[index] == value)
    {
        return index;
    }

    else if (list[index] > value)
    {
        return search(list, value, start, index - 1);
    }

    else if (list[index] < value)
    {
        return search(list, value, index + 1, stop);
    }
    
    console.log('You have reached a logically impossible state!');
}
