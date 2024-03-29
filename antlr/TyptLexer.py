# Generated from antlr/Typt.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr4.Token import CommonToken
import re
import importlib

# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2b")
        buf.write("\u032a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3")
        buf.write(">\3>\3>\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3")
        buf.write("A\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3")
        buf.write("C\3C\3C\3C\3D\3D\3D\3D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3I\3I\3I\3J\3J\3")
        buf.write("J\3J\3K\3K\3K\3K\3K\3K\3L\3L\3L\3L\3L\3L\3L\3M\3M\3M\3")
        buf.write("M\3M\3M\3M\3N\3N\3O\3O\3P\3P\3P\3P\3P\3P\3P\3P\3P\3Q\3")
        buf.write("Q\3Q\3Q\3Q\3R\3R\3R\3R\3R\3R\3S\3S\3S\3S\3T\3T\3T\3T\3")
        buf.write("T\3U\3U\5U\u024b\nU\3V\3V\5V\u024f\nV\3W\3W\3W\3W\3W\3")
        buf.write("W\3W\3W\3W\5W\u025a\nW\3X\3X\3X\3X\5X\u0260\nX\3Y\3Y\3")
        buf.write("Y\5Y\u0265\nY\3Y\3Y\5Y\u0269\nY\3Y\5Y\u026c\nY\5Y\u026e")
        buf.write("\nY\3Y\3Y\3Z\3Z\7Z\u0274\nZ\fZ\16Z\u0277\13Z\3[\3[\7[")
        buf.write("\u027b\n[\f[\16[\u027e\13[\3[\6[\u0281\n[\r[\16[\u0282")
        buf.write("\5[\u0285\n[\3\\\3\\\3\\\6\\\u028a\n\\\r\\\16\\\u028b")
        buf.write("\3]\3]\3]\6]\u0291\n]\r]\16]\u0292\3^\3^\3^\6^\u0298\n")
        buf.write("^\r^\16^\u0299\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_")
        buf.write("\5_\u02a9\n_\3`\3`\3`\5`\u02ae\n`\3`\3`\3a\3a\3b\5b\u02b5")
        buf.write("\nb\3c\3c\5c\u02b9\nc\3d\3d\3e\3e\3f\3f\3g\3g\3h\3h\3")
        buf.write("i\6i\u02c6\ni\ri\16i\u02c7\3j\6j\u02cb\nj\rj\16j\u02cc")
        buf.write("\3k\3k\5k\u02d1\nk\3k\6k\u02d4\nk\rk\16k\u02d5\3l\3l\3")
        buf.write("l\7l\u02db\nl\fl\16l\u02de\13l\3l\3l\3l\3l\7l\u02e4\n")
        buf.write("l\fl\16l\u02e7\13l\3l\5l\u02ea\nl\3m\3m\3m\3m\3m\7m\u02f1")
        buf.write("\nm\fm\16m\u02f4\13m\3m\3m\3m\3m\3m\3m\3m\3m\7m\u02fe")
        buf.write("\nm\fm\16m\u0301\13m\3m\3m\3m\5m\u0306\nm\3n\3n\5n\u030a")
        buf.write("\nn\3o\3o\3p\3p\3p\3p\5p\u0312\np\3q\6q\u0315\nq\rq\16")
        buf.write("q\u0316\3r\3r\7r\u031b\nr\fr\16r\u031e\13r\3s\3s\5s\u0322")
        buf.write("\ns\3s\5s\u0325\ns\3s\3s\5s\u0329\ns\2\2t\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177")
        buf.write("A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008f")
        buf.write("I\u0091J\u0093K\u0095L\u0097M\u0099N\u009bO\u009dP\u009f")
        buf.write("Q\u00a1R\u00a3S\u00a5T\u00a7U\u00a9V\u00abW\u00adX\u00af")
        buf.write("Y\u00b1Z\u00b3[\u00b5\\\u00b7]\u00b9^\u00bb_\u00bd`\u00bf")
        buf.write("a\u00c1b\u00c3\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\u00cd")
        buf.write("\2\u00cf\2\u00d1\2\u00d3\2\u00d5\2\u00d7\2\u00d9\2\u00db")
        buf.write("\2\u00dd\2\u00df\2\u00e1\2\u00e3\2\u00e5\2\3\2\22\4\2")
        buf.write("QQqq\4\2ZZzz\4\2DDdd\5\2C\\aac|\3\2\63;\3\2\62;\3\2\62")
        buf.write("9\5\2\62;CHch\3\2\62\63\4\2GGgg\4\2--//\6\2\f\f\16\17")
        buf.write("))^^\6\2\f\f\16\17$$^^\3\2^^\4\2\13\13\"\"\4\2\f\f\16")
        buf.write("\17\2\u0340\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9")
        buf.write("\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2")
        buf.write("\2\2\u00c1\3\2\2\2\3\u00e7\3\2\2\2\5\u00ed\3\2\2\2\7\u00ef")
        buf.write("\3\2\2\2\t\u00f4\3\2\2\2\13\u00f6\3\2\2\2\r\u00f8\3\2")
        buf.write("\2\2\17\u00fb\3\2\2\2\21\u00fe\3\2\2\2\23\u0101\3\2\2")
        buf.write("\2\25\u0104\3\2\2\2\27\u0107\3\2\2\2\31\u010a\3\2\2\2")
        buf.write("\33\u010d\3\2\2\2\35\u0110\3\2\2\2\37\u0114\3\2\2\2!\u0118")
        buf.write("\3\2\2\2#\u011c\3\2\2\2%\u0120\3\2\2\2\'\u0124\3\2\2\2")
        buf.write(")\u0129\3\2\2\2+\u012f\3\2\2\2-\u0138\3\2\2\2/\u013f\3")
        buf.write("\2\2\2\61\u0142\3\2\2\2\63\u0147\3\2\2\2\65\u014c\3\2")
        buf.write("\2\2\67\u0152\3\2\2\29\u0156\3\2\2\2;\u0159\3\2\2\2=\u015d")
        buf.write("\3\2\2\2?\u015f\3\2\2\2A\u0161\3\2\2\2C\u0164\3\2\2\2")
        buf.write("E\u016d\3\2\2\2G\u0172\3\2\2\2I\u0178\3\2\2\2K\u017a\3")
        buf.write("\2\2\2M\u0187\3\2\2\2O\u0190\3\2\2\2Q\u0193\3\2\2\2S\u0196")
        buf.write("\3\2\2\2U\u0198\3\2\2\2W\u019a\3\2\2\2Y\u019d\3\2\2\2")
        buf.write("[\u01a0\3\2\2\2]\u01a2\3\2\2\2_\u01a4\3\2\2\2a\u01a6\3")
        buf.write("\2\2\2c\u01a8\3\2\2\2e\u01aa\3\2\2\2g\u01ad\3\2\2\2i\u01b0")
        buf.write("\3\2\2\2k\u01b4\3\2\2\2m\u01b8\3\2\2\2o\u01bb\3\2\2\2")
        buf.write("q\u01bd\3\2\2\2s\u01bf\3\2\2\2u\u01c1\3\2\2\2w\u01c4\3")
        buf.write("\2\2\2y\u01c7\3\2\2\2{\u01c9\3\2\2\2}\u01cc\3\2\2\2\177")
        buf.write("\u01d1\3\2\2\2\u0081\u01d6\3\2\2\2\u0083\u01dc\3\2\2\2")
        buf.write("\u0085\u01e6\3\2\2\2\u0087\u01f1\3\2\2\2\u0089\u01fa\3")
        buf.write("\2\2\2\u008b\u0204\3\2\2\2\u008d\u0206\3\2\2\2\u008f\u0208")
        buf.write("\3\2\2\2\u0091\u020a\3\2\2\2\u0093\u020f\3\2\2\2\u0095")
        buf.write("\u0213\3\2\2\2\u0097\u0219\3\2\2\2\u0099\u0220\3\2\2\2")
        buf.write("\u009b\u0227\3\2\2\2\u009d\u0229\3\2\2\2\u009f\u022b\3")
        buf.write("\2\2\2\u00a1\u0234\3\2\2\2\u00a3\u0239\3\2\2\2\u00a5\u023f")
        buf.write("\3\2\2\2\u00a7\u0243\3\2\2\2\u00a9\u024a\3\2\2\2\u00ab")
        buf.write("\u024e\3\2\2\2\u00ad\u0259\3\2\2\2\u00af\u025f\3\2\2\2")
        buf.write("\u00b1\u026d\3\2\2\2\u00b3\u0271\3\2\2\2\u00b5\u0284\3")
        buf.write("\2\2\2\u00b7\u0286\3\2\2\2\u00b9\u028d\3\2\2\2\u00bb\u0294")
        buf.write("\3\2\2\2\u00bd\u02a8\3\2\2\2\u00bf\u02ad\3\2\2\2\u00c1")
        buf.write("\u02b1\3\2\2\2\u00c3\u02b4\3\2\2\2\u00c5\u02b8\3\2\2\2")
        buf.write("\u00c7\u02ba\3\2\2\2\u00c9\u02bc\3\2\2\2\u00cb\u02be\3")
        buf.write("\2\2\2\u00cd\u02c0\3\2\2\2\u00cf\u02c2\3\2\2\2\u00d1\u02c5")
        buf.write("\3\2\2\2\u00d3\u02ca\3\2\2\2\u00d5\u02ce\3\2\2\2\u00d7")
        buf.write("\u02e9\3\2\2\2\u00d9\u0305\3\2\2\2\u00db\u0309\3\2\2\2")
        buf.write("\u00dd\u030b\3\2\2\2\u00df\u0311\3\2\2\2\u00e1\u0314\3")
        buf.write("\2\2\2\u00e3\u0318\3\2\2\2\u00e5\u031f\3\2\2\2\u00e7\u00e8")
        buf.write("\7w\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7p\2\2\u00eb\u00ec\7i\2\2\u00ec\4\3\2\2\2\u00ed\u00ee")
        buf.write("\7<\2\2\u00ee\6\3\2\2\2\u00ef\u00f0\7h\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7o\2\2\u00f3\b")
        buf.write("\3\2\2\2\u00f4\u00f5\7.\2\2\u00f5\n\3\2\2\2\u00f6\u00f7")
        buf.write("\7?\2\2\u00f7\f\3\2\2\2\u00f8\u00f9\7-\2\2\u00f9\u00fa")
        buf.write("\7?\2\2\u00fa\16\3\2\2\2\u00fb\u00fc\7/\2\2\u00fc\u00fd")
        buf.write("\7?\2\2\u00fd\20\3\2\2\2\u00fe\u00ff\7,\2\2\u00ff\u0100")
        buf.write("\7?\2\2\u0100\22\3\2\2\2\u0101\u0102\7\61\2\2\u0102\u0103")
        buf.write("\7?\2\2\u0103\24\3\2\2\2\u0104\u0105\7\'\2\2\u0105\u0106")
        buf.write("\7?\2\2\u0106\26\3\2\2\2\u0107\u0108\7(\2\2\u0108\u0109")
        buf.write("\7?\2\2\u0109\30\3\2\2\2\u010a\u010b\7~\2\2\u010b\u010c")
        buf.write("\7?\2\2\u010c\32\3\2\2\2\u010d\u010e\7`\2\2\u010e\u010f")
        buf.write("\7?\2\2\u010f\34\3\2\2\2\u0110\u0111\7>\2\2\u0111\u0112")
        buf.write("\7>\2\2\u0112\u0113\7?\2\2\u0113\36\3\2\2\2\u0114\u0115")
        buf.write("\7@\2\2\u0115\u0116\7@\2\2\u0116\u0117\7?\2\2\u0117 \3")
        buf.write("\2\2\2\u0118\u0119\7,\2\2\u0119\u011a\7,\2\2\u011a\u011b")
        buf.write("\7?\2\2\u011b\"\3\2\2\2\u011c\u011d\7\61\2\2\u011d\u011e")
        buf.write("\7\61\2\2\u011e\u011f\7?\2\2\u011f$\3\2\2\2\u0120\u0121")
        buf.write("\7f\2\2\u0121\u0122\7g\2\2\u0122\u0123\7n\2\2\u0123&\3")
        buf.write("\2\2\2\u0124\u0125\7r\2\2\u0125\u0126\7c\2\2\u0126\u0127")
        buf.write("\7u\2\2\u0127\u0128\7u\2\2\u0128(\3\2\2\2\u0129\u012a")
        buf.write("\7d\2\2\u012a\u012b\7t\2\2\u012b\u012c\7g\2\2\u012c\u012d")
        buf.write("\7c\2\2\u012d\u012e\7m\2\2\u012e*\3\2\2\2\u012f\u0130")
        buf.write("\7e\2\2\u0130\u0131\7q\2\2\u0131\u0132\7p\2\2\u0132\u0133")
        buf.write("\7v\2\2\u0133\u0134\7k\2\2\u0134\u0135\7p\2\2\u0135\u0136")
        buf.write("\7w\2\2\u0136\u0137\7g\2\2\u0137,\3\2\2\2\u0138\u0139")
        buf.write("\7t\2\2\u0139\u013a\7g\2\2\u013a\u013b\7v\2\2\u013b\u013c")
        buf.write("\7w\2\2\u013c\u013d\7t\2\2\u013d\u013e\7p\2\2\u013e.\3")
        buf.write("\2\2\2\u013f\u0140\7k\2\2\u0140\u0141\7h\2\2\u0141\60")
        buf.write("\3\2\2\2\u0142\u0143\7g\2\2\u0143\u0144\7n\2\2\u0144\u0145")
        buf.write("\7k\2\2\u0145\u0146\7h\2\2\u0146\62\3\2\2\2\u0147\u0148")
        buf.write("\7g\2\2\u0148\u0149\7n\2\2\u0149\u014a\7u\2\2\u014a\u014b")
        buf.write("\7g\2\2\u014b\64\3\2\2\2\u014c\u014d\7y\2\2\u014d\u014e")
        buf.write("\7j\2\2\u014e\u014f\7k\2\2\u014f\u0150\7n\2\2\u0150\u0151")
        buf.write("\7g\2\2\u0151\66\3\2\2\2\u0152\u0153\7h\2\2\u0153\u0154")
        buf.write("\7q\2\2\u0154\u0155\7t\2\2\u01558\3\2\2\2\u0156\u0157")
        buf.write("\7k\2\2\u0157\u0158\7p\2\2\u0158:\3\2\2\2\u0159\u015a")
        buf.write("\7f\2\2\u015a\u015b\7g\2\2\u015b\u015c\7h\2\2\u015c<\3")
        buf.write("\2\2\2\u015d\u015e\7*\2\2\u015e>\3\2\2\2\u015f\u0160\7")
        buf.write("+\2\2\u0160@\3\2\2\2\u0161\u0162\7/\2\2\u0162\u0163\7")
        buf.write("@\2\2\u0163B\3\2\2\2\u0164\u0165\7a\2\2\u0165\u0166\7")
        buf.write("a\2\2\u0166\u0167\7k\2\2\u0167\u0168\7p\2\2\u0168\u0169")
        buf.write("\7k\2\2\u0169\u016a\7v\2\2\u016a\u016b\7a\2\2\u016b\u016c")
        buf.write("\7a\2\2\u016cD\3\2\2\2\u016d\u016e\7u\2\2\u016e\u016f")
        buf.write("\7g\2\2\u016f\u0170\7n\2\2\u0170\u0171\7h\2\2\u0171F\3")
        buf.write("\2\2\2\u0172\u0173\7e\2\2\u0173\u0174\7n\2\2\u0174\u0175")
        buf.write("\7c\2\2\u0175\u0176\7u\2\2\u0176\u0177\7u\2\2\u0177H\3")
        buf.write("\2\2\2\u0178\u0179\7B\2\2\u0179J\3\2\2\2\u017a\u017b\7")
        buf.write("u\2\2\u017b\u017c\7v\2\2\u017c\u017d\7c\2\2\u017d\u017e")
        buf.write("\7v\2\2\u017e\u017f\7k\2\2\u017f\u0180\7e\2\2\u0180\u0181")
        buf.write("\7o\2\2\u0181\u0182\7g\2\2\u0182\u0183\7v\2\2\u0183\u0184")
        buf.write("\7j\2\2\u0184\u0185\7q\2\2\u0185\u0186\7f\2\2\u0186L\3")
        buf.write("\2\2\2\u0187\u0188\7q\2\2\u0188\u0189\7r\2\2\u0189\u018a")
        buf.write("\7g\2\2\u018a\u018b\7t\2\2\u018b\u018c\7c\2\2\u018c\u018d")
        buf.write("\7v\2\2\u018d\u018e\7q\2\2\u018e\u018f\7t\2\2\u018fN\3")
        buf.write("\2\2\2\u0190\u0191\7?\2\2\u0191\u0192\7?\2\2\u0192P\3")
        buf.write("\2\2\2\u0193\u0194\7#\2\2\u0194\u0195\7?\2\2\u0195R\3")
        buf.write("\2\2\2\u0196\u0197\7>\2\2\u0197T\3\2\2\2\u0198\u0199\7")
        buf.write("@\2\2\u0199V\3\2\2\2\u019a\u019b\7>\2\2\u019b\u019c\7")
        buf.write("?\2\2\u019cX\3\2\2\2\u019d\u019e\7@\2\2\u019e\u019f\7")
        buf.write("?\2\2\u019fZ\3\2\2\2\u01a0\u01a1\7-\2\2\u01a1\\\3\2\2")
        buf.write("\2\u01a2\u01a3\7/\2\2\u01a3^\3\2\2\2\u01a4\u01a5\7,\2")
        buf.write("\2\u01a5`\3\2\2\2\u01a6\u01a7\7\61\2\2\u01a7b\3\2\2\2")
        buf.write("\u01a8\u01a9\7\'\2\2\u01a9d\3\2\2\2\u01aa\u01ab\7\61\2")
        buf.write("\2\u01ab\u01ac\7\61\2\2\u01acf\3\2\2\2\u01ad\u01ae\7q")
        buf.write("\2\2\u01ae\u01af\7t\2\2\u01afh\3\2\2\2\u01b0\u01b1\7c")
        buf.write("\2\2\u01b1\u01b2\7p\2\2\u01b2\u01b3\7f\2\2\u01b3j\3\2")
        buf.write("\2\2\u01b4\u01b5\7p\2\2\u01b5\u01b6\7q\2\2\u01b6\u01b7")
        buf.write("\7v\2\2\u01b7l\3\2\2\2\u01b8\u01b9\7k\2\2\u01b9\u01ba")
        buf.write("\7u\2\2\u01ban\3\2\2\2\u01bb\u01bc\7~\2\2\u01bcp\3\2\2")
        buf.write("\2\u01bd\u01be\7`\2\2\u01ber\3\2\2\2\u01bf\u01c0\7(\2")
        buf.write("\2\u01c0t\3\2\2\2\u01c1\u01c2\7>\2\2\u01c2\u01c3\7>\2")
        buf.write("\2\u01c3v\3\2\2\2\u01c4\u01c5\7@\2\2\u01c5\u01c6\7@\2")
        buf.write("\2\u01c6x\3\2\2\2\u01c7\u01c8\7\u0080\2\2\u01c8z\3\2\2")
        buf.write("\2\u01c9\u01ca\7,\2\2\u01ca\u01cb\7,\2\2\u01cb|\3\2\2")
        buf.write("\2\u01cc\u01cd\7P\2\2\u01cd\u01ce\7q\2\2\u01ce\u01cf\7")
        buf.write("p\2\2\u01cf\u01d0\7g\2\2\u01d0~\3\2\2\2\u01d1\u01d2\7")
        buf.write("V\2\2\u01d2\u01d3\7t\2\2\u01d3\u01d4\7w\2\2\u01d4\u01d5")
        buf.write("\7g\2\2\u01d5\u0080\3\2\2\2\u01d6\u01d7\7H\2\2\u01d7\u01d8")
        buf.write("\7c\2\2\u01d8\u01d9\7n\2\2\u01d9\u01da\7u\2\2\u01da\u01db")
        buf.write("\7g\2\2\u01db\u0082\3\2\2\2\u01dc\u01dd\7p\2\2\u01dd\u01de")
        buf.write("\7g\2\2\u01de\u01df\7y\2\2\u01df\u01e0\7\"\2\2\u01e0\u01e1")
        buf.write("\7n\2\2\u01e1\u01e2\7k\2\2\u01e2\u01e3\7u\2\2\u01e3\u01e4")
        buf.write("\7v\2\2\u01e4\u01e5\7*\2\2\u01e5\u0084\3\2\2\2\u01e6\u01e7")
        buf.write("\7p\2\2\u01e7\u01e8\7g\2\2\u01e8\u01e9\7y\2\2\u01e9\u01ea")
        buf.write("\7\"\2\2\u01ea\u01eb\7v\2\2\u01eb\u01ec\7w\2\2\u01ec\u01ed")
        buf.write("\7r\2\2\u01ed\u01ee\7n\2\2\u01ee\u01ef\7g\2\2\u01ef\u01f0")
        buf.write("\7*\2\2\u01f0\u0086\3\2\2\2\u01f1\u01f2\7p\2\2\u01f2\u01f3")
        buf.write("\7g\2\2\u01f3\u01f4\7y\2\2\u01f4\u01f5\7\"\2\2\u01f5\u01f6")
        buf.write("\7u\2\2\u01f6\u01f7\7g\2\2\u01f7\u01f8\7v\2\2\u01f8\u01f9")
        buf.write("\7*\2\2\u01f9\u0088\3\2\2\2\u01fa\u01fb\7p\2\2\u01fb\u01fc")
        buf.write("\7g\2\2\u01fc\u01fd\7y\2\2\u01fd\u01fe\7\"\2\2\u01fe\u01ff")
        buf.write("\7f\2\2\u01ff\u0200\7k\2\2\u0200\u0201\7e\2\2\u0201\u0202")
        buf.write("\7v\2\2\u0202\u0203\7*\2\2\u0203\u008a\3\2\2\2\u0204\u0205")
        buf.write("\7]\2\2\u0205\u008c\3\2\2\2\u0206\u0207\7_\2\2\u0207\u008e")
        buf.write("\3\2\2\2\u0208\u0209\7\60\2\2\u0209\u0090\3\2\2\2\u020a")
        buf.write("\u020b\7D\2\2\u020b\u020c\7q\2\2\u020c\u020d\7q\2\2\u020d")
        buf.write("\u020e\7n\2\2\u020e\u0092\3\2\2\2\u020f\u0210\7K\2\2\u0210")
        buf.write("\u0211\7p\2\2\u0211\u0212\7v\2\2\u0212\u0094\3\2\2\2\u0213")
        buf.write("\u0214\7H\2\2\u0214\u0215\7n\2\2\u0215\u0216\7q\2\2\u0216")
        buf.write("\u0217\7c\2\2\u0217\u0218\7v\2\2\u0218\u0096\3\2\2\2\u0219")
        buf.write("\u021a\7U\2\2\u021a\u021b\7v\2\2\u021b\u021c\7t\2\2\u021c")
        buf.write("\u021d\7k\2\2\u021d\u021e\7p\2\2\u021e\u021f\7i\2\2\u021f")
        buf.write("\u0098\3\2\2\2\u0220\u0221\7Q\2\2\u0221\u0222\7d\2\2\u0222")
        buf.write("\u0223\7l\2\2\u0223\u0224\7g\2\2\u0224\u0225\7e\2\2\u0225")
        buf.write("\u0226\7v\2\2\u0226\u009a\3\2\2\2\u0227\u0228\7}\2\2\u0228")
        buf.write("\u009c\3\2\2\2\u0229\u022a\7\177\2\2\u022a\u009e\3\2\2")
        buf.write("\2\u022b\u022c\7H\2\2\u022c\u022d\7w\2\2\u022d\u022e\7")
        buf.write("p\2\2\u022e\u022f\7e\2\2\u022f\u0230\7v\2\2\u0230\u0231")
        buf.write("\7k\2\2\u0231\u0232\7q\2\2\u0232\u0233\7p\2\2\u0233\u00a0")
        buf.write("\3\2\2\2\u0234\u0235\7N\2\2\u0235\u0236\7k\2\2\u0236\u0237")
        buf.write("\7u\2\2\u0237\u0238\7v\2\2\u0238\u00a2\3\2\2\2\u0239\u023a")
        buf.write("\7V\2\2\u023a\u023b\7w\2\2\u023b\u023c\7r\2\2\u023c\u023d")
        buf.write("\7n\2\2\u023d\u023e\7g\2\2\u023e\u00a4\3\2\2\2\u023f\u0240")
        buf.write("\7U\2\2\u0240\u0241\7g\2\2\u0241\u0242\7v\2\2\u0242\u00a6")
        buf.write("\3\2\2\2\u0243\u0244\7F\2\2\u0244\u0245\7k\2\2\u0245\u0246")
        buf.write("\7e\2\2\u0246\u0247\7v\2\2\u0247\u00a8\3\2\2\2\u0248\u024b")
        buf.write("\5\u00afX\2\u0249\u024b\5\u00bd_\2\u024a\u0248\3\2\2\2")
        buf.write("\u024a\u0249\3\2\2\2\u024b\u00aa\3\2\2\2\u024c\u024f\5")
        buf.write("\u00d7l\2\u024d\u024f\5\u00d9m\2\u024e\u024c\3\2\2\2\u024e")
        buf.write("\u024d\3\2\2\2\u024f\u00ac\3\2\2\2\u0250\u0251\7V\2\2")
        buf.write("\u0251\u0252\7t\2\2\u0252\u0253\7w\2\2\u0253\u025a\7g")
        buf.write("\2\2\u0254\u0255\7H\2\2\u0255\u0256\7c\2\2\u0256\u0257")
        buf.write("\7n\2\2\u0257\u0258\7u\2\2\u0258\u025a\7g\2\2\u0259\u0250")
        buf.write("\3\2\2\2\u0259\u0254\3\2\2\2\u025a\u00ae\3\2\2\2\u025b")
        buf.write("\u0260\5\u00b5[\2\u025c\u0260\5\u00b7\\\2\u025d\u0260")
        buf.write("\5\u00b9]\2\u025e\u0260\5\u00bb^\2\u025f\u025b\3\2\2\2")
        buf.write("\u025f\u025c\3\2\2\2\u025f\u025d\3\2\2\2\u025f\u025e\3")
        buf.write("\2\2\2\u0260\u00b0\3\2\2\2\u0261\u0262\6Y\2\2\u0262\u026e")
        buf.write("\5\u00e1q\2\u0263\u0265\7\17\2\2\u0264\u0263\3\2\2\2\u0264")
        buf.write("\u0265\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0269\7\f\2\2")
        buf.write("\u0267\u0269\4\16\17\2\u0268\u0264\3\2\2\2\u0268\u0267")
        buf.write("\3\2\2\2\u0269\u026b\3\2\2\2\u026a\u026c\5\u00e1q\2\u026b")
        buf.write("\u026a\3\2\2\2\u026b\u026c\3\2\2\2\u026c\u026e\3\2\2\2")
        buf.write("\u026d\u0261\3\2\2\2\u026d\u0268\3\2\2\2\u026e\u026f\3")
        buf.write("\2\2\2\u026f\u0270\bY\2\2\u0270\u00b2\3\2\2\2\u0271\u0275")
        buf.write("\5\u00c3b\2\u0272\u0274\5\u00c5c\2\u0273\u0272\3\2\2\2")
        buf.write("\u0274\u0277\3\2\2\2\u0275\u0273\3\2\2\2\u0275\u0276\3")
        buf.write("\2\2\2\u0276\u00b4\3\2\2\2\u0277\u0275\3\2\2\2\u0278\u027c")
        buf.write("\5\u00c7d\2\u0279\u027b\5\u00c9e\2\u027a\u0279\3\2\2\2")
        buf.write("\u027b\u027e\3\2\2\2\u027c\u027a\3\2\2\2\u027c\u027d\3")
        buf.write("\2\2\2\u027d\u0285\3\2\2\2\u027e\u027c\3\2\2\2\u027f\u0281")
        buf.write("\7\62\2\2\u0280\u027f\3\2\2\2\u0281\u0282\3\2\2\2\u0282")
        buf.write("\u0280\3\2\2\2\u0282\u0283\3\2\2\2\u0283\u0285\3\2\2\2")
        buf.write("\u0284\u0278\3\2\2\2\u0284\u0280\3\2\2\2\u0285\u00b6\3")
        buf.write("\2\2\2\u0286\u0287\7\62\2\2\u0287\u0289\t\2\2\2\u0288")
        buf.write("\u028a\5\u00cbf\2\u0289\u0288\3\2\2\2\u028a\u028b\3\2")
        buf.write("\2\2\u028b\u0289\3\2\2\2\u028b\u028c\3\2\2\2\u028c\u00b8")
        buf.write("\3\2\2\2\u028d\u028e\7\62\2\2\u028e\u0290\t\3\2\2\u028f")
        buf.write("\u0291\5\u00cdg\2\u0290\u028f\3\2\2\2\u0291\u0292\3\2")
        buf.write("\2\2\u0292\u0290\3\2\2\2\u0292\u0293\3\2\2\2\u0293\u00ba")
        buf.write("\3\2\2\2\u0294\u0295\7\62\2\2\u0295\u0297\t\4\2\2\u0296")
        buf.write("\u0298\5\u00cfh\2\u0297\u0296\3\2\2\2\u0298\u0299\3\2")
        buf.write("\2\2\u0299\u0297\3\2\2\2\u0299\u029a\3\2\2\2\u029a\u00bc")
        buf.write("\3\2\2\2\u029b\u029c\5\u00d1i\2\u029c\u029d\7\60\2\2\u029d")
        buf.write("\u029e\5\u00d3j\2\u029e\u02a9\3\2\2\2\u029f\u02a0\5\u00d1")
        buf.write("i\2\u02a0\u02a1\5\u00d5k\2\u02a1\u02a9\3\2\2\2\u02a2\u02a3")
        buf.write("\5\u00d1i\2\u02a3\u02a4\7\60\2\2\u02a4\u02a5\5\u00d3j")
        buf.write("\2\u02a5\u02a6\3\2\2\2\u02a6\u02a7\5\u00d5k\2\u02a7\u02a9")
        buf.write("\3\2\2\2\u02a8\u029b\3\2\2\2\u02a8\u029f\3\2\2\2\u02a8")
        buf.write("\u02a2\3\2\2\2\u02a9\u00be\3\2\2\2\u02aa\u02ae\5\u00e1")
        buf.write("q\2\u02ab\u02ae\5\u00e3r\2\u02ac\u02ae\5\u00e5s\2\u02ad")
        buf.write("\u02aa\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ad\u02ac\3\2\2\2")
        buf.write("\u02ae\u02af\3\2\2\2\u02af\u02b0\b`\3\2\u02b0\u00c0\3")
        buf.write("\2\2\2\u02b1\u02b2\13\2\2\2\u02b2\u00c2\3\2\2\2\u02b3")
        buf.write("\u02b5\t\5\2\2\u02b4\u02b3\3\2\2\2\u02b5\u00c4\3\2\2\2")
        buf.write("\u02b6\u02b9\5\u00c3b\2\u02b7\u02b9\5\u00c9e\2\u02b8\u02b6")
        buf.write("\3\2\2\2\u02b8\u02b7\3\2\2\2\u02b9\u00c6\3\2\2\2\u02ba")
        buf.write("\u02bb\t\6\2\2\u02bb\u00c8\3\2\2\2\u02bc\u02bd\t\7\2\2")
        buf.write("\u02bd\u00ca\3\2\2\2\u02be\u02bf\t\b\2\2\u02bf\u00cc\3")
        buf.write("\2\2\2\u02c0\u02c1\t\t\2\2\u02c1\u00ce\3\2\2\2\u02c2\u02c3")
        buf.write("\t\n\2\2\u02c3\u00d0\3\2\2\2\u02c4\u02c6\5\u00c9e\2\u02c5")
        buf.write("\u02c4\3\2\2\2\u02c6\u02c7\3\2\2\2\u02c7\u02c5\3\2\2\2")
        buf.write("\u02c7\u02c8\3\2\2\2\u02c8\u00d2\3\2\2\2\u02c9\u02cb\5")
        buf.write("\u00c9e\2\u02ca\u02c9\3\2\2\2\u02cb\u02cc\3\2\2\2\u02cc")
        buf.write("\u02ca\3\2\2\2\u02cc\u02cd\3\2\2\2\u02cd\u00d4\3\2\2\2")
        buf.write("\u02ce\u02d0\t\13\2\2\u02cf\u02d1\t\f\2\2\u02d0\u02cf")
        buf.write("\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1\u02d3\3\2\2\2\u02d2")
        buf.write("\u02d4\5\u00c9e\2\u02d3\u02d2\3\2\2\2\u02d4\u02d5\3\2")
        buf.write("\2\2\u02d5\u02d3\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6\u00d6")
        buf.write("\3\2\2\2\u02d7\u02dc\7)\2\2\u02d8\u02db\5\u00dfp\2\u02d9")
        buf.write("\u02db\n\r\2\2\u02da\u02d8\3\2\2\2\u02da\u02d9\3\2\2\2")
        buf.write("\u02db\u02de\3\2\2\2\u02dc\u02da\3\2\2\2\u02dc\u02dd\3")
        buf.write("\2\2\2\u02dd\u02df\3\2\2\2\u02de\u02dc\3\2\2\2\u02df\u02ea")
        buf.write("\7)\2\2\u02e0\u02e5\7$\2\2\u02e1\u02e4\5\u00dfp\2\u02e2")
        buf.write("\u02e4\n\16\2\2\u02e3\u02e1\3\2\2\2\u02e3\u02e2\3\2\2")
        buf.write("\2\u02e4\u02e7\3\2\2\2\u02e5\u02e3\3\2\2\2\u02e5\u02e6")
        buf.write("\3\2\2\2\u02e6\u02e8\3\2\2\2\u02e7\u02e5\3\2\2\2\u02e8")
        buf.write("\u02ea\7$\2\2\u02e9\u02d7\3\2\2\2\u02e9\u02e0\3\2\2\2")
        buf.write("\u02ea\u00d8\3\2\2\2\u02eb\u02ec\7)\2\2\u02ec\u02ed\7")
        buf.write(")\2\2\u02ed\u02ee\7)\2\2\u02ee\u02f2\3\2\2\2\u02ef\u02f1")
        buf.write("\5\u00dbn\2\u02f0\u02ef\3\2\2\2\u02f1\u02f4\3\2\2\2\u02f2")
        buf.write("\u02f0\3\2\2\2\u02f2\u02f3\3\2\2\2\u02f3\u02f5\3\2\2\2")
        buf.write("\u02f4\u02f2\3\2\2\2\u02f5\u02f6\7)\2\2\u02f6\u02f7\7")
        buf.write(")\2\2\u02f7\u0306\7)\2\2\u02f8\u02f9\7$\2\2\u02f9\u02fa")
        buf.write("\7$\2\2\u02fa\u02fb\7$\2\2\u02fb\u02ff\3\2\2\2\u02fc\u02fe")
        buf.write("\5\u00dbn\2\u02fd\u02fc\3\2\2\2\u02fe\u0301\3\2\2\2\u02ff")
        buf.write("\u02fd\3\2\2\2\u02ff\u0300\3\2\2\2\u0300\u0302\3\2\2\2")
        buf.write("\u0301\u02ff\3\2\2\2\u0302\u0303\7$\2\2\u0303\u0304\7")
        buf.write("$\2\2\u0304\u0306\7$\2\2\u0305\u02eb\3\2\2\2\u0305\u02f8")
        buf.write("\3\2\2\2\u0306\u00da\3\2\2\2\u0307\u030a\5\u00ddo\2\u0308")
        buf.write("\u030a\5\u00dfp\2\u0309\u0307\3\2\2\2\u0309\u0308\3\2")
        buf.write("\2\2\u030a\u00dc\3\2\2\2\u030b\u030c\n\17\2\2\u030c\u00de")
        buf.write("\3\2\2\2\u030d\u030e\7^\2\2\u030e\u0312\13\2\2\2\u030f")
        buf.write("\u0310\7^\2\2\u0310\u0312\5\u00b1Y\2\u0311\u030d\3\2\2")
        buf.write("\2\u0311\u030f\3\2\2\2\u0312\u00e0\3\2\2\2\u0313\u0315")
        buf.write("\t\20\2\2\u0314\u0313\3\2\2\2\u0315\u0316\3\2\2\2\u0316")
        buf.write("\u0314\3\2\2\2\u0316\u0317\3\2\2\2\u0317\u00e2\3\2\2\2")
        buf.write("\u0318\u031c\7%\2\2\u0319\u031b\n\21\2\2\u031a\u0319\3")
        buf.write("\2\2\2\u031b\u031e\3\2\2\2\u031c\u031a\3\2\2\2\u031c\u031d")
        buf.write("\3\2\2\2\u031d\u00e4\3\2\2\2\u031e\u031c\3\2\2\2\u031f")
        buf.write("\u0321\7^\2\2\u0320\u0322\5\u00e1q\2\u0321\u0320\3\2\2")
        buf.write("\2\u0321\u0322\3\2\2\2\u0322\u0328\3\2\2\2\u0323\u0325")
        buf.write("\7\17\2\2\u0324\u0323\3\2\2\2\u0324\u0325\3\2\2\2\u0325")
        buf.write("\u0326\3\2\2\2\u0326\u0329\7\f\2\2\u0327\u0329\4\16\17")
        buf.write("\2\u0328\u0324\3\2\2\2\u0328\u0327\3\2\2\2\u0329\u00e6")
        buf.write("\3\2\2\2)\2\u024a\u024e\u0259\u025f\u0264\u0268\u026b")
        buf.write("\u026d\u0275\u027c\u0282\u0284\u028b\u0292\u0299\u02a8")
        buf.write("\u02ad\u02b4\u02b8\u02c7\u02cc\u02d0\u02d5\u02da\u02dc")
        buf.write("\u02e3\u02e5\u02e9\u02f2\u02ff\u0305\u0309\u0311\u0316")
        buf.write("\u031c\u0321\u0324\u0328\4\3Y\2\b\2\2")
        return buf.getvalue()


class TyptLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    T__59 = 60
    T__60 = 61
    T__61 = 62
    T__62 = 63
    T__63 = 64
    T__64 = 65
    T__65 = 66
    T__66 = 67
    T__67 = 68
    T__68 = 69
    T__69 = 70
    T__70 = 71
    T__71 = 72
    T__72 = 73
    T__73 = 74
    T__74 = 75
    T__75 = 76
    T__76 = 77
    T__77 = 78
    T__78 = 79
    T__79 = 80
    T__80 = 81
    T__81 = 82
    T__82 = 83
    NUMBER = 84
    STRING = 85
    BOOLEAN = 86
    INTEGER = 87
    NEWLINE = 88
    NAME = 89
    DECIMAL_INTEGER = 90
    OCT_INTEGER = 91
    HEX_INTEGER = 92
    BIN_INTEGER = 93
    FLOAT_NUMBER = 94
    SKIP_ = 95
    UNKNOWN_CHAR = 96

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'using'", "':'", "'from'", "','", "'='", "'+='", "'-='", "'*='", 
            "'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", "'**='", 
            "'//='", "'del'", "'pass'", "'break'", "'continue'", "'return'", 
            "'if'", "'elif'", "'else'", "'while'", "'for'", "'in'", "'def'", 
            "'('", "')'", "'->'", "'__init__'", "'self'", "'class'", "'@'", 
            "'staticmethod'", "'operator'", "'=='", "'!='", "'<'", "'>'", 
            "'<='", "'>='", "'+'", "'-'", "'*'", "'/'", "'%'", "'//'", "'or'", 
            "'and'", "'not'", "'is'", "'|'", "'^'", "'&'", "'<<'", "'>>'", 
            "'~'", "'**'", "'None'", "'True'", "'False'", "'new list('", 
            "'new tuple('", "'new set('", "'new dict('", "'['", "']'", "'.'", 
            "'Bool'", "'Int'", "'Float'", "'String'", "'Object'", "'{'", 
            "'}'", "'Function'", "'List'", "'Tuple'", "'Set'", "'Dict'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "STRING", "BOOLEAN", "INTEGER", "NEWLINE", "NAME", 
            "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
            "FLOAT_NUMBER", "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "T__50", "T__51", "T__52", "T__53", "T__54", "T__55", 
                  "T__56", "T__57", "T__58", "T__59", "T__60", "T__61", 
                  "T__62", "T__63", "T__64", "T__65", "T__66", "T__67", 
                  "T__68", "T__69", "T__70", "T__71", "T__72", "T__73", 
                  "T__74", "T__75", "T__76", "T__77", "T__78", "T__79", 
                  "T__80", "T__81", "T__82", "NUMBER", "STRING", "BOOLEAN", 
                  "INTEGER", "NEWLINE", "NAME", "DECIMAL_INTEGER", "OCT_INTEGER", 
                  "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", "SKIP_", 
                  "UNKNOWN_CHAR", "NAME_START", "NAME_CONTINUE", "NON_ZERO_DIGIT", 
                  "DIGIT", "OCT_DIGIT", "HEX_DIGIT", "BIN_DIGIT", "INT_PART", 
                  "FRACTION", "EXPONENT", "SHORT_STRING", "LONG_STRING", 
                  "LONG_STRING_ITEM", "LONG_STRING_CHAR", "STRING_ESCAPE_SEQ", 
                  "SPACES", "COMMENT", "LINE_JOINING" ]

    grammarFileName = "Typt.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    @property
    def tokens(self):
        try:
            return self._tokens
        except AttributeError:
            self._tokens = []
            return self._tokens

    @property
    def indents(self):
        try:
            return self._indents
        except AttributeError:
            self._indents = []
            return self._indents

    @property
    def opened(self):
        try:
            return self._opened
        except AttributeError:
            self._opened = 0
            return self._opened

    @opened.setter
    def opened(self, value):
        self._opened = value

    @property
    def last_token(self):
        try:
            return self._last_token
        except AttributeError:
            self._last_token = None
            return self._last_token

    @last_token.setter
    def last_token(self, value):
        self._last_token = value

    def reset(self):
        super().reset()
        self.tokens = []
        self.indents = []
        self.opened = 0
        self.last_token = None

    def emitToken(self, t):
        """Name non-PEP8 as name is fixed by antlr."""
        super().emitToken(t)
        self.tokens.append(t)

    def nextToken(self):
        """Name non-PEP8 as name is fixed by antlr."""
        if self._input.LA(1) == Token.EOF and self.indents:
            for i in range(len(self.tokens)-1,-1,-1):
                if self.tokens[i].type == Token.EOF:
                    self.tokens.pop(i)
        
            self.emitToken(self.common_token(LanguageParser.NEWLINE, '\n'))
        
            # Handle dedents
            while self.indents:
                self.emitToken(self.create_dedent())
                self.indents.pop()
        
            self.emitToken(self.common_token(LanguageParser.EOF, "<EOF>"))
        
        next = super().nextToken()
        if next.channel == Token.DEFAULT_CHANNEL:
            self.last_token = next
        
        return next if not self.tokens else self.tokens.pop(0)

    def create_dedent(self):
        """Return a new DEDENT token at the current line."""
        dedent = self.common_token(LanguageParser.DEDENT, "")
        dedent.line = self.last_token.line
        return dedent

    def common_token(self, type, text, indent=0):
        """Create a common token of the the given type."""
        stop = self.getCharIndex() - 1 - indent
        start = (stop - len(text) + 1) if text else stop
        return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)

    @staticmethod
    def get_indentation_count(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count += 8 - (count % 8)
            else:
                count += 1
        return count

    def at_start_of_line(self):
        """Get the token at the begining of the current line."""
        return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1



    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[87] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            tempt = Lexer.text.fget(self)
            newline = re.sub("[^\r\n\f]+", "", tempt)
            spaces = re.sub("[\r\n\f]+", "", tempt)

            la_char = ""
            try:
                la_char = chr(self._input.LA(1))
            except ValueError:
                # Occurs on EOF
                pass

            if self.opened > 0 or la_char in ('\r', '\n', '\f', '#'):
                self.skip()
            else:
                indent = self.get_indentation_count(spaces)
                previous = self.indents[-1] if self.indents else 0
                self.emitToken(self.common_token(self.NEWLINE, newline, indent=indent))
                
                if indent == previous:
                    self.skip()
                elif indent > previous:
                    self.indents.append(indent)
                    self.emitToken(self.common_token(LanguageParser.INDENT, spaces))
                else:
                    while self.indents and self.indents[-1] > indent:
                        self.emitToken(self.create_dedent())
                        self.indents.pop()
                
                
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[87] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.at_start_of_line()
         


