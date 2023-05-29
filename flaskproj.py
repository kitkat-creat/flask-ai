from flask import Flask,request,render_template
from waitress import serve
import openai
import pickle
# import openai
# import gradio



app = Flask(__name__)

#landing page
@app.route('/')
def hello_world():
    return render_template("/login.html")


@app.route('/form_login',methods=['POST','GET'])
def login():
    text = request.form['username']
    text2 = "choose if this report belongs to urology, radiology,orthopedic,gastroenterology, or neurology"
  
    openai.api_key = "##"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text+text2,
        temperature = 0.6,
        max_tokens = 150,
    )
    ChatGPT_reply = response.choices[0].text
    
    return render_template('/login.html', info=ChatGPT_reply)

if __name__ == '__main__':
    
    serve(app, host="localhost", port=3000)