from flask import Flask, render_template, request, redirect, Response
import csv

app = Flask(__name__)

class WorkerManager:
    def __init__(self):
        self.workers = []
    
    def add_worker(self, name, pay, hours):
        total = float(pay) * float(hours)
        worker = {'name': name, 'pay': pay, 'hours': hours, 'total': total}
        self.workers.append(worker)
    
    def remove_worker(self, index):
        if index < len(self.workers):
            self.workers.pop(index)

worker_manager = WorkerManager()

@app.route('/')
def home():
    return render_template('table.html', workers=worker_manager.workers)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    pay = request.form['pay']
    hours = request.form['hours']
    worker_manager.add_worker(name, pay, hours)
    return redirect('/')

@app.route('/remove/<int:index>')
def remove(index):
    worker_manager.remove_worker(index)
    return redirect('/')

@app.route('/export')
def export_csv():
    def generate():
        data = [['Name', 'Pay', 'Hours', 'Total']]
        total_sum = 0
        for worker in worker_manager.workers:
            data.append([worker['name'], worker['pay'], worker['hours'], worker['total']])
            total_sum += worker['total']
        
        data.append(['', '', 'Total', total_sum])
        for row in data:
            yield ','.join([str(x) for x in row]) + '\n'

    headers = {
        'Content-Disposition': 'attachment; filename=workers.csv',
        'Content-Type': 'text/csv'
    }

    return Response(generate(), headers=headers)

if __name__ == '__main__':
    app.run(debug=True)
