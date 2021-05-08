from operator import index
from os import remove
from random import choice


def build_and_refill_stock(articles, no_of_articles):
    only_articles = ["shirt", "scarf", "gloves", "hat"]  # index 0,1,2,3
    only_sizes = ["S", "M", "L", "XL", "XXL"]  # index 0,1,2,3,4
    print(only_articles)
    print(only_sizes)
    for article_index in range(no_of_articles):
        new_article = (choice(only_articles), choice(only_sizes))
        articles.append(new_article)
    return articles


def sell_latest_article(articles):
    if len(articles) > 0:
        articles.pop()
        return articles
    else:
        print("The stock is empty")


def sell_one_article(article, size, articles):
    if (article, size) in articles:
        print((article, size) in articles)
        del (article, size)
    else:
        print(f'Not found: {(article, size)}')
    return articles


def refill_stock(articles):
    return articles


if __name__ == '__main__':
    hobby_shop_articles = []
    hobby_shop_articles = build_and_refill_stock(hobby_shop_articles, 400)
    print(f'All articles in the store: {hobby_shop_articles}')
    print(f'Total number of articles: {len(hobby_shop_articles)}')
    hobby_shop_articles = sell_latest_article(hobby_shop_articles)
    print(f'Latest article removed -> new no of articles 399: {len(hobby_shop_articles)}')
    article_type = str(input("Enter article type ('shirt', 'scarf', 'gloves' or 'hat'):"))
    article_size = str(input("Enter article size ('S', 'M', 'L', 'XL', 'XXL'):"))
    hobby_shop_articles = sell_one_article(article_type, article_size, hobby_shop_articles)
    print(f'Another article removed -> new no of articles 398: {len(hobby_shop_articles)}')
    hobby_shop_articles = build_and_refill_stock(hobby_shop_articles, 2)  # add 1 new item to the stock
    print(f'AOne more article added -> new no of articles 399: {len(hobby_shop_articles)}')
# Hobby Shop
# #- Have at least 400 articles in the shop
# #- Have at least four types of articles (shirt, scarf, gloves, hat)
# #- Have at least five sizes (S M L XL XXL) for each type of article
# #- To be able to sell the latest article that was added to the shop
# - To be able to sell any item that is in the shop
# - To restock the shop with new items

# no custom OBJECTS
# no dictionaries

# Python types: int, float, str, list, tuple

# NOT ALL IN MAIN!!!
# functions!!!
# Extra
# - Check the LIST methods from PYTHON that have not been discussed and use them in a simple flow (len, min, max, append, extend, insert, clear, pop, remove...)
