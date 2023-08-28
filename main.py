from spiders.CodeScraperG2A import G2aSpider

# start spider crawl and get final cheapest option
def search(game_name):
    g2a_spider = G2aSpider()

    price = G2aSpider.search_game(game_name)

    print(price)
# get game name
game_name = input("what game are you searching for?")

