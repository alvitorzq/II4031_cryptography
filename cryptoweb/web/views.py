from django.shortcuts import render

# Create your views here.
def Vigenere(string, key):
    def vigenereKey(string, key):
        key = list(key)
        if len(string) < len(key):
            key = key[:len(string)]
        else: 
            if len(string) == len(key):
                return key
            else:
                for i in range(len(string) - len(key)):
                    key.append(key[i % len(key)])
        return (''.join(key))
    
    def encryption(string, key):
        encrypttext = []
        for i in range(len(string)):
            num = (ord(string[i]) + ord(key[i])) % 26
            num = num + 65
            encrypttext.append(chr(num))
        return (''.join(encrypttext))

    def decryption(encrypttext, key):
        decrypttext = []
        for i in range(len(encrypttext)):
            num = (ord(encrypttext[i]) - ord(key[i])) % 26
            num = num + 65
            decrypttext.append(chr(num))
        return (''.join(decrypttext))

    string = string.upper()
    key = key.upper()
    # Replacing character other than alphaber in the string and key
    string = string.replace(" ","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("0","").replace("!","").replace("@","").replace("#","").replace("$","").replace("%","").replace("^","").replace("&","").replace("*","").replace("(","").replace(")","").replace("-","").replace("_","").replace("+","").replace("+","").replace("{","").replace("[","").replace("}","").replace("]","").replace("|","").replace(":","").replace(";","").replace("<","").replace(",","").replace(">","").replace(".","").replace("?","")
    key = key.replace(" ","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("0","").replace("!","").replace("@","").replace("#","").replace("$","").replace("%","").replace("^","").replace("&","").replace("*","").replace("(","").replace(")","").replace("-","").replace("_","").replace("+","").replace("+","").replace("{","").replace("[","").replace("}","").replace("]","").replace("|","").replace(":","").replace(";","").replace("<","").replace(",","").replace(">","").replace(".","").replace("?","")
    
    keyword = vigenereKey(string, key)
    result = encryption(string, keyword)

    return result

def ExtendedVigenere(string, key):
    pass

def index(request):
    if request.method == 'POST':
        string = request.POST['string']
        key = request.POST['key']
        if 'vigenere' in request.POST:
            result = Vigenere(string, key)
            return render(request, 'index.html', {'result' : result})
    return render(request, 'index.html')