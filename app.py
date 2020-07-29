from flask import Flask, render_template, url_for
from helper import *

app = Flask(__name__)

@app.route('/')

def home():
	data_hari_ini = ambil_data_hari_ini()
	data_rekap = rekapitulasi()
	list_daerah = ['jkt','banten','jabar','jateng','jatim']
	data_daerah = {}
	for item in list_daerah:
		prov,data = get_daerah(item)
		data_daerah[prov] = [data['positif'],data['sembuh'],data['meninggal']]
	return render_template('index.html',data_hari_ini=data_hari_ini,
										data_rekap=data_rekap,
										data_daerah=data_daerah)

@app.route('/table/')
@app.route('/table/<page>')

def table(page=1):
	page=int(page)
	data_rekap = rekapitulasi_table()
	max_page= (len(data_rekap) // 10) + 1
	if page == 1:
		page_list = [1,2,3]
	elif page == max_page:
		page_list = [page-2,page-1,page]
	else:
		page_list = [page-1,page,page+1]

	min_elemen = (10*(page-1))
	max_elemen = min_elemen  + 10

	return render_template('table.html',data_rekap=data_rekap[min_elemen:max_elemen],
										page=page,
										list_page = page_list,
										max_page=max_page
										)

if __name__ == '__main__':
	app.run(debug=True)