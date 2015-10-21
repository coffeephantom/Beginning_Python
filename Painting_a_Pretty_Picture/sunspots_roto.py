from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
    (2015, 4, 127.6, 128.6, 126.6),
    (2015, 5, 123.9, 124.9, 122.9),
    (2015, 6, 119.8, 121.8, 117.8),
    (2015, 7, 116.3, 119.3, 113.3),
    (2015, 8, 113.8, 117.8, 109.8),
    (2015, 9, 111.8, 115.8, 107.8)
]

drawing = Drawing(200, 150)

pred = [row[2] - 40 for row in data]
high = [row[3] - 40 for row in data]
low = [row[4] - 40 for row in data]
times = [200 * ((row[0] + row[1] / 12.0) - 2015)  for row in data]

drawing.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
drawing.add(PolyLine(zip(times, high), strokeColor=colors.red))
drawing.add(PolyLine(zip(times, low), strokeColor=colors.green))
drawing.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')
