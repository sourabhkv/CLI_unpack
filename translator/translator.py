import argparse
from translate import Translator

parser = argparse.ArgumentParser(prog='Translator',
                    description='Translates text',
                    epilog='Developed by sourabhkv')

parser.add_argument('--version',"-v",dest='version',action='version', version='%(prog)s 1.0',help="Current program version")

parser.add_argument('text', help='text to translated')

parser.add_argument('--lang-codes',dest='lang_codes',
                    help='''
                    display all supported language codes
                    en - English ,
                    ja - Japanese ,
                    hi - Hindi ,
                    ka - Kannada ,
                    mr - Marathi ,
                    ml - Malayalam ,
                    bn - Bengali ,
                    it - Italian ,
                    de - German ,
                    fr - French ,
                    ar - Arabic ,
                    es - Spanish ,
                    ru - Russian ,
                    pt - Portuguese ,
                    zh - Chinese Mandarin Simplified ,
                    \nFor more https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages''')

parser.add_argument('--to', dest='to_lang', help='language to be translated in')

args = parser.parse_args()

translator= Translator(to_lang=args.to_lang)

translation = translator.translate(args.text)

print(translation)
