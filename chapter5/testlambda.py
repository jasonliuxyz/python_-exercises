# 权重
# price占权重40%，sales占权重17%，starts占权重13%，comments占权重30%
goods = [{"name":"good1", "price":200, "sales": 100, "starts":5, "comments":400}, {"name":"good2", "price":300, "sales": 400, "starts":100, "comments":400},{"name":"good3", "price":199, "sales": 500, "starts":300, "comments":299}, {"name":"good4", "price":690, "sales": 19999, "starts":5, "comments":1000}]

def my_sorted(args):
    price = args["price"]
    sales = args["sales"]
    starts = args["starts"]
    comments = args["comments"]
    
    data = price * 0.4 + sales * 0.17 + starts * 0.13 + comments * 0.3
    return data

#print(sorted(goods, key=my_sorted))

print(sorted(goods, key=lambda x : x["price"] * 0.4 + x["sales"] * 0.17 + x["starts"] * 0.13 + x["comments"] * 0.3))

