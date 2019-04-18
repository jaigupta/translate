from google.cloud import translate

client= translate.Client()

def printAllLanguagesAvailable():
    print("Following languages are available:")
    for item in client.get_languages():
        print(item)

def translate(sentences, input_lang, output_lang):
    return [client.translate(sentence, source_language=input_lang, target_language=output_lang)
        for sentence in sentences]

printAllLanguagesAvailable()

english_sentences=[
        'Modi was appointed Chief Minister of Gujarat in 2001, due to Keshubhai Patel\'s failing health and poor public image following the earthquake in Bhuj. ',
        'A Supreme Court-appointed Special Investigation Team found no evidence to initiate prosecution proceedings against Modi personally.',
        'His policies as chief minister, credited with encouraging economic growth, have received praise.']

for output in translate(english_sentences, 'en', 'hi'):
    print(output['translatedText'])

