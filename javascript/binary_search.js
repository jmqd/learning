function search(list, value, start = null, stop = null)
{
    if (start == null || stop == null)
    {
        start = 0;
        stop = list.length
        console.log('initializing: start = 0; stop = ' + stop);
    }

    index = start + Math.floor((stop - start) / 2)
    console.log('setting index to ' + index);

    if (index < 0 || index > list.length - 1 || start > stop)
    {
        console.log('value not in array');
        return false;
    }

    if (list[index] == value)
    {
        console.log(index, ' is ', value)
        return index;
    }

    else if (list[index] > value)
    {
        console.log('list[' + index + '] == ' + list[index]
                    + '... going to list[' + start + ':' + (index - 1) + ']');
        return search(list, value, start, index - 1);
    }

    else if (list[index] < value)
    {
        console.log('list[' + index + '] == ' + list[index] + '... going to'
                    + ' list[' + (index + 1) + ':' + stop + ']');
        return search(list, value, index + 1, stop);
    }
    
    console.log('You have reached a logically impossible state!');
}
