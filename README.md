


# Learn Grafana 7.0

<a href="https://www.packtpub.com/eu/data/learn-grafana-7-0?utm_source=github&utm_medium=repository&utm_campaign=9781838826581"><img src="https://www.packtpub.com/media/catalog/product/cache/bf3310292d6e1b4ca15aeea773aca35e/9/7/9781838826581-original_36.jpeg" alt="Learn Grafana 7.0" height="256px" align="right"></a>

This is the code repository for [Learn Grafana 7.0](https://www.packtpub.com/eu/data/learn-grafana-7-0?utm_source=github&utm_medium=repository&utm_campaign=9781838826581), published by Packt.

**A beginner's guide to getting well versed in analytics, interactive dashboards, and monitoring**

## What is this book about?
Grafana is an open-source analytical platform used to analyze and monitoring time-series data. This beginner's guide will help you get to grips with Grafana's new features for querying, visualizing, and exploring metrics and logs no matter where they are stored.

This book covers the following exciting features: 
* Find out how to visualize data using Grafana
* Understand how to work with the major components of the Graph panel
* Explore mixed data sources, query inspector, and time interval settings
* Discover advanced dashboard features such as annotations, templating with variables, dashboard linking, and dashboard sharing techniques
* Connect user authentication to Google, GitHub, and a variety of external services

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1838826580) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
def main():
    logging.basicConfig(level=logging.INFO)
```

**Following is what you need for this book:**
This book is for business intelligence developers, business analysts, data analysts, and anyone interested in performing time-series data analysis and monitoring using Grafana. Those looking to create and share interactive dashboards or looking to get up to speed with the latest features of Grafana will also find this book useful. Although no prior knowledge of Grafana is required, basic knowledge of data visualization and some experience in Python programming will help you understand the concepts covered in the book.	

With the following software and hardware list you can run all code files present in the book (Chapter 1-14).

### Software and Hardware List

| Software required                   | OS required                        |
| ------------------------------------| -----------------------------------|
| Grafana                             | Windows 10 Pro, Linux, Docker      |
| Docker                              | Windows 10 Pro, or Linux |
| Loki/Promtail	                      | Runs in Docker
| Prometheus                          | Runs in Docker |
| InfluxDB                            | Runs in Docker |
| Logstash                            | Runs in Docker |
| Elasticsearch                       | Runs in Docker |
| OpenLDAP                            | Runs in Docker |




We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781838826581_ColorImages.pdf)

### Errata

Chapter 06, Page 133 should read:

  3. Build the Python container to run our scripts:
  
  ```sh
      $ docker build --pull --tag python/ch6 .
  ```
  4. ...
```sh
    $ docker run --rm --network=host -v "$(PWD):/usr/src/app" \
             --name python python/ch6 bin/weather.py \
             --output data/wx.txt \
             --stations KSFO,KDEN,KSTL,KJFK
```
  5. ...
```sh
    $ docker run --rm --network=host -v "$(PWD):/usr/src/app" \
             --name python python/ch6 bin/weather.py \
             --input data/wx.txt \
             --db weatherdb
```
---
Chapter 06, page 157 should read:

### Adding load_eq_data()
The only significant differences in our file load subroutine, called `load_eq_data()` is the encoding of the data to accommodate Unicode (`UTF-8`) characters: 

``` python
    data = input_file.read().encode('utf-8')
```

and the specification of time precision in milliseconds (`ms`):

``` python
response = requests.post(url, params=dict(db=db_name, precision="ms"),
data=data)
```
---
Chapter 08, page 204 should include additional lines:

To load the data into ElasticSearch, run the following command:
``` sh
% docker-compose run logstash logstash < data/Current_FY_Cases.csv
```
For Windows PowerShell, the command is:

``` sh
Get-Content .\data\Current_FY_Cases.csv | docker-compose run logstash logstash
```

### Related products <Other books you may enjoy>
* Hands-On Infrastructure Monitoring with Prometheus [[Packt]](https://www.packtpub.com/eu/virtualization-and-cloud/hands-infrastructure-monitoring-prometheus?utm_source=github&utm_medium=repository&utm_campaign=9781789612349) [[Amazon]](https://www.amazon.com/dp/B07MT42315)

* Learning Kibana 7 - Second Edition [[Packt]](https://www.packtpub.com/eu/data/learning-kibana-7-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781838550363) [[Amazon]](https://www.amazon.com/dp/B07V4SQR6T)

## Get to Know the Author
**Eric Salituro**
is currently a senior software engineer with the enterprise data and analytics platform team at Zendesk. He has an IT career that spans more than 30 years, over 20 of which were spent in the motion picture industry working as a pipeline technical director and software developer for innovative and creative studios such as DreamWorks, Digital Domain, and Pixar. Before moving to Zendesk, he worked at Pixar, helping to manage and maintain their production render farm as a senior software developer. Among his accomplishments is the development of a Python API toolkit for Grafana aimed at streamlining the creation of rendering metrics dashboards.

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.
### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781838826581">https://packt.link/free-ebook/9781838826581 </a> </p>