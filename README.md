### Spider

> Crawl the daily price of goods in Hong Kong.

* First you should install scrapy (make sure you have installed pip before)

  `pip install scrapy`

* Start

  > * To the Directory './pricescrapy/pricescapy/'.
  >
  > * Do the commands and you can see the result on the terminal window.
  >
  >   `scrapy crawl consumer`
  >
  > * Or do `scrapy crawl consumer -o item.json -t json` to format the result data into json.
  >
  > * Ps: For the convenience of testing. I set `start_urls` to ` "https://www3.consumer.org.hk/pricewatch/supermarket/index.php?view=0&filter1=004&filter2=007&filter3=001"`  . Actually we should set it to ` https://www3.consumer.org.hk/pricewatch/supermarket/index.php?view=0&filter1=&filter2=&filter3= ` to grab all data.
  >
  >   ​

  ​