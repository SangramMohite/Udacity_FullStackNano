#!/usr/bin/env python3
import datetime
import psycopg2

DB_NAME = "news"


def get_top3_popular_articles():
    """Return Top 3 most viewed articles from the 'database'."""
    postsdb = psycopg2.connect(database=DB_NAME)
    cursor = postsdb.cursor()
    top3_articles = """select articles.title, count(articles.title) as num
     from articles,log where log.path like '%article%' and articles.slug like
     substring(log.path from 10) group by articles.title
     order by count(articles.title) desc limit 3;"""
    cursor.execute(top3_articles)
    articles_anaylytics = cursor.fetchall()
    print("Most popular three articles of all time:")
    for row in articles_anaylytics:
        print("{} ---- {}".format(row[0], row[1]))
    postsdb.close()


def get_top3_popular_authors():
    """Return Top 3 most viewed articles from the 'database'."""
    postsdb = psycopg2.connect(database=DB_NAME)
    cursor = postsdb.cursor()
    top3_authors = """select w.name, sum(p.views) from authors w,
     (select articles.title, count(articles.title) as views from articles, log
     where log.path like '%article%' and articles.slug
     like substring(log.path from 10) group by articles.title
     order by count(articles.title) desc)as p, articles a
     where a.title = p.title and a.author = w.id group by w.name
     order by sum(p.views) desc;"""
    cursor.execute(top3_authors)
    author_anaylytics = cursor.fetchall()
    print("Most popular article authors of all time:")
    for row in author_anaylytics:
        print("{} ---- {}".format(row[0], row[1]))
    postsdb.close()


def get_days_with_1pct_error():
    """Return Top 3 most viewed articles from the 'database'."""
    postsdb = psycopg2.connect(database=DB_NAME)
    cursor = postsdb.cursor()
    errors = """select my_day, percentage as error_day from
     (select e.my_day as my_day, e.error, t.status, (e.error * 100.0)/t.status
     as percentage from (select date_trunc('day',time) as my_day, count(status)
     as error from log where status like '4%' or status like '5%'
     group by date_trunc('day',time) order by my_day desc) as e,
     (select count(status) as status, date_trunc('day', time)as my_day
     from log group by my_day order by my_day desc) as t
     where e.my_day = t.my_day) as t where t.percentage > 1.0;"""
    cursor.execute(errors)
    error_anaylytics = cursor.fetchall()
    print("days did more than 1% of requests lead to errors:")
    for row in error_anaylytics:
        print("{} ---- {}".format(row[0], row[1]))
    postsdb.close()


get_top3_popular_articles()
print("")
get_top3_popular_authors()
print("")
get_days_with_1pct_error()
