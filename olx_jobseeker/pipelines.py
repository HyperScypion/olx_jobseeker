# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import *


class OlxJobseekerPipeline:

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.engine = create_engine('sqlite:///../data/jobs.db')
        self.metadata = MetaData(self.engine)

    def process_item(self, item, spider):
        self.store_db(item)
        print(f'ITEM: {item}')
        return item

    def store_db(self, item):
        self.table = Table('jobs', self.metadata, autoload=True)
        self.insert = self.table.insert()
        self.insert.execute(title=item['title'][0],
                            description=item['description'][0],
                            location=item['location'][0],
                            link=item['link'],
                            salary_from=item['salary_from'],
                            salary_to=item['salary_to'])

