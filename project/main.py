from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from .models import Todo
from .forms import TaskForm
from . import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def root():
    return redirect(url_for('main.welcome'))

@main.route('/welcome')
def welcome():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return render_template('welcome.html')

@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = TaskForm()
    if form.validate_on_submit():
        task = Todo(content=form.content.data, user_id=current_user.id)
        try:
            db.session.add(task)
            db.session.commit()
            flash('Task added successfully!', 'success')
            return redirect(url_for('main.home'))
        except Exception as e:
            db.session.rollback()
            flash('Error adding task. Please try again.', 'danger')
            # Consider logging the error e
    
    # Get filter parameters from URL
    status_filter = request.args.get('status', 'all')
    priority_filter = request.args.get('priority', 'all')
    
    # Base query for user's tasks
    query = Todo.query.filter_by(user_id=current_user.id)
    
    # Apply status filter
    if status_filter == 'todo':
        query = query.filter_by(completed=False)
    elif status_filter == 'done':
        query = query.filter_by(completed=True)
    # 'all' and 'in_progress' don't filter (since we don't have in_progress status in the model)
    
    tasks = query.order_by(Todo.date_created).all()
    
    # Calculate stats for all user tasks (not filtered)
    all_tasks = Todo.query.filter_by(user_id=current_user.id).all()
    total_tasks = len(all_tasks)
    completed_count = len([task for task in all_tasks if task.completed])
    to_do_count = total_tasks - completed_count
    in_progress_count = 0  # Not applicable with current model
    
    return render_template('index.html', 
                         tasks=tasks, 
                         form=form,
                         selected_status=status_filter,
                         selected_priority=priority_filter,
                         total_tasks=total_tasks,
                         to_do_count=to_do_count,
                         in_progress_count=in_progress_count,
                         completed_count=completed_count)
    

@main.route('/delete/<int:id>')
@login_required
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    if task_to_delete.author != current_user:
        abort(403)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('main.home'))
    except:
        return 'There was a problem deleting that task'

@main.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    task = Todo.query.get_or_404(id)
    if task.author != current_user:
        abort(403)
        
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect(url_for('main.home'))
        except:
            return 'There was an issue updating this task'
    else:
        return render_template('update.html', task=task)

@main.route('/toggle/<int:id>')
@login_required
def toggle_complete(id):
    task = Todo.query.get_or_404(id)
    if task.user_id != current_user.id:
        abort(403)
    task.completed = not task.completed
    task.date_completed = datetime.utcnow() if task.completed else None
    db.session.commit()
    return redirect(url_for('main.home'))