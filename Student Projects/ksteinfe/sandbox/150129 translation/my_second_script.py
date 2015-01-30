import translate

langs = ["de"]

fname = "play.txt"
with open(fname) as f: content = str(f.readlines())

for lang in langs:
    trans = translate.Translator(to_lang=lang)
    print trans.translate("child")

    transcontent = trans.translate(content).encode("utf8","ignore")
    with open("out_"+lang+".txt", "w") as text_file:
        text_file.write(transcontent)   
