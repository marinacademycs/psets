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
    """Handles Wikipedia example"""
    input = "Wkh Fdhvdu flskhu lv qdphg diwhu Mxolxv Fdhvdu, zkr, dffruglqj wr Vxhwrqlxv, xvhg lw zlwk d vkliw ri wkuhh (D ehfrplqj G zkhq hqfubswlqj, dqg G ehfrplqj D zkhq ghfubswlqj) wr surwhfw phvvdjhv ri plolwdub vljqlilfdqfh. Zkloh Fdhvdu'v zdv wkh iluvw uhfrughg xvh ri wklv vfkhph, rwkhu vxevwlwxwlrq flskhuv duh nqrzq wr kdyh ehhq xvhg hduolhu. (iurp Zlnlshgld)"
    ex_output = "Decipher with key: 23\nplaintext: The Caesar cipher is named after Julius Caesar, who, according to Suetonius, used it with a shift of three (A becoming D when encrypting, and D becoming A when decrypting) to protect messages of military significance. While Caesar's was the first recorded use of this scheme, other substitution ciphers are known to have been used earlier. (from Wikipedia)\n"

    program_output = check50.run("./caesar_decipher").stdin(input).stdout()

    if ex_output != program_output:
        raise check50.Mismatch(ex_output, program_output)
        

@check50.check(compiles)
def check_2():
    """Handles Stairway to Heaven"""
    input = "Espcp'd l wloj hsz'd dfcp lww esle rwteepcd td rzwo / Lyo dsp'd mfjtyr l deltchlj ez Splgpy / Hspy dsp rped espcp dsp vyzhd, tq esp dezcpd lcp lww nwzdpo / Htes l hzco dsp nly rpe hsle dsp nlxp qzc / Zzs, zzs, lyo dsp'd mfjtyr l deltchlj ez Splgpy / Espcp'd l dtry zy esp hlww, mfe dsp hlyed ez mp dfcp / 'Nlfdp jzf vyzh dzxpetxpd hzcod slgp ehz xplytyrd / Ty l ecpp mj esp mczzv, espcp'd l dzyrmtco hsz dtyrd / Dzxpetxpd lww zq zfc eszfrsed lcp xtdrtgpy"
    ex_output = "Decipher with key: 15\nplaintext: There's a lady who's sure all that glitters is gold / And she's buying a stairway to Heaven / When she gets there she knows, if the stores are all closed / With a word she can get what she came for / Ooh, ooh, and she's buying a stairway to Heaven / There's a sign on the wall, but she wants to be sure / 'Cause you know sometimes words have two meanings / In a tree by the brook, there's a songbird who sings / Sometimes all of our thoughts are misgiven\n"

    program_output = check50.run("./caesar_decipher").stdin(input).stdout()

    if ex_output != program_output:
        raise check50.Mismatch(ex_output, program_output)
        
        
@check50.check(compiles)
def check_3():
    """Handles Random English"""
    input = "Vszzc am boas wg Pcp obr W oa ucwbu hc hvs tcfsgh hc soh twgv. Ozzwuohcf. Xcvbgcb. Pcp. Hvwg wg xigh o fobrca dwsqs ct Sbuzwgv hslh. Rwr mci ybck hvoh gboysg ofs qccz? Kvoh rc mci qozz o gdwrsf kwhv twjs smsg? O gdwwwwwrsf. Gc, hvsfs'g o aob qfokzwbu hvfciuv hvs rsgsfh. Hvoh'g o eichs. Hvoby mci tcf ohhsbrwbu am Hsr Hozy. Obmhvwbu szgs? aVaa."
    ex_output = "Decipher with key: 12\nplaintext: Hello my name is Bob and I am going to the forest to eat fish. Alligator. Johnson. Bob. This is just a random piece of English text. Did you know that snakes are cool? What do you call a spider with five eyes? A spiiiiider. So, there's a man crawling through the desert. That's a quote. Thank you for attending my Ted Talk. Anything else? mHmm.\n"

    program_output = check50.run("./caesar_decipher").stdin(input).stdout()

    if ex_output != program_output:
        raise check50.Mismatch(ex_output, program_output)
        
        
        
@check50.check(compiles)
def check_4():
    """Handles Upper Case Letters"""
    input = "WKH FDHVDU FLSKHU LV QDPHG DIWHU MXOLXV FDHVDU, ZKR, DFFRUGLQJ WR VXHWRQLXV, XVHG LW ZLWK D VKLIW RI WKUHH (D EHFRPLQJ G ZKHQ HQFUBSWLQJ, DQG G EHFRPLQJ D ZKHQ GHFUBSWLQJ) WR SURWHFW PHVVDJHV RI PLOLWDUB VLJQLILFDQFH. ZKLOH FDHVDU'V ZDV WKH ILUVW UHFRUGHG XVH RI WKLV VFKHPH, RWKHU VXEVWLWXWLRQ FLSKHUV DUH NQRZQ WR KDYH EHHQ XVHG HDUOLHU. (IURP ZLNLSHGLD)"
    ex_output = "THE CAESAR CIPHER IS NAMED AFTER JULIUS CAESAR, WHO, ACCORDING TO SUETONIUS, USED IT WITH A SHIFT OF THREE (A BECOMING D WHEN ENCRYPTING, AND D BECOMING A WHEN DECRYPTING) TO PROTECT MESSAGES OF MILITARY SIGNIFICANCE. WHILE CAESAR'S WAS THE FIRST RECORDED USE OF THIS SCHEME, OTHER SUBSTITUTION CIPHERS ARE KNOWN TO HAVE BEEN USED EARLIER. (FROM WIKIPEDIA)\n"
    
    program_output = check50.run("./caesar_decipher").stdin(input).stdout()

    if ex_output != program_output:
        raise check50.Mismatch(ex_output, program_output)
