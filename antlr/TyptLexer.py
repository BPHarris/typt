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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2]")
        buf.write("\u02ef\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3&\3&")
        buf.write("\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3(\3)\3)\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3")
        buf.write(".\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3;\3<\3<\3=\3=\3=\3>\3>\3>\3>\3")
        buf.write(">\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3B\3B\3C\3C\3")
        buf.write("D\3D\3D\3D\3D\3E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3G\3G\3G\3")
        buf.write("G\3G\3G\3G\3H\3H\3H\3H\3H\3H\3H\3I\3I\3J\3J\3K\3K\3K\3")
        buf.write("K\3K\3K\3K\3K\3K\3L\3L\3L\3L\3L\3M\3M\3M\3M\3M\3M\3N\3")
        buf.write("N\3N\3N\3O\3O\3O\3O\3O\3P\3P\5P\u0210\nP\3Q\3Q\5Q\u0214")
        buf.write("\nQ\3R\3R\3R\3R\3R\3R\3R\3R\3R\5R\u021f\nR\3S\3S\3S\3")
        buf.write("S\5S\u0225\nS\3T\3T\3T\5T\u022a\nT\3T\3T\5T\u022e\nT\3")
        buf.write("T\5T\u0231\nT\5T\u0233\nT\3T\3T\3U\3U\7U\u0239\nU\fU\16")
        buf.write("U\u023c\13U\3V\3V\7V\u0240\nV\fV\16V\u0243\13V\3V\6V\u0246")
        buf.write("\nV\rV\16V\u0247\5V\u024a\nV\3W\3W\3W\6W\u024f\nW\rW\16")
        buf.write("W\u0250\3X\3X\3X\6X\u0256\nX\rX\16X\u0257\3Y\3Y\3Y\6Y")
        buf.write("\u025d\nY\rY\16Y\u025e\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3")
        buf.write("Z\3Z\3Z\5Z\u026e\nZ\3[\3[\3[\5[\u0273\n[\3[\3[\3\\\3\\")
        buf.write("\3]\5]\u027a\n]\3^\3^\5^\u027e\n^\3_\3_\3`\3`\3a\3a\3")
        buf.write("b\3b\3c\3c\3d\6d\u028b\nd\rd\16d\u028c\3e\6e\u0290\ne")
        buf.write("\re\16e\u0291\3f\3f\5f\u0296\nf\3f\6f\u0299\nf\rf\16f")
        buf.write("\u029a\3g\3g\3g\7g\u02a0\ng\fg\16g\u02a3\13g\3g\3g\3g")
        buf.write("\3g\7g\u02a9\ng\fg\16g\u02ac\13g\3g\5g\u02af\ng\3h\3h")
        buf.write("\3h\3h\3h\7h\u02b6\nh\fh\16h\u02b9\13h\3h\3h\3h\3h\3h")
        buf.write("\3h\3h\3h\7h\u02c3\nh\fh\16h\u02c6\13h\3h\3h\3h\5h\u02cb")
        buf.write("\nh\3i\3i\5i\u02cf\ni\3j\3j\3k\3k\3k\3k\5k\u02d7\nk\3")
        buf.write("l\6l\u02da\nl\rl\16l\u02db\3m\3m\7m\u02e0\nm\fm\16m\u02e3")
        buf.write("\13m\3n\3n\5n\u02e7\nn\3n\5n\u02ea\nn\3n\3n\5n\u02ee\n")
        buf.write("n\2\2o\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F")
        buf.write("\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097M\u0099")
        buf.write("N\u009bO\u009dP\u009fQ\u00a1R\u00a3S\u00a5T\u00a7U\u00a9")
        buf.write("V\u00abW\u00adX\u00afY\u00b1Z\u00b3[\u00b5\\\u00b7]\u00b9")
        buf.write("\2\u00bb\2\u00bd\2\u00bf\2\u00c1\2\u00c3\2\u00c5\2\u00c7")
        buf.write("\2\u00c9\2\u00cb\2\u00cd\2\u00cf\2\u00d1\2\u00d3\2\u00d5")
        buf.write("\2\u00d7\2\u00d9\2\u00db\2\3\2\22\4\2QQqq\4\2ZZzz\4\2")
        buf.write("DDdd\5\2C\\aac|\3\2\63;\3\2\62;\3\2\629\5\2\62;CHch\3")
        buf.write("\2\62\63\4\2GGgg\4\2--//\6\2\f\f\16\17))^^\6\2\f\f\16")
        buf.write("\17$$^^\3\2^^\4\2\13\13\"\"\4\2\f\f\16\17\2\u0305\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
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
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\3\u00dd\3\2\2\2\5\u00e3")
        buf.write("\3\2\2\2\7\u00e5\3\2\2\2\t\u00ea\3\2\2\2\13\u00ec\3\2")
        buf.write("\2\2\r\u00ee\3\2\2\2\17\u00f1\3\2\2\2\21\u00f4\3\2\2\2")
        buf.write("\23\u00f7\3\2\2\2\25\u00fa\3\2\2\2\27\u00fd\3\2\2\2\31")
        buf.write("\u0100\3\2\2\2\33\u0103\3\2\2\2\35\u0106\3\2\2\2\37\u010a")
        buf.write("\3\2\2\2!\u010e\3\2\2\2#\u0112\3\2\2\2%\u0116\3\2\2\2")
        buf.write("\'\u011a\3\2\2\2)\u011f\3\2\2\2+\u0125\3\2\2\2-\u012e")
        buf.write("\3\2\2\2/\u0135\3\2\2\2\61\u0138\3\2\2\2\63\u013d\3\2")
        buf.write("\2\2\65\u0142\3\2\2\2\67\u0148\3\2\2\29\u014c\3\2\2\2")
        buf.write(";\u014f\3\2\2\2=\u0153\3\2\2\2?\u0155\3\2\2\2A\u0157\3")
        buf.write("\2\2\2C\u015a\3\2\2\2E\u0163\3\2\2\2G\u0168\3\2\2\2I\u016e")
        buf.write("\3\2\2\2K\u0170\3\2\2\2M\u017d\3\2\2\2O\u0180\3\2\2\2")
        buf.write("Q\u0184\3\2\2\2S\u0188\3\2\2\2U\u018a\3\2\2\2W\u018c\3")
        buf.write("\2\2\2Y\u018f\3\2\2\2[\u0192\3\2\2\2]\u0195\3\2\2\2_\u0198")
        buf.write("\3\2\2\2a\u019b\3\2\2\2c\u019d\3\2\2\2e\u019f\3\2\2\2")
        buf.write("g\u01a1\3\2\2\2i\u01a4\3\2\2\2k\u01a7\3\2\2\2m\u01a9\3")
        buf.write("\2\2\2o\u01ab\3\2\2\2q\u01ad\3\2\2\2s\u01af\3\2\2\2u\u01b1")
        buf.write("\3\2\2\2w\u01b4\3\2\2\2y\u01b6\3\2\2\2{\u01b9\3\2\2\2")
        buf.write("}\u01be\3\2\2\2\177\u01c3\3\2\2\2\u0081\u01c9\3\2\2\2")
        buf.write("\u0083\u01cb\3\2\2\2\u0085\u01cd\3\2\2\2\u0087\u01cf\3")
        buf.write("\2\2\2\u0089\u01d4\3\2\2\2\u008b\u01d8\3\2\2\2\u008d\u01de")
        buf.write("\3\2\2\2\u008f\u01e5\3\2\2\2\u0091\u01ec\3\2\2\2\u0093")
        buf.write("\u01ee\3\2\2\2\u0095\u01f0\3\2\2\2\u0097\u01f9\3\2\2\2")
        buf.write("\u0099\u01fe\3\2\2\2\u009b\u0204\3\2\2\2\u009d\u0208\3")
        buf.write("\2\2\2\u009f\u020f\3\2\2\2\u00a1\u0213\3\2\2\2\u00a3\u021e")
        buf.write("\3\2\2\2\u00a5\u0224\3\2\2\2\u00a7\u0232\3\2\2\2\u00a9")
        buf.write("\u0236\3\2\2\2\u00ab\u0249\3\2\2\2\u00ad\u024b\3\2\2\2")
        buf.write("\u00af\u0252\3\2\2\2\u00b1\u0259\3\2\2\2\u00b3\u026d\3")
        buf.write("\2\2\2\u00b5\u0272\3\2\2\2\u00b7\u0276\3\2\2\2\u00b9\u0279")
        buf.write("\3\2\2\2\u00bb\u027d\3\2\2\2\u00bd\u027f\3\2\2\2\u00bf")
        buf.write("\u0281\3\2\2\2\u00c1\u0283\3\2\2\2\u00c3\u0285\3\2\2\2")
        buf.write("\u00c5\u0287\3\2\2\2\u00c7\u028a\3\2\2\2\u00c9\u028f\3")
        buf.write("\2\2\2\u00cb\u0293\3\2\2\2\u00cd\u02ae\3\2\2\2\u00cf\u02ca")
        buf.write("\3\2\2\2\u00d1\u02ce\3\2\2\2\u00d3\u02d0\3\2\2\2\u00d5")
        buf.write("\u02d6\3\2\2\2\u00d7\u02d9\3\2\2\2\u00d9\u02dd\3\2\2\2")
        buf.write("\u00db\u02e4\3\2\2\2\u00dd\u00de\7w\2\2\u00de\u00df\7")
        buf.write("u\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2")
        buf.write("\7i\2\2\u00e2\4\3\2\2\2\u00e3\u00e4\7<\2\2\u00e4\6\3\2")
        buf.write("\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7o\2\2\u00e9\b\3\2\2\2\u00ea\u00eb")
        buf.write("\7.\2\2\u00eb\n\3\2\2\2\u00ec\u00ed\7?\2\2\u00ed\f\3\2")
        buf.write("\2\2\u00ee\u00ef\7-\2\2\u00ef\u00f0\7?\2\2\u00f0\16\3")
        buf.write("\2\2\2\u00f1\u00f2\7/\2\2\u00f2\u00f3\7?\2\2\u00f3\20")
        buf.write("\3\2\2\2\u00f4\u00f5\7,\2\2\u00f5\u00f6\7?\2\2\u00f6\22")
        buf.write("\3\2\2\2\u00f7\u00f8\7\61\2\2\u00f8\u00f9\7?\2\2\u00f9")
        buf.write("\24\3\2\2\2\u00fa\u00fb\7\'\2\2\u00fb\u00fc\7?\2\2\u00fc")
        buf.write("\26\3\2\2\2\u00fd\u00fe\7(\2\2\u00fe\u00ff\7?\2\2\u00ff")
        buf.write("\30\3\2\2\2\u0100\u0101\7~\2\2\u0101\u0102\7?\2\2\u0102")
        buf.write("\32\3\2\2\2\u0103\u0104\7`\2\2\u0104\u0105\7?\2\2\u0105")
        buf.write("\34\3\2\2\2\u0106\u0107\7>\2\2\u0107\u0108\7>\2\2\u0108")
        buf.write("\u0109\7?\2\2\u0109\36\3\2\2\2\u010a\u010b\7@\2\2\u010b")
        buf.write("\u010c\7@\2\2\u010c\u010d\7?\2\2\u010d \3\2\2\2\u010e")
        buf.write("\u010f\7,\2\2\u010f\u0110\7,\2\2\u0110\u0111\7?\2\2\u0111")
        buf.write("\"\3\2\2\2\u0112\u0113\7\61\2\2\u0113\u0114\7\61\2\2\u0114")
        buf.write("\u0115\7?\2\2\u0115$\3\2\2\2\u0116\u0117\7f\2\2\u0117")
        buf.write("\u0118\7g\2\2\u0118\u0119\7n\2\2\u0119&\3\2\2\2\u011a")
        buf.write("\u011b\7r\2\2\u011b\u011c\7c\2\2\u011c\u011d\7u\2\2\u011d")
        buf.write("\u011e\7u\2\2\u011e(\3\2\2\2\u011f\u0120\7d\2\2\u0120")
        buf.write("\u0121\7t\2\2\u0121\u0122\7g\2\2\u0122\u0123\7c\2\2\u0123")
        buf.write("\u0124\7m\2\2\u0124*\3\2\2\2\u0125\u0126\7e\2\2\u0126")
        buf.write("\u0127\7q\2\2\u0127\u0128\7p\2\2\u0128\u0129\7v\2\2\u0129")
        buf.write("\u012a\7k\2\2\u012a\u012b\7p\2\2\u012b\u012c\7w\2\2\u012c")
        buf.write("\u012d\7g\2\2\u012d,\3\2\2\2\u012e\u012f\7t\2\2\u012f")
        buf.write("\u0130\7g\2\2\u0130\u0131\7v\2\2\u0131\u0132\7w\2\2\u0132")
        buf.write("\u0133\7t\2\2\u0133\u0134\7p\2\2\u0134.\3\2\2\2\u0135")
        buf.write("\u0136\7k\2\2\u0136\u0137\7h\2\2\u0137\60\3\2\2\2\u0138")
        buf.write("\u0139\7g\2\2\u0139\u013a\7n\2\2\u013a\u013b\7k\2\2\u013b")
        buf.write("\u013c\7h\2\2\u013c\62\3\2\2\2\u013d\u013e\7g\2\2\u013e")
        buf.write("\u013f\7n\2\2\u013f\u0140\7u\2\2\u0140\u0141\7g\2\2\u0141")
        buf.write("\64\3\2\2\2\u0142\u0143\7y\2\2\u0143\u0144\7j\2\2\u0144")
        buf.write("\u0145\7k\2\2\u0145\u0146\7n\2\2\u0146\u0147\7g\2\2\u0147")
        buf.write("\66\3\2\2\2\u0148\u0149\7h\2\2\u0149\u014a\7q\2\2\u014a")
        buf.write("\u014b\7t\2\2\u014b8\3\2\2\2\u014c\u014d\7k\2\2\u014d")
        buf.write("\u014e\7p\2\2\u014e:\3\2\2\2\u014f\u0150\7f\2\2\u0150")
        buf.write("\u0151\7g\2\2\u0151\u0152\7h\2\2\u0152<\3\2\2\2\u0153")
        buf.write("\u0154\7*\2\2\u0154>\3\2\2\2\u0155\u0156\7+\2\2\u0156")
        buf.write("@\3\2\2\2\u0157\u0158\7/\2\2\u0158\u0159\7@\2\2\u0159")
        buf.write("B\3\2\2\2\u015a\u015b\7a\2\2\u015b\u015c\7a\2\2\u015c")
        buf.write("\u015d\7k\2\2\u015d\u015e\7p\2\2\u015e\u015f\7k\2\2\u015f")
        buf.write("\u0160\7v\2\2\u0160\u0161\7a\2\2\u0161\u0162\7a\2\2\u0162")
        buf.write("D\3\2\2\2\u0163\u0164\7u\2\2\u0164\u0165\7g\2\2\u0165")
        buf.write("\u0166\7n\2\2\u0166\u0167\7h\2\2\u0167F\3\2\2\2\u0168")
        buf.write("\u0169\7e\2\2\u0169\u016a\7n\2\2\u016a\u016b\7c\2\2\u016b")
        buf.write("\u016c\7u\2\2\u016c\u016d\7u\2\2\u016dH\3\2\2\2\u016e")
        buf.write("\u016f\7B\2\2\u016fJ\3\2\2\2\u0170\u0171\7u\2\2\u0171")
        buf.write("\u0172\7v\2\2\u0172\u0173\7c\2\2\u0173\u0174\7v\2\2\u0174")
        buf.write("\u0175\7k\2\2\u0175\u0176\7e\2\2\u0176\u0177\7o\2\2\u0177")
        buf.write("\u0178\7g\2\2\u0178\u0179\7v\2\2\u0179\u017a\7j\2\2\u017a")
        buf.write("\u017b\7q\2\2\u017b\u017c\7f\2\2\u017cL\3\2\2\2\u017d")
        buf.write("\u017e\7q\2\2\u017e\u017f\7t\2\2\u017fN\3\2\2\2\u0180")
        buf.write("\u0181\7c\2\2\u0181\u0182\7p\2\2\u0182\u0183\7f\2\2\u0183")
        buf.write("P\3\2\2\2\u0184\u0185\7p\2\2\u0185\u0186\7q\2\2\u0186")
        buf.write("\u0187\7v\2\2\u0187R\3\2\2\2\u0188\u0189\7>\2\2\u0189")
        buf.write("T\3\2\2\2\u018a\u018b\7@\2\2\u018bV\3\2\2\2\u018c\u018d")
        buf.write("\7?\2\2\u018d\u018e\7?\2\2\u018eX\3\2\2\2\u018f\u0190")
        buf.write("\7@\2\2\u0190\u0191\7?\2\2\u0191Z\3\2\2\2\u0192\u0193")
        buf.write("\7>\2\2\u0193\u0194\7?\2\2\u0194\\\3\2\2\2\u0195\u0196")
        buf.write("\7#\2\2\u0196\u0197\7?\2\2\u0197^\3\2\2\2\u0198\u0199")
        buf.write("\7k\2\2\u0199\u019a\7u\2\2\u019a`\3\2\2\2\u019b\u019c")
        buf.write("\7~\2\2\u019cb\3\2\2\2\u019d\u019e\7`\2\2\u019ed\3\2\2")
        buf.write("\2\u019f\u01a0\7(\2\2\u01a0f\3\2\2\2\u01a1\u01a2\7>\2")
        buf.write("\2\u01a2\u01a3\7>\2\2\u01a3h\3\2\2\2\u01a4\u01a5\7@\2")
        buf.write("\2\u01a5\u01a6\7@\2\2\u01a6j\3\2\2\2\u01a7\u01a8\7-\2")
        buf.write("\2\u01a8l\3\2\2\2\u01a9\u01aa\7/\2\2\u01aan\3\2\2\2\u01ab")
        buf.write("\u01ac\7,\2\2\u01acp\3\2\2\2\u01ad\u01ae\7\61\2\2\u01ae")
        buf.write("r\3\2\2\2\u01af\u01b0\7\'\2\2\u01b0t\3\2\2\2\u01b1\u01b2")
        buf.write("\7\61\2\2\u01b2\u01b3\7\61\2\2\u01b3v\3\2\2\2\u01b4\u01b5")
        buf.write("\7\u0080\2\2\u01b5x\3\2\2\2\u01b6\u01b7\7,\2\2\u01b7\u01b8")
        buf.write("\7,\2\2\u01b8z\3\2\2\2\u01b9\u01ba\7P\2\2\u01ba\u01bb")
        buf.write("\7q\2\2\u01bb\u01bc\7p\2\2\u01bc\u01bd\7g\2\2\u01bd|\3")
        buf.write("\2\2\2\u01be\u01bf\7V\2\2\u01bf\u01c0\7t\2\2\u01c0\u01c1")
        buf.write("\7w\2\2\u01c1\u01c2\7g\2\2\u01c2~\3\2\2\2\u01c3\u01c4")
        buf.write("\7H\2\2\u01c4\u01c5\7c\2\2\u01c5\u01c6\7n\2\2\u01c6\u01c7")
        buf.write("\7u\2\2\u01c7\u01c8\7g\2\2\u01c8\u0080\3\2\2\2\u01c9\u01ca")
        buf.write("\7]\2\2\u01ca\u0082\3\2\2\2\u01cb\u01cc\7_\2\2\u01cc\u0084")
        buf.write("\3\2\2\2\u01cd\u01ce\7\60\2\2\u01ce\u0086\3\2\2\2\u01cf")
        buf.write("\u01d0\7D\2\2\u01d0\u01d1\7q\2\2\u01d1\u01d2\7q\2\2\u01d2")
        buf.write("\u01d3\7n\2\2\u01d3\u0088\3\2\2\2\u01d4\u01d5\7K\2\2\u01d5")
        buf.write("\u01d6\7p\2\2\u01d6\u01d7\7v\2\2\u01d7\u008a\3\2\2\2\u01d8")
        buf.write("\u01d9\7H\2\2\u01d9\u01da\7n\2\2\u01da\u01db\7q\2\2\u01db")
        buf.write("\u01dc\7c\2\2\u01dc\u01dd\7v\2\2\u01dd\u008c\3\2\2\2\u01de")
        buf.write("\u01df\7U\2\2\u01df\u01e0\7v\2\2\u01e0\u01e1\7t\2\2\u01e1")
        buf.write("\u01e2\7k\2\2\u01e2\u01e3\7p\2\2\u01e3\u01e4\7i\2\2\u01e4")
        buf.write("\u008e\3\2\2\2\u01e5\u01e6\7Q\2\2\u01e6\u01e7\7d\2\2\u01e7")
        buf.write("\u01e8\7l\2\2\u01e8\u01e9\7g\2\2\u01e9\u01ea\7e\2\2\u01ea")
        buf.write("\u01eb\7v\2\2\u01eb\u0090\3\2\2\2\u01ec\u01ed\7}\2\2\u01ed")
        buf.write("\u0092\3\2\2\2\u01ee\u01ef\7\177\2\2\u01ef\u0094\3\2\2")
        buf.write("\2\u01f0\u01f1\7H\2\2\u01f1\u01f2\7w\2\2\u01f2\u01f3\7")
        buf.write("p\2\2\u01f3\u01f4\7e\2\2\u01f4\u01f5\7v\2\2\u01f5\u01f6")
        buf.write("\7k\2\2\u01f6\u01f7\7q\2\2\u01f7\u01f8\7p\2\2\u01f8\u0096")
        buf.write("\3\2\2\2\u01f9\u01fa\7N\2\2\u01fa\u01fb\7k\2\2\u01fb\u01fc")
        buf.write("\7u\2\2\u01fc\u01fd\7v\2\2\u01fd\u0098\3\2\2\2\u01fe\u01ff")
        buf.write("\7V\2\2\u01ff\u0200\7w\2\2\u0200\u0201\7r\2\2\u0201\u0202")
        buf.write("\7n\2\2\u0202\u0203\7g\2\2\u0203\u009a\3\2\2\2\u0204\u0205")
        buf.write("\7U\2\2\u0205\u0206\7g\2\2\u0206\u0207\7v\2\2\u0207\u009c")
        buf.write("\3\2\2\2\u0208\u0209\7F\2\2\u0209\u020a\7k\2\2\u020a\u020b")
        buf.write("\7e\2\2\u020b\u020c\7v\2\2\u020c\u009e\3\2\2\2\u020d\u0210")
        buf.write("\5\u00a5S\2\u020e\u0210\5\u00b3Z\2\u020f\u020d\3\2\2\2")
        buf.write("\u020f\u020e\3\2\2\2\u0210\u00a0\3\2\2\2\u0211\u0214\5")
        buf.write("\u00cdg\2\u0212\u0214\5\u00cfh\2\u0213\u0211\3\2\2\2\u0213")
        buf.write("\u0212\3\2\2\2\u0214\u00a2\3\2\2\2\u0215\u0216\7V\2\2")
        buf.write("\u0216\u0217\7t\2\2\u0217\u0218\7w\2\2\u0218\u021f\7g")
        buf.write("\2\2\u0219\u021a\7H\2\2\u021a\u021b\7c\2\2\u021b\u021c")
        buf.write("\7n\2\2\u021c\u021d\7u\2\2\u021d\u021f\7g\2\2\u021e\u0215")
        buf.write("\3\2\2\2\u021e\u0219\3\2\2\2\u021f\u00a4\3\2\2\2\u0220")
        buf.write("\u0225\5\u00abV\2\u0221\u0225\5\u00adW\2\u0222\u0225\5")
        buf.write("\u00afX\2\u0223\u0225\5\u00b1Y\2\u0224\u0220\3\2\2\2\u0224")
        buf.write("\u0221\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0223\3\2\2\2")
        buf.write("\u0225\u00a6\3\2\2\2\u0226\u0227\6T\2\2\u0227\u0233\5")
        buf.write("\u00d7l\2\u0228\u022a\7\17\2\2\u0229\u0228\3\2\2\2\u0229")
        buf.write("\u022a\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022e\7\f\2\2")
        buf.write("\u022c\u022e\4\16\17\2\u022d\u0229\3\2\2\2\u022d\u022c")
        buf.write("\3\2\2\2\u022e\u0230\3\2\2\2\u022f\u0231\5\u00d7l\2\u0230")
        buf.write("\u022f\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0233\3\2\2\2")
        buf.write("\u0232\u0226\3\2\2\2\u0232\u022d\3\2\2\2\u0233\u0234\3")
        buf.write("\2\2\2\u0234\u0235\bT\2\2\u0235\u00a8\3\2\2\2\u0236\u023a")
        buf.write("\5\u00b9]\2\u0237\u0239\5\u00bb^\2\u0238\u0237\3\2\2\2")
        buf.write("\u0239\u023c\3\2\2\2\u023a\u0238\3\2\2\2\u023a\u023b\3")
        buf.write("\2\2\2\u023b\u00aa\3\2\2\2\u023c\u023a\3\2\2\2\u023d\u0241")
        buf.write("\5\u00bd_\2\u023e\u0240\5\u00bf`\2\u023f\u023e\3\2\2\2")
        buf.write("\u0240\u0243\3\2\2\2\u0241\u023f\3\2\2\2\u0241\u0242\3")
        buf.write("\2\2\2\u0242\u024a\3\2\2\2\u0243\u0241\3\2\2\2\u0244\u0246")
        buf.write("\7\62\2\2\u0245\u0244\3\2\2\2\u0246\u0247\3\2\2\2\u0247")
        buf.write("\u0245\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u024a\3\2\2\2")
        buf.write("\u0249\u023d\3\2\2\2\u0249\u0245\3\2\2\2\u024a\u00ac\3")
        buf.write("\2\2\2\u024b\u024c\7\62\2\2\u024c\u024e\t\2\2\2\u024d")
        buf.write("\u024f\5\u00c1a\2\u024e\u024d\3\2\2\2\u024f\u0250\3\2")
        buf.write("\2\2\u0250\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u00ae")
        buf.write("\3\2\2\2\u0252\u0253\7\62\2\2\u0253\u0255\t\3\2\2\u0254")
        buf.write("\u0256\5\u00c3b\2\u0255\u0254\3\2\2\2\u0256\u0257\3\2")
        buf.write("\2\2\u0257\u0255\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u00b0")
        buf.write("\3\2\2\2\u0259\u025a\7\62\2\2\u025a\u025c\t\4\2\2\u025b")
        buf.write("\u025d\5\u00c5c\2\u025c\u025b\3\2\2\2\u025d\u025e\3\2")
        buf.write("\2\2\u025e\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u00b2")
        buf.write("\3\2\2\2\u0260\u0261\5\u00c7d\2\u0261\u0262\7\60\2\2\u0262")
        buf.write("\u0263\5\u00c9e\2\u0263\u026e\3\2\2\2\u0264\u0265\5\u00c7")
        buf.write("d\2\u0265\u0266\5\u00cbf\2\u0266\u026e\3\2\2\2\u0267\u0268")
        buf.write("\5\u00c7d\2\u0268\u0269\7\60\2\2\u0269\u026a\5\u00c9e")
        buf.write("\2\u026a\u026b\3\2\2\2\u026b\u026c\5\u00cbf\2\u026c\u026e")
        buf.write("\3\2\2\2\u026d\u0260\3\2\2\2\u026d\u0264\3\2\2\2\u026d")
        buf.write("\u0267\3\2\2\2\u026e\u00b4\3\2\2\2\u026f\u0273\5\u00d7")
        buf.write("l\2\u0270\u0273\5\u00d9m\2\u0271\u0273\5\u00dbn\2\u0272")
        buf.write("\u026f\3\2\2\2\u0272\u0270\3\2\2\2\u0272\u0271\3\2\2\2")
        buf.write("\u0273\u0274\3\2\2\2\u0274\u0275\b[\3\2\u0275\u00b6\3")
        buf.write("\2\2\2\u0276\u0277\13\2\2\2\u0277\u00b8\3\2\2\2\u0278")
        buf.write("\u027a\t\5\2\2\u0279\u0278\3\2\2\2\u027a\u00ba\3\2\2\2")
        buf.write("\u027b\u027e\5\u00b9]\2\u027c\u027e\5\u00bf`\2\u027d\u027b")
        buf.write("\3\2\2\2\u027d\u027c\3\2\2\2\u027e\u00bc\3\2\2\2\u027f")
        buf.write("\u0280\t\6\2\2\u0280\u00be\3\2\2\2\u0281\u0282\t\7\2\2")
        buf.write("\u0282\u00c0\3\2\2\2\u0283\u0284\t\b\2\2\u0284\u00c2\3")
        buf.write("\2\2\2\u0285\u0286\t\t\2\2\u0286\u00c4\3\2\2\2\u0287\u0288")
        buf.write("\t\n\2\2\u0288\u00c6\3\2\2\2\u0289\u028b\5\u00bf`\2\u028a")
        buf.write("\u0289\3\2\2\2\u028b\u028c\3\2\2\2\u028c\u028a\3\2\2\2")
        buf.write("\u028c\u028d\3\2\2\2\u028d\u00c8\3\2\2\2\u028e\u0290\5")
        buf.write("\u00bf`\2\u028f\u028e\3\2\2\2\u0290\u0291\3\2\2\2\u0291")
        buf.write("\u028f\3\2\2\2\u0291\u0292\3\2\2\2\u0292\u00ca\3\2\2\2")
        buf.write("\u0293\u0295\t\13\2\2\u0294\u0296\t\f\2\2\u0295\u0294")
        buf.write("\3\2\2\2\u0295\u0296\3\2\2\2\u0296\u0298\3\2\2\2\u0297")
        buf.write("\u0299\5\u00bf`\2\u0298\u0297\3\2\2\2\u0299\u029a\3\2")
        buf.write("\2\2\u029a\u0298\3\2\2\2\u029a\u029b\3\2\2\2\u029b\u00cc")
        buf.write("\3\2\2\2\u029c\u02a1\7)\2\2\u029d\u02a0\5\u00d5k\2\u029e")
        buf.write("\u02a0\n\r\2\2\u029f\u029d\3\2\2\2\u029f\u029e\3\2\2\2")
        buf.write("\u02a0\u02a3\3\2\2\2\u02a1\u029f\3\2\2\2\u02a1\u02a2\3")
        buf.write("\2\2\2\u02a2\u02a4\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a4\u02af")
        buf.write("\7)\2\2\u02a5\u02aa\7$\2\2\u02a6\u02a9\5\u00d5k\2\u02a7")
        buf.write("\u02a9\n\16\2\2\u02a8\u02a6\3\2\2\2\u02a8\u02a7\3\2\2")
        buf.write("\2\u02a9\u02ac\3\2\2\2\u02aa\u02a8\3\2\2\2\u02aa\u02ab")
        buf.write("\3\2\2\2\u02ab\u02ad\3\2\2\2\u02ac\u02aa\3\2\2\2\u02ad")
        buf.write("\u02af\7$\2\2\u02ae\u029c\3\2\2\2\u02ae\u02a5\3\2\2\2")
        buf.write("\u02af\u00ce\3\2\2\2\u02b0\u02b1\7)\2\2\u02b1\u02b2\7")
        buf.write(")\2\2\u02b2\u02b3\7)\2\2\u02b3\u02b7\3\2\2\2\u02b4\u02b6")
        buf.write("\5\u00d1i\2\u02b5\u02b4\3\2\2\2\u02b6\u02b9\3\2\2\2\u02b7")
        buf.write("\u02b5\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02ba\3\2\2\2")
        buf.write("\u02b9\u02b7\3\2\2\2\u02ba\u02bb\7)\2\2\u02bb\u02bc\7")
        buf.write(")\2\2\u02bc\u02cb\7)\2\2\u02bd\u02be\7$\2\2\u02be\u02bf")
        buf.write("\7$\2\2\u02bf\u02c0\7$\2\2\u02c0\u02c4\3\2\2\2\u02c1\u02c3")
        buf.write("\5\u00d1i\2\u02c2\u02c1\3\2\2\2\u02c3\u02c6\3\2\2\2\u02c4")
        buf.write("\u02c2\3\2\2\2\u02c4\u02c5\3\2\2\2\u02c5\u02c7\3\2\2\2")
        buf.write("\u02c6\u02c4\3\2\2\2\u02c7\u02c8\7$\2\2\u02c8\u02c9\7")
        buf.write("$\2\2\u02c9\u02cb\7$\2\2\u02ca\u02b0\3\2\2\2\u02ca\u02bd")
        buf.write("\3\2\2\2\u02cb\u00d0\3\2\2\2\u02cc\u02cf\5\u00d3j\2\u02cd")
        buf.write("\u02cf\5\u00d5k\2\u02ce\u02cc\3\2\2\2\u02ce\u02cd\3\2")
        buf.write("\2\2\u02cf\u00d2\3\2\2\2\u02d0\u02d1\n\17\2\2\u02d1\u00d4")
        buf.write("\3\2\2\2\u02d2\u02d3\7^\2\2\u02d3\u02d7\13\2\2\2\u02d4")
        buf.write("\u02d5\7^\2\2\u02d5\u02d7\5\u00a7T\2\u02d6\u02d2\3\2\2")
        buf.write("\2\u02d6\u02d4\3\2\2\2\u02d7\u00d6\3\2\2\2\u02d8\u02da")
        buf.write("\t\20\2\2\u02d9\u02d8\3\2\2\2\u02da\u02db\3\2\2\2\u02db")
        buf.write("\u02d9\3\2\2\2\u02db\u02dc\3\2\2\2\u02dc\u00d8\3\2\2\2")
        buf.write("\u02dd\u02e1\7%\2\2\u02de\u02e0\n\21\2\2\u02df\u02de\3")
        buf.write("\2\2\2\u02e0\u02e3\3\2\2\2\u02e1\u02df\3\2\2\2\u02e1\u02e2")
        buf.write("\3\2\2\2\u02e2\u00da\3\2\2\2\u02e3\u02e1\3\2\2\2\u02e4")
        buf.write("\u02e6\7^\2\2\u02e5\u02e7\5\u00d7l\2\u02e6\u02e5\3\2\2")
        buf.write("\2\u02e6\u02e7\3\2\2\2\u02e7\u02ed\3\2\2\2\u02e8\u02ea")
        buf.write("\7\17\2\2\u02e9\u02e8\3\2\2\2\u02e9\u02ea\3\2\2\2\u02ea")
        buf.write("\u02eb\3\2\2\2\u02eb\u02ee\7\f\2\2\u02ec\u02ee\4\16\17")
        buf.write("\2\u02ed\u02e9\3\2\2\2\u02ed\u02ec\3\2\2\2\u02ee\u00dc")
        buf.write("\3\2\2\2)\2\u020f\u0213\u021e\u0224\u0229\u022d\u0230")
        buf.write("\u0232\u023a\u0241\u0247\u0249\u0250\u0257\u025e\u026d")
        buf.write("\u0272\u0279\u027d\u028c\u0291\u0295\u029a\u029f\u02a1")
        buf.write("\u02a8\u02aa\u02ae\u02b7\u02c4\u02ca\u02ce\u02d6\u02db")
        buf.write("\u02e1\u02e6\u02e9\u02ed\4\3T\2\b\2\2")
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
    NUMBER = 79
    STRING = 80
    BOOLEAN = 81
    INTEGER = 82
    NEWLINE = 83
    NAME = 84
    DECIMAL_INTEGER = 85
    OCT_INTEGER = 86
    HEX_INTEGER = 87
    BIN_INTEGER = 88
    FLOAT_NUMBER = 89
    SKIP_ = 90
    UNKNOWN_CHAR = 91

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
            "'None'", "'True'", "'False'", "'['", "']'", "'.'", "'Bool'", 
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
                  "T__74", "T__75", "T__76", "T__77", "NUMBER", "STRING", 
                  "BOOLEAN", "INTEGER", "NEWLINE", "NAME", "DECIMAL_INTEGER", 
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
            actions[82] = self.NEWLINE_action 
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
            preds[82] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.at_start_of_line()
         


