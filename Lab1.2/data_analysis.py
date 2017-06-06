from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

def getvalue(x):
    return x.value

a=list(map(getvalue, sheet['A'][1:]))
b=list(map(getvalue, sheet['B'][1:]))
c=list(map(getvalue, sheet['C'][1:]))
print(a)
print(b)
print(c)

pyplot.plot(a, b, label="RU-US Relation", color="blue", )
pyplot.plot(a, c, label="Sun activity", linestyle="dashed")
pyplot.hlines(80,1900,2020, color="red", linestyle="dotted")
#pyplot.xlabel('Годы')
#pyplot.ylabel('Отношения/Активность Солнца')
pyplot.legend()
pyplot.show()