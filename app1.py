from flask import Flask, render_template
app=Flask(__name__,template_folder='tamplate')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/singup.html')    
def sing():
    return render_template('singup.html') 
@app.route('/login.html')    
def log():
    return render_template('login.html')     
if __name__ == '__main__':
    app.run(debug=True)    