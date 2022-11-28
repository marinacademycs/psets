import check50
import check50.c

filename = "hours.c"
@check50.check()
def hours_exist():
    """%s exists.""" % filename
    check50.exists(filename)

@check50.check(hours_exist)
def compiles():
    """%s compiles.""" % filename
    check50.c.compile(filename, lcs50=True)
