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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2^")
        buf.write("\u02f6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3(\3)\3)\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3;\3<\3<\3=\3=\3=\3>\3>\3>\3")
        buf.write(">\3>\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3B\3B\3C\3")
        buf.write("C\3C\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3G\3G\3G\3H\3H\3H\3")
        buf.write("H\3I\3I\3I\3I\3I\3I\3J\3J\3J\3J\3J\3J\3J\3K\3K\3K\3K\3")
        buf.write("K\3K\3K\3L\3L\3L\3L\3L\3L\3L\3L\3L\3M\3M\3M\3M\3M\3N\3")
        buf.write("N\3N\3N\3N\3N\3O\3O\3O\3O\3P\3P\3P\3P\3P\3Q\3Q\5Q\u0217")
        buf.write("\nQ\3R\3R\5R\u021b\nR\3S\3S\3S\3S\3S\3S\3S\3S\3S\5S\u0226")
        buf.write("\nS\3T\3T\3T\3T\5T\u022c\nT\3U\3U\3U\5U\u0231\nU\3U\3")
        buf.write("U\5U\u0235\nU\3U\5U\u0238\nU\5U\u023a\nU\3U\3U\3V\3V\7")
        buf.write("V\u0240\nV\fV\16V\u0243\13V\3W\3W\7W\u0247\nW\fW\16W\u024a")
        buf.write("\13W\3W\6W\u024d\nW\rW\16W\u024e\5W\u0251\nW\3X\3X\3X")
        buf.write("\6X\u0256\nX\rX\16X\u0257\3Y\3Y\3Y\6Y\u025d\nY\rY\16Y")
        buf.write("\u025e\3Z\3Z\3Z\6Z\u0264\nZ\rZ\16Z\u0265\3[\3[\3[\3[\3")
        buf.write("[\3[\3[\3[\3[\3[\3[\3[\3[\5[\u0275\n[\3\\\3\\\3\\\5\\")
        buf.write("\u027a\n\\\3\\\3\\\3]\3]\3^\5^\u0281\n^\3_\3_\5_\u0285")
        buf.write("\n_\3`\3`\3a\3a\3b\3b\3c\3c\3d\3d\3e\6e\u0292\ne\re\16")
        buf.write("e\u0293\3f\6f\u0297\nf\rf\16f\u0298\3g\3g\5g\u029d\ng")
        buf.write("\3g\6g\u02a0\ng\rg\16g\u02a1\3h\3h\3h\7h\u02a7\nh\fh\16")
        buf.write("h\u02aa\13h\3h\3h\3h\3h\7h\u02b0\nh\fh\16h\u02b3\13h\3")
        buf.write("h\5h\u02b6\nh\3i\3i\3i\3i\3i\7i\u02bd\ni\fi\16i\u02c0")
        buf.write("\13i\3i\3i\3i\3i\3i\3i\3i\3i\7i\u02ca\ni\fi\16i\u02cd")
        buf.write("\13i\3i\3i\3i\5i\u02d2\ni\3j\3j\5j\u02d6\nj\3k\3k\3l\3")
        buf.write("l\3l\3l\5l\u02de\nl\3m\6m\u02e1\nm\rm\16m\u02e2\3n\3n")
        buf.write("\7n\u02e7\nn\fn\16n\u02ea\13n\3o\3o\5o\u02ee\no\3o\5o")
        buf.write("\u02f1\no\3o\3o\5o\u02f5\no\2\2p\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091")
        buf.write("J\u0093K\u0095L\u0097M\u0099N\u009bO\u009dP\u009fQ\u00a1")
        buf.write("R\u00a3S\u00a5T\u00a7U\u00a9V\u00abW\u00adX\u00afY\u00b1")
        buf.write("Z\u00b3[\u00b5\\\u00b7]\u00b9^\u00bb\2\u00bd\2\u00bf\2")
        buf.write("\u00c1\2\u00c3\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\u00cd")
        buf.write("\2\u00cf\2\u00d1\2\u00d3\2\u00d5\2\u00d7\2\u00d9\2\u00db")
        buf.write("\2\u00dd\2\3\2\22\4\2QQqq\4\2ZZzz\4\2DDdd\5\2C\\aac|\3")
        buf.write("\2\63;\3\2\62;\3\2\629\5\2\62;CHch\3\2\62\63\4\2GGgg\4")
        buf.write("\2--//\6\2\f\f\16\17))^^\6\2\f\f\16\17$$^^\3\2^^\4\2\13")
        buf.write("\13\"\"\4\2\f\f\16\17\2\u030c\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9")
        buf.write("\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2")
        buf.write("\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7")
        buf.write("\3\2\2\2\2\u00b9\3\2\2\2\3\u00df\3\2\2\2\5\u00e5\3\2\2")
        buf.write("\2\7\u00e7\3\2\2\2\t\u00ec\3\2\2\2\13\u00ee\3\2\2\2\r")
        buf.write("\u00f0\3\2\2\2\17\u00f3\3\2\2\2\21\u00f6\3\2\2\2\23\u00f9")
        buf.write("\3\2\2\2\25\u00fc\3\2\2\2\27\u00ff\3\2\2\2\31\u0102\3")
        buf.write("\2\2\2\33\u0105\3\2\2\2\35\u0108\3\2\2\2\37\u010c\3\2")
        buf.write("\2\2!\u0110\3\2\2\2#\u0114\3\2\2\2%\u0118\3\2\2\2\'\u011c")
        buf.write("\3\2\2\2)\u0121\3\2\2\2+\u0127\3\2\2\2-\u0130\3\2\2\2")
        buf.write("/\u0137\3\2\2\2\61\u013a\3\2\2\2\63\u013f\3\2\2\2\65\u0144")
        buf.write("\3\2\2\2\67\u014a\3\2\2\29\u014e\3\2\2\2;\u0151\3\2\2")
        buf.write("\2=\u0155\3\2\2\2?\u0157\3\2\2\2A\u0159\3\2\2\2C\u015c")
        buf.write("\3\2\2\2E\u0165\3\2\2\2G\u016a\3\2\2\2I\u0170\3\2\2\2")
        buf.write("K\u0172\3\2\2\2M\u017f\3\2\2\2O\u0182\3\2\2\2Q\u0186\3")
        buf.write("\2\2\2S\u018a\3\2\2\2U\u018c\3\2\2\2W\u018e\3\2\2\2Y\u0191")
        buf.write("\3\2\2\2[\u0194\3\2\2\2]\u0197\3\2\2\2_\u019a\3\2\2\2")
        buf.write("a\u019d\3\2\2\2c\u019f\3\2\2\2e\u01a1\3\2\2\2g\u01a3\3")
        buf.write("\2\2\2i\u01a6\3\2\2\2k\u01a9\3\2\2\2m\u01ab\3\2\2\2o\u01ad")
        buf.write("\3\2\2\2q\u01af\3\2\2\2s\u01b1\3\2\2\2u\u01b3\3\2\2\2")
        buf.write("w\u01b6\3\2\2\2y\u01b8\3\2\2\2{\u01bb\3\2\2\2}\u01c0\3")
        buf.write("\2\2\2\177\u01c5\3\2\2\2\u0081\u01cb\3\2\2\2\u0083\u01cd")
        buf.write("\3\2\2\2\u0085\u01cf\3\2\2\2\u0087\u01d4\3\2\2\2\u0089")
        buf.write("\u01d6\3\2\2\2\u008b\u01d8\3\2\2\2\u008d\u01da\3\2\2\2")
        buf.write("\u008f\u01df\3\2\2\2\u0091\u01e3\3\2\2\2\u0093\u01e9\3")
        buf.write("\2\2\2\u0095\u01f0\3\2\2\2\u0097\u01f7\3\2\2\2\u0099\u0200")
        buf.write("\3\2\2\2\u009b\u0205\3\2\2\2\u009d\u020b\3\2\2\2\u009f")
        buf.write("\u020f\3\2\2\2\u00a1\u0216\3\2\2\2\u00a3\u021a\3\2\2\2")
        buf.write("\u00a5\u0225\3\2\2\2\u00a7\u022b\3\2\2\2\u00a9\u0239\3")
        buf.write("\2\2\2\u00ab\u023d\3\2\2\2\u00ad\u0250\3\2\2\2\u00af\u0252")
        buf.write("\3\2\2\2\u00b1\u0259\3\2\2\2\u00b3\u0260\3\2\2\2\u00b5")
        buf.write("\u0274\3\2\2\2\u00b7\u0279\3\2\2\2\u00b9\u027d\3\2\2\2")
        buf.write("\u00bb\u0280\3\2\2\2\u00bd\u0284\3\2\2\2\u00bf\u0286\3")
        buf.write("\2\2\2\u00c1\u0288\3\2\2\2\u00c3\u028a\3\2\2\2\u00c5\u028c")
        buf.write("\3\2\2\2\u00c7\u028e\3\2\2\2\u00c9\u0291\3\2\2\2\u00cb")
        buf.write("\u0296\3\2\2\2\u00cd\u029a\3\2\2\2\u00cf\u02b5\3\2\2\2")
        buf.write("\u00d1\u02d1\3\2\2\2\u00d3\u02d5\3\2\2\2\u00d5\u02d7\3")
        buf.write("\2\2\2\u00d7\u02dd\3\2\2\2\u00d9\u02e0\3\2\2\2\u00db\u02e4")
        buf.write("\3\2\2\2\u00dd\u02eb\3\2\2\2\u00df\u00e0\7w\2\2\u00e0")
        buf.write("\u00e1\7u\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3")
        buf.write("\u00e4\7i\2\2\u00e4\4\3\2\2\2\u00e5\u00e6\7<\2\2\u00e6")
        buf.write("\6\3\2\2\2\u00e7\u00e8\7h\2\2\u00e8\u00e9\7t\2\2\u00e9")
        buf.write("\u00ea\7q\2\2\u00ea\u00eb\7o\2\2\u00eb\b\3\2\2\2\u00ec")
        buf.write("\u00ed\7.\2\2\u00ed\n\3\2\2\2\u00ee\u00ef\7?\2\2\u00ef")
        buf.write("\f\3\2\2\2\u00f0\u00f1\7-\2\2\u00f1\u00f2\7?\2\2\u00f2")
        buf.write("\16\3\2\2\2\u00f3\u00f4\7/\2\2\u00f4\u00f5\7?\2\2\u00f5")
        buf.write("\20\3\2\2\2\u00f6\u00f7\7,\2\2\u00f7\u00f8\7?\2\2\u00f8")
        buf.write("\22\3\2\2\2\u00f9\u00fa\7\61\2\2\u00fa\u00fb\7?\2\2\u00fb")
        buf.write("\24\3\2\2\2\u00fc\u00fd\7\'\2\2\u00fd\u00fe\7?\2\2\u00fe")
        buf.write("\26\3\2\2\2\u00ff\u0100\7(\2\2\u0100\u0101\7?\2\2\u0101")
        buf.write("\30\3\2\2\2\u0102\u0103\7~\2\2\u0103\u0104\7?\2\2\u0104")
        buf.write("\32\3\2\2\2\u0105\u0106\7`\2\2\u0106\u0107\7?\2\2\u0107")
        buf.write("\34\3\2\2\2\u0108\u0109\7>\2\2\u0109\u010a\7>\2\2\u010a")
        buf.write("\u010b\7?\2\2\u010b\36\3\2\2\2\u010c\u010d\7@\2\2\u010d")
        buf.write("\u010e\7@\2\2\u010e\u010f\7?\2\2\u010f \3\2\2\2\u0110")
        buf.write("\u0111\7,\2\2\u0111\u0112\7,\2\2\u0112\u0113\7?\2\2\u0113")
        buf.write("\"\3\2\2\2\u0114\u0115\7\61\2\2\u0115\u0116\7\61\2\2\u0116")
        buf.write("\u0117\7?\2\2\u0117$\3\2\2\2\u0118\u0119\7f\2\2\u0119")
        buf.write("\u011a\7g\2\2\u011a\u011b\7n\2\2\u011b&\3\2\2\2\u011c")
        buf.write("\u011d\7r\2\2\u011d\u011e\7c\2\2\u011e\u011f\7u\2\2\u011f")
        buf.write("\u0120\7u\2\2\u0120(\3\2\2\2\u0121\u0122\7d\2\2\u0122")
        buf.write("\u0123\7t\2\2\u0123\u0124\7g\2\2\u0124\u0125\7c\2\2\u0125")
        buf.write("\u0126\7m\2\2\u0126*\3\2\2\2\u0127\u0128\7e\2\2\u0128")
        buf.write("\u0129\7q\2\2\u0129\u012a\7p\2\2\u012a\u012b\7v\2\2\u012b")
        buf.write("\u012c\7k\2\2\u012c\u012d\7p\2\2\u012d\u012e\7w\2\2\u012e")
        buf.write("\u012f\7g\2\2\u012f,\3\2\2\2\u0130\u0131\7t\2\2\u0131")
        buf.write("\u0132\7g\2\2\u0132\u0133\7v\2\2\u0133\u0134\7w\2\2\u0134")
        buf.write("\u0135\7t\2\2\u0135\u0136\7p\2\2\u0136.\3\2\2\2\u0137")
        buf.write("\u0138\7k\2\2\u0138\u0139\7h\2\2\u0139\60\3\2\2\2\u013a")
        buf.write("\u013b\7g\2\2\u013b\u013c\7n\2\2\u013c\u013d\7k\2\2\u013d")
        buf.write("\u013e\7h\2\2\u013e\62\3\2\2\2\u013f\u0140\7g\2\2\u0140")
        buf.write("\u0141\7n\2\2\u0141\u0142\7u\2\2\u0142\u0143\7g\2\2\u0143")
        buf.write("\64\3\2\2\2\u0144\u0145\7y\2\2\u0145\u0146\7j\2\2\u0146")
        buf.write("\u0147\7k\2\2\u0147\u0148\7n\2\2\u0148\u0149\7g\2\2\u0149")
        buf.write("\66\3\2\2\2\u014a\u014b\7h\2\2\u014b\u014c\7q\2\2\u014c")
        buf.write("\u014d\7t\2\2\u014d8\3\2\2\2\u014e\u014f\7k\2\2\u014f")
        buf.write("\u0150\7p\2\2\u0150:\3\2\2\2\u0151\u0152\7f\2\2\u0152")
        buf.write("\u0153\7g\2\2\u0153\u0154\7h\2\2\u0154<\3\2\2\2\u0155")
        buf.write("\u0156\7*\2\2\u0156>\3\2\2\2\u0157\u0158\7+\2\2\u0158")
        buf.write("@\3\2\2\2\u0159\u015a\7/\2\2\u015a\u015b\7@\2\2\u015b")
        buf.write("B\3\2\2\2\u015c\u015d\7a\2\2\u015d\u015e\7a\2\2\u015e")
        buf.write("\u015f\7k\2\2\u015f\u0160\7p\2\2\u0160\u0161\7k\2\2\u0161")
        buf.write("\u0162\7v\2\2\u0162\u0163\7a\2\2\u0163\u0164\7a\2\2\u0164")
        buf.write("D\3\2\2\2\u0165\u0166\7u\2\2\u0166\u0167\7g\2\2\u0167")
        buf.write("\u0168\7n\2\2\u0168\u0169\7h\2\2\u0169F\3\2\2\2\u016a")
        buf.write("\u016b\7e\2\2\u016b\u016c\7n\2\2\u016c\u016d\7c\2\2\u016d")
        buf.write("\u016e\7u\2\2\u016e\u016f\7u\2\2\u016fH\3\2\2\2\u0170")
        buf.write("\u0171\7B\2\2\u0171J\3\2\2\2\u0172\u0173\7u\2\2\u0173")
        buf.write("\u0174\7v\2\2\u0174\u0175\7c\2\2\u0175\u0176\7v\2\2\u0176")
        buf.write("\u0177\7k\2\2\u0177\u0178\7e\2\2\u0178\u0179\7o\2\2\u0179")
        buf.write("\u017a\7g\2\2\u017a\u017b\7v\2\2\u017b\u017c\7j\2\2\u017c")
        buf.write("\u017d\7q\2\2\u017d\u017e\7f\2\2\u017eL\3\2\2\2\u017f")
        buf.write("\u0180\7q\2\2\u0180\u0181\7t\2\2\u0181N\3\2\2\2\u0182")
        buf.write("\u0183\7c\2\2\u0183\u0184\7p\2\2\u0184\u0185\7f\2\2\u0185")
        buf.write("P\3\2\2\2\u0186\u0187\7p\2\2\u0187\u0188\7q\2\2\u0188")
        buf.write("\u0189\7v\2\2\u0189R\3\2\2\2\u018a\u018b\7>\2\2\u018b")
        buf.write("T\3\2\2\2\u018c\u018d\7@\2\2\u018dV\3\2\2\2\u018e\u018f")
        buf.write("\7?\2\2\u018f\u0190\7?\2\2\u0190X\3\2\2\2\u0191\u0192")
        buf.write("\7@\2\2\u0192\u0193\7?\2\2\u0193Z\3\2\2\2\u0194\u0195")
        buf.write("\7>\2\2\u0195\u0196\7?\2\2\u0196\\\3\2\2\2\u0197\u0198")
        buf.write("\7#\2\2\u0198\u0199\7?\2\2\u0199^\3\2\2\2\u019a\u019b")
        buf.write("\7k\2\2\u019b\u019c\7u\2\2\u019c`\3\2\2\2\u019d\u019e")
        buf.write("\7~\2\2\u019eb\3\2\2\2\u019f\u01a0\7`\2\2\u01a0d\3\2\2")
        buf.write("\2\u01a1\u01a2\7(\2\2\u01a2f\3\2\2\2\u01a3\u01a4\7>\2")
        buf.write("\2\u01a4\u01a5\7>\2\2\u01a5h\3\2\2\2\u01a6\u01a7\7@\2")
        buf.write("\2\u01a7\u01a8\7@\2\2\u01a8j\3\2\2\2\u01a9\u01aa\7-\2")
        buf.write("\2\u01aal\3\2\2\2\u01ab\u01ac\7/\2\2\u01acn\3\2\2\2\u01ad")
        buf.write("\u01ae\7,\2\2\u01aep\3\2\2\2\u01af\u01b0\7\61\2\2\u01b0")
        buf.write("r\3\2\2\2\u01b1\u01b2\7\'\2\2\u01b2t\3\2\2\2\u01b3\u01b4")
        buf.write("\7\61\2\2\u01b4\u01b5\7\61\2\2\u01b5v\3\2\2\2\u01b6\u01b7")
        buf.write("\7\u0080\2\2\u01b7x\3\2\2\2\u01b8\u01b9\7,\2\2\u01b9\u01ba")
        buf.write("\7,\2\2\u01baz\3\2\2\2\u01bb\u01bc\7P\2\2\u01bc\u01bd")
        buf.write("\7q\2\2\u01bd\u01be\7p\2\2\u01be\u01bf\7g\2\2\u01bf|\3")
        buf.write("\2\2\2\u01c0\u01c1\7V\2\2\u01c1\u01c2\7t\2\2\u01c2\u01c3")
        buf.write("\7w\2\2\u01c3\u01c4\7g\2\2\u01c4~\3\2\2\2\u01c5\u01c6")
        buf.write("\7H\2\2\u01c6\u01c7\7c\2\2\u01c7\u01c8\7n\2\2\u01c8\u01c9")
        buf.write("\7u\2\2\u01c9\u01ca\7g\2\2\u01ca\u0080\3\2\2\2\u01cb\u01cc")
        buf.write("\7]\2\2\u01cc\u0082\3\2\2\2\u01cd\u01ce\7_\2\2\u01ce\u0084")
        buf.write("\3\2\2\2\u01cf\u01d0\7U\2\2\u01d0\u01d1\7g\2\2\u01d1\u01d2")
        buf.write("\7v\2\2\u01d2\u01d3\7*\2\2\u01d3\u0086\3\2\2\2\u01d4\u01d5")
        buf.write("\7}\2\2\u01d5\u0088\3\2\2\2\u01d6\u01d7\7\177\2\2\u01d7")
        buf.write("\u008a\3\2\2\2\u01d8\u01d9\7\60\2\2\u01d9\u008c\3\2\2")
        buf.write("\2\u01da\u01db\7D\2\2\u01db\u01dc\7q\2\2\u01dc\u01dd\7")
        buf.write("q\2\2\u01dd\u01de\7n\2\2\u01de\u008e\3\2\2\2\u01df\u01e0")
        buf.write("\7K\2\2\u01e0\u01e1\7p\2\2\u01e1\u01e2\7v\2\2\u01e2\u0090")
        buf.write("\3\2\2\2\u01e3\u01e4\7H\2\2\u01e4\u01e5\7n\2\2\u01e5\u01e6")
        buf.write("\7q\2\2\u01e6\u01e7\7c\2\2\u01e7\u01e8\7v\2\2\u01e8\u0092")
        buf.write("\3\2\2\2\u01e9\u01ea\7U\2\2\u01ea\u01eb\7v\2\2\u01eb\u01ec")
        buf.write("\7t\2\2\u01ec\u01ed\7k\2\2\u01ed\u01ee\7p\2\2\u01ee\u01ef")
        buf.write("\7i\2\2\u01ef\u0094\3\2\2\2\u01f0\u01f1\7Q\2\2\u01f1\u01f2")
        buf.write("\7d\2\2\u01f2\u01f3\7l\2\2\u01f3\u01f4\7g\2\2\u01f4\u01f5")
        buf.write("\7e\2\2\u01f5\u01f6\7v\2\2\u01f6\u0096\3\2\2\2\u01f7\u01f8")
        buf.write("\7H\2\2\u01f8\u01f9\7w\2\2\u01f9\u01fa\7p\2\2\u01fa\u01fb")
        buf.write("\7e\2\2\u01fb\u01fc\7v\2\2\u01fc\u01fd\7k\2\2\u01fd\u01fe")
        buf.write("\7q\2\2\u01fe\u01ff\7p\2\2\u01ff\u0098\3\2\2\2\u0200\u0201")
        buf.write("\7N\2\2\u0201\u0202\7k\2\2\u0202\u0203\7u\2\2\u0203\u0204")
        buf.write("\7v\2\2\u0204\u009a\3\2\2\2\u0205\u0206\7V\2\2\u0206\u0207")
        buf.write("\7w\2\2\u0207\u0208\7r\2\2\u0208\u0209\7n\2\2\u0209\u020a")
        buf.write("\7g\2\2\u020a\u009c\3\2\2\2\u020b\u020c\7U\2\2\u020c\u020d")
        buf.write("\7g\2\2\u020d\u020e\7v\2\2\u020e\u009e\3\2\2\2\u020f\u0210")
        buf.write("\7F\2\2\u0210\u0211\7k\2\2\u0211\u0212\7e\2\2\u0212\u0213")
        buf.write("\7v\2\2\u0213\u00a0\3\2\2\2\u0214\u0217\5\u00a7T\2\u0215")
        buf.write("\u0217\5\u00b5[\2\u0216\u0214\3\2\2\2\u0216\u0215\3\2")
        buf.write("\2\2\u0217\u00a2\3\2\2\2\u0218\u021b\5\u00cfh\2\u0219")
        buf.write("\u021b\5\u00d1i\2\u021a\u0218\3\2\2\2\u021a\u0219\3\2")
        buf.write("\2\2\u021b\u00a4\3\2\2\2\u021c\u021d\7V\2\2\u021d\u021e")
        buf.write("\7t\2\2\u021e\u021f\7w\2\2\u021f\u0226\7g\2\2\u0220\u0221")
        buf.write("\7H\2\2\u0221\u0222\7c\2\2\u0222\u0223\7n\2\2\u0223\u0224")
        buf.write("\7u\2\2\u0224\u0226\7g\2\2\u0225\u021c\3\2\2\2\u0225\u0220")
        buf.write("\3\2\2\2\u0226\u00a6\3\2\2\2\u0227\u022c\5\u00adW\2\u0228")
        buf.write("\u022c\5\u00afX\2\u0229\u022c\5\u00b1Y\2\u022a\u022c\5")
        buf.write("\u00b3Z\2\u022b\u0227\3\2\2\2\u022b\u0228\3\2\2\2\u022b")
        buf.write("\u0229\3\2\2\2\u022b\u022a\3\2\2\2\u022c\u00a8\3\2\2\2")
        buf.write("\u022d\u022e\6U\2\2\u022e\u023a\5\u00d9m\2\u022f\u0231")
        buf.write("\7\17\2\2\u0230\u022f\3\2\2\2\u0230\u0231\3\2\2\2\u0231")
        buf.write("\u0232\3\2\2\2\u0232\u0235\7\f\2\2\u0233\u0235\4\16\17")
        buf.write("\2\u0234\u0230\3\2\2\2\u0234\u0233\3\2\2\2\u0235\u0237")
        buf.write("\3\2\2\2\u0236\u0238\5\u00d9m\2\u0237\u0236\3\2\2\2\u0237")
        buf.write("\u0238\3\2\2\2\u0238\u023a\3\2\2\2\u0239\u022d\3\2\2\2")
        buf.write("\u0239\u0234\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u023c\b")
        buf.write("U\2\2\u023c\u00aa\3\2\2\2\u023d\u0241\5\u00bb^\2\u023e")
        buf.write("\u0240\5\u00bd_\2\u023f\u023e\3\2\2\2\u0240\u0243\3\2")
        buf.write("\2\2\u0241\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u00ac")
        buf.write("\3\2\2\2\u0243\u0241\3\2\2\2\u0244\u0248\5\u00bf`\2\u0245")
        buf.write("\u0247\5\u00c1a\2\u0246\u0245\3\2\2\2\u0247\u024a\3\2")
        buf.write("\2\2\u0248\u0246\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u0251")
        buf.write("\3\2\2\2\u024a\u0248\3\2\2\2\u024b\u024d\7\62\2\2\u024c")
        buf.write("\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u024c\3\2\2\2")
        buf.write("\u024e\u024f\3\2\2\2\u024f\u0251\3\2\2\2\u0250\u0244\3")
        buf.write("\2\2\2\u0250\u024c\3\2\2\2\u0251\u00ae\3\2\2\2\u0252\u0253")
        buf.write("\7\62\2\2\u0253\u0255\t\2\2\2\u0254\u0256\5\u00c3b\2\u0255")
        buf.write("\u0254\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0255\3\2\2\2")
        buf.write("\u0257\u0258\3\2\2\2\u0258\u00b0\3\2\2\2\u0259\u025a\7")
        buf.write("\62\2\2\u025a\u025c\t\3\2\2\u025b\u025d\5\u00c5c\2\u025c")
        buf.write("\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u025c\3\2\2\2")
        buf.write("\u025e\u025f\3\2\2\2\u025f\u00b2\3\2\2\2\u0260\u0261\7")
        buf.write("\62\2\2\u0261\u0263\t\4\2\2\u0262\u0264\5\u00c7d\2\u0263")
        buf.write("\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0263\3\2\2\2")
        buf.write("\u0265\u0266\3\2\2\2\u0266\u00b4\3\2\2\2\u0267\u0268\5")
        buf.write("\u00c9e\2\u0268\u0269\7\60\2\2\u0269\u026a\5\u00cbf\2")
        buf.write("\u026a\u0275\3\2\2\2\u026b\u026c\5\u00c9e\2\u026c\u026d")
        buf.write("\5\u00cdg\2\u026d\u0275\3\2\2\2\u026e\u026f\5\u00c9e\2")
        buf.write("\u026f\u0270\7\60\2\2\u0270\u0271\5\u00cbf\2\u0271\u0272")
        buf.write("\3\2\2\2\u0272\u0273\5\u00cdg\2\u0273\u0275\3\2\2\2\u0274")
        buf.write("\u0267\3\2\2\2\u0274\u026b\3\2\2\2\u0274\u026e\3\2\2\2")
        buf.write("\u0275\u00b6\3\2\2\2\u0276\u027a\5\u00d9m\2\u0277\u027a")
        buf.write("\5\u00dbn\2\u0278\u027a\5\u00ddo\2\u0279\u0276\3\2\2\2")
        buf.write("\u0279\u0277\3\2\2\2\u0279\u0278\3\2\2\2\u027a\u027b\3")
        buf.write("\2\2\2\u027b\u027c\b\\\3\2\u027c\u00b8\3\2\2\2\u027d\u027e")
        buf.write("\13\2\2\2\u027e\u00ba\3\2\2\2\u027f\u0281\t\5\2\2\u0280")
        buf.write("\u027f\3\2\2\2\u0281\u00bc\3\2\2\2\u0282\u0285\5\u00bb")
        buf.write("^\2\u0283\u0285\5\u00c1a\2\u0284\u0282\3\2\2\2\u0284\u0283")
        buf.write("\3\2\2\2\u0285\u00be\3\2\2\2\u0286\u0287\t\6\2\2\u0287")
        buf.write("\u00c0\3\2\2\2\u0288\u0289\t\7\2\2\u0289\u00c2\3\2\2\2")
        buf.write("\u028a\u028b\t\b\2\2\u028b\u00c4\3\2\2\2\u028c\u028d\t")
        buf.write("\t\2\2\u028d\u00c6\3\2\2\2\u028e\u028f\t\n\2\2\u028f\u00c8")
        buf.write("\3\2\2\2\u0290\u0292\5\u00c1a\2\u0291\u0290\3\2\2\2\u0292")
        buf.write("\u0293\3\2\2\2\u0293\u0291\3\2\2\2\u0293\u0294\3\2\2\2")
        buf.write("\u0294\u00ca\3\2\2\2\u0295\u0297\5\u00c1a\2\u0296\u0295")
        buf.write("\3\2\2\2\u0297\u0298\3\2\2\2\u0298\u0296\3\2\2\2\u0298")
        buf.write("\u0299\3\2\2\2\u0299\u00cc\3\2\2\2\u029a\u029c\t\13\2")
        buf.write("\2\u029b\u029d\t\f\2\2\u029c\u029b\3\2\2\2\u029c\u029d")
        buf.write("\3\2\2\2\u029d\u029f\3\2\2\2\u029e\u02a0\5\u00c1a\2\u029f")
        buf.write("\u029e\3\2\2\2\u02a0\u02a1\3\2\2\2\u02a1\u029f\3\2\2\2")
        buf.write("\u02a1\u02a2\3\2\2\2\u02a2\u00ce\3\2\2\2\u02a3\u02a8\7")
        buf.write(")\2\2\u02a4\u02a7\5\u00d7l\2\u02a5\u02a7\n\r\2\2\u02a6")
        buf.write("\u02a4\3\2\2\2\u02a6\u02a5\3\2\2\2\u02a7\u02aa\3\2\2\2")
        buf.write("\u02a8\u02a6\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02ab\3")
        buf.write("\2\2\2\u02aa\u02a8\3\2\2\2\u02ab\u02b6\7)\2\2\u02ac\u02b1")
        buf.write("\7$\2\2\u02ad\u02b0\5\u00d7l\2\u02ae\u02b0\n\16\2\2\u02af")
        buf.write("\u02ad\3\2\2\2\u02af\u02ae\3\2\2\2\u02b0\u02b3\3\2\2\2")
        buf.write("\u02b1\u02af\3\2\2\2\u02b1\u02b2\3\2\2\2\u02b2\u02b4\3")
        buf.write("\2\2\2\u02b3\u02b1\3\2\2\2\u02b4\u02b6\7$\2\2\u02b5\u02a3")
        buf.write("\3\2\2\2\u02b5\u02ac\3\2\2\2\u02b6\u00d0\3\2\2\2\u02b7")
        buf.write("\u02b8\7)\2\2\u02b8\u02b9\7)\2\2\u02b9\u02ba\7)\2\2\u02ba")
        buf.write("\u02be\3\2\2\2\u02bb\u02bd\5\u00d3j\2\u02bc\u02bb\3\2")
        buf.write("\2\2\u02bd\u02c0\3\2\2\2\u02be\u02bc\3\2\2\2\u02be\u02bf")
        buf.write("\3\2\2\2\u02bf\u02c1\3\2\2\2\u02c0\u02be\3\2\2\2\u02c1")
        buf.write("\u02c2\7)\2\2\u02c2\u02c3\7)\2\2\u02c3\u02d2\7)\2\2\u02c4")
        buf.write("\u02c5\7$\2\2\u02c5\u02c6\7$\2\2\u02c6\u02c7\7$\2\2\u02c7")
        buf.write("\u02cb\3\2\2\2\u02c8\u02ca\5\u00d3j\2\u02c9\u02c8\3\2")
        buf.write("\2\2\u02ca\u02cd\3\2\2\2\u02cb\u02c9\3\2\2\2\u02cb\u02cc")
        buf.write("\3\2\2\2\u02cc\u02ce\3\2\2\2\u02cd\u02cb\3\2\2\2\u02ce")
        buf.write("\u02cf\7$\2\2\u02cf\u02d0\7$\2\2\u02d0\u02d2\7$\2\2\u02d1")
        buf.write("\u02b7\3\2\2\2\u02d1\u02c4\3\2\2\2\u02d2\u00d2\3\2\2\2")
        buf.write("\u02d3\u02d6\5\u00d5k\2\u02d4\u02d6\5\u00d7l\2\u02d5\u02d3")
        buf.write("\3\2\2\2\u02d5\u02d4\3\2\2\2\u02d6\u00d4\3\2\2\2\u02d7")
        buf.write("\u02d8\n\17\2\2\u02d8\u00d6\3\2\2\2\u02d9\u02da\7^\2\2")
        buf.write("\u02da\u02de\13\2\2\2\u02db\u02dc\7^\2\2\u02dc\u02de\5")
        buf.write("\u00a9U\2\u02dd\u02d9\3\2\2\2\u02dd\u02db\3\2\2\2\u02de")
        buf.write("\u00d8\3\2\2\2\u02df\u02e1\t\20\2\2\u02e0\u02df\3\2\2")
        buf.write("\2\u02e1\u02e2\3\2\2\2\u02e2\u02e0\3\2\2\2\u02e2\u02e3")
        buf.write("\3\2\2\2\u02e3\u00da\3\2\2\2\u02e4\u02e8\7%\2\2\u02e5")
        buf.write("\u02e7\n\21\2\2\u02e6\u02e5\3\2\2\2\u02e7\u02ea\3\2\2")
        buf.write("\2\u02e8\u02e6\3\2\2\2\u02e8\u02e9\3\2\2\2\u02e9\u00dc")
        buf.write("\3\2\2\2\u02ea\u02e8\3\2\2\2\u02eb\u02ed\7^\2\2\u02ec")
        buf.write("\u02ee\5\u00d9m\2\u02ed\u02ec\3\2\2\2\u02ed\u02ee\3\2")
        buf.write("\2\2\u02ee\u02f4\3\2\2\2\u02ef\u02f1\7\17\2\2\u02f0\u02ef")
        buf.write("\3\2\2\2\u02f0\u02f1\3\2\2\2\u02f1\u02f2\3\2\2\2\u02f2")
        buf.write("\u02f5\7\f\2\2\u02f3\u02f5\4\16\17\2\u02f4\u02f0\3\2\2")
        buf.write("\2\u02f4\u02f3\3\2\2\2\u02f5\u00de\3\2\2\2)\2\u0216\u021a")
        buf.write("\u0225\u022b\u0230\u0234\u0237\u0239\u0241\u0248\u024e")
        buf.write("\u0250\u0257\u025e\u0265\u0274\u0279\u0280\u0284\u0293")
        buf.write("\u0298\u029c\u02a1\u02a6\u02a8\u02af\u02b1\u02b5\u02be")
        buf.write("\u02cb\u02d1\u02d5\u02dd\u02e2\u02e8\u02ed\u02f0\u02f4")
        buf.write("\4\3U\2\b\2\2")
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
    NUMBER = 80
    STRING = 81
    BOOLEAN = 82
    INTEGER = 83
    NEWLINE = 84
    NAME = 85
    DECIMAL_INTEGER = 86
    OCT_INTEGER = 87
    HEX_INTEGER = 88
    BIN_INTEGER = 89
    FLOAT_NUMBER = 90
    SKIP_ = 91
    UNKNOWN_CHAR = 92

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
            "'None'", "'True'", "'False'", "'['", "']'", "'Set('", "'{'", 
            "'}'", "'.'", "'Bool'", "'Int'", "'Float'", "'String'", "'Object'", 
            "'Function'", "'List'", "'Tuple'", "'Set'", "'Dict'" ]

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
                  "T__74", "T__75", "T__76", "T__77", "T__78", "NUMBER", 
                  "STRING", "BOOLEAN", "INTEGER", "NEWLINE", "NAME", "DECIMAL_INTEGER", 
                  "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", 
                  "SKIP_", "UNKNOWN_CHAR", "NAME_START", "NAME_CONTINUE", 
                  "NON_ZERO_DIGIT", "DIGIT", "OCT_DIGIT", "HEX_DIGIT", "BIN_DIGIT", 
                  "INT_PART", "FRACTION", "EXPONENT", "SHORT_STRING", "LONG_STRING", 
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
            actions[83] = self.NEWLINE_action 
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
            preds[83] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.at_start_of_line()
         


