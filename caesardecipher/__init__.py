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


@check50.check(compiles)
def check_1():
    """Handles From Wikipedia example"""
    input = "Wkh Fdhvdu flskhu lv qdphg diwhu Mxolxv Fdhvdu, zkr, dffruglqj wr Vxhwrqlxv, xvhg lw zlwk d vkliw ri wkuhh (D ehfrplqj G zkhq hqfubswlqj, dqg G ehfrplqj D zkhq ghfubswlqj) wr surwhfw phvvdjhv ri plolwdub vljqlilfdqfh. Zkloh Fdhvdu'v zdv wkh iluvw uhfrughg xvh ri wklv vfkhph, rwkhu vxevwlwxwlrq flskhuv duh nqrzq wr kdyh ehhq xvhg hduolhu. (iurp Zlnlshgld)"
    ex_output = "Decipher with key: 23\nplaintext: The Caesar cipher is named after Julius Caesar, who, according to Suetonius, used it with a shift of three (A becoming D when encrypting, and D becoming A when decrypting) to protect messages of military significance. While Caesar's was the first recorded use of this scheme, other substitution ciphers are known to have been used earlier. (from Wikipedia)\n"

    program_output = check50.run("./caesar_decipher").stdin(input).stdout()

    if ex_output != program_output:
        raise check50.Mismatch(ex_output, program_output)
