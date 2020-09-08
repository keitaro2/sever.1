from flask import Flask, request, render_template
app = Flask(__name__)
file_path = "./sensor_data.csv"
port_num = 16074

@app.route('/', methods=['GET'])
def get_html():
    return render_template('./index.html')

@app.route('/beat', methods=['POST'])
def update_beat():
    time = request.form["time"]
    beat = request.form["beat"]
    try:
        f = open(file_path, 'w')
        f.write(time + "," + beat)
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()

@app.route('/beat', methods=['GET'])
def get_beat():
    try:
        f = open(file_path, 'r')
        for row in f:
        beat = row
        return beat
    except Exception as e:
        print(e)
        return e
    finally:
        f.close()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_num)
