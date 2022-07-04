# web-crawler
VUB Task - Web Crawler
<h1 style='font-size: 20px; text-align:center'>Using <a href='https://docs.scrapy.org/en/latest/index.html'>Scrapy</a> to get the required data from the website</h1>

<p>The spider that is created for scrapping the data from the requested website is <span style="font-weight: bold">ihvz_spider.py</span>
<p>

<p style="color: red; font-weight: bold">This code works on Python3</p>

<h2 style='font-size: 16px; margin-top: 75px'>Running the application:</h2>
<ul>
    <li style="margin-bottom: 20px">
        py -m venv venv            
        ==>
        making a virtual environment with the name 'venv'
    </li>
    <li style="margin-bottom: 20px">
        source venev/bin/activate  (For Mac)
        .\venv\Scripts\activate  (For Windows)
        ==>
        Activating the v environment 
    </li>
    <li style="margin-bottom: 20px">
        pip install -r requirements.txt
        ==>
        To install the required packages to run the code
    </li>
    <li style="margin-bottom: 20px">
        cd ihvz_connector
    </li>
    <li style="margin-bottom: 20px">
        scrapy crawl content -o articles.json
        =>
        creating a JSON file named 'articles.json' to store the required data in it.
    </li>
    
</ul>
