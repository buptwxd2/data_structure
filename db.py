from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import re
import jieba


Base = declarative_base()
engine = create_engine('mysql+pymysql://root:AI@2019@ai@rm-8vbwj6507z6465505ro.mysql.zhangbei.rds.aliyuncs.com:3306/stu_db',
                       echo=True)

class News_Chinese(Base):
    __tablename__ = 'news_chinese'
    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    source = Column(String(), nullable=False)
    content = Column(String(), nullable=False)
    feature = Column(String(), nullable=False)
    title = Column(String(64), nullable=False)
    url = Column(nullable=False)

DBsession = sessionmaker(bind=engine)
sess = DBsession()

def token(string):
    if not string:
        return ""
    # no idea why the new line is "\\n" in the news_content
    if "\\n" in string:
        remove_new_line_str = ''.join(string.split("\\n"))
    else:
        remove_new_line_str = ''.join(string.split("\n"))
    return "".join(re.findall(r'[\d|\w]+', remove_new_line_str))

def cut(string):
    return ' '.join(jieba.cut(string))

# all_news_content = []
# for news in sess.query(News_Chinese).order_by(News_Chinese.id):
#     news_content = news.content
#     cut_word_str = cut(token(news_content))
#     if cut_word_str:
#         all_news_content.append(cut_word_str)
#
#     if len(all_news_content) % 50 == 0:
#         print(len(all_news_content))
#
# print("Total length is {}".format(len(all_news_content)))
#
# with open('news-cut.txt', 'w+', encoding='utf8') as f:
#     for news_content in all_news_content:
#         f.write(news_content + "\n")


all_news_content = []
for news in sess.query(News_Chinese).order_by(News_Chinese.id):
    news_content = news.content
    print(news_content)
    news_content = token(news_content)
    print(news_content)
    if news_content:
        all_news_content.append(news_content)

    if len(all_news_content) % 50 == 0:
        print(len(all_news_content))

print("Total length is {}".format(len(all_news_content)))

with open('news-content.txt', 'w+', encoding='utf8') as f:
    for news_content in all_news_content:
        f.write(news_content + "\n") 
