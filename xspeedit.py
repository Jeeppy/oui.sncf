
class Box:

    CAPACITY = 10

    def __init__(self, article=0):
        self.contains = article or ''

    def __str__(self):
        return f"{self.contains}"

    @property
    def size(self):
        return sum([int(article)for article in self.contains])

    def can_put_inside(self, article):
        return int(article) + self.size <= self.CAPACITY

    def add(self, article):
        if not self.can_put_inside(article):
            return False
        self.contains = self.contains + article
        return True


class Droid:

    def __init__(self):
        self.boxes = []

    def __str__(self):
        return '/'.join(box.contains for box in self.boxes)

    def put(self, article_chain):
        article_chain = sorted(article_chain, reverse=True)
        for article in article_chain:
            if article.isdigit():
                for box in self.boxes:
                    tidy = box.add(article)
                    if tidy:
                        break
                else:
                    box = Box(article)
                    self.boxes.append(box)
            else:
                print(f"Impossible de mettre {article} dans un carton")


articles = '163841689525773'
droid = Droid()
droid.put(articles)

print(f"Articles : {articles}")
print(f"Robot : {droid} => {len(droid.boxes)} cartons")
