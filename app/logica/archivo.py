def arreglarhtml(html):
    var=""
    for linea in html:
        x=str(linea).replace("b'", "")
        x=x.replace("'", "")
        x=x.replace("\\n", "")
        x=x.replace("\\r", "")
        var=var+x
    return var