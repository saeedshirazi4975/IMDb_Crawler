IMDb-crawler developed in PYTHON-V3.8.6 by 'Saeed Shirazi' at December 11, 2020


This crawler take a query as string from you and do search in IMDb, crawl the data and give you top 5 results and finally save them in results directory as a json file.

an example for result if query = 'inception' :

                                              titles  ...                                               imgs
0                                   Inception (2010)  ...  https://m.media-amazon.com/images/M/MV5BMjAxMz...
1                           Inception (2014) (Short)  ...  https://m.media-amazon.com/images/M/MV5BYWJmYW...
2  Inception (2017) (TV Episode)\n- Season 1 | Ep...  ...  https://m.media-amazon.com/images/M/MV5BODI4ZW...
3            Inception: The Cobol Job (2010) (Video)  ...  https://m.media-amazon.com/images/M/MV5BMjE0NG...
4  Inception: Jump Right Into the Action (2010) (...  ...  https://m.media-amazon.com/images/M/MV5BZGFjOT...

[5 rows x 4 columns]

*'inception.json' file in results