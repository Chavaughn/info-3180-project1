"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from app import app, db
from flask import abort, flash, render_template, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash

from app.forms import AddPropertyForm
from .models import Property, PropertyType, PhotoAlbum, Photo

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Chavaughn Wilkins")


@app.route('/new-property', methods=['GET', 'POST'])
def new_property():
    """Render the new property page."""
    form = AddPropertyForm()
    try:
        if request.method == 'POST':
            file = form.main_photo.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['PROPERTIES_FOLDER'], filename))
            # Create a new Property object
            title = request.form['title']
            description = request.form['description']
            rooms = request.form['rooms']
            bathrooms = request.form['bathrooms']
            price = request.form['price']
            location = request.form['location']
            property_type_id = request.form['property_type']
            photo_album = PhotoAlbum(name=title)
            db.session.add(photo_album)
            db.session.commit()
            main_photo = Photo(name=filename, photo_album_id=photo_album.id)
            db.session.add(main_photo)
            db.session.commit()
            property = Property(
                title=title,
                description=description,
                rooms=rooms,
                bathrooms=bathrooms,
                price=price,
                location=location,
                property_type_id=property_type_id,
                photo_album_id=photo_album.id,
                main_photo_id=main_photo.id
            )
            db.session.add(property)
            db.session.commit()
            flash('New property added successfully!', 'success')
            return redirect(url_for('properties'))
    except:
        flash('Error adding new property', 'danger')
        db.session.rollback()
    property_types = PropertyType.query.all()
    form.property_type.choices = [(pt.id, pt.name) for pt in property_types]
    return render_template('new_property.html', form = form)


@app.route('/properties')
def properties():
    """Render the properties page."""
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/property/<int:property_id>')
def property_detail(property_id):
    """Render the property detail page."""
    property = Property.query.get(property_id)
    property_type = PropertyType.query.get(property.property_type_id)
    if property is None:
        abort(404)
    return render_template('property_detail.html', property=property, type = property_type.name)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/properties/<filename>')
def get_image(filename):
    return send_from_directory(app.config['PROPERTIES_FOLDER'], filename)

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

