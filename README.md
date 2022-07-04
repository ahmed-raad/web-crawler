# web-crawler
VUB Task - Web Crawler
<h1 style='font-size: 20px; text-align:center'>Using <a href='https://docs.scrapy.org/en/latest/index.html'>Scrapy</a> to get the required data from the website</h1>

<p>The spider that is created for scrapping the data from the requested website is <span style="font-weight: bold">ihvz_spider.py</span>
<p>

<p style="color: red; font-weight: bold">This code works on Python3</p>

<h2 style='font-size: 16px; margin-top: 75px'>Running the application:</h2>
<ul>
    <li style="margin-bottom: 20px">
        <span style='background: #e0e0e0; display: block; width: 220px; text-align: center; border-radius: 10px; font-weight: 500;'>
            py -m venv venv
        </span>
        making a virtual environment with the name 'venv'
    </li>
    <li style="margin-bottom: 20px">
        <span style='background: #e0e0e0; display: block; width: 280px; text-align: center; border-radius: 10px; font-weight: 500;'>
            source venev/bin/activate  (For Mac)
            .\venv\Scripts\activate  (For Windows)
        </span>
        Activating the v environment 
    </li>
    <li style="margin-bottom: 20px">
        <span style='background: #e0e0e0; display: block; width: 220px; text-align: center; border-radius: 10px; font-weight: 500;'>
        pip install -r requirements.txt
        </span>
        To install the required packages to run the code
    </li>
    <li style="margin-bottom: 20px">
        <span style='background: #e0e0e0; display: block; width: 150px; text-align: center; border-radius: 10px; font-weight: 500'>
        cd ihvz_connector
        </span>
    </li>
    <li style="margin-bottom: 20px">
        <span style='background: #e0e0e0; display: block; width: 300px; text-align: center; border-radius: 10px; font-weight: 500'>
        scrapy crawl content -o articles.json
        </span>
        creating a JSON file named 'articles.json' to store the required data in it.
    </li>
    
</ul>
