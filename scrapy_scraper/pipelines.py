# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
import rethinkdb as r

r.connect("162.242.238.193", 28015).repl()

class ScrapyScraperPipeline(object):

  def process_item(self, item, spider):

    law_grams = item['law'].upper()
    law_grams = law_grams.replace('TO ', '')
    law_grams = law_grams.replace('OF ', '')
    law_grams = law_grams.replace('AND ', '')
    law_grams = law_grams.replace('THE ', '')
    law_grams = law_grams.replace('A ', '')
    law_grams = law_grams.replace('AN ', '')
    item['law_grams'] = law_grams
    item['active'] = True
    item['precision'] = 1

    r.db('jurispect').table('laws').insert({"law": item['law'], "law_grams": item['law_grams'],
                                            "active": item['active'], "precision": item['precision'],
                                            "created": r.now()}).run()
