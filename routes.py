from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_email_password'    # Replace with your email password

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    photos = [
        {'title': 'Old House', 'url': 'photos/old_house.jpg'},
        {'title': 'College', 'url': 'photos/college.jpg'},
        {'title': 'Flats', 'url': 'photos/flat.jpg'},
        {'title': 'station', 'url': 'photos/station.jpg'},
        {'title': 'sunset', 'url': 'photos/sunset.jpg'},
        {'title': 'Symmetrical house', 'url': 'photos/symmetrical_house.jpg'},
        # Add more photos as needed
    ]
    return render_template('gallery.html', photos=photos)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject='New Contact Inquiry',
                      sender=email,
                      recipients=['your_email@example.com'])  # Replace with your email address
        msg.body = f'You have received a new message from {name} ({email}):\n\n{message}'
        mail.send(msg)

        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
