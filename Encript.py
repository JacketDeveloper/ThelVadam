from colorama import Fore
import os, time, base64, sys
#entrada de texto lento(efecto Codding by Jacket)
def printlento(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 10)

banner =  Fore.BLUE + """;ttttttttttttttttttttttttttttttttt%X:888:;;;X8;S8S88@8@88%X S;;:;ttttttt;ttttttttttt8XXXXXXXXS%SSX@X
:StXt%@;%Xt%%%%%Xt@t%XtXtXtXtXt%%%%ttX8XX;;t@X:t;::88;;:...t88:;tS%%%%%%Xt%%Xt@;Xt%S;X@XX@@X@X@@@@X@
:tXX@@XS%SXtXtXt%%%S%StXXX8X%8;tXtXtS:8@X;tS@::t88XXS8XXS.:tXt;t88XXXtXttSXtt%%%S%t%S@t@XS@@X@@X@@@X
:8@SXXXX88@8tt%%SXt%%t@t@SXX8@8;;%%%tS@88;@@8..8888;t8888t:;tttXX@XXX88Xt%X@X@88@@S88X@XXX@SX@XSX@@X
;%t%%X8@;St@@%XtS;X%@tSt%X8@t%Stt@t%X:S@8;;88:..:tX888X;tt::8;8S@S@t@%8@@88@@8@@@@8@X@@@X@XX@@XX;X@X
:X@@%X;Xt%%@Xtt%%%Xt%8;X%%Xt@%X@%%Stt%%@88:88@..S@X8888XS::X8@;%88@@S8@SXX@@@S;X@@@X@X@XX@@X@XS@XS@@
XXSSXtX;8X@@XtS@tStXt8X@8%@8%8@@@ttXtXt88@:88t:. 8@8%@8X:.tX8XS;X@@;%%8X;t@SXXt8XXSX@XXX8@X@@@SXXX@S
:St888X8;X;tXtSt%%%%ttt;XXt8@tt%%Xtt%%%XXXtXtS;...::;:;;.S8t88:;%@SSXXt%8@tXtSStt@XSXS@Xt@t8X@S%@@@@
:t%tt;;tttSt%St@t@%%S;tt;tt%t%XXtt%X;t%:8X8;8@X:.......:t8t%@@tttt;;SXt@XX@X8XS8X%8tXSX:@@%XXXSX@@@X
:XXSStt%%%88t%%t%ttttS8St;%t%%%%;;t;t88:8XXX88@8..   ..;8@@@88X8St8::;;;X@ttXX@@88XXt8t8X@X@XXt8X@@X
.;8@tX%8%8XtStXtS:;t%S;@XSSSt8%X:;ttX@8t%@@Xt8@88t:.. .XS88@8888:%88;XS;tt@XXSSt8SX@8tX%@SX@X@@X@X@@
:t;S@X%S@SSt%ttS;:;tS;tt8X;Xtt%ttttt@8t;;%88tXS@8%;:::St%@@8888:8X@8:8@@88tt8@@8XSX@tXX@XX@X@XtXS@@X
:ttt%%%;tttt%Xt%t::;;;;%%t;;%%t%%%X@88%;;X8@t:S8t@88::;;8@%8@8tXX88@8888@;;;@SX@@S;::t8;%8XXX@XtXXX:
:St%%%%%tSt%S;SXt%S%tt%@tSt%Xt%%%X88X8@:::8@8.;@8XXtt%X88@88X888@888888@X8StXtX;tttSStXX@XXXXXX%XSt%
StSS%S%%%St%Xt@X8%%8XXtt;;;;;tt888S;;;  ;SS88;t8@88@8ttt@;8X:  .:%X8888888X8@XXtX%tX;XtXtt@X@X:t%Xtt
88@tXtt%SSStXtSS8X;;X8X::;XS%t@ ;SS%8;     88@8tX88SX8@;t@;  S t8tXS  8.X8X8;tXt@X%XtXSt8Xt8S:ttt%SS
.;Xtt;t%%t%X;%t@@t@@888;..:%t::  .t@8%X%  @ @888888ttttXS   t8SX%@      .t%;.%888@X;ttX@tSXtt@t%tX;t
;;;t%%t%%t%XSSSt%  :t8.X ... t8@   X;X8X@@X:  88@@@X%%XX .SX@@8%SX:  @X:  .t X:S;t: :%8tXt8%Xt%tt;%;
;XXtX;tX;%SX@t:8%8   SX88%S:88   @t;;%@@88;.@Xt8X88@X8::8SS88X8tt;%8.. S8 tt@8 :  .SS8 S%%X;:%8;t;%;
..:ttS;;tt@SXX8@;. S  t..   8t8S  :8;tSXt88SXS8tX888X@Xt%@8@8;X:S8:..@StS.    .      XS%tS8;t%;;;;%;
.;ttt;;t8%%%X%.;;  ;@8S.. @  .S8@X8:XS X8t8XS;%%888;t;;88X88;8 %S%S@S8@.: X   %88.   : %%;:S@::;:;;;
@St;;;t%SXSXS@X8@  : :@ %8 S  @::;.:t:S 8t:.:;8%%;::::t%8888@ S%8:.:;:8..  8:.@     8@S@:tX@X:.;t;;S
:;;;:;;.;.%@%XXSt.@@SS8XX:8  :.8:::: ;%%88:.:;88::..;XXXX888X;8::;tt%S.;  @;%8@888X ;SX:;SXtS.::::tt
.;tt;;:.;8%@% .SSS;t;%:X ;:X.   8.tt;t:t888...tSt8888tt8XSS;:;;t;tS;S   ;:@: 8S:.:.XSX SS%S@::::::;;
.;t;;;:;t.:;;%t;;tt%%%;8. .@:8  .%;tt%@;;;:...:@%X;t;%%ttt;%%:;;tt@%; :;%S; .X.;tt;;;t%tt::::.:::;::"""
print(banner)
print("___________________________________________________________________________________byDefalt")
print("___________________________________________________________________________________V1")
time.sleep(3)
os.system('clear')


print("_____________________")
print("[1] Encode base64    |")
print("[2] Descode base64   |")
print("_____________________|")
sukablyat = input("Elije pibe >> ")

if sukablyat == "1":
    encript = input(b'Escribe lo que vas a encriptar >> ')
    pito = base64.b64encode(bytes(encript, 'utf-8'))
    print(pito)
