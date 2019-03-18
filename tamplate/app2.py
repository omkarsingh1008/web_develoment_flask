from flask import Flask, render_template
app=Flask(__name__,template_folder='tamplate')
@app.route('/')
def home():
    return render_template('base_template.html')
@app.route('/singup/')    
def sing():
    return render_template('singup.html') 
@app.route('/login/')    
def log():
    return render_template('login2.html')     
if __name__ == '__main__':
    app.run('localhost',8000,debug=True)  