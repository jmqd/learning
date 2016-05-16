<?php
// ................
// Jordan McQueen
// ................

require_once('GooglePlot.php');

class Report
{
    protected $data;
    public $summary;
    public $name;
    public $date;
    public $description;
    protected $headers;
    public $plot;

    function __construct($data, $name)
    {
        if (is_array($data))
        {
            foreach ($data as $row)
            {
                $data = json_decode(json_encode($data));
            }
        }

        $this->name = $name;
        $this->date = new DateTime();
        $this->data = $data;
        $this->refreshHeaders();
        $this->summary = False;
        $this->description = False;
    }


    protected function refreshHeaders()
    {
        $this->headers = [];

        foreach ($this->data[0] as $key => $value)
        {
            $this->headers[] = $key;
        }
    }


    public function delData()
    {
        unset($this->$data);
        return $this;
    }

    public function setData($data)
    {
        if (is_array($data))
        {
            foreach ($data as $row)
            {
                $data = json_decode(json_encode($data)); // converts array to object structure
            }
        }
        $this->data = $data; 
        $this->refreshHeaders();
        return $this;

    }

    public function getData()
    {
        return $this->data;
    }

    public function setName($name)
    {
        $this->name = $name;
        return $this;
    }

    public function getName()
    {
        return $this->name;
    }

    public function setSummary($summary)
    {
        $this->summary = $summary;
        return $this;
    }

    public function setDescription($description)
    {
        $this->description = $description;
        return $this;
    }


    public function getDescription()
    {
        return $this->description;
    }

    public function renewDate()
    {
        $this->date = new DateTime();
        return $this;
    }


    public function asHtmlTable()
    {
        $html = "<table class='table'>\n<thead>\n<tr>";
        foreach ($this->headers as $header)
        {
            $html .= "\n<th>$header</th>";
        }
        $html .= "</tr>\n</thead>\n<tbody>";
        foreach ($this->data as $row)
        {
            $html .= "\n<tr>";
            foreach ($this->headers as $column)
            {
                $html .= "\n<td>{$row->$column}</td>";
            }
            $html .= "\n</tr>";
        }
        $html .= "\n</tbody>\n</table>";
        return $html;
    }


    public function asEmailHtmlTable()
    {
        $html = "<table class='table'>\n<thead>\n<tr>";
         foreach ($this->headers as $header)
         {
             $html .= "\n<th>$header</th>";
         }
         $html .= "</tr>\n</thead>\n<tbody>";
         foreach ($this->data as $row)
         {
             $html .= "\n<tr>";
             foreach ($this->headers as $column)
             {
                 $html .= "\n<td>{$row->$column}</td>";
             }
             $html .= "\n</tr>";
         }
         $html .= "\n</tbody>\n</table>";
         return $html;
 
    }


    public function displayForEmail()
    {   
        $html = "
            <h2>{$this->name}</h2>";

        if ($this->summary)
        {
            $html .= "<h5><br><em>{$this->summary}</em></h5>";
        }
        if ($this->description)
        {
            $html .= "{$this->description}<br>";
        }
        $html .= "{$this->asEmailHtmlTable()}
             <br>";
         return $html; 
    }


    public function display()
    {
        $html = "
            <h1>{$this->name}</h1>
            <h5><em>{$this->summary}</em></h5>
            {$this->description}<br>
            {$this->asHtmlTable()}
            <br>
            ";
        return $html;
    }


    public function asCSV()
    {
        foreach ($this->data[0] as $key => $value)
        {
            $header[] = $key; // grab the column names from the mysql_result object
        }
        if (!$fp = fopen('php://temp', 'w+')) // open the memory for csvwriter fputcsv() 
        {
            return False; // if the fopen() doesn't work, shut it all down
        }

        fputcsv($fp, $header); // make the csv header

        foreach ($this->data as $datarow)
        {
            foreach ($header as $var)
            {
                $line[] = $datarow->$var;
            }
            fputcsv($fp, $line);
            unset($line);
        }
        rewind($fp);

        return stream_get_contents($fp);
    }


    public function asHyperlinkedHtmlTable($is_new_tab=False)
    {
        global $linkables;
        $linkables = [
            'order_id' => 'https://secure.example.com/admin/orders/view/',
            'account_id' => 'https://secure.example.com/admin/accounts/view/',
            'product_id' => 'https://secure.example.com/admin/products/browse?filter%5Bname%5D='
            ];

        function link_it($column_name, $value, $is_new_tab)
        {
            global $linkables;
            $extras = "";
            if ($is_new_tab)
            {
                $extras = " target=\"_blank\"";
            }

            $linked = "<a href=\"{$linkables[$column_name]}{$value}\"{$extras}>{$value}</a>";
            return $linked;
        }

        foreach ($this->data[0] as $key => $value)
        {
            $column_header_names[$key] = False;
        }

        $html = "<table class='table'>\n<thead>\n<tr>";

        foreach ($column_header_names as $column_name => $is_linkable)
        {
            $html .= "\n<th>$column_name</th>";

            if (array_key_exists($column_name, $linkables))
            {
                $column_header_names[$column_name] = True;
            }
        }

        $html .= "</tr>\n</thead>\n<tbody>";

        foreach ($this->data as $row)
        {
            $html .= "<tr>\n";
            foreach ($column_header_names as $column_name => $is_linkable)
            {
                if ($is_linkable)
                {
                    $linked = link_it($column_name, $row->{$column_name}, $is_new_tab);
                    $html .= "<td>{$linked}</td>";
                }
                else if (!$is_linkable)
                {
                    $html .= "<td>{$row->$column_name}</td>";
                }
            }
            $html .= "</tr>";
        }
        $html .= "</tbody></table>";
        return $html;
    }
 

    public function plot($args=[])
    {
        $args['title'] = array_key_exists('title', $args) ? $args['title'] : $this->name;
        $args['data'] = $this->data;
        $this->plot = new GooglePlot($args);
        return $this->plot;
    }
}

