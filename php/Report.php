<?php
// Jordan McQueen

require_once('GooglePlot.php');

class Report
{
    public $data;
    public $summary;
    public $name;
    public $date;
    public $description;
    protected $headers;
    public $plot;

    static $linkables = [
        'orderid' => 'https://example.ecomm.com/admin/orders/view/',
        'accountid' => 'https://example.ecomm.com/admin/accounts/view/',
        'productid' => 'https://example.ecomm.com/admin/products/browse?filter%5Bname%5D=',
        ];


    function __construct($data, $name)
    {
        $this->name = $name;
        $this->date = new DateTime();
        $this->data = $data;
        $this->data = $this->iPreferToBeObjectified();
        $this->refreshHeaders();
        $this->summary = False;
        $this->description = False;
    }


    private function iPreferToBeObjectified()
    {
        if (! ($this->data instanceof Mysql_Result))
        {
            foreach ($this->data as $index => $row)
            {
                if (isset($row))
                {
                    $data[$index] = json_decode(json_encode($row));
                }
            }
            return $data;
        }       
        return $this->data;
    }


    protected function refreshHeaders()
    {
        $this->headers = array_keys(get_object_vars($this->data[0]));
        return $this;
    }


    public function delData()
    {
        unset($this->$data);
        return $this;
    }

    public function setData($data)
    {
        $this->data = $data; 
        $this->data = $this->iPreferToBeObjectified();
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
        $this->refreshHeaders();
        $html = "
            <h1>{$this->name}</h1>
            <h5><em>{$this->summary}</em></h5>
            {$this->description}<br>
            {$this->asHtmlTable()}
            <br>
            ";
        return $html;
    }


    public function asCsv()
    {
        if (!$fp = fopen('php://temp', 'w+')) // open the memory for csvwriter fputcsv() 
        {
            return False; // if the fopen() doesn't work, shut it all down
        }

        fputcsv($fp, $this->headers); // make the csv header

        foreach ($this->data as $datarow)
        {
            foreach ($this->headers as $column)
            {
                $line[] = $datarow->$column;
            }
            fputcsv($fp, $line);
            unset($line);
        }
        rewind($fp);

        return stream_get_contents($fp);
    }
    
    private function link_it($column_name, $value, $is_new_tab)
        {
            $extras = "";
            if ($is_new_tab)
            {
                $extras = " target=\"_blank\"";
            }

            $linked = "<a href=\"".Report::$linkables[strtolower(preg_replace('/[^a-zA-Z]/', '', $column_name))]."{$value}\"{$extras}>{$value}</a>";
            return $linked;
        }



    public function asHyperlinkedHtmlTable($is_new_tab=False)
    {
        foreach ($this->data[0] as $key => $value)
        {
            $column_header_names[$key] = False;
        }

        $html = "<table class='table'>\n<thead>\n<tr>";

        foreach ($column_header_names as $column_name => $is_linkable)
        {
            $html .= "\n<th>$column_name</th>";

            if (array_key_exists(strtolower(preg_replace('/[^a-zA-Z]/', '', $column_name)), Report::$linkables))
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
                    $linked = $this->link_it($column_name, $row->{$column_name}, $is_new_tab);
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

