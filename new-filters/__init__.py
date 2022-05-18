import check50
import check50.c

filename = "helpers.c"
@check50.check()
def helpers_exist():
    """%s exists.""" % filename
    check50.exists(filename)

@check50.check(helpers_exist)
def compiles():
    """%s compiles.""" % filename
    check50.c.compile(filename, lcs50=True)

filename2 = "helpers.h"
@check50.check()
def helpersh_exist():
    """%s exists.""" % filename2
    check50.exists(filename2)

makefile = "Makefile"
@check50.check()
def makefile_exists():
    """%s exists.""" % makefile
    check50.exists(makefile)    

@check50.check(filterc_exists)
def compiles():
    """%s compiles.""" % filename3
    check50.c.compile(filename3, lcs50=True)
    
filename4 = "bmp.h"
@check50.check()
def bmph_exist():
    """%s exists.""" % filename2
    check50.exists(filename2)
