# This is a test script to begin playing with Python Data mining
sentences_list = []
words = []

email = """
Dear Hiring Manager,

I would like to express my deep interest in a position as editorial assistant for your publishing company.As a recent graduate with writing, editing, and administrative experience, I believe I am a strong candidate for a position at the 123 Publishing Company.You specify that you are looking for someone with strong writing skills. As an English major at XYZ University, a writing tutor, and an editorial intern for both a government magazine and a college marketing office, I have become a skilled writer with a variety of publication experience.My maturity, practical experience, attention to detail, and eagerness to enter the publishing business will make me an excellent editorial assistant. I would love to begin my career with your company, and am confident that I would be a beneficial addition to the 123 Publishing Company.I have enclosed my resume, and will call within the next week to see if we might arrange a time to speak together.

Thank you so much for your time and consideration.

Sincerely,

Jane Jones
"""
# Clean up the email body by removing line breaks
email = email.replace('\n',' ')

# Split the email into sentences
sentences = email.split('.')

for each in sentences:
    sentence = each.strip()
    sentences_list.append(sentence)
#Break each sentence into words

for each in sentences_list:
    a = each.split(" ")
    for each_el in a:
        thing = each_el.strip()
        words.append(thing)
