import jieba
import jieba.analyse
import re
import math

class CoSim:
    def __init__(self, txt1, txt2):
        self.CoSim = self.CoSim(txt1, txt2)

    def __str__(self):
        return str(self.CoSim)

    #清除文本噪音
    def ClearContent(self, content):
        repl = re.compile(u"[^\u4a00-\u9fa5]")
        content = repl.sub('', content)
        return content

    def DealString(self, content):
        content = self.ClearContent(content)
        #调用jieba库的方法进行分词和提取关键词
        seg = jieba.cut(content)
        jieba.analyse.set_stop_words('stop_words.txt')
        KeyWords = jieba.analyse.extract_tags(
            '|'.join(seg), topK = 10, allowPOS = ())
        #print(KeyWords)

        #计算关键词词频
        list_seg = jieba.lcut(content)
        keydict = {}
        tf_list = []
        for word in list_seg:
            if word in KeyWords:
                keydict[word] = keydict.get(word, 0) + 1
        for key in keydict:
            keydict[key] = keydict[key]/len(list_seg)
            tf_list.append(keydict[key])

        #把生成的词频向量进行排序
        tf_list.sort(reverse = True)
        #print(tf_list)

        return tf_list
        #print(keydict)
        #print(tf_list)

    #求余弦值
    def CoSim(self, t1, t2):
        vector_t1 = self.DealString(t1)
        vector_t2 = self.DealString(t2)
        dif = len(vector_t1) - len(vector_t2)
        if dif < 0:
            for i in range(dif):
                vector_t1.append(0)
        elif dif >0:
            for i in range(dif):
                vector_t2.append(0)

        part_1 , part_2, part_3= 0, 0, 0
        for i in range(len(vector_t1)):
            part_1 += vector_t1[i]*vector_t2[i]
            part_2 += vector_t1[i]**2
            part_3 += vector_t2[i]**2
        cosine = part_1/(math.sqrt(part_2)*math.sqrt(part_3))
        return cosine
