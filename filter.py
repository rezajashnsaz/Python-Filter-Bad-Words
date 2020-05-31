

def filter_bad_words(sentence):
    #این فانکشن کلمات رکیک را  در جمله پیدا و حذف میکند

    bad_words = ['test','example','foo']
    #لیست کلماتی که میخواهیم فیلتر شود

    

    i = 0
    clean_sentence =''


    for word in bad_words:

        if i == 0:
            #اگه دفعه اول اجرای حلقه بود رشته ورودی رو بخونه
            string = sentence
        else:
            #اگه دفعه اول نبود رشته ای که یه بار فیلتر شده رو بخونه
            string = clean_sentence

        i = i + 1
        #شمارنده حلقه یکی زیاد میشه

        if word in string:
            clean_sentence = string.replace(word, '{***}')

    return clean_sentence
            
            


###
#نحوه استفاده از این فانکشن در پایین
###
sentence = 'hi this is test sentence . and example'
#رشته ای که کاربر فرستاده است

new_sentence = filter_bad_words(sentence)
print(new_sentence)

