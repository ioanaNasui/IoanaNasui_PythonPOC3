from operator import index
from os import remove
from random import choice


def build_stock(number_of_articles):
    only_articles = ["shirt", "scarf", "gloves", "hat"]  # index 0,1,2,3
    only_sizes = ["S", "M", "L", "XL", "XXL"]  # index 0,1,2,3,4
    # print(only_articles)
    # print(only_sizes)
    articles = []
    for article_index in range(number_of_articles):
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
        # print((article, size) in articles)
        print(f'article to be removed: {(article, size)}')
        articles.remove((article, size))
        print(f'number of articles: {len(hobby_shop_articles)}')
    else:
        print(f'Not found: {(article, size)}')
    return articles


def refill_stock(articles, no_of_articles):
    for no_of_article in range(0, no_of_articles):
        only_articles = ["shirt", "scarf", "gloves", "hat"]  # index 0,1,2,3
        only_sizes = ["S", "M", "L", "XL", "XXL"]  # index 0,1,2,3,4
        new_article = (choice(only_articles), choice(only_sizes))
        articles.append(new_article)
    return articles


def articles_to_add():
    no_of_articles_to_add = int(input("Enter how many articles to add: (must be an int):"))
    if type(no_of_articles_to_add) != int:
        for tries in range(3):
            no_of_articles_to_add_other_try = int(input("Enter how many articles to add: (must be an int):"))
            return no_of_articles_to_add_other_try
    else:
        return no_of_articles_to_add


def list_methods_in_python(article, size, articles):
    print('--------------This part tests some methods---------')
    print(
        f"Number of similar articles of type {article} with size {size} is {articles.count((article, size))}")
    # starting the search from index 1
    if articles.count((article, size)):
        print(
            f"The index where one article of type {article} with size {size} is {articles.index((article, size), 0)}"
         )
    # using extend method on the list: will add 2 new elements: <article> and <size> and not 1 tuple <(article,size)>
    print(
        f"Added one article of type {article} with size {size} {articles.extend((article,size))}"
    )
    print(f"New length: {len(articles)} and the list: {articles}")
    # reverse the list
    new_articles = ['hat', 'shirt', 'gloves', 'scarf']
    new_articles.reverse()
    print(f"Reverse List: {new_articles}")
    # using sort() method
    new_articles.sort(key=len, reverse=True)
    print(f"The sorted list reverse based on length:{new_articles}")


if __name__ == '__main__':
    print('-----------Homework-----------')
    hobby_shop_articles = build_stock(400)
    print(f'Total number of articles in the store: {len(hobby_shop_articles)} and all articles in the store after '
          f'initial stock: {hobby_shop_articles}')

    hobby_shop_articles = sell_latest_article(hobby_shop_articles)
    print(f'Latest article added was removed; new no of articles is (399): {len(hobby_shop_articles)} and all articles '
          f'in the store after last article was removed: {hobby_shop_articles}')

    article_type = str(input("Enter article type ('shirt', 'scarf', 'gloves' or 'hat'):"))
    article_size = str(input("Enter article size ('S', 'M', 'L', 'XL', 'XXL'):"))
    hobby_shop_articles = sell_one_article(article_type, article_size, hobby_shop_articles)
    print(f'Another article removed -> new no of articles is (398): {len(hobby_shop_articles)} and all articles in '
          f'the store after second article ({article_type}, {article_size}) was removed: {hobby_shop_articles}')

    # no_of_articles_to_add = int(input("Enter how many articles to add: (must be an int):"))
    how_many_articles_to_add = articles_to_add()  # to be removed
    hobby_shop_articles = refill_stock(hobby_shop_articles, how_many_articles_to_add)  # add x new item to the stock
    print(f'New article(s) added {how_many_articles_to_add}-> new no of articles {398+how_many_articles_to_add}: {len(hobby_shop_articles)}')
    print(f'All articles in the store: {hobby_shop_articles}')
    print('-----------Homework part 2-----------')
    list_methods_in_python('hat', 'S', hobby_shop_articles)


