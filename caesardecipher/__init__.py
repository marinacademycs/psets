import check50
import check50.c


@check50.check()
def exists():
    """caesar_decipher.c exists"""
    check50.exists("caesar_decipher.c")


@check50.check(exists)
def compiles():
    """caesar_decipher.c compiles"""
    check50.c.compile("caesar_decipher.c", lcs50=True)
