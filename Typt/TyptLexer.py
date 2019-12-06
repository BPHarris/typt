# Generated from .\Typt\Typt.g4 by ANTLR 4.7.2
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
        buf.write("\u02f8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("p\tp\4q\tq\4r\tr\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u012d\n\16")
        buf.write("\3\17\3\17\5\17\u0131\n\17\3\20\3\20\5\20\u0135\n\20\3")
        buf.write("\21\3\21\5\21\u0139\n\21\3\22\3\22\3\22\3\22\5\22\u013f")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\5)\u01b2\n)\3")
        buf.write(")\3)\5)\u01b6\n)\3)\5)\u01b9\n)\5)\u01bb\n)\3)\3)\3*\3")
        buf.write("*\7*\u01c1\n*\f*\16*\u01c4\13*\3+\3+\7+\u01c8\n+\f+\16")
        buf.write("+\u01cb\13+\3+\6+\u01ce\n+\r+\16+\u01cf\5+\u01d2\n+\3")
        buf.write(",\3,\3,\6,\u01d7\n,\r,\16,\u01d8\3-\3-\3-\6-\u01de\n-")
        buf.write("\r-\16-\u01df\3.\3.\3.\6.\u01e5\n.\r.\16.\u01e6\3/\3/")
        buf.write("\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01f6\n/\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\3;\3;\3")
        buf.write(";\3<\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3A\3B\3B\3B\3")
        buf.write("C\3C\3C\3D\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3H\3H\3I\3")
        buf.write("I\3J\3J\3J\3K\3K\3K\3L\3L\3L\3M\3M\3M\3N\3N\3N\3O\3O\3")
        buf.write("P\3P\3P\3Q\3Q\3R\3R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3U\3V\3")
        buf.write("V\3V\3W\3W\3W\3X\3X\3X\3Y\3Y\3Y\3Z\3Z\3Z\3[\3[\3[\3[\3")
        buf.write("\\\3\\\3\\\3\\\3]\3]\3]\3]\3^\3^\3^\3^\3_\3_\3_\5_\u027c")
        buf.write("\n_\3_\3_\3`\3`\3a\5a\u0283\na\3b\3b\5b\u0287\nb\3c\3")
        buf.write("c\3d\3d\3e\3e\3f\3f\3g\3g\3h\6h\u0294\nh\rh\16h\u0295")
        buf.write("\3i\6i\u0299\ni\ri\16i\u029a\3j\3j\5j\u029f\nj\3j\6j\u02a2")
        buf.write("\nj\rj\16j\u02a3\3k\3k\3k\7k\u02a9\nk\fk\16k\u02ac\13")
        buf.write("k\3k\3k\3k\3k\7k\u02b2\nk\fk\16k\u02b5\13k\3k\5k\u02b8")
        buf.write("\nk\3l\3l\3l\3l\3l\7l\u02bf\nl\fl\16l\u02c2\13l\3l\3l")
        buf.write("\3l\3l\3l\3l\3l\3l\7l\u02cc\nl\fl\16l\u02cf\13l\3l\3l")
        buf.write("\3l\5l\u02d4\nl\3m\3m\5m\u02d8\nm\3n\3n\3o\3o\3o\3o\5")
        buf.write("o\u02e0\no\3p\6p\u02e3\np\rp\16p\u02e4\3q\3q\7q\u02e9")
        buf.write("\nq\fq\16q\u02ec\13q\3r\3r\5r\u02f0\nr\3r\5r\u02f3\nr")
        buf.write("\3r\3r\5r\u02f7\nr\2\2s\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C")
        buf.write("\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093")
        buf.write("K\u0095L\u0097M\u0099N\u009bO\u009dP\u009fQ\u00a1R\u00a3")
        buf.write("S\u00a5T\u00a7U\u00a9V\u00abW\u00adX\u00afY\u00b1Z\u00b3")
        buf.write("[\u00b5\\\u00b7]\u00b9^\u00bb_\u00bd`\u00bfa\u00c1\2\u00c3")
        buf.write("\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\u00cd\2\u00cf\2\u00d1")
        buf.write("\2\u00d3\2\u00d5\2\u00d7\2\u00d9\2\u00db\2\u00dd\2\u00df")
        buf.write("\2\u00e1\2\u00e3\2\3\2\22\4\2QQqq\4\2ZZzz\4\2DDdd\5\2")
        buf.write("C\\aac|\3\2\63;\3\2\62;\3\2\629\5\2\62;CHch\3\2\62\63")
        buf.write("\4\2GGgg\4\2--//\6\2\f\f\16\17))^^\6\2\f\f\16\17$$^^\3")
        buf.write("\2^^\4\2\13\13\"\"\4\2\f\f\16\17\2\u0311\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7")
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2")
        buf.write("\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5")
        buf.write("\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2")
        buf.write("\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\3\u00e5\3\2\2\2\5\u00ea")
        buf.write("\3\2\2\2\7\u00ed\3\2\2\2\t\u00f1\3\2\2\2\13\u00f7\3\2")
        buf.write("\2\2\r\u00fe\3\2\2\2\17\u0103\3\2\2\2\21\u0109\3\2\2\2")
        buf.write("\23\u0112\3\2\2\2\25\u0117\3\2\2\2\27\u011b\3\2\2\2\31")
        buf.write("\u0121\3\2\2\2\33\u012c\3\2\2\2\35\u0130\3\2\2\2\37\u0134")
        buf.write("\3\2\2\2!\u0138\3\2\2\2#\u013e\3\2\2\2%\u0140\3\2\2\2")
        buf.write("\'\u0146\3\2\2\2)\u014a\3\2\2\2+\u0151\3\2\2\2-\u0158")
        buf.write("\3\2\2\2/\u015b\3\2\2\2\61\u0160\3\2\2\2\63\u0165\3\2")
        buf.write("\2\2\65\u016b\3\2\2\2\67\u016f\3\2\2\29\u0172\3\2\2\2")
        buf.write(";\u0175\3\2\2\2=\u0179\3\2\2\2?\u017d\3\2\2\2A\u0180\3")
        buf.write("\2\2\2C\u0186\3\2\2\2E\u018a\3\2\2\2G\u018f\3\2\2\2I\u0198")
        buf.write("\3\2\2\2K\u019e\3\2\2\2M\u01a3\3\2\2\2O\u01a8\3\2\2\2")
        buf.write("Q\u01ba\3\2\2\2S\u01be\3\2\2\2U\u01d1\3\2\2\2W\u01d3\3")
        buf.write("\2\2\2Y\u01da\3\2\2\2[\u01e1\3\2\2\2]\u01f5\3\2\2\2_\u01f7")
        buf.write("\3\2\2\2a\u01f9\3\2\2\2c\u01fd\3\2\2\2e\u01ff\3\2\2\2")
        buf.write("g\u0201\3\2\2\2i\u0203\3\2\2\2k\u0205\3\2\2\2m\u0207\3")
        buf.write("\2\2\2o\u0209\3\2\2\2q\u020b\3\2\2\2s\u020d\3\2\2\2u\u0210")
        buf.write("\3\2\2\2w\u0213\3\2\2\2y\u0216\3\2\2\2{\u0218\3\2\2\2")
        buf.write("}\u021a\3\2\2\2\177\u021c\3\2\2\2\u0081\u021e\3\2\2\2")
        buf.write("\u0083\u0221\3\2\2\2\u0085\u0224\3\2\2\2\u0087\u0227\3")
        buf.write("\2\2\2\u0089\u022a\3\2\2\2\u008b\u022d\3\2\2\2\u008d\u0230")
        buf.write("\3\2\2\2\u008f\u0233\3\2\2\2\u0091\u0235\3\2\2\2\u0093")
        buf.write("\u0237\3\2\2\2\u0095\u023a\3\2\2\2\u0097\u023d\3\2\2\2")
        buf.write("\u0099\u0240\3\2\2\2\u009b\u0243\3\2\2\2\u009d\u0246\3")
        buf.write("\2\2\2\u009f\u0248\3\2\2\2\u00a1\u024b\3\2\2\2\u00a3\u024d")
        buf.write("\3\2\2\2\u00a5\u0250\3\2\2\2\u00a7\u0253\3\2\2\2\u00a9")
        buf.write("\u0256\3\2\2\2\u00ab\u0259\3\2\2\2\u00ad\u025c\3\2\2\2")
        buf.write("\u00af\u025f\3\2\2\2\u00b1\u0262\3\2\2\2\u00b3\u0265\3")
        buf.write("\2\2\2\u00b5\u0268\3\2\2\2\u00b7\u026c\3\2\2\2\u00b9\u0270")
        buf.write("\3\2\2\2\u00bb\u0274\3\2\2\2\u00bd\u027b\3\2\2\2\u00bf")
        buf.write("\u027f\3\2\2\2\u00c1\u0282\3\2\2\2\u00c3\u0286\3\2\2\2")
        buf.write("\u00c5\u0288\3\2\2\2\u00c7\u028a\3\2\2\2\u00c9\u028c\3")
        buf.write("\2\2\2\u00cb\u028e\3\2\2\2\u00cd\u0290\3\2\2\2\u00cf\u0293")
        buf.write("\3\2\2\2\u00d1\u0298\3\2\2\2\u00d3\u029c\3\2\2\2\u00d5")
        buf.write("\u02b7\3\2\2\2\u00d7\u02d3\3\2\2\2\u00d9\u02d7\3\2\2\2")
        buf.write("\u00db\u02d9\3\2\2\2\u00dd\u02df\3\2\2\2\u00df\u02e2\3")
        buf.write("\2\2\2\u00e1\u02e6\3\2\2\2\u00e3\u02ed\3\2\2\2\u00e5\u00e6")
        buf.write("\7h\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7o\2\2\u00e9\4\3\2\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec")
        buf.write("\7u\2\2\u00ec\6\3\2\2\2\u00ed\u00ee\7\60\2\2\u00ee\u00ef")
        buf.write("\7\60\2\2\u00ef\u00f0\7\61\2\2\u00f0\b\3\2\2\2\u00f1\u00f2")
        buf.write("\7N\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5")
        buf.write("\7v\2\2\u00f5\u00f6\7]\2\2\u00f6\n\3\2\2\2\u00f7\u00f8")
        buf.write("\7V\2\2\u00f8\u00f9\7w\2\2\u00f9\u00fa\7r\2\2\u00fa\u00fb")
        buf.write("\7n\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7*\2\2\u00fd\f")
        buf.write("\3\2\2\2\u00fe\u00ff\7U\2\2\u00ff\u0100\7g\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\u0102\7*\2\2\u0102\16\3\2\2\2\u0103\u0104")
        buf.write("\7F\2\2\u0104\u0105\7k\2\2\u0105\u0106\7e\2\2\u0106\u0107")
        buf.write("\7v\2\2\u0107\u0108\7}\2\2\u0108\20\3\2\2\2\u0109\u010a")
        buf.write("\7H\2\2\u010a\u010b\7w\2\2\u010b\u010c\7p\2\2\u010c\u010d")
        buf.write("\7e\2\2\u010d\u010e\7v\2\2\u010e\u010f\7k\2\2\u010f\u0110")
        buf.write("\7q\2\2\u0110\u0111\7p\2\2\u0111\22\3\2\2\2\u0112\u0113")
        buf.write("\7D\2\2\u0113\u0114\7q\2\2\u0114\u0115\7q\2\2\u0115\u0116")
        buf.write("\7n\2\2\u0116\24\3\2\2\2\u0117\u0118\7K\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119\u011a\7v\2\2\u011a\26\3\2\2\2\u011b\u011c")
        buf.write("\7H\2\2\u011c\u011d\7n\2\2\u011d\u011e\7q\2\2\u011e\u011f")
        buf.write("\7c\2\2\u011f\u0120\7v\2\2\u0120\30\3\2\2\2\u0121\u0122")
        buf.write("\7U\2\2\u0122\u0123\7v\2\2\u0123\u0124\7t\2\2\u0124\u0125")
        buf.write("\7k\2\2\u0125\u0126\7p\2\2\u0126\u0127\7i\2\2\u0127\32")
        buf.write("\3\2\2\2\u0128\u012d\5S*\2\u0129\u012d\5\35\17\2\u012a")
        buf.write("\u012d\5\37\20\2\u012b\u012d\5!\21\2\u012c\u0128\3\2\2")
        buf.write("\2\u012c\u0129\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012b")
        buf.write("\3\2\2\2\u012d\34\3\2\2\2\u012e\u0131\5#\22\2\u012f\u0131")
        buf.write("\5]/\2\u0130\u012e\3\2\2\2\u0130\u012f\3\2\2\2\u0131\36")
        buf.write("\3\2\2\2\u0132\u0135\5\u00d5k\2\u0133\u0135\5\u00d7l\2")
        buf.write("\u0134\u0132\3\2\2\2\u0134\u0133\3\2\2\2\u0135 \3\2\2")
        buf.write("\2\u0136\u0139\5M\'\2\u0137\u0139\5O(\2\u0138\u0136\3")
        buf.write("\2\2\2\u0138\u0137\3\2\2\2\u0139\"\3\2\2\2\u013a\u013f")
        buf.write("\5U+\2\u013b\u013f\5W,\2\u013c\u013f\5Y-\2\u013d\u013f")
        buf.write("\5[.\2\u013e\u013a\3\2\2\2\u013e\u013b\3\2\2\2\u013e\u013c")
        buf.write("\3\2\2\2\u013e\u013d\3\2\2\2\u013f$\3\2\2\2\u0140\u0141")
        buf.write("\7w\2\2\u0141\u0142\7u\2\2\u0142\u0143\7k\2\2\u0143\u0144")
        buf.write("\7p\2\2\u0144\u0145\7i\2\2\u0145&\3\2\2\2\u0146\u0147")
        buf.write("\7f\2\2\u0147\u0148\7g\2\2\u0148\u0149\7h\2\2\u0149(\3")
        buf.write("\2\2\2\u014a\u014b\7t\2\2\u014b\u014c\7g\2\2\u014c\u014d")
        buf.write("\7v\2\2\u014d\u014e\7w\2\2\u014e\u014f\7t\2\2\u014f\u0150")
        buf.write("\7p\2\2\u0150*\3\2\2\2\u0151\u0152\7k\2\2\u0152\u0153")
        buf.write("\7o\2\2\u0153\u0154\7r\2\2\u0154\u0155\7q\2\2\u0155\u0156")
        buf.write("\7t\2\2\u0156\u0157\7v\2\2\u0157,\3\2\2\2\u0158\u0159")
        buf.write("\7k\2\2\u0159\u015a\7h\2\2\u015a.\3\2\2\2\u015b\u015c")
        buf.write("\7g\2\2\u015c\u015d\7n\2\2\u015d\u015e\7k\2\2\u015e\u015f")
        buf.write("\7h\2\2\u015f\60\3\2\2\2\u0160\u0161\7g\2\2\u0161\u0162")
        buf.write("\7n\2\2\u0162\u0163\7u\2\2\u0163\u0164\7g\2\2\u0164\62")
        buf.write("\3\2\2\2\u0165\u0166\7y\2\2\u0166\u0167\7j\2\2\u0167\u0168")
        buf.write("\7k\2\2\u0168\u0169\7n\2\2\u0169\u016a\7g\2\2\u016a\64")
        buf.write("\3\2\2\2\u016b\u016c\7h\2\2\u016c\u016d\7q\2\2\u016d\u016e")
        buf.write("\7t\2\2\u016e\66\3\2\2\2\u016f\u0170\7k\2\2\u0170\u0171")
        buf.write("\7p\2\2\u01718\3\2\2\2\u0172\u0173\7q\2\2\u0173\u0174")
        buf.write("\7t\2\2\u0174:\3\2\2\2\u0175\u0176\7c\2\2\u0176\u0177")
        buf.write("\7p\2\2\u0177\u0178\7f\2\2\u0178<\3\2\2\2\u0179\u017a")
        buf.write("\7p\2\2\u017a\u017b\7q\2\2\u017b\u017c\7v\2\2\u017c>\3")
        buf.write("\2\2\2\u017d\u017e\7k\2\2\u017e\u017f\7u\2\2\u017f@\3")
        buf.write("\2\2\2\u0180\u0181\7e\2\2\u0181\u0182\7n\2\2\u0182\u0183")
        buf.write("\7c\2\2\u0183\u0184\7u\2\2\u0184\u0185\7u\2\2\u0185B\3")
        buf.write("\2\2\2\u0186\u0187\7f\2\2\u0187\u0188\7g\2\2\u0188\u0189")
        buf.write("\7n\2\2\u0189D\3\2\2\2\u018a\u018b\7r\2\2\u018b\u018c")
        buf.write("\7c\2\2\u018c\u018d\7u\2\2\u018d\u018e\7u\2\2\u018eF\3")
        buf.write("\2\2\2\u018f\u0190\7e\2\2\u0190\u0191\7q\2\2\u0191\u0192")
        buf.write("\7p\2\2\u0192\u0193\7v\2\2\u0193\u0194\7k\2\2\u0194\u0195")
        buf.write("\7p\2\2\u0195\u0196\7w\2\2\u0196\u0197\7g\2\2\u0197H\3")
        buf.write("\2\2\2\u0198\u0199\7d\2\2\u0199\u019a\7t\2\2\u019a\u019b")
        buf.write("\7g\2\2\u019b\u019c\7c\2\2\u019c\u019d\7m\2\2\u019dJ\3")
        buf.write("\2\2\2\u019e\u019f\7P\2\2\u019f\u01a0\7q\2\2\u01a0\u01a1")
        buf.write("\7p\2\2\u01a1\u01a2\7g\2\2\u01a2L\3\2\2\2\u01a3\u01a4")
        buf.write("\7V\2\2\u01a4\u01a5\7t\2\2\u01a5\u01a6\7w\2\2\u01a6\u01a7")
        buf.write("\7g\2\2\u01a7N\3\2\2\2\u01a8\u01a9\7H\2\2\u01a9\u01aa")
        buf.write("\7c\2\2\u01aa\u01ab\7n\2\2\u01ab\u01ac\7u\2\2\u01ac\u01ad")
        buf.write("\7g\2\2\u01adP\3\2\2\2\u01ae\u01af\6)\2\2\u01af\u01bb")
        buf.write("\5\u00dfp\2\u01b0\u01b2\7\17\2\2\u01b1\u01b0\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b6\7\f\2\2")
        buf.write("\u01b4\u01b6\4\16\17\2\u01b5\u01b1\3\2\2\2\u01b5\u01b4")
        buf.write("\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b9\5\u00dfp\2\u01b8")
        buf.write("\u01b7\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2")
        buf.write("\u01ba\u01ae\3\2\2\2\u01ba\u01b5\3\2\2\2\u01bb\u01bc\3")
        buf.write("\2\2\2\u01bc\u01bd\b)\2\2\u01bdR\3\2\2\2\u01be\u01c2\5")
        buf.write("\u00c1a\2\u01bf\u01c1\5\u00c3b\2\u01c0\u01bf\3\2\2\2\u01c1")
        buf.write("\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2")
        buf.write("\u01c3T\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c9\5\u00c5")
        buf.write("c\2\u01c6\u01c8\5\u00c7d\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb")
        buf.write("\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write("\u01d2\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01ce\7\62\2")
        buf.write("\2\u01cd\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01cd")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1")
        buf.write("\u01c5\3\2\2\2\u01d1\u01cd\3\2\2\2\u01d2V\3\2\2\2\u01d3")
        buf.write("\u01d4\7\62\2\2\u01d4\u01d6\t\2\2\2\u01d5\u01d7\5\u00c9")
        buf.write("e\2\u01d6\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d6")
        buf.write("\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9X\3\2\2\2\u01da\u01db")
        buf.write("\7\62\2\2\u01db\u01dd\t\3\2\2\u01dc\u01de\5\u00cbf\2\u01dd")
        buf.write("\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01dd\3\2\2\2")
        buf.write("\u01df\u01e0\3\2\2\2\u01e0Z\3\2\2\2\u01e1\u01e2\7\62\2")
        buf.write("\2\u01e2\u01e4\t\4\2\2\u01e3\u01e5\5\u00cdg\2\u01e4\u01e3")
        buf.write("\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6")
        buf.write("\u01e7\3\2\2\2\u01e7\\\3\2\2\2\u01e8\u01e9\5\u00cfh\2")
        buf.write("\u01e9\u01ea\7\60\2\2\u01ea\u01eb\5\u00d1i\2\u01eb\u01f6")
        buf.write("\3\2\2\2\u01ec\u01ed\5\u00cfh\2\u01ed\u01ee\5\u00d3j\2")
        buf.write("\u01ee\u01f6\3\2\2\2\u01ef\u01f0\5\u00cfh\2\u01f0\u01f1")
        buf.write("\7\60\2\2\u01f1\u01f2\5\u00d1i\2\u01f2\u01f3\3\2\2\2\u01f3")
        buf.write("\u01f4\5\u00d3j\2\u01f4\u01f6\3\2\2\2\u01f5\u01e8\3\2")
        buf.write("\2\2\u01f5\u01ec\3\2\2\2\u01f5\u01ef\3\2\2\2\u01f6^\3")
        buf.write("\2\2\2\u01f7\u01f8\7\60\2\2\u01f8`\3\2\2\2\u01f9\u01fa")
        buf.write("\7\60\2\2\u01fa\u01fb\7\60\2\2\u01fb\u01fc\7\60\2\2\u01fc")
        buf.write("b\3\2\2\2\u01fd\u01fe\7,\2\2\u01fed\3\2\2\2\u01ff\u0200")
        buf.write("\7.\2\2\u0200f\3\2\2\2\u0201\u0202\7<\2\2\u0202h\3\2\2")
        buf.write("\2\u0203\u0204\7=\2\2\u0204j\3\2\2\2\u0205\u0206\7(\2")
        buf.write("\2\u0206l\3\2\2\2\u0207\u0208\7~\2\2\u0208n\3\2\2\2\u0209")
        buf.write("\u020a\7`\2\2\u020ap\3\2\2\2\u020b\u020c\7\u0080\2\2\u020c")
        buf.write("r\3\2\2\2\u020d\u020e\7,\2\2\u020e\u020f\7,\2\2\u020f")
        buf.write("t\3\2\2\2\u0210\u0211\7>\2\2\u0211\u0212\7>\2\2\u0212")
        buf.write("v\3\2\2\2\u0213\u0214\7@\2\2\u0214\u0215\7@\2\2\u0215")
        buf.write("x\3\2\2\2\u0216\u0217\7-\2\2\u0217z\3\2\2\2\u0218\u0219")
        buf.write("\7/\2\2\u0219|\3\2\2\2\u021a\u021b\7\61\2\2\u021b~\3\2")
        buf.write("\2\2\u021c\u021d\7\'\2\2\u021d\u0080\3\2\2\2\u021e\u021f")
        buf.write("\7\61\2\2\u021f\u0220\7\61\2\2\u0220\u0082\3\2\2\2\u0221")
        buf.write("\u0222\7*\2\2\u0222\u0223\bB\3\2\u0223\u0084\3\2\2\2\u0224")
        buf.write("\u0225\7+\2\2\u0225\u0226\bC\4\2\u0226\u0086\3\2\2\2\u0227")
        buf.write("\u0228\7]\2\2\u0228\u0229\bD\5\2\u0229\u0088\3\2\2\2\u022a")
        buf.write("\u022b\7_\2\2\u022b\u022c\bE\6\2\u022c\u008a\3\2\2\2\u022d")
        buf.write("\u022e\7}\2\2\u022e\u022f\bF\7\2\u022f\u008c\3\2\2\2\u0230")
        buf.write("\u0231\7\177\2\2\u0231\u0232\bG\b\2\u0232\u008e\3\2\2")
        buf.write("\2\u0233\u0234\7>\2\2\u0234\u0090\3\2\2\2\u0235\u0236")
        buf.write("\7@\2\2\u0236\u0092\3\2\2\2\u0237\u0238\7?\2\2\u0238\u0239")
        buf.write("\7?\2\2\u0239\u0094\3\2\2\2\u023a\u023b\7@\2\2\u023b\u023c")
        buf.write("\7?\2\2\u023c\u0096\3\2\2\2\u023d\u023e\7>\2\2\u023e\u023f")
        buf.write("\7?\2\2\u023f\u0098\3\2\2\2\u0240\u0241\7>\2\2\u0241\u0242")
        buf.write("\7@\2\2\u0242\u009a\3\2\2\2\u0243\u0244\7#\2\2\u0244\u0245")
        buf.write("\7?\2\2\u0245\u009c\3\2\2\2\u0246\u0247\7B\2\2\u0247\u009e")
        buf.write("\3\2\2\2\u0248\u0249\7/\2\2\u0249\u024a\7@\2\2\u024a\u00a0")
        buf.write("\3\2\2\2\u024b\u024c\7?\2\2\u024c\u00a2\3\2\2\2\u024d")
        buf.write("\u024e\7-\2\2\u024e\u024f\7?\2\2\u024f\u00a4\3\2\2\2\u0250")
        buf.write("\u0251\7/\2\2\u0251\u0252\7?\2\2\u0252\u00a6\3\2\2\2\u0253")
        buf.write("\u0254\7,\2\2\u0254\u0255\7?\2\2\u0255\u00a8\3\2\2\2\u0256")
        buf.write("\u0257\7B\2\2\u0257\u0258\7?\2\2\u0258\u00aa\3\2\2\2\u0259")
        buf.write("\u025a\7\61\2\2\u025a\u025b\7?\2\2\u025b\u00ac\3\2\2\2")
        buf.write("\u025c\u025d\7\'\2\2\u025d\u025e\7?\2\2\u025e\u00ae\3")
        buf.write("\2\2\2\u025f\u0260\7(\2\2\u0260\u0261\7?\2\2\u0261\u00b0")
        buf.write("\3\2\2\2\u0262\u0263\7~\2\2\u0263\u0264\7?\2\2\u0264\u00b2")
        buf.write("\3\2\2\2\u0265\u0266\7`\2\2\u0266\u0267\7?\2\2\u0267\u00b4")
        buf.write("\3\2\2\2\u0268\u0269\7>\2\2\u0269\u026a\7>\2\2\u026a\u026b")
        buf.write("\7?\2\2\u026b\u00b6\3\2\2\2\u026c\u026d\7@\2\2\u026d\u026e")
        buf.write("\7@\2\2\u026e\u026f\7?\2\2\u026f\u00b8\3\2\2\2\u0270\u0271")
        buf.write("\7,\2\2\u0271\u0272\7,\2\2\u0272\u0273\7?\2\2\u0273\u00ba")
        buf.write("\3\2\2\2\u0274\u0275\7\61\2\2\u0275\u0276\7\61\2\2\u0276")
        buf.write("\u0277\7?\2\2\u0277\u00bc\3\2\2\2\u0278\u027c\5\u00df")
        buf.write("p\2\u0279\u027c\5\u00e1q\2\u027a\u027c\5\u00e3r\2\u027b")
        buf.write("\u0278\3\2\2\2\u027b\u0279\3\2\2\2\u027b\u027a\3\2\2\2")
        buf.write("\u027c\u027d\3\2\2\2\u027d\u027e\b_\t\2\u027e\u00be\3")
        buf.write("\2\2\2\u027f\u0280\13\2\2\2\u0280\u00c0\3\2\2\2\u0281")
        buf.write("\u0283\t\5\2\2\u0282\u0281\3\2\2\2\u0283\u00c2\3\2\2\2")
        buf.write("\u0284\u0287\5\u00c1a\2\u0285\u0287\5\u00c7d\2\u0286\u0284")
        buf.write("\3\2\2\2\u0286\u0285\3\2\2\2\u0287\u00c4\3\2\2\2\u0288")
        buf.write("\u0289\t\6\2\2\u0289\u00c6\3\2\2\2\u028a\u028b\t\7\2\2")
        buf.write("\u028b\u00c8\3\2\2\2\u028c\u028d\t\b\2\2\u028d\u00ca\3")
        buf.write("\2\2\2\u028e\u028f\t\t\2\2\u028f\u00cc\3\2\2\2\u0290\u0291")
        buf.write("\t\n\2\2\u0291\u00ce\3\2\2\2\u0292\u0294\5\u00c7d\2\u0293")
        buf.write("\u0292\3\2\2\2\u0294\u0295\3\2\2\2\u0295\u0293\3\2\2\2")
        buf.write("\u0295\u0296\3\2\2\2\u0296\u00d0\3\2\2\2\u0297\u0299\5")
        buf.write("\u00c7d\2\u0298\u0297\3\2\2\2\u0299\u029a\3\2\2\2\u029a")
        buf.write("\u0298\3\2\2\2\u029a\u029b\3\2\2\2\u029b\u00d2\3\2\2\2")
        buf.write("\u029c\u029e\t\13\2\2\u029d\u029f\t\f\2\2\u029e\u029d")
        buf.write("\3\2\2\2\u029e\u029f\3\2\2\2\u029f\u02a1\3\2\2\2\u02a0")
        buf.write("\u02a2\5\u00c7d\2\u02a1\u02a0\3\2\2\2\u02a2\u02a3\3\2")
        buf.write("\2\2\u02a3\u02a1\3\2\2\2\u02a3\u02a4\3\2\2\2\u02a4\u00d4")
        buf.write("\3\2\2\2\u02a5\u02aa\7)\2\2\u02a6\u02a9\5\u00ddo\2\u02a7")
        buf.write("\u02a9\n\r\2\2\u02a8\u02a6\3\2\2\2\u02a8\u02a7\3\2\2\2")
        buf.write("\u02a9\u02ac\3\2\2\2\u02aa\u02a8\3\2\2\2\u02aa\u02ab\3")
        buf.write("\2\2\2\u02ab\u02ad\3\2\2\2\u02ac\u02aa\3\2\2\2\u02ad\u02b8")
        buf.write("\7)\2\2\u02ae\u02b3\7$\2\2\u02af\u02b2\5\u00ddo\2\u02b0")
        buf.write("\u02b2\n\16\2\2\u02b1\u02af\3\2\2\2\u02b1\u02b0\3\2\2")
        buf.write("\2\u02b2\u02b5\3\2\2\2\u02b3\u02b1\3\2\2\2\u02b3\u02b4")
        buf.write("\3\2\2\2\u02b4\u02b6\3\2\2\2\u02b5\u02b3\3\2\2\2\u02b6")
        buf.write("\u02b8\7$\2\2\u02b7\u02a5\3\2\2\2\u02b7\u02ae\3\2\2\2")
        buf.write("\u02b8\u00d6\3\2\2\2\u02b9\u02ba\7)\2\2\u02ba\u02bb\7")
        buf.write(")\2\2\u02bb\u02bc\7)\2\2\u02bc\u02c0\3\2\2\2\u02bd\u02bf")
        buf.write("\5\u00d9m\2\u02be\u02bd\3\2\2\2\u02bf\u02c2\3\2\2\2\u02c0")
        buf.write("\u02be\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1\u02c3\3\2\2\2")
        buf.write("\u02c2\u02c0\3\2\2\2\u02c3\u02c4\7)\2\2\u02c4\u02c5\7")
        buf.write(")\2\2\u02c5\u02d4\7)\2\2\u02c6\u02c7\7$\2\2\u02c7\u02c8")
        buf.write("\7$\2\2\u02c8\u02c9\7$\2\2\u02c9\u02cd\3\2\2\2\u02ca\u02cc")
        buf.write("\5\u00d9m\2\u02cb\u02ca\3\2\2\2\u02cc\u02cf\3\2\2\2\u02cd")
        buf.write("\u02cb\3\2\2\2\u02cd\u02ce\3\2\2\2\u02ce\u02d0\3\2\2\2")
        buf.write("\u02cf\u02cd\3\2\2\2\u02d0\u02d1\7$\2\2\u02d1\u02d2\7")
        buf.write("$\2\2\u02d2\u02d4\7$\2\2\u02d3\u02b9\3\2\2\2\u02d3\u02c6")
        buf.write("\3\2\2\2\u02d4\u00d8\3\2\2\2\u02d5\u02d8\5\u00dbn\2\u02d6")
        buf.write("\u02d8\5\u00ddo\2\u02d7\u02d5\3\2\2\2\u02d7\u02d6\3\2")
        buf.write("\2\2\u02d8\u00da\3\2\2\2\u02d9\u02da\n\17\2\2\u02da\u00dc")
        buf.write("\3\2\2\2\u02db\u02dc\7^\2\2\u02dc\u02e0\13\2\2\2\u02dd")
        buf.write("\u02de\7^\2\2\u02de\u02e0\5Q)\2\u02df\u02db\3\2\2\2\u02df")
        buf.write("\u02dd\3\2\2\2\u02e0\u00de\3\2\2\2\u02e1\u02e3\t\20\2")
        buf.write("\2\u02e2\u02e1\3\2\2\2\u02e3\u02e4\3\2\2\2\u02e4\u02e2")
        buf.write("\3\2\2\2\u02e4\u02e5\3\2\2\2\u02e5\u00e0\3\2\2\2\u02e6")
        buf.write("\u02ea\7%\2\2\u02e7\u02e9\n\21\2\2\u02e8\u02e7\3\2\2\2")
        buf.write("\u02e9\u02ec\3\2\2\2\u02ea\u02e8\3\2\2\2\u02ea\u02eb\3")
        buf.write("\2\2\2\u02eb\u00e2\3\2\2\2\u02ec\u02ea\3\2\2\2\u02ed\u02ef")
        buf.write("\7^\2\2\u02ee\u02f0\5\u00dfp\2\u02ef\u02ee\3\2\2\2\u02ef")
        buf.write("\u02f0\3\2\2\2\u02f0\u02f6\3\2\2\2\u02f1\u02f3\7\17\2")
        buf.write("\2\u02f2\u02f1\3\2\2\2\u02f2\u02f3\3\2\2\2\u02f3\u02f4")
        buf.write("\3\2\2\2\u02f4\u02f7\7\f\2\2\u02f5\u02f7\4\16\17\2\u02f6")
        buf.write("\u02f2\3\2\2\2\u02f6\u02f5\3\2\2\2\u02f7\u00e4\3\2\2\2")
        buf.write("*\2\u012c\u0130\u0134\u0138\u013e\u01b1\u01b5\u01b8\u01ba")
        buf.write("\u01c2\u01c9\u01cf\u01d1\u01d8\u01df\u01e6\u01f5\u027b")
        buf.write("\u0282\u0286\u0295\u029a\u029e\u02a3\u02a8\u02aa\u02b1")
        buf.write("\u02b3\u02b7\u02c0\u02cd\u02d3\u02d7\u02df\u02e4\u02ea")
        buf.write("\u02ef\u02f2\u02f6\n\3)\2\3B\3\3C\4\3D\5\3E\6\3F\7\3G")
        buf.write("\b\b\2\2")
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
    VALUE = 13
    NUMBER = 14
    STRING = 15
    BOOLEAN = 16
    INTEGER = 17
    USING = 18
    DEF = 19
    RETURN = 20
    IMPORT = 21
    IF = 22
    ELIF = 23
    ELSE = 24
    WHILE = 25
    FOR = 26
    IN = 27
    OR = 28
    AND = 29
    NOT = 30
    IS = 31
    CLASS = 32
    DEL = 33
    PASS = 34
    CONTINUE = 35
    BREAK = 36
    NONE = 37
    TRUE = 38
    FALSE = 39
    NEWLINE = 40
    NAME = 41
    DECIMAL_INTEGER = 42
    OCT_INTEGER = 43
    HEX_INTEGER = 44
    BIN_INTEGER = 45
    FLOAT_NUMBER = 46
    DOT = 47
    ELLIPSIS = 48
    STAR = 49
    COMMA = 50
    COLON = 51
    SEMI_COLON = 52
    AND_OP = 53
    OR_OP = 54
    XOR_OP = 55
    NOT_OP = 56
    POWER = 57
    LEFT_SHIFT = 58
    RIGHT_SHIFT = 59
    ADD = 60
    MINUS = 61
    DIV = 62
    MOD = 63
    IDIV = 64
    OPEN_PARENTHESIS = 65
    CLOSE_PARENTHESIS = 66
    OPEN_BRACKET = 67
    CLOSE_BRACKET = 68
    OPEN_BRACE = 69
    CLOSE_BRACE = 70
    LESS_THAN = 71
    GREATER_THAN = 72
    EQUALS = 73
    GT_EQ = 74
    LT_EQ = 75
    NOT_EQ_1 = 76
    NOT_EQ_2 = 77
    AT = 78
    ARROW = 79
    ASSIGN = 80
    ADD_ASSIGN = 81
    SUB_ASSIGN = 82
    MULT_ASSIGN = 83
    AT_ASSIGN = 84
    DIV_ASSIGN = 85
    MOD_ASSIGN = 86
    AND_ASSIGN = 87
    OR_ASSIGN = 88
    XOR_ASSIGN = 89
    LEFT_SHIFT_ASSIGN = 90
    RIGHT_SHIFT_ASSIGN = 91
    POWER_ASSIGN = 92
    IDIV_ASSIGN = 93
    SKIP_ = 94
    UNKNOWN_CHAR = 95

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'from'", "'as'", "'../'", "'List['", "'Tuple('", "'Set('", 
            "'Dict{'", "'Function'", "'Bool'", "'Int'", "'Float'", "'String'", 
            "'using'", "'def'", "'return'", "'import'", "'if'", "'elif'", 
            "'else'", "'while'", "'for'", "'in'", "'or'", "'and'", "'not'", 
            "'is'", "'class'", "'del'", "'pass'", "'continue'", "'break'", 
            "'None'", "'True'", "'False'", "'.'", "'...'", "'*'", "','", 
            "':'", "';'", "'&'", "'|'", "'^'", "'~'", "'**'", "'<<'", "'>>'", 
            "'+'", "'-'", "'/'", "'%'", "'//'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "'<'", "'>'", "'=='", "'>='", "'<='", "'<>'", 
            "'!='", "'@'", "'->'", "'='", "'+='", "'-='", "'*='", "'@='", 
            "'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", "'**='", 
            "'//='" ]

    symbolicNames = [ "<INVALID>",
            "VALUE", "NUMBER", "STRING", "BOOLEAN", "INTEGER", "USING", 
            "DEF", "RETURN", "IMPORT", "IF", "ELIF", "ELSE", "WHILE", "FOR", 
            "IN", "OR", "AND", "NOT", "IS", "CLASS", "DEL", "PASS", "CONTINUE", 
            "BREAK", "NONE", "TRUE", "FALSE", "NEWLINE", "NAME", "DECIMAL_INTEGER", 
            "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", 
            "DOT", "ELLIPSIS", "STAR", "COMMA", "COLON", "SEMI_COLON", "AND_OP", 
            "OR_OP", "XOR_OP", "NOT_OP", "POWER", "LEFT_SHIFT", "RIGHT_SHIFT", 
            "ADD", "MINUS", "DIV", "MOD", "IDIV", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", 
            "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", 
            "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", 
            "NOT_EQ_2", "AT", "ARROW", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
            "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", 
            "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", "RIGHT_SHIFT_ASSIGN", 
            "POWER_ASSIGN", "IDIV_ASSIGN", "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "VALUE", "NUMBER", 
                  "STRING", "BOOLEAN", "INTEGER", "USING", "DEF", "RETURN", 
                  "IMPORT", "IF", "ELIF", "ELSE", "WHILE", "FOR", "IN", 
                  "OR", "AND", "NOT", "IS", "CLASS", "DEL", "PASS", "CONTINUE", 
                  "BREAK", "NONE", "TRUE", "FALSE", "NEWLINE", "NAME", "DECIMAL_INTEGER", 
                  "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", 
                  "DOT", "ELLIPSIS", "STAR", "COMMA", "COLON", "SEMI_COLON", 
                  "AND_OP", "OR_OP", "XOR_OP", "NOT_OP", "POWER", "LEFT_SHIFT", 
                  "RIGHT_SHIFT", "ADD", "MINUS", "DIV", "MOD", "IDIV", "OPEN_PARENTHESIS", 
                  "CLOSE_PARENTHESIS", "OPEN_BRACKET", "CLOSE_BRACKET", 
                  "OPEN_BRACE", "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", 
                  "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "AT", 
                  "ARROW", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MULT_ASSIGN", 
                  "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", 
                  "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", "RIGHT_SHIFT_ASSIGN", 
                  "POWER_ASSIGN", "IDIV_ASSIGN", "SKIP_", "UNKNOWN_CHAR", 
                  "NAME_START", "NAME_CONTINUE", "NON_ZERO_DIGIT", "DIGIT", 
                  "OCT_DIGIT", "HEX_DIGIT", "BIN_DIGIT", "INT_PART", "FRACTION", 
                  "EXPONENT", "SHORT_STRING", "LONG_STRING", "LONG_STRING_ITEM", 
                  "LONG_STRING_CHAR", "STRING_ESCAPE_SEQ", "SPACES", "COMMENT", 
                  "LINE_JOINING" ]

    grammarFileName = "Typt.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
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
            actions[39] = self.NEWLINE_action 
            actions[64] = self.OPEN_PARENTHESIS_action 
            actions[65] = self.CLOSE_PARENTHESIS_action 
            actions[66] = self.OPEN_BRACKET_action 
            actions[67] = self.CLOSE_BRACKET_action 
            actions[68] = self.OPEN_BRACE_action 
            actions[69] = self.CLOSE_BRACE_action 
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
                
                
     

    def OPEN_PARENTHESIS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.opened += 1
     

    def CLOSE_PARENTHESIS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.opened -= 1
     

    def OPEN_BRACKET_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.opened += 1
     

    def CLOSE_BRACKET_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.opened -= 1
     

    def OPEN_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.opened += 1
     

    def CLOSE_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.opened -= 1
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[39] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.at_start_of_line()
         


