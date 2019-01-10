from scrapy_djangoitem import DjangoItem


class DjangoItemPlus(DjangoItem):
    def all(self):
        return self.instance.all()

    def filter(self, **kwargs):
        return self.instance.filter(**kwargs)

    def get(self, **kwargs):
        return self.instance.get(**kwargs)

    def update(self, **kwargs):
        return self.instance.update(**kwargs)
