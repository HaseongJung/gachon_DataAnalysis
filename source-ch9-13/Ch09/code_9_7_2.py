#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 9.7 정보를 한눈에 보여주는 워드 클라우드 , 232쪽
#
import wikipedia
from wordcloud import WordCloud

# 위키백과 사전의 컨텐츠 제목을 명시해 준다
wiki = wikipedia.page('Artificial intelligence')
# 이 페이지의 텍스트 컨텐츠를 추출하도록 한다
text = wiki.content
# 워드 클라우드를 생성하기 위해 위의 코드를 삽입할 것
wordcloud = WordCloud(width = 500, height = 500).generate(text)