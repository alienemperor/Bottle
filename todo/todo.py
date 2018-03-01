import sqlite3
from bottle import route, run, template, request, error

@route('/')
@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    output = template('make_table', rows=result)
    return output

@route('/new', method='GET')
def new_item():

    if request.GET.save:

        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        alert = '<div class="alert alert-success" role="alert">New item %s was created successfully' \
                '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' \
                '<span aria-hidden="true">&times;</span>' \
                '</button></div>' % new_id

        return template('new_task.tpl'), alert
    else:
        return template('new_task.tpl')

@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        alert = '<div class="container" style="margin:auto;width:80%;padding-top:20px;">' \
                '<div class="alert alert-primary  alert-dismissible fade show" role="alert">' \
                'The item number %s was successfully updated' \
                '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' \
                '<span aria-hidden="true">&times</span></button>' \
                '</div></div>' % no

        return todo_list(), alert
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no)

@error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

run(host='192.168.100.222', port=8000, debug=True, reloader=True)
