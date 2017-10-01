# web_scraper

This web_scraper is use to crawl news info and it is built on top of django and Scrapy framework. It use to crawl "www.bbc.com" news at the moment. Current hosted at Amazon instance http://13.229.116.155/news_scrappy/.

Project Requirements
----------------------------
1. django & django rest framework for API. 
2. scrapy
3. mongoDB
4. mysql


How to Use
---------------
1. git clone the project.
2. go to project directory and prepare virtual environment.
    - virtualenv venv
3. install application requirements
    - pip install -r requirements.txt 
4. install mysql and mongodb.


How to crawl news
----------------------
1. go to web_scraper/crawl_bot directory.
2. run crawling command 
   - scrapy crawl news_crawling 
   
   
How to retrieve/search article by keyword
--------------------------------------
1. go to web_scraper directory.
2. run django application command below.

   - Query by Article Text 
      - python manage.py mongo_api --host=http://13.229.116.155 --query_article_text=Rugby
   - Query by Article Headline
      - python manage.py mongo_api --host=http://13.229.116.155 --query_article_headline=Rugby
   - Query by Article Tag
      - python manage.py mongo_api --host=http://13.229.116.155 --query_article_tag=Rugby
   - Query based on Keyword for article_tag, article_text, article_headline
      - python manage.py mongo_api --host=http://13.229.116.155 --query_any=Rugby   
   - Help 
      - python manage.py mongo_api --help
   
   - API response Example
     * Query result = "[{"id":"59d0c3413f6f67258f1c3576","article_text":"New Zealand cap their fifth Rugby Championship victory in six years with a comprehensive win over Argentina.","article_headline":"NZ beat Argentina after retaining title","article_url":"http://www.bbc.com/sport/rugby-union/41458218","article_tag":"Rugby Union"}]"
     * Query status code = "200"
     * Query number of results"1"
      
