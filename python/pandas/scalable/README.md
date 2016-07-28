# Currency Converter
#### A proof-of-concept of a solution to a currency conversion problem involving historical sales data. Inputs: a csv of [row_id, date, currency_code, amount]. Outputs: text to standard output [row_id, conversion, amount_in_usd]

##### The test.csv example above outputs the following into transform.tsv.
```
row_id	      date	  currency	    amount	    in_usd
      1231	2016-01-02	       CAD	    221.56	159.60147172808627
      1232	2014-05-22	       GBP	   2232.97	3773.0560803794892
      1233	2006-11-09	       AUD	    252.45	194.26702047586514
      1234	2009-01-02	       SEK	   2222.76	288.41917058229836
      1235	2011-12-17	       HKD	    522.32	67.1220114004617
      1236	2013-04-14	       SGD	    554.31	448.04313340365866
      1237	2012-02-09	       KRW	      14.0	0.0125391848850996
      1238	2011-07-05	       BRL	   2231.12	1438.0406589222039
      1239	2010-03-12	       INR	    104.88	2.3051561965048064``
```
