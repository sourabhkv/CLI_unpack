import argparse
from translate import Translator

class Parse:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(prog='Translator',description='Translates text',epilog='Developed by sourabhkv')
        self.parser.add_argument('--version',"-v",dest='version',action='version', version='%(prog)s 1.0',help="Current program version")
        self.parser.add_argument('--text','-t','-i',dest='text' ,help='text/file to be translated')
        self.parser.add_argument('--lang-codes','-lc',dest='language',help="display all supported language codes")
        self.parser.add_argument('--to-lang','-tl', dest='to_lang', help='language to be translated in')
        self.parser.add_argument('--output','-o', dest='output', help='output to saved at location')
        self.args = self.parser.parse_args()
        self.checker()
    
    def checker(self):
        if self.args.text==None and self.args.to_lang!=None:
            print("Did not recieve text")
            raise SystemExit
        if self.args.language!=None and self.args.text==None:
            self.lang_info()
        elif self.args.text!=None and self.args.to_lang!=None:
            self.Translate(self.args.to_lang)
    
    def Translate(self,lang="en"):
        if ".txt" in self.args.text:
            with open(self.args.text,"r") as file:
                self.args.text = file.read()
            
        translator= Translator(to_lang=lang)
        translation = translator.translate(self.args.text)
        if self.args.output!=None:
            with open(self.args.output,"w",encoding="utf-8") as file:
                file.write(translation)
        else:
            print(translation)
    
    def lang_info(self):
        lang_dict = {"english":"en",
                     "japanese":"ja",
                     "hindi":"hi",
                     "kannada":"ka",
                     "marathi":"mr",
                     "malayalam":"ml",
                     "bengali":"bn",
                     "italian":"it",
                     "german":"de",
                     "french":"fr",
                     "arabic":"ar",
                     "spanish":"es",
                     "russian":"ru",
                     "portuguese":"pt",
                     "chinese":"zh"}
        print(lang_dict[self.args.language.lower()])
    
if __name__=='__main__':
    Parse()