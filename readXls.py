import xlrd
def main():
	fname = "DB.xls"
	bk = xlrd.open_workbook(fname)
	try:
		sh = bk.sheet_by_name("Sheet1")
	except:
		print "no sheet in %s named Sheet1"%fname
		return None
	nrows = sh.nrows
	ncols = sh.ncols
	print "nrows is %d, ncols is %d"%(nrows, ncols)

	cell_value = sh.cell_value(1, 1)
	# print cell_value

	
	for x in xrange(1,nrows):
		# row_data = sh.row_values(x)
		for i in xrange(1,ncols):
                        
			cell_data = sh.cell_value(x, i)
			print cell_data
		print "---------------"
if __name__ == '__main__':
	main()
