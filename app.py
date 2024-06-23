from tkinter import *
from mydb import Database
from tkinter import messagebox
from sentiment import analyze_sentiment
from emotion import client
from NER import ner_analysis
from text_summary import text_summarization
from lang_detect import detect_languages_with_scores


class NLPApp:

    def __init__(self):

        #database class object
        self.dbo = Database()

        #login Gui
        self.root = Tk() #Tk class
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#808B96')
        self.login_gui()
        self.root.mainloop() #this line is to hold the gui in the screen.Otherwise the screen will vanish in seconds



    def login_gui(self):

        self.clear()

        #Heading related edit
        heading = Label(self.root,text='NLPApp',bg='#808B96', fg='White')
        heading.pack(pady=(30,30)) #upore niche margin or space
        heading.configure(font=('verdana',24,'bold'))

        #Enter email
        label1 = Label(self.root,text='Enter Email', font=('Helvetica',12))
        label1.pack(pady=(10,10))

        #Email Input box
        self.user_email= Entry(self.root,width=50)#self use kora hoise user_email variable e because onno func o ei var use korbe
        self.user_email.pack(pady=(5,10),ipady=4) #ipady=inner padding in the box horizontally

        #Enter Passoword
        label2 = Label(self.root,text='Enter Password', font=('Helvetica',12))
        label2.pack(pady=(10,10))
        #Password Input
        self.user_pass= Entry(self.root,width=50,show='*')
        self.user_pass.pack(pady=(5,10),ipady=4)

        #loginButton
        login_button = Button(self.root,text='Login',width=20,height=2,command=self.login_check)
        login_button.pack(pady=(10,10))

        #Not a member
        label3 = Label(self.root,text='Not a member?',bg='#808B96', fg='Yellow', font=('Helvetica',10))
        label3.pack(pady=(10,5))

        #Register now
        register_button = Button(self.root,text='Register',width=12,height=2,command=self.register_gui)
        register_button.pack(pady=(5,10))


    def register_gui(self):
        #to clear the current gui
        self.clear()

        #Heading related edit
        heading = Label(self.root,text='NLPApp',bg='#808B96', fg='White')
        heading.pack(pady=(30,30)) #upore niche margin or space
        heading.configure(font=('verdana',24,'bold'))

        #Enter name
        label0 = Label(self.root,text='Enter Name', font=('Helvetica',12))
        label0.pack(pady=(10,10))

        #Name Input
        self.user_name= Entry(self.root,width=50)
        self.user_name.pack(pady=(5,10),ipady=4)

        #Enter email
        label1 = Label(self.root,text='Enter Email', font=('Helvetica',12))
        label1.pack(pady=(10,10))

        #Email Input
        self.user_email= Entry(self.root,width=50)#self use kora hoise user_email variable e because onno func o ei var use korbe
        self.user_email.pack(pady=(5,10),ipady=4) #ipady=inner padding in the box horizontally

        #Enter Passoword text
        label2 = Label(self.root,text='Enter Password', font=('Helvetica',12))
        label2.pack(pady=(10,10))

        #User Password Input
        self.user_pass= Entry(self.root,width=50,show='*')
        self.user_pass.pack(pady=(5,10),ipady=4)

        #Register Button
        register_button = Button(self.root,text='Register Now',width=20,height=2,command=self.store_database)
        register_button.pack(pady=(10,10))

        #Already a member
        label3 = Label(self.root,text='Already a member?',bg='#808B96', fg='Yellow', font=('Helvetica',10))
        label3.pack(pady=(10,5))

        #Login now
        login_button = Button(self.root,text='Login now',width=12,height=2,command=self.login_gui)
        login_button.pack(pady=(5,10))



    def home_gui(self):

        self.clear()

        # Heading related edit
        heading = Label(self.root, text='NLPApp', bg='#808B96', fg='White')
        heading.pack(pady=(30, 30))  # upore niche margin or space
        heading.configure(font=('verdana', 24, 'bold'))

        #sentiment button
        sentiment_button = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.Sentiment_analysis)
        sentiment_button.pack(pady=(10, 10))

        #NER button
        NER_button = Button(self.root, text='Named Entity Recognition Analysis', width=30, height=4, command=self.NER_analysis)
        NER_button.pack(pady=(10, 10))

        #Emotion button
        emotion_button = Button(self.root, text='Emotion Analysis', width=30, height=4, command=self.Emotion_analysis)
        emotion_button.pack(pady=(10, 10))

        #text_summary button
        text_summary_button = Button(self.root, text='Text summary', width=30, height=4, command=self.text_summary)
        text_summary_button .pack(pady=(10, 10))

        #lang_ditect button
        lang_detect_button = Button(self.root, text='Language detection', width=30, height=4, command=self.language_detection)
        lang_detect_button.pack(pady=(10, 10))

        #logout button
        logout_button = Button(self.root, text='Logout', width=12, height=2, command=self.login_gui)
        logout_button.pack(pady=(10, 10))



    def Sentiment_analysis(self):

        #clearing gui
        self.clear()

        # Heading related edit
        heading1 = Label(self.root, text='NLPApp', bg='#808B96', fg='White')
        heading1.pack(pady=(30, 30))  # upore niche margin or space
        heading1.configure(font=('verdana', 24, 'bold'))

        # Sentiment Analysis text
        heading2 = Label(self.root, text='Sentiment Analysis', bg='#808B96', fg='White')
        heading2.pack(pady=(20, 30))  # upore niche margin or space
        heading2.configure(font=('verdana', 20, 'bold'))

        #Enter text
        label1 = Label(self.root,text='Enter text', font=('Helvetica',12),width=12)
        label1.pack(pady=(10,10))

        #User text Input Box
        self.user_text= Entry(self.root,width=50)
        self.user_text.pack(pady=(10,10),ipady=50)

        # Analysis button
        analysis_button = Button(self.root, text='Analyze Sentiment', font=('Helvetica',12), width=15, command=self.do_sentiment_analysis)
        analysis_button.pack(pady=(10, 10))

        #result text
        self.sentiment_result = Label(self.root,text='', font=('Helvetica',12),bg='#808B96',fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana', 12))

        #goback button
        goback_button = Button(self.root, text='Go back', width=12, font=('Helvetica',12), command=self.home_gui)
        goback_button.pack(pady=(10, 10))


    #sentiment analysis button e click korar por ekhane ashbe
    def do_sentiment_analysis(self):
        text = self.user_text.get()
        #print(text)
        result = analyze_sentiment(text)
        #print(result)
        d = {}
        for i in result:
            d = i
        print(d)
        txt=''
        for i in d:
            txt = txt + i + '->' + str(d[i]) + '\n'

        self.sentiment_result['text']=txt



    def NER_analysis(self):

        #clearing gui
        self.clear()

        # Heading related edit
        heading1 = Label(self.root, text='NLPApp', bg='#808B96', fg='White')
        heading1.pack(pady=(30, 30))  # upore niche margin or space
        heading1.configure(font=('verdana', 24, 'bold'))

        # Heading NER Analysis text
        heading2 = Label(self.root, text='Named Entity Recognition (NER)', bg='#808B96', fg='White')
        heading2.pack(pady=(20, 30))  # upore niche margin or space
        heading2.configure(font=('verdana', 20, 'bold'))

        #Enter text
        label1 = Label(self.root,text='Enter text', font=('Helvetica',12),width=12)
        label1.pack(pady=(10,10))

        #User text Input Box
        self.user_text= Entry(self.root,width=50)
        self.user_text.pack(pady=(10,10),ipady=50)

        # Analysis button
        analysis_button = Button(self.root, text='NER', font=('Helvetica',12), width=15, command=self.do_ner_analysis)
        analysis_button.pack(pady=(10, 10))

        #result text(jekhane result show hobe)
        self.ner_result = Label(self.root,text='', font=('Helvetica',12),bg='#808B96',fg='white')
        self.ner_result.pack(pady=(10,10))
        self.ner_result.configure(font=('verdana', 12))

        #goback button
        goback_button = Button(self.root, text='Go back', width=12, font=('Helvetica',12), command=self.home_gui)
        goback_button.pack(pady=(10, 10))

    def do_ner_analysis(self):
        text = self.user_text.get()
        result = ner_analysis(text)
        print(result)

        txt = ''
        for i in result:
            txt = txt + str(i) + '\n'
        self.ner_result['text']=txt


    def Emotion_analysis(self):

        #clearing gui
        self.clear()

        # Heading related edit
        heading1 = Label(self.root, text='NLPApp', bg='#808B96', fg='White')
        heading1.pack(pady=(30, 30))  # upore niche margin or space
        heading1.configure(font=('verdana', 24, 'bold'))

        # Heading Emotional Analysis text
        heading2 = Label(self.root, text='Emotional Analysis', bg='#808B96', fg='White')
        heading2.pack(pady=(20, 30))  # upore niche margin or space
        heading2.configure(font=('verdana', 20, 'bold'))

        #Enter text
        label1 = Label(self.root,text='Enter text', font=('Helvetica',12),width=12)
        label1.pack(pady=(10,10))

        #User text Input Box
        self.user_text= Entry(self.root,width=50)
        self.user_text.pack(pady=(10,10),ipady=50)

        # Analysis button
        analysis_button = Button(self.root, text='Analyze Emotion', font=('Helvetica',12), width=15, command=self.do_emotional_analysis)
        analysis_button.pack(pady=(10, 10))

        #result text
        self.emotional_result = Label(self.root,text='', font=('Helvetica',12),bg='#808B96',fg='white')
        self.emotional_result.pack(pady=(10,10))
        self.emotional_result.configure(font=('verdana', 12))

        #goback button
        goback_button = Button(self.root, text='Go back', width=12, font=('Helvetica',12), command=self.home_gui)
        goback_button.pack(pady=(10, 10))

    def do_emotional_analysis(self):
        text = self.user_text.get()
        #txt=''
        result = client.sentiment(text)
        print(result)
        list = result['scored_labels']
        print(list)
        txt = ''
        for i in list:
            txt = txt + str(i['label']) + ' ' + '->' + ' ' + str(i['score']) + '\n'
        print(txt)
        self.emotional_result['text']= txt


    def text_summary(self):

        #clearing gui
        self.clear()

        # Heading related edit
        heading1 = Label(self.root, text='NLPApp', bg='#808B96', fg='White')
        heading1.pack(pady=(30, 30))  # upore niche margin or space
        heading1.configure(font=('verdana', 24, 'bold'))

        # heading text summary text
        heading2 = Label(self.root, text='Text Summary', bg='#808B96', fg='White')
        heading2.pack(pady=(20, 30))  # upore niche margin or space
        heading2.configure(font=('verdana', 20, 'bold'))

        #Enter text
        label1 = Label(self.root,text='Enter text', font=('Helvetica',12),width=12)
        label1.pack(pady=(10,10))

        #User text Input Box
        self.user_text= Entry(self.root,width=50)
        self.user_text.pack(pady=(10,10),ipady=50)

        # Analysis button
        analysis_button = Button(self.root, text='Summary', font=('Helvetica',12), width=15, command=self.do_text_summary)
        analysis_button.pack(pady=(10, 10))

        #result text
        self.summary_result = Label(self.root,text='', font=('Helvetica',12),bg='#808B96',fg='white')
        self.summary_result.pack(pady=(10,10))
        self.summary_result.configure(font=('verdana', 12))

        #goback button
        goback_button = Button(self.root, text='Go back', width=12, font=('Helvetica',12), command=self.home_gui)
        goback_button.pack(pady=(10, 10))

    def do_text_summary(self):

        text = self.user_text.get()
        result = text_summarization(text)
        print(result)

        txt=''
        for i in result:
            txt = txt + str(i) + '\n'
        print('txt')
        self.summary_result['text']=txt


    def language_detection(self):

        #clearing gui
        self.clear()

        # Heading related edit
        heading1 = Label(self.root, text='NLPApp', bg='#808B96', fg='White')
        heading1.pack(pady=(30, 30))  # upore niche margin or space
        heading1.configure(font=('verdana', 24, 'bold'))

        # Heading language detection text
        heading2 = Label(self.root, text='Language Detection', bg='#808B96', fg='White')
        heading2.pack(pady=(20, 30))  # upore niche margin or space
        heading2.configure(font=('verdana', 20, 'bold'))

        #Enter text
        label1 = Label(self.root,text='Enter text', font=('Helvetica',12),width=12)
        label1.pack(pady=(10,10))

        #User text Input Box
        self.user_text= Entry(self.root,width=50)
        self.user_text.pack(pady=(10,10),ipady=50)

        # Analysis button
        analysis_button = Button(self.root, text='Detect languages', font=('Helvetica',12), width=15, command=self.do_language_detection)
        analysis_button.pack(pady=(10, 10))

        #result text
        self.lang_detect_result = Label(self.root,text='', font=('Helvetica',12),bg='#808B96',fg='white')
        self.lang_detect_result.pack(pady=(10,10))
        self.lang_detect_result.configure(font=('verdana', 12))

        #goback button
        goback_button = Button(self.root, text='Go back', width=12, font=('Helvetica',12), command=self.home_gui)
        goback_button.pack(pady=(10, 10))

    def do_language_detection(self):

        text = self.user_text.get()
        print(text)
        result = detect_languages_with_scores(text)
        print(len(result))
        print(result)

        for lang, score in result:
            print(f"{lang} -> {score}")

    #any gui clear function
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    #fetch data from register gui
    def store_database(self):
        name = self.user_name.get()
        email = self.user_email.get()
        password = self.user_pass.get()

        #add_data function calling
        response = self.dbo.add_data(name,email,password)

        if response:
            #print('ok')
            messagebox.showinfo('success','Registration Successful.You can login now')
        else:
            #print('not ok')
            messagebox.showinfo('Error','Email already exists')


    #fetch data from login_gui
    def login_check(self):
        email = self.user_email.get()
        password = self.user_pass.get()

        response = self.dbo.check_data(email, password)

        if response:
            messagebox.showinfo('success', 'Login Successful')
            self.home_gui()
        else:
            messagebox.showinfo('Error', 'Incorrect email/password')


nlp = NLPApp()






