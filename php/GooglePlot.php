<?php
// Jordan McQueen

class GooglePlot
{
    private $kind;
    private $dependents;
    private $independent;
    private $dataTable;
    private $codename;
    private $title;
    private $data;
    private $chartClass;
    private $package;
    private $isSharingAxes;
    private $independentType;
    private $dataHeaders;
    

    static $releases = [
        '2014-02-07' => 'Born of the Gods',
        '2014-05-02' => 'Journey into Nyx',
        '2014-07-18' => '2015 Core Set',
        '2014-09-26' => 'Khans of Tarkir',
        '2015-01-23' => 'Fate Reforged',
        '2015-03-27' => 'Dragons of Tarkir',
        '2015-07-17' => 'Magic Origins',
        '2015-10-02' => 'Battle for Zendikar',
        '2016-01-22' => 'Oath of the Gatewatch',
        '2016-04-08' => 'Shadows Over Innistrad' 
        ];
    
    public function __construct($args)
    {
        $this->title = $args['title'];
        $this->kind = array_key_exists('kind', $args) ? strtolower($args['kind']) : 'line';
        $this->codename = preg_replace('/[\s0-9,\'"\)\(]+/', '', $this->title) . substr(md5(rand()), 0, 7);
        $this->data = $args['data'];
        $this->refreshDataHeaders();
        $args['independent'] = array_key_exists('independent', $args) ? $args['independent'] : '';
        $this->setIndependent($args['independent']);
        $this->dependents = array_key_exists('dependents', $args) ? $args['dependents'] : $this->buildDependentsGuess();
        $this->chartClass = $this->lookupChartClass();
        $this->package = $this->lookupPackage(); 
        $this->isSharingAxes = array_key_exists('isSharingAxes', $args) ? $args['isSharingAxes'] : True;
        $this->makeJsDataTable();
    }


    private function refreshDataHeaders()
    {
        $this->dataHeaders = [];

        foreach ($this->data[0] as $key => $value)
        {
            $this->dataHeaders[] = $key;
        }
    }


    public function getDataHeaders()
    {
        $this->refreshDataHeaders();
        return $this->dataHeaders;
    }


    public function getIndependent()
    {
        return $this->independent;
    }


    private function buildDependentsGuess()
    {   
        return array_diff($this->getDataHeaders(), [$this->getIndependent()]);
    }


    public function setIndependent($independent)
    {
        if (is_array($independent))
        {
            $this->independent = $independent['name'];
            $this->independentType = $independent['type'];
        }
        else if (!empty($independent) && DateTime::createFromFormat('Y-m-d', $this->getData()[0]->$independent) !== FALSE)
        {
            $this->independent = $independent;
            $this->independentType = 'datetime';
        }
        else if (in_array('date', $this->getDataHeaders()) && empty($independent))
        {
            $this->independent = 'date';
            $this->independentType = 'datetime';
        }
        else
        {
            $this->independent = $independent;
            $this->independentType = 'generic';
        }
        return $this;
    } 


    public function setKind($kind)
    {
        $this->kind = $kind;
        return $this;
    }


    public function setIsSharingAxes($boolean)
    {
        if (!is_bool($boolean))
        {
            $type = gettype($boolean);
            throw new Exception ("setIsSharingAxes() of GooglePlot class requires type Boolean; $type was given.");
        }
        $this->isSharingAxes = $boolean;
        return $this;
    }


    public function getKind()
    {   
        return $this->kind;
    }


    public function getData()
    {
        return $this->data;
    }


    public function setDependents($dependents)
    {
        $this->dependents = $dependents;
        return $this;
    }


    public function setTitle($title)
    {
        $this->title = $title;
        return $this;
    }


    public function getTitle()
    {
        return $this->title;
    }

    public function getDependents()
    {
        return $this->dependents;
    }


    public function getIndependentType()
    {
        return $this->independentType;
    }

    public function addDependent($dependent)
    {
        $this->dependents[] = $dependent;
        return $this;
    }


    private function independentlyDolledUp($value)
    {
        if ($this->getIndependentType() == 'datetime')
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


    private function getDataTable()
    {
        return $this->dataTable;
    }


    private function makeJsDataTable()
    {
        $data_header = "['$this->independent'";
        foreach ($this->dependents as $dependent)
        {
            $data_header .= ", '$dependent'";
        }
        if ($this->independentType == 'datetime')
        {
            $data_header .= ", { role: 'annotation' }, { role: 'annotationText' }";
        }
        $data_header .= "],\n";
        $data_body = "";
        foreach ($this->data as $row)
        {
            if ($this-> independentType == 'datetime' && array_key_exists($row->{$this->independent}, $this::$releases))
            {
                $annotation = "'R'";
                $annotation_text = "'{$this::$releases[$row->{$this->independent}]}'";
            }
            else
            {
                $annotation = 'null';
                $annotation_text = "null";
            }
            $x = $this->independentlyDolledUp($row->{$this->independent});
            $data_body .= "[$x";
            foreach ($this->dependents as $y)
            {
                $value = $row->{$y};
                if ($value == NULL)
                {
                    $value = 0;
                }
                $data_body .= ", $value";
            }
            if ($this->independentType == 'datetime')
            {
                $data_body .= ", $annotation";
                $data_body .= ", $annotation_text";
            }
            $data_body .= "],\n";
        }
        $this->dataTable = $data_header . $data_body;
    }    


    private function getSpecialOptions()
    {
        $special_options = "";
        switch ($this->kind)
        {
            case 'stacked':
                $special_options .= "isStacked: true\n";
        }
        return $special_options;
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
            'line' => 'LineChart',
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
        if (!$this->isSharingAxes)
        {
            foreach ($this->dependents as $index => $y)
            {
                $axes .= "$index: {title: '$y'},\n";
                $series .= "$index:{ targetAxisIndex: $index},\n";
            }
        }
        else if ($this->isSharingAxes)
        {
            $axes .= "0: {title: ''},\n";
            foreach ($this->dependents as $index => $y)
            {
                $series .= "$index:{ targetAxisIndex: 0},\n";
            }
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
                {$this->getDataTable()}
            ]);
            {$this->getOptions()}
            var chart = new google.visualization.{$this->chartClass}(document.getElementById('$this->codename'));
            chart.draw(data, options);
        }
        </script>";
        return $js;
    }


    public function display()
    {
        echo $this->getJavascript();
    }
}

