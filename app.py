from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    page="""
    <body style="backgroud-color:red;">
    <h1 style='color:red'>
    welcome to first flask powerd by page
    </h1>
    <a href='/data/'>click me</a>
    </body>
    
    """
    return page
@app.route('/data/')
def data():
    page="""
    <h1> ohh you are in data page</h1>
    <a href='/'>click me</a>
    <h1> hii user</h1>
    <a href ='/hi/'>back to home page</a>
    
    """
    return page
@app.route('/hi/')    
def hi():
    page="""
    <h1> hii user</h1>
    <a href ='/data/'>back to home page</a>
    """

        
    return page  
if __name__=="__main__":
    app.run()


