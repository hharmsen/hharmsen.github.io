import cgi
import csv
import StringIO
import sys

class Page:
    def __init__(self, rfilename, wfilename, title):
        self.rfilename = rfilename
        self.wfilename = wfilename
        self.title = title
    def _makelist(self):
        rfile = file(self.rfilename, "rb")
        csvreader = csv.reader(rfile)
        listbuffer = StringIO.StringIO()
        for row in csvreader:
            listbuffer.write('      <li><a href="%s" rel="nofollow">%s</a>\n' %
                             (cgi.escape(row[0]),
                              cgi.escape(row[1])))
        rfile.close()
        return listbuffer.getvalue()
    def render(self):
        wfile = file(self.wfilename, "wt")
        wfile.write("""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>%s</title>
  <style type="text/css">
    body {
      background-color: Peru;
    }
    li {
      list-style: none;
    }
    li a {
      display: block;
      margin: 5px 5px 5px 5px;
      padding: 5px 5px;
      width: 300px;
      background-color: BurlyWood;
      color: Black;
      border-color: Black;
      text-align: center;
      text-decoration: none;
    }
    li a:hover {
      background: Wheat;
    }
  </style>
</head>
<body>
  <nav>
    <ul>
%s    </ul>
  </nav>
</body>
</html>""" % (cgi.escape(self.title), self._makelist()))
        wfile.close()
 
page = Page(sys.argv[1], sys.argv[2], sys.argv[3])
page.render()
