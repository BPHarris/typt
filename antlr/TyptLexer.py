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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2a")
        buf.write("\u031f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("p\tp\4q\tq\4r\tr\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$")
        buf.write("\3$\3$\3$\3$\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\3<\3<")
        buf.write("\3=\3=\3=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3@\3@\3@\3@\3")
        buf.write("@\3@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3C\3D\3D\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3H\3H\3H\3I\3")
        buf.write("I\3I\3I\3J\3J\3J\3J\3J\3J\3K\3K\3K\3K\3K\3K\3K\3L\3L\3")
        buf.write("L\3L\3L\3L\3L\3M\3M\3N\3N\3O\3O\3O\3O\3O\3O\3O\3O\3O\3")
        buf.write("P\3P\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3R\3S\3S\3S\3")
        buf.write("S\3S\3T\3T\5T\u0240\nT\3U\3U\5U\u0244\nU\3V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\5V\u024f\nV\3W\3W\3W\3W\5W\u0255\nW\3X\3")
        buf.write("X\3X\5X\u025a\nX\3X\3X\5X\u025e\nX\3X\5X\u0261\nX\5X\u0263")
        buf.write("\nX\3X\3X\3Y\3Y\7Y\u0269\nY\fY\16Y\u026c\13Y\3Z\3Z\7Z")
        buf.write("\u0270\nZ\fZ\16Z\u0273\13Z\3Z\6Z\u0276\nZ\rZ\16Z\u0277")
        buf.write("\5Z\u027a\nZ\3[\3[\3[\6[\u027f\n[\r[\16[\u0280\3\\\3\\")
        buf.write("\3\\\6\\\u0286\n\\\r\\\16\\\u0287\3]\3]\3]\6]\u028d\n")
        buf.write("]\r]\16]\u028e\3^\3^\3^\3^\3^\3^\3^\3^\3^\3^\3^\3^\3^")
        buf.write("\5^\u029e\n^\3_\3_\3_\5_\u02a3\n_\3_\3_\3`\3`\3a\5a\u02aa")
        buf.write("\na\3b\3b\5b\u02ae\nb\3c\3c\3d\3d\3e\3e\3f\3f\3g\3g\3")
        buf.write("h\6h\u02bb\nh\rh\16h\u02bc\3i\6i\u02c0\ni\ri\16i\u02c1")
        buf.write("\3j\3j\5j\u02c6\nj\3j\6j\u02c9\nj\rj\16j\u02ca\3k\3k\3")
        buf.write("k\7k\u02d0\nk\fk\16k\u02d3\13k\3k\3k\3k\3k\7k\u02d9\n")
        buf.write("k\fk\16k\u02dc\13k\3k\5k\u02df\nk\3l\3l\3l\3l\3l\7l\u02e6")
        buf.write("\nl\fl\16l\u02e9\13l\3l\3l\3l\3l\3l\3l\3l\3l\7l\u02f3")
        buf.write("\nl\fl\16l\u02f6\13l\3l\3l\3l\5l\u02fb\nl\3m\3m\5m\u02ff")
        buf.write("\nm\3n\3n\3o\3o\3o\3o\5o\u0307\no\3p\6p\u030a\np\rp\16")
        buf.write("p\u030b\3q\3q\7q\u0310\nq\fq\16q\u0313\13q\3r\3r\5r\u0317")
        buf.write("\nr\3r\5r\u031a\nr\3r\3r\5r\u031e\nr\2\2s\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177")
        buf.write("A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008f")
        buf.write("I\u0091J\u0093K\u0095L\u0097M\u0099N\u009bO\u009dP\u009f")
        buf.write("Q\u00a1R\u00a3S\u00a5T\u00a7U\u00a9V\u00abW\u00adX\u00af")
        buf.write("Y\u00b1Z\u00b3[\u00b5\\\u00b7]\u00b9^\u00bb_\u00bd`\u00bf")
        buf.write("a\u00c1\2\u00c3\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\u00cd")
        buf.write("\2\u00cf\2\u00d1\2\u00d3\2\u00d5\2\u00d7\2\u00d9\2\u00db")
        buf.write("\2\u00dd\2\u00df\2\u00e1\2\u00e3\2\3\2\22\4\2QQqq\4\2")
        buf.write("ZZzz\4\2DDdd\5\2C\\aac|\3\2\63;\3\2\62;\3\2\629\5\2\62")
        buf.write(";CHch\3\2\62\63\4\2GGgg\4\2--//\6\2\f\f\16\17))^^\6\2")
        buf.write("\f\f\16\17$$^^\3\2^^\4\2\13\13\"\"\4\2\f\f\16\17\2\u0335")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\3\u00e5\3\2\2")
        buf.write("\2\5\u00eb\3\2\2\2\7\u00ed\3\2\2\2\t\u00f2\3\2\2\2\13")
        buf.write("\u00f4\3\2\2\2\r\u00f6\3\2\2\2\17\u00f9\3\2\2\2\21\u00fc")
        buf.write("\3\2\2\2\23\u00ff\3\2\2\2\25\u0102\3\2\2\2\27\u0105\3")
        buf.write("\2\2\2\31\u0108\3\2\2\2\33\u010b\3\2\2\2\35\u010e\3\2")
        buf.write("\2\2\37\u0112\3\2\2\2!\u0116\3\2\2\2#\u011a\3\2\2\2%\u011e")
        buf.write("\3\2\2\2\'\u0122\3\2\2\2)\u0127\3\2\2\2+\u012d\3\2\2\2")
        buf.write("-\u0136\3\2\2\2/\u013d\3\2\2\2\61\u0140\3\2\2\2\63\u0145")
        buf.write("\3\2\2\2\65\u014a\3\2\2\2\67\u0150\3\2\2\29\u0154\3\2")
        buf.write("\2\2;\u0157\3\2\2\2=\u015b\3\2\2\2?\u015d\3\2\2\2A\u015f")
        buf.write("\3\2\2\2C\u0162\3\2\2\2E\u016b\3\2\2\2G\u0170\3\2\2\2")
        buf.write("I\u0176\3\2\2\2K\u0178\3\2\2\2M\u0185\3\2\2\2O\u0188\3")
        buf.write("\2\2\2Q\u018c\3\2\2\2S\u0190\3\2\2\2U\u0192\3\2\2\2W\u0194")
        buf.write("\3\2\2\2Y\u0197\3\2\2\2[\u019a\3\2\2\2]\u019d\3\2\2\2")
        buf.write("_\u01a0\3\2\2\2a\u01a3\3\2\2\2c\u01a5\3\2\2\2e\u01a7\3")
        buf.write("\2\2\2g\u01a9\3\2\2\2i\u01ac\3\2\2\2k\u01af\3\2\2\2m\u01b1")
        buf.write("\3\2\2\2o\u01b3\3\2\2\2q\u01b5\3\2\2\2s\u01b7\3\2\2\2")
        buf.write("u\u01b9\3\2\2\2w\u01bc\3\2\2\2y\u01be\3\2\2\2{\u01c1\3")
        buf.write("\2\2\2}\u01c6\3\2\2\2\177\u01cb\3\2\2\2\u0081\u01d1\3")
        buf.write("\2\2\2\u0083\u01db\3\2\2\2\u0085\u01e6\3\2\2\2\u0087\u01ef")
        buf.write("\3\2\2\2\u0089\u01f9\3\2\2\2\u008b\u01fb\3\2\2\2\u008d")
        buf.write("\u01fd\3\2\2\2\u008f\u01ff\3\2\2\2\u0091\u0204\3\2\2\2")
        buf.write("\u0093\u0208\3\2\2\2\u0095\u020e\3\2\2\2\u0097\u0215\3")
        buf.write("\2\2\2\u0099\u021c\3\2\2\2\u009b\u021e\3\2\2\2\u009d\u0220")
        buf.write("\3\2\2\2\u009f\u0229\3\2\2\2\u00a1\u022e\3\2\2\2\u00a3")
        buf.write("\u0234\3\2\2\2\u00a5\u0238\3\2\2\2\u00a7\u023f\3\2\2\2")
        buf.write("\u00a9\u0243\3\2\2\2\u00ab\u024e\3\2\2\2\u00ad\u0254\3")
        buf.write("\2\2\2\u00af\u0262\3\2\2\2\u00b1\u0266\3\2\2\2\u00b3\u0279")
        buf.write("\3\2\2\2\u00b5\u027b\3\2\2\2\u00b7\u0282\3\2\2\2\u00b9")
        buf.write("\u0289\3\2\2\2\u00bb\u029d\3\2\2\2\u00bd\u02a2\3\2\2\2")
        buf.write("\u00bf\u02a6\3\2\2\2\u00c1\u02a9\3\2\2\2\u00c3\u02ad\3")
        buf.write("\2\2\2\u00c5\u02af\3\2\2\2\u00c7\u02b1\3\2\2\2\u00c9\u02b3")
        buf.write("\3\2\2\2\u00cb\u02b5\3\2\2\2\u00cd\u02b7\3\2\2\2\u00cf")
        buf.write("\u02ba\3\2\2\2\u00d1\u02bf\3\2\2\2\u00d3\u02c3\3\2\2\2")
        buf.write("\u00d5\u02de\3\2\2\2\u00d7\u02fa\3\2\2\2\u00d9\u02fe\3")
        buf.write("\2\2\2\u00db\u0300\3\2\2\2\u00dd\u0306\3\2\2\2\u00df\u0309")
        buf.write("\3\2\2\2\u00e1\u030d\3\2\2\2\u00e3\u0314\3\2\2\2\u00e5")
        buf.write("\u00e6\7w\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8\7k\2\2\u00e8")
        buf.write("\u00e9\7p\2\2\u00e9\u00ea\7i\2\2\u00ea\4\3\2\2\2\u00eb")
        buf.write("\u00ec\7<\2\2\u00ec\6\3\2\2\2\u00ed\u00ee\7h\2\2\u00ee")
        buf.write("\u00ef\7t\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1\7o\2\2\u00f1")
        buf.write("\b\3\2\2\2\u00f2\u00f3\7.\2\2\u00f3\n\3\2\2\2\u00f4\u00f5")
        buf.write("\7?\2\2\u00f5\f\3\2\2\2\u00f6\u00f7\7-\2\2\u00f7\u00f8")
        buf.write("\7?\2\2\u00f8\16\3\2\2\2\u00f9\u00fa\7/\2\2\u00fa\u00fb")
        buf.write("\7?\2\2\u00fb\20\3\2\2\2\u00fc\u00fd\7,\2\2\u00fd\u00fe")
        buf.write("\7?\2\2\u00fe\22\3\2\2\2\u00ff\u0100\7\61\2\2\u0100\u0101")
        buf.write("\7?\2\2\u0101\24\3\2\2\2\u0102\u0103\7\'\2\2\u0103\u0104")
        buf.write("\7?\2\2\u0104\26\3\2\2\2\u0105\u0106\7(\2\2\u0106\u0107")
        buf.write("\7?\2\2\u0107\30\3\2\2\2\u0108\u0109\7~\2\2\u0109\u010a")
        buf.write("\7?\2\2\u010a\32\3\2\2\2\u010b\u010c\7`\2\2\u010c\u010d")
        buf.write("\7?\2\2\u010d\34\3\2\2\2\u010e\u010f\7>\2\2\u010f\u0110")
        buf.write("\7>\2\2\u0110\u0111\7?\2\2\u0111\36\3\2\2\2\u0112\u0113")
        buf.write("\7@\2\2\u0113\u0114\7@\2\2\u0114\u0115\7?\2\2\u0115 \3")
        buf.write("\2\2\2\u0116\u0117\7,\2\2\u0117\u0118\7,\2\2\u0118\u0119")
        buf.write("\7?\2\2\u0119\"\3\2\2\2\u011a\u011b\7\61\2\2\u011b\u011c")
        buf.write("\7\61\2\2\u011c\u011d\7?\2\2\u011d$\3\2\2\2\u011e\u011f")
        buf.write("\7f\2\2\u011f\u0120\7g\2\2\u0120\u0121\7n\2\2\u0121&\3")
        buf.write("\2\2\2\u0122\u0123\7r\2\2\u0123\u0124\7c\2\2\u0124\u0125")
        buf.write("\7u\2\2\u0125\u0126\7u\2\2\u0126(\3\2\2\2\u0127\u0128")
        buf.write("\7d\2\2\u0128\u0129\7t\2\2\u0129\u012a\7g\2\2\u012a\u012b")
        buf.write("\7c\2\2\u012b\u012c\7m\2\2\u012c*\3\2\2\2\u012d\u012e")
        buf.write("\7e\2\2\u012e\u012f\7q\2\2\u012f\u0130\7p\2\2\u0130\u0131")
        buf.write("\7v\2\2\u0131\u0132\7k\2\2\u0132\u0133\7p\2\2\u0133\u0134")
        buf.write("\7w\2\2\u0134\u0135\7g\2\2\u0135,\3\2\2\2\u0136\u0137")
        buf.write("\7t\2\2\u0137\u0138\7g\2\2\u0138\u0139\7v\2\2\u0139\u013a")
        buf.write("\7w\2\2\u013a\u013b\7t\2\2\u013b\u013c\7p\2\2\u013c.\3")
        buf.write("\2\2\2\u013d\u013e\7k\2\2\u013e\u013f\7h\2\2\u013f\60")
        buf.write("\3\2\2\2\u0140\u0141\7g\2\2\u0141\u0142\7n\2\2\u0142\u0143")
        buf.write("\7k\2\2\u0143\u0144\7h\2\2\u0144\62\3\2\2\2\u0145\u0146")
        buf.write("\7g\2\2\u0146\u0147\7n\2\2\u0147\u0148\7u\2\2\u0148\u0149")
        buf.write("\7g\2\2\u0149\64\3\2\2\2\u014a\u014b\7y\2\2\u014b\u014c")
        buf.write("\7j\2\2\u014c\u014d\7k\2\2\u014d\u014e\7n\2\2\u014e\u014f")
        buf.write("\7g\2\2\u014f\66\3\2\2\2\u0150\u0151\7h\2\2\u0151\u0152")
        buf.write("\7q\2\2\u0152\u0153\7t\2\2\u01538\3\2\2\2\u0154\u0155")
        buf.write("\7k\2\2\u0155\u0156\7p\2\2\u0156:\3\2\2\2\u0157\u0158")
        buf.write("\7f\2\2\u0158\u0159\7g\2\2\u0159\u015a\7h\2\2\u015a<\3")
        buf.write("\2\2\2\u015b\u015c\7*\2\2\u015c>\3\2\2\2\u015d\u015e\7")
        buf.write("+\2\2\u015e@\3\2\2\2\u015f\u0160\7/\2\2\u0160\u0161\7")
        buf.write("@\2\2\u0161B\3\2\2\2\u0162\u0163\7a\2\2\u0163\u0164\7")
        buf.write("a\2\2\u0164\u0165\7k\2\2\u0165\u0166\7p\2\2\u0166\u0167")
        buf.write("\7k\2\2\u0167\u0168\7v\2\2\u0168\u0169\7a\2\2\u0169\u016a")
        buf.write("\7a\2\2\u016aD\3\2\2\2\u016b\u016c\7u\2\2\u016c\u016d")
        buf.write("\7g\2\2\u016d\u016e\7n\2\2\u016e\u016f\7h\2\2\u016fF\3")
        buf.write("\2\2\2\u0170\u0171\7e\2\2\u0171\u0172\7n\2\2\u0172\u0173")
        buf.write("\7c\2\2\u0173\u0174\7u\2\2\u0174\u0175\7u\2\2\u0175H\3")
        buf.write("\2\2\2\u0176\u0177\7B\2\2\u0177J\3\2\2\2\u0178\u0179\7")
        buf.write("u\2\2\u0179\u017a\7v\2\2\u017a\u017b\7c\2\2\u017b\u017c")
        buf.write("\7v\2\2\u017c\u017d\7k\2\2\u017d\u017e\7e\2\2\u017e\u017f")
        buf.write("\7o\2\2\u017f\u0180\7g\2\2\u0180\u0181\7v\2\2\u0181\u0182")
        buf.write("\7j\2\2\u0182\u0183\7q\2\2\u0183\u0184\7f\2\2\u0184L\3")
        buf.write("\2\2\2\u0185\u0186\7q\2\2\u0186\u0187\7t\2\2\u0187N\3")
        buf.write("\2\2\2\u0188\u0189\7c\2\2\u0189\u018a\7p\2\2\u018a\u018b")
        buf.write("\7f\2\2\u018bP\3\2\2\2\u018c\u018d\7p\2\2\u018d\u018e")
        buf.write("\7q\2\2\u018e\u018f\7v\2\2\u018fR\3\2\2\2\u0190\u0191")
        buf.write("\7>\2\2\u0191T\3\2\2\2\u0192\u0193\7@\2\2\u0193V\3\2\2")
        buf.write("\2\u0194\u0195\7?\2\2\u0195\u0196\7?\2\2\u0196X\3\2\2")
        buf.write("\2\u0197\u0198\7@\2\2\u0198\u0199\7?\2\2\u0199Z\3\2\2")
        buf.write("\2\u019a\u019b\7>\2\2\u019b\u019c\7?\2\2\u019c\\\3\2\2")
        buf.write("\2\u019d\u019e\7#\2\2\u019e\u019f\7?\2\2\u019f^\3\2\2")
        buf.write("\2\u01a0\u01a1\7k\2\2\u01a1\u01a2\7u\2\2\u01a2`\3\2\2")
        buf.write("\2\u01a3\u01a4\7~\2\2\u01a4b\3\2\2\2\u01a5\u01a6\7`\2")
        buf.write("\2\u01a6d\3\2\2\2\u01a7\u01a8\7(\2\2\u01a8f\3\2\2\2\u01a9")
        buf.write("\u01aa\7>\2\2\u01aa\u01ab\7>\2\2\u01abh\3\2\2\2\u01ac")
        buf.write("\u01ad\7@\2\2\u01ad\u01ae\7@\2\2\u01aej\3\2\2\2\u01af")
        buf.write("\u01b0\7-\2\2\u01b0l\3\2\2\2\u01b1\u01b2\7/\2\2\u01b2")
        buf.write("n\3\2\2\2\u01b3\u01b4\7,\2\2\u01b4p\3\2\2\2\u01b5\u01b6")
        buf.write("\7\61\2\2\u01b6r\3\2\2\2\u01b7\u01b8\7\'\2\2\u01b8t\3")
        buf.write("\2\2\2\u01b9\u01ba\7\61\2\2\u01ba\u01bb\7\61\2\2\u01bb")
        buf.write("v\3\2\2\2\u01bc\u01bd\7\u0080\2\2\u01bdx\3\2\2\2\u01be")
        buf.write("\u01bf\7,\2\2\u01bf\u01c0\7,\2\2\u01c0z\3\2\2\2\u01c1")
        buf.write("\u01c2\7P\2\2\u01c2\u01c3\7q\2\2\u01c3\u01c4\7p\2\2\u01c4")
        buf.write("\u01c5\7g\2\2\u01c5|\3\2\2\2\u01c6\u01c7\7V\2\2\u01c7")
        buf.write("\u01c8\7t\2\2\u01c8\u01c9\7w\2\2\u01c9\u01ca\7g\2\2\u01ca")
        buf.write("~\3\2\2\2\u01cb\u01cc\7H\2\2\u01cc\u01cd\7c\2\2\u01cd")
        buf.write("\u01ce\7n\2\2\u01ce\u01cf\7u\2\2\u01cf\u01d0\7g\2\2\u01d0")
        buf.write("\u0080\3\2\2\2\u01d1\u01d2\7p\2\2\u01d2\u01d3\7g\2\2\u01d3")
        buf.write("\u01d4\7y\2\2\u01d4\u01d5\7\"\2\2\u01d5\u01d6\7n\2\2\u01d6")
        buf.write("\u01d7\7k\2\2\u01d7\u01d8\7u\2\2\u01d8\u01d9\7v\2\2\u01d9")
        buf.write("\u01da\7*\2\2\u01da\u0082\3\2\2\2\u01db\u01dc\7p\2\2\u01dc")
        buf.write("\u01dd\7g\2\2\u01dd\u01de\7y\2\2\u01de\u01df\7\"\2\2\u01df")
        buf.write("\u01e0\7v\2\2\u01e0\u01e1\7w\2\2\u01e1\u01e2\7r\2\2\u01e2")
        buf.write("\u01e3\7n\2\2\u01e3\u01e4\7g\2\2\u01e4\u01e5\7*\2\2\u01e5")
        buf.write("\u0084\3\2\2\2\u01e6\u01e7\7p\2\2\u01e7\u01e8\7g\2\2\u01e8")
        buf.write("\u01e9\7y\2\2\u01e9\u01ea\7\"\2\2\u01ea\u01eb\7u\2\2\u01eb")
        buf.write("\u01ec\7g\2\2\u01ec\u01ed\7v\2\2\u01ed\u01ee\7*\2\2\u01ee")
        buf.write("\u0086\3\2\2\2\u01ef\u01f0\7p\2\2\u01f0\u01f1\7g\2\2\u01f1")
        buf.write("\u01f2\7y\2\2\u01f2\u01f3\7\"\2\2\u01f3\u01f4\7f\2\2\u01f4")
        buf.write("\u01f5\7k\2\2\u01f5\u01f6\7e\2\2\u01f6\u01f7\7v\2\2\u01f7")
        buf.write("\u01f8\7*\2\2\u01f8\u0088\3\2\2\2\u01f9\u01fa\7]\2\2\u01fa")
        buf.write("\u008a\3\2\2\2\u01fb\u01fc\7_\2\2\u01fc\u008c\3\2\2\2")
        buf.write("\u01fd\u01fe\7\60\2\2\u01fe\u008e\3\2\2\2\u01ff\u0200")
        buf.write("\7D\2\2\u0200\u0201\7q\2\2\u0201\u0202\7q\2\2\u0202\u0203")
        buf.write("\7n\2\2\u0203\u0090\3\2\2\2\u0204\u0205\7K\2\2\u0205\u0206")
        buf.write("\7p\2\2\u0206\u0207\7v\2\2\u0207\u0092\3\2\2\2\u0208\u0209")
        buf.write("\7H\2\2\u0209\u020a\7n\2\2\u020a\u020b\7q\2\2\u020b\u020c")
        buf.write("\7c\2\2\u020c\u020d\7v\2\2\u020d\u0094\3\2\2\2\u020e\u020f")
        buf.write("\7U\2\2\u020f\u0210\7v\2\2\u0210\u0211\7t\2\2\u0211\u0212")
        buf.write("\7k\2\2\u0212\u0213\7p\2\2\u0213\u0214\7i\2\2\u0214\u0096")
        buf.write("\3\2\2\2\u0215\u0216\7Q\2\2\u0216\u0217\7d\2\2\u0217\u0218")
        buf.write("\7l\2\2\u0218\u0219\7g\2\2\u0219\u021a\7e\2\2\u021a\u021b")
        buf.write("\7v\2\2\u021b\u0098\3\2\2\2\u021c\u021d\7}\2\2\u021d\u009a")
        buf.write("\3\2\2\2\u021e\u021f\7\177\2\2\u021f\u009c\3\2\2\2\u0220")
        buf.write("\u0221\7H\2\2\u0221\u0222\7w\2\2\u0222\u0223\7p\2\2\u0223")
        buf.write("\u0224\7e\2\2\u0224\u0225\7v\2\2\u0225\u0226\7k\2\2\u0226")
        buf.write("\u0227\7q\2\2\u0227\u0228\7p\2\2\u0228\u009e\3\2\2\2\u0229")
        buf.write("\u022a\7N\2\2\u022a\u022b\7k\2\2\u022b\u022c\7u\2\2\u022c")
        buf.write("\u022d\7v\2\2\u022d\u00a0\3\2\2\2\u022e\u022f\7V\2\2\u022f")
        buf.write("\u0230\7w\2\2\u0230\u0231\7r\2\2\u0231\u0232\7n\2\2\u0232")
        buf.write("\u0233\7g\2\2\u0233\u00a2\3\2\2\2\u0234\u0235\7U\2\2\u0235")
        buf.write("\u0236\7g\2\2\u0236\u0237\7v\2\2\u0237\u00a4\3\2\2\2\u0238")
        buf.write("\u0239\7F\2\2\u0239\u023a\7k\2\2\u023a\u023b\7e\2\2\u023b")
        buf.write("\u023c\7v\2\2\u023c\u00a6\3\2\2\2\u023d\u0240\5\u00ad")
        buf.write("W\2\u023e\u0240\5\u00bb^\2\u023f\u023d\3\2\2\2\u023f\u023e")
        buf.write("\3\2\2\2\u0240\u00a8\3\2\2\2\u0241\u0244\5\u00d5k\2\u0242")
        buf.write("\u0244\5\u00d7l\2\u0243\u0241\3\2\2\2\u0243\u0242\3\2")
        buf.write("\2\2\u0244\u00aa\3\2\2\2\u0245\u0246\7V\2\2\u0246\u0247")
        buf.write("\7t\2\2\u0247\u0248\7w\2\2\u0248\u024f\7g\2\2\u0249\u024a")
        buf.write("\7H\2\2\u024a\u024b\7c\2\2\u024b\u024c\7n\2\2\u024c\u024d")
        buf.write("\7u\2\2\u024d\u024f\7g\2\2\u024e\u0245\3\2\2\2\u024e\u0249")
        buf.write("\3\2\2\2\u024f\u00ac\3\2\2\2\u0250\u0255\5\u00b3Z\2\u0251")
        buf.write("\u0255\5\u00b5[\2\u0252\u0255\5\u00b7\\\2\u0253\u0255")
        buf.write("\5\u00b9]\2\u0254\u0250\3\2\2\2\u0254\u0251\3\2\2\2\u0254")
        buf.write("\u0252\3\2\2\2\u0254\u0253\3\2\2\2\u0255\u00ae\3\2\2\2")
        buf.write("\u0256\u0257\6X\2\2\u0257\u0263\5\u00dfp\2\u0258\u025a")
        buf.write("\7\17\2\2\u0259\u0258\3\2\2\2\u0259\u025a\3\2\2\2\u025a")
        buf.write("\u025b\3\2\2\2\u025b\u025e\7\f\2\2\u025c\u025e\4\16\17")
        buf.write("\2\u025d\u0259\3\2\2\2\u025d\u025c\3\2\2\2\u025e\u0260")
        buf.write("\3\2\2\2\u025f\u0261\5\u00dfp\2\u0260\u025f\3\2\2\2\u0260")
        buf.write("\u0261\3\2\2\2\u0261\u0263\3\2\2\2\u0262\u0256\3\2\2\2")
        buf.write("\u0262\u025d\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0265\b")
        buf.write("X\2\2\u0265\u00b0\3\2\2\2\u0266\u026a\5\u00c1a\2\u0267")
        buf.write("\u0269\5\u00c3b\2\u0268\u0267\3\2\2\2\u0269\u026c\3\2")
        buf.write("\2\2\u026a\u0268\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u00b2")
        buf.write("\3\2\2\2\u026c\u026a\3\2\2\2\u026d\u0271\5\u00c5c\2\u026e")
        buf.write("\u0270\5\u00c7d\2\u026f\u026e\3\2\2\2\u0270\u0273\3\2")
        buf.write("\2\2\u0271\u026f\3\2\2\2\u0271\u0272\3\2\2\2\u0272\u027a")
        buf.write("\3\2\2\2\u0273\u0271\3\2\2\2\u0274\u0276\7\62\2\2\u0275")
        buf.write("\u0274\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u0275\3\2\2\2")
        buf.write("\u0277\u0278\3\2\2\2\u0278\u027a\3\2\2\2\u0279\u026d\3")
        buf.write("\2\2\2\u0279\u0275\3\2\2\2\u027a\u00b4\3\2\2\2\u027b\u027c")
        buf.write("\7\62\2\2\u027c\u027e\t\2\2\2\u027d\u027f\5\u00c9e\2\u027e")
        buf.write("\u027d\3\2\2\2\u027f\u0280\3\2\2\2\u0280\u027e\3\2\2\2")
        buf.write("\u0280\u0281\3\2\2\2\u0281\u00b6\3\2\2\2\u0282\u0283\7")
        buf.write("\62\2\2\u0283\u0285\t\3\2\2\u0284\u0286\5\u00cbf\2\u0285")
        buf.write("\u0284\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0285\3\2\2\2")
        buf.write("\u0287\u0288\3\2\2\2\u0288\u00b8\3\2\2\2\u0289\u028a\7")
        buf.write("\62\2\2\u028a\u028c\t\4\2\2\u028b\u028d\5\u00cdg\2\u028c")
        buf.write("\u028b\3\2\2\2\u028d\u028e\3\2\2\2\u028e\u028c\3\2\2\2")
        buf.write("\u028e\u028f\3\2\2\2\u028f\u00ba\3\2\2\2\u0290\u0291\5")
        buf.write("\u00cfh\2\u0291\u0292\7\60\2\2\u0292\u0293\5\u00d1i\2")
        buf.write("\u0293\u029e\3\2\2\2\u0294\u0295\5\u00cfh\2\u0295\u0296")
        buf.write("\5\u00d3j\2\u0296\u029e\3\2\2\2\u0297\u0298\5\u00cfh\2")
        buf.write("\u0298\u0299\7\60\2\2\u0299\u029a\5\u00d1i\2\u029a\u029b")
        buf.write("\3\2\2\2\u029b\u029c\5\u00d3j\2\u029c\u029e\3\2\2\2\u029d")
        buf.write("\u0290\3\2\2\2\u029d\u0294\3\2\2\2\u029d\u0297\3\2\2\2")
        buf.write("\u029e\u00bc\3\2\2\2\u029f\u02a3\5\u00dfp\2\u02a0\u02a3")
        buf.write("\5\u00e1q\2\u02a1\u02a3\5\u00e3r\2\u02a2\u029f\3\2\2\2")
        buf.write("\u02a2\u02a0\3\2\2\2\u02a2\u02a1\3\2\2\2\u02a3\u02a4\3")
        buf.write("\2\2\2\u02a4\u02a5\b_\3\2\u02a5\u00be\3\2\2\2\u02a6\u02a7")
        buf.write("\13\2\2\2\u02a7\u00c0\3\2\2\2\u02a8\u02aa\t\5\2\2\u02a9")
        buf.write("\u02a8\3\2\2\2\u02aa\u00c2\3\2\2\2\u02ab\u02ae\5\u00c1")
        buf.write("a\2\u02ac\u02ae\5\u00c7d\2\u02ad\u02ab\3\2\2\2\u02ad\u02ac")
        buf.write("\3\2\2\2\u02ae\u00c4\3\2\2\2\u02af\u02b0\t\6\2\2\u02b0")
        buf.write("\u00c6\3\2\2\2\u02b1\u02b2\t\7\2\2\u02b2\u00c8\3\2\2\2")
        buf.write("\u02b3\u02b4\t\b\2\2\u02b4\u00ca\3\2\2\2\u02b5\u02b6\t")
        buf.write("\t\2\2\u02b6\u00cc\3\2\2\2\u02b7\u02b8\t\n\2\2\u02b8\u00ce")
        buf.write("\3\2\2\2\u02b9\u02bb\5\u00c7d\2\u02ba\u02b9\3\2\2\2\u02bb")
        buf.write("\u02bc\3\2\2\2\u02bc\u02ba\3\2\2\2\u02bc\u02bd\3\2\2\2")
        buf.write("\u02bd\u00d0\3\2\2\2\u02be\u02c0\5\u00c7d\2\u02bf\u02be")
        buf.write("\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1\u02bf\3\2\2\2\u02c1")
        buf.write("\u02c2\3\2\2\2\u02c2\u00d2\3\2\2\2\u02c3\u02c5\t\13\2")
        buf.write("\2\u02c4\u02c6\t\f\2\2\u02c5\u02c4\3\2\2\2\u02c5\u02c6")
        buf.write("\3\2\2\2\u02c6\u02c8\3\2\2\2\u02c7\u02c9\5\u00c7d\2\u02c8")
        buf.write("\u02c7\3\2\2\2\u02c9\u02ca\3\2\2\2\u02ca\u02c8\3\2\2\2")
        buf.write("\u02ca\u02cb\3\2\2\2\u02cb\u00d4\3\2\2\2\u02cc\u02d1\7")
        buf.write(")\2\2\u02cd\u02d0\5\u00ddo\2\u02ce\u02d0\n\r\2\2\u02cf")
        buf.write("\u02cd\3\2\2\2\u02cf\u02ce\3\2\2\2\u02d0\u02d3\3\2\2\2")
        buf.write("\u02d1\u02cf\3\2\2\2\u02d1\u02d2\3\2\2\2\u02d2\u02d4\3")
        buf.write("\2\2\2\u02d3\u02d1\3\2\2\2\u02d4\u02df\7)\2\2\u02d5\u02da")
        buf.write("\7$\2\2\u02d6\u02d9\5\u00ddo\2\u02d7\u02d9\n\16\2\2\u02d8")
        buf.write("\u02d6\3\2\2\2\u02d8\u02d7\3\2\2\2\u02d9\u02dc\3\2\2\2")
        buf.write("\u02da\u02d8\3\2\2\2\u02da\u02db\3\2\2\2\u02db\u02dd\3")
        buf.write("\2\2\2\u02dc\u02da\3\2\2\2\u02dd\u02df\7$\2\2\u02de\u02cc")
        buf.write("\3\2\2\2\u02de\u02d5\3\2\2\2\u02df\u00d6\3\2\2\2\u02e0")
        buf.write("\u02e1\7)\2\2\u02e1\u02e2\7)\2\2\u02e2\u02e3\7)\2\2\u02e3")
        buf.write("\u02e7\3\2\2\2\u02e4\u02e6\5\u00d9m\2\u02e5\u02e4\3\2")
        buf.write("\2\2\u02e6\u02e9\3\2\2\2\u02e7\u02e5\3\2\2\2\u02e7\u02e8")
        buf.write("\3\2\2\2\u02e8\u02ea\3\2\2\2\u02e9\u02e7\3\2\2\2\u02ea")
        buf.write("\u02eb\7)\2\2\u02eb\u02ec\7)\2\2\u02ec\u02fb\7)\2\2\u02ed")
        buf.write("\u02ee\7$\2\2\u02ee\u02ef\7$\2\2\u02ef\u02f0\7$\2\2\u02f0")
        buf.write("\u02f4\3\2\2\2\u02f1\u02f3\5\u00d9m\2\u02f2\u02f1\3\2")
        buf.write("\2\2\u02f3\u02f6\3\2\2\2\u02f4\u02f2\3\2\2\2\u02f4\u02f5")
        buf.write("\3\2\2\2\u02f5\u02f7\3\2\2\2\u02f6\u02f4\3\2\2\2\u02f7")
        buf.write("\u02f8\7$\2\2\u02f8\u02f9\7$\2\2\u02f9\u02fb\7$\2\2\u02fa")
        buf.write("\u02e0\3\2\2\2\u02fa\u02ed\3\2\2\2\u02fb\u00d8\3\2\2\2")
        buf.write("\u02fc\u02ff\5\u00dbn\2\u02fd\u02ff\5\u00ddo\2\u02fe\u02fc")
        buf.write("\3\2\2\2\u02fe\u02fd\3\2\2\2\u02ff\u00da\3\2\2\2\u0300")
        buf.write("\u0301\n\17\2\2\u0301\u00dc\3\2\2\2\u0302\u0303\7^\2\2")
        buf.write("\u0303\u0307\13\2\2\2\u0304\u0305\7^\2\2\u0305\u0307\5")
        buf.write("\u00afX\2\u0306\u0302\3\2\2\2\u0306\u0304\3\2\2\2\u0307")
        buf.write("\u00de\3\2\2\2\u0308\u030a\t\20\2\2\u0309\u0308\3\2\2")
        buf.write("\2\u030a\u030b\3\2\2\2\u030b\u0309\3\2\2\2\u030b\u030c")
        buf.write("\3\2\2\2\u030c\u00e0\3\2\2\2\u030d\u0311\7%\2\2\u030e")
        buf.write("\u0310\n\21\2\2\u030f\u030e\3\2\2\2\u0310\u0313\3\2\2")
        buf.write("\2\u0311\u030f\3\2\2\2\u0311\u0312\3\2\2\2\u0312\u00e2")
        buf.write("\3\2\2\2\u0313\u0311\3\2\2\2\u0314\u0316\7^\2\2\u0315")
        buf.write("\u0317\5\u00dfp\2\u0316\u0315\3\2\2\2\u0316\u0317\3\2")
        buf.write("\2\2\u0317\u031d\3\2\2\2\u0318\u031a\7\17\2\2\u0319\u0318")
        buf.write("\3\2\2\2\u0319\u031a\3\2\2\2\u031a\u031b\3\2\2\2\u031b")
        buf.write("\u031e\7\f\2\2\u031c\u031e\4\16\17\2\u031d\u0319\3\2\2")
        buf.write("\2\u031d\u031c\3\2\2\2\u031e\u00e4\3\2\2\2)\2\u023f\u0243")
        buf.write("\u024e\u0254\u0259\u025d\u0260\u0262\u026a\u0271\u0277")
        buf.write("\u0279\u0280\u0287\u028e\u029d\u02a2\u02a9\u02ad\u02bc")
        buf.write("\u02c1\u02c5\u02ca\u02cf\u02d1\u02d8\u02da\u02de\u02e7")
        buf.write("\u02f4\u02fa\u02fe\u0306\u030b\u0311\u0316\u0319\u031d")
        buf.write("\4\3X\2\b\2\2")
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
    NUMBER = 83
    STRING = 84
    BOOLEAN = 85
    INTEGER = 86
    NEWLINE = 87
    NAME = 88
    DECIMAL_INTEGER = 89
    OCT_INTEGER = 90
    HEX_INTEGER = 91
    BIN_INTEGER = 92
    FLOAT_NUMBER = 93
    SKIP_ = 94
    UNKNOWN_CHAR = 95

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'using'", "':'", "'from'", "','", "'='", "'+='", "'-='", "'*='", 
            "'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", "'**='", 
            "'//='", "'del'", "'pass'", "'break'", "'continue'", "'return'", 
            "'if'", "'elif'", "'else'", "'while'", "'for'", "'in'", "'def'", 
            "'('", "')'", "'->'", "'__init__'", "'self'", "'class'", "'@'", 
            "'staticmethod'", "'or'", "'and'", "'not'", "'<'", "'>'", "'=='", 
            "'>='", "'<='", "'!='", "'is'", "'|'", "'^'", "'&'", "'<<'", 
            "'>>'", "'+'", "'-'", "'*'", "'/'", "'%'", "'//'", "'~'", "'**'", 
            "'None'", "'True'", "'False'", "'new list('", "'new tuple('", 
            "'new set('", "'new dict('", "'['", "']'", "'.'", "'Bool'", 
            "'Int'", "'Float'", "'String'", "'Object'", "'{'", "'}'", "'Function'", 
            "'List'", "'Tuple'", "'Set'", "'Dict'" ]

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
                  "T__80", "T__81", "NUMBER", "STRING", "BOOLEAN", "INTEGER", 
                  "NEWLINE", "NAME", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
                  "BIN_INTEGER", "FLOAT_NUMBER", "SKIP_", "UNKNOWN_CHAR", 
                  "NAME_START", "NAME_CONTINUE", "NON_ZERO_DIGIT", "DIGIT", 
                  "OCT_DIGIT", "HEX_DIGIT", "BIN_DIGIT", "INT_PART", "FRACTION", 
                  "EXPONENT", "SHORT_STRING", "LONG_STRING", "LONG_STRING_ITEM", 
                  "LONG_STRING_CHAR", "STRING_ESCAPE_SEQ", "SPACES", "COMMENT", 
                  "LINE_JOINING" ]

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
            actions[86] = self.NEWLINE_action 
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
            preds[86] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.at_start_of_line()
         


