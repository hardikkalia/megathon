from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Sample list of tuples

@app.route('/', methods=['GET', 'POST'])
def job_position_form():
    if request.method == 'POST':
        job_position = request.form['job_position']

        # Place your database connection and query logic here
        # Replace this with your database logic
        conn = sqlite3.connect('userdatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mytable")
        result = cursor.fetchall()
        conn.close()

        list2 = ["Accounting", "Sales", "HR", "Tech", "Design", "Manager", "Design Head", "Tech Head"]
        list3 = [
            ["2", "4", "6", "caution", "safety"],
            ["0", "3", "6", "safety", "initiative"],
            ["0", "2", "4", "6", "safety", "caution"],
            ["2", "4", "6", "safety", "caution"],
            ["3", "5", "7", "calculated risks"],
            ["0", "2", "4", "5", "6", "9", "10", "strong leadership qualities", "initiative"],
            ["0", "3", "5", "6", "7", "9", "10", "strong leadership qualities", "calculated risks"],
            ["0", "2", "4", "6", "9", "10", "strong leadership qualities", "initiative"]
        ]
        list4 = [
            ["11", "8", "5", "calculated risks"],
            ["1", "11", "caution"],
            ["1", "11", "8", "calculated risks"],
            ["3", "5", "8", "11", "calculated risks"],
            ["11", "caution"],
            ["1", "8", "11"],
            ["1", "8", "11"],
            ["1", "3", "8", "11", "calculated risks"]
        ]
        ls = []
        checkjob = job_position
        for i in range(0, len(result)):
            score = result[i][len(result[i]) - 2]
            flag = []
            for j in range(0, 12):
                flag.append(result[i][j + 4])

            list1 = []
            if score >= 5:
                list1.append("strong leadership qualities")
                list1.append("calculated risks")
            elif score >= 3:
                list1.append("safety")
                list1.append("initiative")
            else:
                list1.append("caution")
                list1.append("safety")
            uj = list2.index(checkjob)
            sum = 0
            for j in range(0, len(list3[uj])):
                if len(list3[uj][j]) > 1:
                    for k in list1:
                        if k == list3[uj][j]:
                            sum += 2
                elif flag[int(list3[uj][j])] == '1':
                    sum += 2
            for j in range(0, len(list4[uj])):
                if len(list4[uj][j]) > 1:
                    for k in list1:
                        if k == list4[uj][j]:
                            sum -= 1
                elif flag[int(list4[uj][j])] == '1':
                    sum -= 1
            ls.append((result[i][0], sum))
        sorted_list = sorted(ls, key=lambda x: x[1], reverse=True)
        names = []
        aa = 0
        for i in sorted_list:
            if aa == 5:
                break
            aa += 1
            if i[1] < 0:
                break
            names.append(i[0])
        print(names)
        return redirect(url_for('searchresults', names=','.join(names)))
    return render_template('search-form.html')

@app.route('/searchresults')
def searchresults():
    names = request.args.get('names').split(',')
    return render_template('searchresults.html', names=names)

@app.route('/details/<name>')
def details(name):
    list11=''
    conn = sqlite3.connect('userdatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT summary FROM mytable WHERE name=?", (name,))
    result = cursor.fetchone()
    conn.close()
    return render_template('details.html', data=result[0])

if __name__ == '__main__':
    app.run(debug=True, port=8000)
