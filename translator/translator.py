import argparse
from translate import Translator

class Parse:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(prog='Translator',description='Translates text',epilog='Developed by sourabhkv')
        self.parser.add_argument('--version',"-v",dest='version',action='version', version='%(prog)s 1.0',help="Current program version")
        self.parser.add_argument('text', help='text to translated')
        self.parser.add_argument('--lang-codes',dest='lang_codes',help="display all supported language codes")
        self.parser.add_argument('--to', dest='to_lang', help='language to be translated in')
        self.args = self.parser.parse_args()
        self.Translate()
    
    def Translate(self):
        __translator= Translator(to_lang=self.args.to_lang)
        __translation = __translator.translate(self.args.text)
        print(__translation)
    
if __name__=='__main__':
    Parse()
