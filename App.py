from flask import Flask, render_template, request
from googletrans import Translator ; import wolframalpha

  







app = Flask(__name__)
 
#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(english_bot)

#for files in os.listdir("turkish\\"):
#    data = open("turkish\\"+files,encoding="utf8").readlines()
#    trainer.train(data)	

#trainer.train("chatterbot.corpus.turkish")
 
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    #language = Translator().detect(userText).lang
    language = 'tr'
    question = Translator().translate(userText, src=language, dest='en').text
    client = wolframalpha.Client('KP62YE-GGKGTVHAJY')
    res = client.query(question)
    answer = next(res.results).text
    
    answer_last = Translator().translate(answer, src='en', dest=language).text
    return str(answer_last)
 
 
# heroku app
# if __name__ == "__main__":
#     app.run(port=3000)
