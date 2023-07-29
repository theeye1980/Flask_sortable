from flask import Flask, render_template, request
# from jinja2 import Environment

app = Flask(__name__)
app.jinja_env.globals['enumerate'] = enumerate

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_order = request.form.getlist('new_order[]')
        # Save the new sorted array here
        return 'Array saved successfully'
    else:
        article_image = [
              "3526_nowodvorski",
              "2997_nowodvorski",
              "TL1179H-04BK_toplight",
              "TL1136-3H_toplight",
              "E4-07-G-LMP-O-23-CRL-E4-07-CH-DN_maytoni",
              "3641_nowodvorski",
              "450018103_de_city",
              "69014-5H_globo_new",
              "68410-5_globo_new",
              "2996_nowodvorski",
              "3528_nowodvorski",
              "450019805_de_city",
              "E4-07-G-LMP-O-32_maytoni",
              "A4900PL-3SS",
              "3642_nowodvorski",
              "275-107-03_velante",
              "3513/3_lumion",
              "E4-07-G-LMP-O-18-CRL-E4-07-GB-DN_maytoni",
              "Carina E 1.1.5 GB_arti_lampadari",
              "V4255-1/3_vitaluce",
              "318014705_de_city",
              "2998_nowodvorski",
              "TL5670D-03WG_toplight",
              "E3-07-H-LMP-O-33_maytoni",
              "450019703_de_city",
              "TL2670X-03WC_toplight",
              "287/3pf-blackchrome_idlamp",
              "GRLSP-8063_lussole",
              "V3252/3PL_vitaluce",
              "V3946-0/3PL_vitaluce",
              "5620311_britop",
              "CL113135_citilux",
              "69017-3H_globo_new",
              "A4530LM-5AB",
              "CL434131_citilux"
        ]  # Your original array
        return render_template('index.html', article_image=article_image)


if __name__ == '__main__':
    app.run()
