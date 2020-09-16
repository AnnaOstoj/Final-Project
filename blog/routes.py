from flask import render_template, request, redirect, url_for, flash
from blog import app, models, services, db
from blog.forms import EntryForm
from blog.models import Entry


@app.route("/blog", methods=["GET", "POST"])
def index():
   posts_list = services.load()
   if request.method == "POST":
      return redirect(url_for("create_entry"))

   return render_template("homepage.html", all_posts=posts_list)

@app.route("/blog/add", methods=["GET", "POST"])
def create_entry():
   errors = None
   entry_form = EntryForm()
   if request.method == "POST":
      if entry_form.validate_on_submit():
         new_entry = Entry(
                           title = entry_form.title.data,
                           body = entry_form.body.data,
                           is_published = entry_form.is_published.data
                           )
         db.session.add(new_entry)
         db.session.commit()
         flash('Post added successfully!', 'success')
         return redirect(url_for("index"))
      else:
         errors = entry_form.errors
         flash('Post not added successfully!', 'danger')
   return render_template("entry_form.html", entry_form=entry_form, errors=errors)