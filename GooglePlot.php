<?php

class GooglePlot
{
    private $kind;
    private $dependents;
    private $independent;
    private $dataTable;
    private $codename;
    private $data;
    private $chartType;

    
    public function __construct($args)
    {
        $this->title = $args['title'];
        $this->kind = strtolower($args['kind']);
        $this->dependents = $args['dependents'];
        $this->independent = $args['independent'];
        $this->codename = preg_replace('/[\s0-9]+/', '', $this->title) . substr(md5(rand()), 0, 7);
        $this->data = $args['data'];
        $this->chartClass = $this->lookupChartClass();
        $this->package = $this->lookupPackage(); 
    }
    

    public function setIndependent($independent)
    {
        $this->independent = $independent;
        return $this;
    } 

    public function setKind($kind)
    {
        $this->kind = $kind;
        return $this;
    }


    public function getKind()
    {   
        return $this->kind;
    }


    public function setDependents($dependents)
    {
        $this->dependents = $dependents;
        return $this;
    }


    public function getDependents()
    {
        return $this->dependents;
    }


    public function addDependent($dependent)
    {
        $this->dependents[] = $dependent;
        return $this;
    }


    private function independentlyDolledUp($value)
    {
        if ($this->kind == 'timeseries')
        {
            $value = new DateTime($value);
            $value = $value->modify('+1 day')->format('Y-m-d');
            $value = "new Date('$value')";
            return $value;
        }
        else 
        {
            return "'$value'";
        }
    }


    public function getJsDataTable()
    {
        $data_header = "['$this->independent'";
        foreach ($this->dependents as $dependent)
        {
            $data_header .= ", '$dependent'";
        }
        $data_header .= "],\n";
        $data_body = "";
        foreach ($this->data as $row)
        {
            $x = $this->independentlyDolledUp($row->{$this->independent});
            $data_body .= "[$x";
            foreach ($this->dependents as $y)
            {
                $value = $row->{$y};
                $data_body .= ", $value";
            }
            $data_body .= "],\n";
        }
        return $data_header . $data_body;
    }    


    private function getSpecialOptions()
    {
        $special_options = "";
        switch ($this->kind)
        {
            case 'stacked':
                $special_options .= "isStacked: true\n";
        }
    }


    private function getOptions()
    {
        $options = "var options = {
            title: '$this->title',
            height: 400,
            {$this->getAxesOptions()},
            {$this->getSpecialOptions()}
        };";
        return $options;
    }
    

    private function lookupPackage()
    {
        switch ($this->kind)
        {
            case 'table':
                return 'table';
                break;
            default:
                return 'corechart';
                break;
        }
    }


    private function lookupChartClass()
    {
        $class_lookup = [
            'timeseries' => 'LineChart',
            'column' => 'ColumnChart',
            'combo' => 'ComboChart',
            'pie' => 'PieChart',
            'area' => 'AreaChart',
            'stacked' => 'AreaChart',
            'bar' => 'BarChart',
            'table' => 'Table',
            ];
        return $class_lookup[$this->kind];
    }


    private function getAxesOptions()
    {
        $axes = "vAxes: {\n";
        $series = "series: {\n";
        foreach ($this->dependents as $index => $y)
        {
            $axes .= "$index: {title: '$y'},\n";
            $series .= "$index:{ targetAxisIndex: $index},\n";
        }
        $axes .= "},\n";
        $series .= "}\n";
        return $axes . $series;
    }


    public function getJavascript()
    {
        $js = "
        <div id='$this->codename' style='border: 0px solid; width:1400px;'></div>
        <script type='text/javascript'>
        google.load('visualization', '1', {packages:['{$this->package}']});
        google.setOnLoadCallback($this->codename);
        function $this->codename() {
            var data = google.visualization.arrayToDataTable(
            [
                {$this->getJsDataTable()}
            ]);
            {$this->getOptions()}
            var chart = new google.visualization.{$this->chartClass}(document.getElementById('$this->codename'));
            chart.draw(data, options);
        }
        </script>";
        return $js;
    }
}

