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
   return edit_add_entry()

@app.route("/blog/edit/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
   return edit_add_entry(entry_id)


def edit_add_entry(entry_id = 0):
   errors = None
   if entry_id == 0:
      entry_form = EntryForm()
   else:
      entry = Entry.query.filter_by(id=entry_id).first_or_404()
      entry_form = EntryForm(obj=entry)

   if request.method == "POST":
      if entry_form.validate_on_submit():
         if entry_id == 0:
            entry = Entry(
                           title = entry_form.title.data,
                           body = entry_form.body.data,
                           is_published = entry_form.is_published.data
                           )
            db.session.add(entry)
         else:
            entry_form.populate_obj(entry)
      else:
         errors = entry_form.errors
         flash('Change done unsuccessfully', 'danger')

      db.session.commit()
      flash('Change done successfully', 'success')
      return redirect(url_for("index"))

   return render_template("entry_form.html", entry_form=entry_form, errors=errors)