alfabetoPrevio=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',' ' ,',','.']
alfabeto={}

for i in range(len(alfabetoPrevio)):
    alfabeto[alfabetoPrevio[i]]=i


cifrada="l.ziu,mf .fzmk,wzilwgfqw mfai kwukmsw flw,wfifsif.upamz plilflmf .fik,.isfm k.lwfmufmsfk.isfmsfiñ.psiftmcpkiuifdfmsfkwulwzfiulpuwgfk.isfiamfjpkmnisigfxzw,mñmufmsflm xspmñ.mflmsftixiflmfitmzpkifsi,puigflm lmfsifnzwu,mzifuwz,mflmftmcpkwfoi ,ifmsfkijwflmfowzuw gfxsi tiulwfsif.upnpkikpwuflmfsw fpjmzwitmzpkiuw gfu.m ,zwfkwu,pumu,mfu.mawfdfiu,pñ.wgfxzmlm ,puilwfifkwu,mumzf.uifzieify.pu,igfsifzieifkw tpkigfmufsifk.isf mfn.ulpziufsi flp xmz i fdf mfkwu .tizifsif.uplilh"

decifradaReal=""

for i in range(1,29):
    decifrada=""
    for caracter in cifrada:
        index=alfabeto[caracter]
        index+=i
        if index>30:
            index=index%30

        decifrada+=alfabetoPrevio[index-1]
    
    if i==23: decifradaReal=decifrada

    print("\n!!//////////////////!! clave numero: " + str(i-1))
    print(decifrada)

print("\nla clave para decifrar el mensaje es la numero 22 y el texto decifrado es:" )
print(decifradaReal)


        