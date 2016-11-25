<?php
// Jordan McQueen

require_once('Report.php');

class Dashboard
{
    private $reports;
    public $summary;
    public $name;
    public $date;
    public $description;
    private $url;
    public $message;
    private $headers;

    function __construct($name)
    {   
        $this->reports = [];
        $this->name = $name;
        $this->date = new DateTime();
        $this->summary = "";
        $this->description = "";
        $this->url = url::current(); 
    }


    public function delReport($name)
    {
        unset($this->$reports[$name]);
        $this->refreshHeaders();
        return $this;
    }


    public function addReport($reports)
    {
        if (!is_array($reports)) {
            $reports = [$reports];
        }
        foreach ($reports as $report)
        {
            if (! $report instanceof Report) {
                $type = gettype($report);
                throw new Exception("addReport() of Dashboard class requires object of type Report. $type was given.");
            }
            $this->reports[$report->name] = $report;
        }
        $this->refreshHeaders();
        return $this;
    }


    protected function refreshHeaders()
    {
        $this->headers = [];
        foreach ($this->reports as $key => $value)
        {
            $this->headers[] = $key;
        }
        
        return $this;
    }


    public function getReport($name)
    {
        if (! isset($this->reports[$name])) {
            throw new Exception("Report named \"$name\" does not exist.");
        }
        return $this->reports[$name];
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


    public function getSummary()
    {
        return $this->summary;
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


    public function display()
    {
        $html = "<h1>{$this->name}</h1>
            <h5><em>{$this->summary}</em></h5>
            {$this->description}<br>";
        foreach ($this->reports as $report)
        {
            $html .= $report->display()."<br>";
        }
        return $html;
    }
    

    public function displayForEmail()
    {
        $html = "<h1><u>{$this->name}</u></h1>";
        if ($this->summary) {
            $html .= "<h5><em>{$this->summary}</em></h5>";
        }
        if ($this->description) {
            $html .= "{$this->description}";
        }
        foreach ($this->reports as $report)
        {
            $html .= $report->displayForEmail();
        }

        return $html;
    }

    
    private function buildSwiftEmail()
    {
        $subject = $this->name . " -- " . $this->date->format('Y-m-d');
        $this->message = new Swift_Message($subject);
        include('email_template/report_email.php'); // loads template with $header & $footer
        $body = $header;
        $body .= $this->displayForEmail();
        $body .= $footer;
        $body = new Swift_Message_Part($body, "text/html");
        $this->message->attach($body);
    }


    public function asSwiftEmail()
    {
        $this->buildSwiftEmail();
        return $this->message;
    }

}
