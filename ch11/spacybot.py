import spacy
from telegram.ext import Updater, MessageHandler, Filters
#the callback function that uses spaCy
def utterance(update, context):
  msg = update.message.text
  nlp = spacy.load('en')
  doc = nlp(msg)
  for token in doc:
    if token.dep_ == 'dobj':
      update.message.reply_text('We are processing your request...')
      return
  update.message.reply_text('Please rephrase your request. Be as specific aspossible!')
#the code responsible for interactions with Telegram
updater = Updater('TOKEN', use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text, utterance))
updater.start_polling()
updater.idle()
