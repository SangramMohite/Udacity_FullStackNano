#!/usr/bin/env python3

"""Log analyis of website peformance. Get data from database."""

import datetime
import psycopg2

DB_NAME = "news"


def get_top3_popular_articles():
    """Return Top 3 most viewed articles from the 'database'."""
    postsdb = psycopg2.connect(database=DB_NAME)
    cursor = postsdb.cursor()
    top3_articles = """SELECT articles.title, count(articles.title) AS num
     FROM articles,log WHERE log.path LIKE '%article%' AND articles.slug LIKE
     substring(log.path FROM 10) GROUP BY articles.title
     ORDER BY count(articles.title) DESC LIMIT 3;"""
    cursor.execute(top3_articles)
    articles_anaylytics = cursor.fetchall()
    print("Most popular three articles of all time:")
    for row in articles_anaylytics:
        print("{} ---- {}".format(row[0], row[1]))
    postsdb.close()


def get_top3_popular_authors():
    """Return the most popular authors from the 'database'."""
    postsdb = psycopg2.connect(database=DB_NAME)
    cursor = postsdb.cursor()
    top3_authors = """SELECT w.name, sum(p.views) FROM authors w,
     (SELECT articles.title, count(articles.title) AS views FROM articles, log
     WHERE log.path LIKE '%article%' AND articles.slug
     LIKE substring(log.path FROM 10) GROUP BY articles.title
     ORDER BY count(articles.title) DESC)AS p, articles a
     WHERE a.title = p.title AND a.author = w.id GROUP BY  w.name
     ORDER BY sum(p.views) DESC;"""
    cursor.execute(top3_authors)
    author_anaylytics = cursor.fetchall()
    print("Most popular article authors of all time:")
    hyphens = "-------"
    for row in author_anaylytics:
        print("{:<25} ---- {:<10}".format(row[0], row[1]))
    postsdb.close()


def get_days_with_1pct_error():
    """Return dates having more than 1% error requesting from the website."""
    postsdb = psycopg2.connect(database=DB_NAME)
    cursor = postsdb.cursor()
    errors = """SELECT my_day, percentage AS error_day FROM
     (SELECT e.my_day AS my_day, e.error, t.status, (e.error * 100.0)/t.status
     As percentage FROM (SELECT date_trunc('day',time) AS my_day, count(status)
     AS error FROM log WHERE status LIKE '4%' OR status LIKE '5%'
     GROUP BY date_trunc('day',time) ORDER BY my_day DESC) AS e,
     (SELECT count(status) AS status, date_trunc('day', time) AS my_day
     FROM log GROUP BY my_day ORDER BY my_day DESC) AS t
     WHERE e.my_day = t.my_day) AS t WHERE t.percentage > 1.0;"""
    cursor.execute(errors)
    error_anaylytics = cursor.fetchall()
    print("days did more than 1% of requests lead to errors:")
    for row in error_anaylytics:
        print("{:%Y-%m-%d} ---- {:04.2f}".format(row[0], row[1]))
    postsdb.close()


get_top3_popular_articles()
print("")
get_top3_popular_authors()
print("")
get_days_with_1pct_error()
