# -*- coding:utf-8 -*-

from lxml import html
import requests
import json
import re

class Tool:
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;') #去除Img标签
    removeAddr = re.compile('<a.*?>| </a>') #去除链接
    replaceLine = re.compile('<br>|<div>|</div>|<p>|</p>')

    removeTag = re.compile('<.*?>')

    @classmethod
    def replace(cls,x):
        x = re.sub(cls.removeImg,'',x)
        x = re.sub(cls.removeAddr,'',x)
        x = re.sub(cls.replaceLine,'',x)
        x = re.sub(cls.removeTag,'',x)

        return x.strip()

class Weibo(object):

    def get_weibo(self, id, page):
        url = 'https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}&containerid=107603{}&page={}'.format(id,id,id,page)
        response = requests.get(url)
        print 'url='+url
        ob_json = json.loads(response.text)
        #print type(ob_json)
        list_cards = ob_json.get('cards')
        return list_cards

    def get_comments(self,id,page):
        url = 'https://m.weibo.cn/api/comments/show?id={}&page={}'.format(id, page)
        response = requests.get(url)
        ob_json = json.loads(response.text)
        list_comments = ob_json.get('hot_data')
        return list_comments

    def main(self, uid, page):
        list_cards = self.get_weibo(uid, page)
        for card in list_cards:
            if card.get('card_type') == 9:
                id = card.get('mblog').get('id')
                text = card.get('mblog').get('text')
                text = Tool.replace(text)
                print '*****'
                print u'@@@微博:'+text+'\n'

                # list_comments = weibo.get_comments(id, 1)
                # print 'id='+id
                # print 'uid='+uid
                # print list_comments
                # count_hotcomments = 1
                # for comment in list_comments:
                #     created_at = comment.get('created_at')
                #     link_counts = comment.get('link_counts')
                #     text = comment.get('text')
                #     tree = html.fromstring(text)
                #     text = tree.xpath('string(.)')
                #     name_user = comment.get('user').get('screen_name')
                #     source = comment.get('source')
                #     if source == '':
                #         source = u'未知'
                #
                #     print str(count_hotcomments),':**',name_user,'**',u'发表于:**'+created_at, u'**点赞:**'+str(link_counts)+u'  **来自:**'+source
                #     print text+'\n'
                #     count_hotcomments += 1
                print '========================'

if __name__ == '__main__':
    weibo = Weibo()
    # weibo.main('1239246050', 1)
    for x in range(10):
        print '第'+str(x+1)+'页微博：'
        weibo.main('5685740343', x+1)

#http://weibo.com/u/5685740343?refer_flag=1001030102_&is_hot=1
#http://weibo.com/p/1004061239246050/home?from=page_100406&mod=TAB&is_hot=1#place
#http://weibo.com/p/1005055685740343/home?from=page_100505&mod=TAB&is_hot=1#place
#https://m.weibo.cn/api/container/getIndex?uid=5685740343&type=uid&value=5685740343&containerid=1076035685740343&page=1
#https://m.weibo.cn/api/container/getIndex?uid=1239246050&type=uid&value=1239246050&containerid=1076031239246050&page=1