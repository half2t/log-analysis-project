### Project: Logs Analysis
-----------------------------------------------------------------
This project generate report to answer three Questions about news
website:
1.What are the most popular three articles of all time?
2.Who are the most popular article authors of all time?
3.On which days did more than 1% of requests lead to errors?
-----------------------------------------------------------------
#### Requirements
-----------------------------------------------------------------
You can run the app in python 2 or python 3
-----------------------------------------------------------------
I'm using Vagrant/VirtualBox
Download VirtualBox from below link:
https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
Download Vagrant from below link:
https://www.vagrantup.com/downloads.html
Download VM configuration from below link:
https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/
5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip

Download the database script file 'newsdata.sql' from this link
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/
57b5f748_newsdata/newsdata.zip
copy it to your virtual shared folder then login to your postgresql
and create database name it 'news' then run this command 
[psql -f newsdata.sql news]
-----------------------------------------------------------------
create this views in the news database
Just copy-paste and run it
-----------------------------------------------------------------
create view vwerrorlogcount as
SELECT date(log."time") AS onlydate,
    count(*) AS errors
   FROM log
  WHERE log.status ~~ '4%'::text OR log.status ~~ '5%'::text
  GROUP BY onlydate;

create view vwlogcount as
SELECT date(log."time") AS onlydate,
    count(*) AS num
   FROM log
  GROUP BY onlydate;
-----------------------------------------------------------------
