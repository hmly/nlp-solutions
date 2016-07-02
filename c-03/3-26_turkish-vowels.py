# Chapter 3 - exercise 26

# Imports
import nltk
import re

# Text (Lang: Turkish)
text = '''
        Her şahsın öğrenim hakkı vardır. Öğrenim hiç olmazsa ilk ve temel 
        safhalarında parasızdır. İlk öğretim mecburidir. Teknik ve mesleki 
        öğretimden herkes istifade edebilmelidir. Yüksek öğretim, 
        liyakatlerine göre herkese tam eşitlikle açık olmalıdır.
        Öğretim insan şahsiyetinin tam gelişmesini ve insan haklarıyla ana 
        hürriyetlerine saygının kuvvetlenmesini hedef almalıdır. Öğretim 
        bütün milletler, ırk ve din grupları arasında anlayış, hoşgörü ve 
        dostluğu teşvik etmeli ve Birleşmiş Milletlerin barışın idamesi 
        yolundaki çalışmalarını geliştirmelidir.
        Ana baba, çocuklarına verilecek eğitim türünü seçmek hakkını 
        öncelikle haizdirler.
        Herkes, topluluğun kültürel faaliyetine serbestçe katılmak, güzel 
        sanatları tatmak, ilim sahasındaki ilerleyişe iştirak etmek ve bundan 
        faydalanmak hakkını haizdir.
        Herkesin yarattığı, her türlü bilim, edebiyat veya sanat eserlerinden 
        mütevellit manevi ve maddi menfaatlerin korunmasına hakkı 
        vardır.
        '''

# Main
# text = open('turkish.txt', 'rU') -> loss of turkish char: ö..
fd = nltk.FreqDist(vowel for w in text
                        for vowel in re.findall(r'[aeıioöuü]', w))
print fd.items()
