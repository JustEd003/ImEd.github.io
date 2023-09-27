from flask import Flask, render_template, request
import smtplib

app = Flask(__name__, static_folder='style')
app.template_folder = 'template'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        address = request.form.get('address')
        email = request.form.get('email')
        phone = request.form.get('phone')
        jobtitle = request.form.get('jobtitle')
        message = request.form.get('message')

        sender_email = 'itsed87000@gmail.com'
        receiver_email = 'hied87000@gmail.com'  
        subject = 'New Form Submission'
        email_body = f"Firstname: {firstname}\nLastname: {lastname}\nAddress:{address}\nEmail: {email}\nPhone: {phone}\nJob Title: {jobtitle}\nMessage: {message}"

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, 'yobvrhceepjdnpva')  
            smtp.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{email_body}")

        return 'Form submitted successfully'
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
