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
    private $hasResults;
    private $options;
    private $codename;
    
    private static $supported_options = ['export_csv'];
    private static $linkables = [
        'orderid' => 'https://example.ecomm.com/admin/orders/view/',
        'poid' => 'https://example.ecomm.com/admin/purchase_orders/view/',
        'accountid' => 'https://example.ecomm.com/admin/accounts/view/',
        'productid' => 'https://example.ecomm.com/admin/products/browse?filter%5Bname%5D=',
        ];


    function __construct($data, $name)
    {
        if ($data != Null)
        {
            $this->data = $data;
            if ($this->data[0] == False) { 
                $this->hasResults = False; 
            } else { 
                $this->hasResults = True; 
            }
        }
        if ($data == Null)
        {
            $this->data[0]['results'] = "Nothing found for $name.";
            $this->hasResults = False;
        }
        $this->options = [];
        $this->codename = preg_replace('/[\s0-9,\'"\)\(]+/', '', $this->name) . substr(md5(rand()), 0, 7);
        $this->data = $this->iPreferToBeObjectified();
        $this->name = $name;
        $this->date = new DateTime();
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
        if ($this->hasResults)
        {
            $this->headers = array_keys(get_object_vars($this->data[0]));
        }
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
        $this->iPreferToBeObjectified();
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
        if ($this->hasResults === False) {
            return "<br>No results found for {$this->name}.";
        }
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
        if ($this->hasResults == False)
        {
            return "<br>Nothing found for {$this->name}.";
        }

        $html = "
            <h2>{$this->name}</h2>";

        if ($this->summary) {
            $html .= "<h5><br><em>{$this->summary}</em></h5>";
        }
        if ($this->description) {
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


    public function with($option)
    {
        $option = strtolower($option);
        if (!in_array($option, Report::$supported_options))
        {
            echo "{$option} not in supported_options for Reports.";
            return $this;
        }
        $this->options[] = $option;
        return $this;
    }


    private function add_option_export_csv()
    {
        $js = "
<script type='text/javascript'>
        $(document).ready(function () {
            console.log('HELLO')
            function exportTableToCSV(\$table, filename) {
                var \$headers = \$table.find('tr:has(th)')
                    ,\$rows = \$table.find('tr:has(td)')
                    // Temporary delimiter characters unlikely to be typed by keyboard
                    // This is to avoid accidentally splitting the actual contents
                    ,tmpColDelim = String.fromCharCode(11) // vertical tab character
                    ,tmpRowDelim = String.fromCharCode(0) // null character
                    // actual delimiter characters for CSV format
                    ,colDelim = '\",\"'
                    ,rowDelim = '\"\\r\\n\"';
                    // Grab text from table into CSV formatted string
                    var csv = '\"';
                    csv += formatRows(\$headers.map(grabRow));
                    csv += rowDelim;
                    csv += formatRows(\$rows.map(grabRow)) + '\"';
                    // Data URI
                    var csvData = 'data:application/csv;charset=utf-8,' + encodeURIComponent(csv);
                $(this)
                    .attr({
                    'download': filename
                        ,'href': csvData
                        //,'target' : '_blank' //if you want it to open in a new window
                });
                //------------------------------------------------------------
                // Helper Functions 
                //------------------------------------------------------------
                // Format the output so it has the appropriate delimiters
                function formatRows(rows){
                    return rows.get().join(tmpRowDelim)
                        .split(tmpRowDelim).join(rowDelim)
                        .split(tmpColDelim).join(colDelim);
                }
                // Grab and format a row from the table
                function grabRow(i,row){
                     
                    var \$row = $(row);
                    //for some reason \$cols = \$row.find('td') || \$row.find('th') won't work...
                    var \$cols = \$row.find('td'); 
                    if(!\$cols.length) \$cols = \$row.find('th');  
                    return \$cols.map(grabCol)
                                .get().join(tmpColDelim);
                }
                // Grab and format a column from the table 
                function grabCol(j,col){
                    var \$col = $(col),
                        \$text = \$col.text();
                    return \$text.replace('\"', '\"\"'); // escape double quotes
                }
            }
            // This must be a hyperlink
            $(\"#button_{$this->codename}\").click(function (event) {
                // var outputFile = 'export'
                var outputFile = window.prompt(\"What do you want to name your output file (Note: This won't have any effect on Safari)\") || 'export';
                outputFile = outputFile.replace('.csv','') + '.csv'
                 
                // CSV
                exportTableToCSV.apply(this, [$('#table_{$this->codename}>table'), outputFile]);
                
                // IF CSV, don't do event.preventDefault() or return false
                // We actually need this to be a typical hyperlink
            });
        });
    </script>";
        $button = "
            <div class='button'>
                <a href='#' id ='button_{$this->codename}' role='button'>Click On This Here Link To Export The Table Data into a CSV File
                </a>
                </div>";
        return $button . $js;
    }


    private function comes_with_options()
    {
        $html = "";
        foreach ($this->options as $option)
        {
            $function_name = "add_option_" . $option;
            $html .= $this->{$function_name}();
        } 
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
            if ($is_new_tab) {
                $extras = " target=\"_blank\"";
            }

            $linked = "<a href=\"".Report::$linkables[strtolower(preg_replace('/[^a-zA-Z]/', '', $column_name))]."{$value}\"{$extras}>{$value}</a>";
            return $linked;
        }


    public function asHyperlinkedHtmlTable($is_new_tab=False)
    {
        if ($this->hasResults == False) {
            return "<br>Nothing found for {$this->name}.";
        }
        foreach ($this->data[0] as $key => $value)
        {
            $column_header_names[$key] = False;
        }
        
        $html = "";

        if (in_array('export_csv', $this->options))
        {
            $html .= "<div class='container'><div id='table_{$this->codename}'>";
        }

        $html .= "<table class='table'>\n<thead>\n<tr>";

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

        if (in_array('export_csv', $this->options))
        {
            $html .= "</div>";
        }

        $html .= $this->comes_with_options();
        return $html;
    }
 

    public function plot($args=[])
    {
        $args['hasResults'] = $this->hasResults;
        $args['linkedReport'] = $this;
        $args['title'] = array_key_exists('title', $args) ? $args['title'] : $this->name;
        $args['data'] = $this->data;
        $this->plot = new GooglePlot($args);
        return $this->plot;
    }
}

