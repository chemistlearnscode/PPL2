# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u019a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\5\2^\n\2\3\2\3\2\3\2\3\3\6\3d\n\3\r\3\16\3e\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\7\5p\n\5\f\5\16\5s\13\5\3\6\3")
        buf.write("\6\5\6w\n\6\3\7\3\7\6\7{\n\7\r\7\16\7|\3\7\3\7\5\7\u0081")
        buf.write("\n\7\3\b\3\b\3\b\5\b\u0086\n\b\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\13\7\13\u008f\n\13\f\13\16\13\u0092\13\13\3\f\3\f\3")
        buf.write("\f\3\f\5\f\u0098\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\7\16\u00a3\n\16\f\16\16\16\u00a6\13\16\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u00b9\n\21\3\22\7\22\u00bc\n")
        buf.write("\22\f\22\16\22\u00bf\13\22\3\22\7\22\u00c2\n\22\f\22\16")
        buf.write("\22\u00c5\13\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\7\25\u00d3\n\25\f\25\16\25\u00d6")
        buf.write("\13\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7")
        buf.write("\26\u00e1\n\26\f\26\16\26\u00e4\13\26\3\27\3\27\5\27\u00e8")
        buf.write("\n\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\7\31\u00f1\n")
        buf.write("\31\f\31\16\31\u00f4\13\31\3\31\6\31\u00f7\n\31\r\31\16")
        buf.write("\31\u00f8\3\31\6\31\u00fc\n\31\r\31\16\31\u00fd\3\31\7")
        buf.write("\31\u0101\n\31\f\31\16\31\u0104\13\31\5\31\u0106\n\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\5#\u0137")
        buf.write("\n#\3#\3#\3#\3$\3$\3$\7$\u013f\n$\f$\16$\u0142\13$\3%")
        buf.write("\3%\5%\u0146\n%\3%\3%\3&\3&\3&\3&\3&\3&\7&\u0150\n&\f")
        buf.write("&\16&\u0153\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u015b\n\'")
        buf.write("\f\'\16\'\u015e\13\'\3(\3(\3(\3(\3(\3(\7(\u0166\n(\f(")
        buf.write("\16(\u0169\13(\3)\3)\3)\3)\3)\3)\7)\u0171\n)\f)\16)\u0174")
        buf.write("\13)\3*\3*\3*\5*\u0179\n*\3+\3+\3+\5+\u017e\n+\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\5,\u018a\n,\3-\3-\3-\5-\u018f\n")
        buf.write("-\3-\3-\3.\3.\3.\3.\3.\5.\u0198\n.\3.\2\6JLNP/\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\2\b\3\2\679\3\2(\62\3\2&\'\3\2\34\37")
        buf.write("\3\2 $\3\2\36\37\2\u0199\2]\3\2\2\2\4c\3\2\2\2\6g\3\2")
        buf.write("\2\2\bl\3\2\2\2\nv\3\2\2\2\fx\3\2\2\2\16\u0082\3\2\2\2")
        buf.write("\20\u0087\3\2\2\2\22\u008b\3\2\2\2\24\u0090\3\2\2\2\26")
        buf.write("\u0093\3\2\2\2\30\u009b\3\2\2\2\32\u009f\3\2\2\2\34\u00a7")
        buf.write("\3\2\2\2\36\u00a9\3\2\2\2 \u00b8\3\2\2\2\"\u00bd\3\2\2")
        buf.write("\2$\u00c6\3\2\2\2&\u00c8\3\2\2\2(\u00cd\3\2\2\2*\u00d7")
        buf.write("\3\2\2\2,\u00e7\3\2\2\2.\u00ec\3\2\2\2\60\u0105\3\2\2")
        buf.write("\2\62\u0107\3\2\2\2\64\u0118\3\2\2\2\66\u011a\3\2\2\2")
        buf.write("8\u011c\3\2\2\2:\u011e\3\2\2\2<\u0120\3\2\2\2>\u0127\3")
        buf.write("\2\2\2@\u012d\3\2\2\2B\u0130\3\2\2\2D\u0133\3\2\2\2F\u013b")
        buf.write("\3\2\2\2H\u0143\3\2\2\2J\u0149\3\2\2\2L\u0154\3\2\2\2")
        buf.write("N\u015f\3\2\2\2P\u016a\3\2\2\2R\u0178\3\2\2\2T\u017d\3")
        buf.write("\2\2\2V\u0189\3\2\2\2X\u018b\3\2\2\2Z\u0197\3\2\2\2\\")
        buf.write("^\5\4\3\2]\\\3\2\2\2]^\3\2\2\2^_\3\2\2\2_`\5\24\13\2`")
        buf.write("a\7\2\2\3a\3\3\2\2\2bd\5\6\4\2cb\3\2\2\2de\3\2\2\2ec\3")
        buf.write("\2\2\2ef\3\2\2\2f\5\3\2\2\2gh\7\n\2\2hi\7\7\2\2ij\5\b")
        buf.write("\5\2jk\7\6\2\2k\7\3\2\2\2lq\5\n\6\2mn\7\5\2\2np\5\n\6")
        buf.write("\2om\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2r\t\3\2\2\2")
        buf.write("sq\3\2\2\2tw\5\f\7\2uw\5\16\b\2vt\3\2\2\2vu\3\2\2\2w\13")
        buf.write("\3\2\2\2xz\7\4\2\2y{\5\20\t\2zy\3\2\2\2{|\3\2\2\2|z\3")
        buf.write("\2\2\2|}\3\2\2\2}\u0080\3\2\2\2~\177\7\t\2\2\177\u0081")
        buf.write("\5\22\n\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\r\3")
        buf.write("\2\2\2\u0082\u0085\7\4\2\2\u0083\u0084\7\t\2\2\u0084\u0086")
        buf.write("\5\22\n\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\17\3\2\2\2\u0087\u0088\7\63\2\2\u0088\u0089\7\67\2\2")
        buf.write("\u0089\u008a\7\64\2\2\u008a\21\3\2\2\2\u008b\u008c\t\2")
        buf.write("\2\2\u008c\23\3\2\2\2\u008d\u008f\5\26\f\2\u008e\u008d")
        buf.write("\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\25\3\2\2\2\u0092\u0090\3\2\2\2\u0093")
        buf.write("\u0094\7\13\2\2\u0094\u0095\7\7\2\2\u0095\u0097\7\4\2")
        buf.write("\2\u0096\u0098\5\30\r\2\u0097\u0096\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\5\36\20\2\u009a")
        buf.write("\27\3\2\2\2\u009b\u009c\7\f\2\2\u009c\u009d\7\7\2\2\u009d")
        buf.write("\u009e\5\32\16\2\u009e\31\3\2\2\2\u009f\u00a4\5\34\17")
        buf.write("\2\u00a0\u00a1\7\5\2\2\u00a1\u00a3\5\34\17\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\33\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7")
        buf.write("\u00a8\5\n\6\2\u00a8\35\3\2\2\2\u00a9\u00aa\7\r\2\2\u00aa")
        buf.write("\u00ab\7\7\2\2\u00ab\u00ac\5\"\22\2\u00ac\u00ad\7\16\2")
        buf.write("\2\u00ad\u00ae\7\b\2\2\u00ae\37\3\2\2\2\u00af\u00b9\5")
        buf.write("&\24\2\u00b0\u00b9\5.\30\2\u00b1\u00b9\5\62\32\2\u00b2")
        buf.write("\u00b9\5<\37\2\u00b3\u00b9\5> \2\u00b4\u00b9\5@!\2\u00b5")
        buf.write("\u00b9\5B\"\2\u00b6\u00b9\5D#\2\u00b7\u00b9\5H%\2\u00b8")
        buf.write("\u00af\3\2\2\2\u00b8\u00b0\3\2\2\2\u00b8\u00b1\3\2\2\2")
        buf.write("\u00b8\u00b2\3\2\2\2\u00b8\u00b3\3\2\2\2\u00b8\u00b4\3")
        buf.write("\2\2\2\u00b8\u00b5\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7")
        buf.write("\3\2\2\2\u00b9!\3\2\2\2\u00ba\u00bc\5$\23\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00c3\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00c0\u00c2\5 \21\2\u00c1\u00c0\3\2\2\2\u00c2\u00c5\3")
        buf.write("\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4#")
        buf.write("\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7\5\6\4\2\u00c7")
        buf.write("%\3\2\2\2\u00c8\u00c9\5(\25\2\u00c9\u00ca\7\t\2\2\u00ca")
        buf.write("\u00cb\5J&\2\u00cb\u00cc\7\6\2\2\u00cc\'\3\2\2\2\u00cd")
        buf.write("\u00d4\7\4\2\2\u00ce\u00cf\7\63\2\2\u00cf\u00d0\5J&\2")
        buf.write("\u00d0\u00d1\7\64\2\2\u00d1\u00d3\3\2\2\2\u00d2\u00ce")
        buf.write("\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5)\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7")
        buf.write("\u00d8\7\30\2\2\u00d8\u00d9\5J&\2\u00d9\u00da\7\32\2\2")
        buf.write("\u00da\u00e2\5\60\31\2\u00db\u00dc\7\23\2\2\u00dc\u00dd")
        buf.write("\5J&\2\u00dd\u00de\7\32\2\2\u00de\u00df\5\60\31\2\u00df")
        buf.write("\u00e1\3\2\2\2\u00e0\u00db\3\2\2\2\u00e1\u00e4\3\2\2\2")
        buf.write("\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3+\3\2\2")
        buf.write("\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6\7\22\2\2\u00e6\u00e8")
        buf.write("\5\60\31\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00ea\7\24\2\2\u00ea\u00eb\7\b\2")
        buf.write("\2\u00eb-\3\2\2\2\u00ec\u00ed\5*\26\2\u00ed\u00ee\5,\27")
        buf.write("\2\u00ee/\3\2\2\2\u00ef\u00f1\5$\23\2\u00f0\u00ef\3\2")
        buf.write("\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3")
        buf.write("\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5")
        buf.write("\u00f7\5 \21\2\u00f6\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u0106\3")
        buf.write("\2\2\2\u00fa\u00fc\5$\23\2\u00fb\u00fa\3\2\2\2\u00fc\u00fd")
        buf.write("\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe")
        buf.write("\u0102\3\2\2\2\u00ff\u0101\5 \21\2\u0100\u00ff\3\2\2\2")
        buf.write("\u0101\u0104\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3")
        buf.write("\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u00f2")
        buf.write("\3\2\2\2\u0105\u00fb\3\2\2\2\u0106\61\3\2\2\2\u0107\u0108")
        buf.write("\7\27\2\2\u0108\u0109\7\65\2\2\u0109\u010a\5\64\33\2\u010a")
        buf.write("\u010b\7\t\2\2\u010b\u010c\5\66\34\2\u010c\u010d\7\5\2")
        buf.write("\2\u010d\u010e\58\35\2\u010e\u010f\7\5\2\2\u010f\u0110")
        buf.write("\5\64\33\2\u0110\u0111\7\t\2\2\u0111\u0112\5:\36\2\u0112")
        buf.write("\u0113\7\66\2\2\u0113\u0114\7\21\2\2\u0114\u0115\5\60")
        buf.write("\31\2\u0115\u0116\7\25\2\2\u0116\u0117\7\b\2\2\u0117\63")
        buf.write("\3\2\2\2\u0118\u0119\7\4\2\2\u0119\65\3\2\2\2\u011a\u011b")
        buf.write("\5J&\2\u011b\67\3\2\2\2\u011c\u011d\5J&\2\u011d9\3\2\2")
        buf.write("\2\u011e\u011f\5J&\2\u011f;\3\2\2\2\u0120\u0121\7\33\2")
        buf.write("\2\u0121\u0122\5J&\2\u0122\u0123\7\21\2\2\u0123\u0124")
        buf.write("\5\60\31\2\u0124\u0125\7\26\2\2\u0125\u0126\7\b\2\2\u0126")
        buf.write("=\3\2\2\2\u0127\u0128\7\21\2\2\u0128\u0129\5\60\31\2\u0129")
        buf.write("\u012a\7\33\2\2\u012a\u012b\5J&\2\u012b\u012c\7\6\2\2")
        buf.write("\u012c?\3\2\2\2\u012d\u012e\7\17\2\2\u012e\u012f\7\6\2")
        buf.write("\2\u012fA\3\2\2\2\u0130\u0131\7\20\2\2\u0131\u0132\7\6")
        buf.write("\2\2\u0132C\3\2\2\2\u0133\u0134\7\4\2\2\u0134\u0136\7")
        buf.write("\65\2\2\u0135\u0137\5F$\2\u0136\u0135\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0139\7\66\2\2\u0139")
        buf.write("\u013a\7\6\2\2\u013aE\3\2\2\2\u013b\u0140\5J&\2\u013c")
        buf.write("\u013d\7\5\2\2\u013d\u013f\5J&\2\u013e\u013c\3\2\2\2\u013f")
        buf.write("\u0142\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2")
        buf.write("\u0141G\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0145\7\31\2")
        buf.write("\2\u0144\u0146\5J&\2\u0145\u0144\3\2\2\2\u0145\u0146\3")
        buf.write("\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\7\6\2\2\u0148I")
        buf.write("\3\2\2\2\u0149\u014a\b&\1\2\u014a\u014b\5L\'\2\u014b\u0151")
        buf.write("\3\2\2\2\u014c\u014d\f\4\2\2\u014d\u014e\t\3\2\2\u014e")
        buf.write("\u0150\5L\'\2\u014f\u014c\3\2\2\2\u0150\u0153\3\2\2\2")
        buf.write("\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152K\3\2\2")
        buf.write("\2\u0153\u0151\3\2\2\2\u0154\u0155\b\'\1\2\u0155\u0156")
        buf.write("\5N(\2\u0156\u015c\3\2\2\2\u0157\u0158\f\4\2\2\u0158\u0159")
        buf.write("\t\4\2\2\u0159\u015b\5N(\2\u015a\u0157\3\2\2\2\u015b\u015e")
        buf.write("\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("M\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160\b(\1\2\u0160")
        buf.write("\u0161\5P)\2\u0161\u0167\3\2\2\2\u0162\u0163\f\4\2\2\u0163")
        buf.write("\u0164\t\5\2\2\u0164\u0166\5P)\2\u0165\u0162\3\2\2\2\u0166")
        buf.write("\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2")
        buf.write("\u0168O\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016b\b)\1\2")
        buf.write("\u016b\u016c\5R*\2\u016c\u0172\3\2\2\2\u016d\u016e\f\4")
        buf.write("\2\2\u016e\u016f\t\6\2\2\u016f\u0171\5R*\2\u0170\u016d")
        buf.write("\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172")
        buf.write("\u0173\3\2\2\2\u0173Q\3\2\2\2\u0174\u0172\3\2\2\2\u0175")
        buf.write("\u0176\7%\2\2\u0176\u0179\5T+\2\u0177\u0179\5T+\2\u0178")
        buf.write("\u0175\3\2\2\2\u0178\u0177\3\2\2\2\u0179S\3\2\2\2\u017a")
        buf.write("\u017b\t\7\2\2\u017b\u017e\5V,\2\u017c\u017e\5V,\2\u017d")
        buf.write("\u017a\3\2\2\2\u017d\u017c\3\2\2\2\u017eU\3\2\2\2\u017f")
        buf.write("\u018a\5(\25\2\u0180\u0181\7\65\2\2\u0181\u0182\5J&\2")
        buf.write("\u0182\u0183\7\66\2\2\u0183\u018a\3\2\2\2\u0184\u018a")
        buf.write("\5X-\2\u0185\u018a\7\67\2\2\u0186\u018a\78\2\2\u0187\u018a")
        buf.write("\7:\2\2\u0188\u018a\79\2\2\u0189\u017f\3\2\2\2\u0189\u0180")
        buf.write("\3\2\2\2\u0189\u0184\3\2\2\2\u0189\u0185\3\2\2\2\u0189")
        buf.write("\u0186\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u0188\3\2\2\2")
        buf.write("\u018aW\3\2\2\2\u018b\u018c\7\4\2\2\u018c\u018e\7\65\2")
        buf.write("\2\u018d\u018f\5Z.\2\u018e\u018d\3\2\2\2\u018e\u018f\3")
        buf.write("\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\7\66\2\2\u0191")
        buf.write("Y\3\2\2\2\u0192\u0193\5J&\2\u0193\u0194\7\5\2\2\u0194")
        buf.write("\u0195\5Z.\2\u0195\u0198\3\2\2\2\u0196\u0198\5J&\2\u0197")
        buf.write("\u0192\3\2\2\2\u0197\u0196\3\2\2\2\u0198[\3\2\2\2#]eq")
        buf.write("v|\u0080\u0085\u0090\u0097\u00a4\u00b8\u00bd\u00c3\u00d4")
        buf.write("\u00e2\u00e7\u00f2\u00f8\u00fd\u0102\u0105\u0136\u0140")
        buf.write("\u0145\u0151\u015c\u0167\u0172\u0178\u017d\u0189\u018e")
        buf.write("\u0197")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "','", "';'", 
                     "':'", "'.'", "'='", "'Var'", "'Function'", "'Parameter'", 
                     "'Body'", "'EndBody'", "'Break'", "'Continue'", "'Do'", 
                     "'Else'", "'ElseIf'", "'EndIf'", "'EndFor'", "'EndWhile'", 
                     "'For'", "'If'", "'Return'", "'Then'", "'While'", "'+'", 
                     "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", 
                     "'>=.'", "'['", "']'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'int'", "'boolean'", 
                     "'string'", "'array'" ]

    symbolicNames = [ "<INVALID>", "CMT", "ID", "COMMA", "SEMI", "COLON", 
                      "DOT", "ASSIGN", "VAR", "FUNCTION", "PARA", "BODY", 
                      "ENDBODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
                      "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "IF", "RETURN", 
                      "THEN", "WHILE", "IADD", "FADD", "ISUB", "FSUB", "IMUL", 
                      "FMUL", "IDIV", "FDIV", "IREM", "NEG", "CONJ", "DISJ", 
                      "EQ", "NOEQ", "LESS", "GREAT", "LEEQ", "GREQ", "NOEQF", 
                      "LEF", "GRF", "LEQF", "GEQF", "LS", "RS", "LB", "RB", 
                      "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "WS", 
                      "INTTYPE", "BOOLEANTYPE", "STRINGTYPE", "ARRAYTYPE", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_glovardeclprt = 1
    RULE_vardecl = 2
    RULE_varlist = 3
    RULE_vari = 4
    RULE_vari_array = 5
    RULE_vari_scalar = 6
    RULE_indexop = 7
    RULE_lit = 8
    RULE_funcdeclprt = 9
    RULE_funcdecl = 10
    RULE_parafun = 11
    RULE_paralist = 12
    RULE_para = 13
    RULE_bodyfun = 14
    RULE_stmttype = 15
    RULE_nulstmtlst = 16
    RULE_varstmt = 17
    RULE_asstmt = 18
    RULE_value = 19
    RULE_ifthenStmt = 20
    RULE_elseStmt = 21
    RULE_ifstmt = 22
    RULE_stmtlst = 23
    RULE_forstmt = 24
    RULE_scava = 25
    RULE_inex = 26
    RULE_conExp = 27
    RULE_upex = 28
    RULE_whilestmt = 29
    RULE_dowhistmt = 30
    RULE_breakstmt = 31
    RULE_contstmt = 32
    RULE_callstmt = 33
    RULE_bet = 34
    RULE_returnstmt = 35
    RULE_exp = 36
    RULE_exp1 = 37
    RULE_exp2 = 38
    RULE_exp3 = 39
    RULE_exp4 = 40
    RULE_exp5 = 41
    RULE_exp6 = 42
    RULE_funccall = 43
    RULE_explist = 44

    ruleNames =  [ "program", "glovardeclprt", "vardecl", "varlist", "vari", 
                   "vari_array", "vari_scalar", "indexop", "lit", "funcdeclprt", 
                   "funcdecl", "parafun", "paralist", "para", "bodyfun", 
                   "stmttype", "nulstmtlst", "varstmt", "asstmt", "value", 
                   "ifthenStmt", "elseStmt", "ifstmt", "stmtlst", "forstmt", 
                   "scava", "inex", "conExp", "upex", "whilestmt", "dowhistmt", 
                   "breakstmt", "contstmt", "callstmt", "bet", "returnstmt", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "funccall", "explist" ]

    EOF = Token.EOF
    CMT=1
    ID=2
    COMMA=3
    SEMI=4
    COLON=5
    DOT=6
    ASSIGN=7
    VAR=8
    FUNCTION=9
    PARA=10
    BODY=11
    ENDBODY=12
    BREAK=13
    CONTINUE=14
    DO=15
    ELSE=16
    ELSEIF=17
    ENDIF=18
    ENDFOR=19
    ENDWHILE=20
    FOR=21
    IF=22
    RETURN=23
    THEN=24
    WHILE=25
    IADD=26
    FADD=27
    ISUB=28
    FSUB=29
    IMUL=30
    FMUL=31
    IDIV=32
    FDIV=33
    IREM=34
    NEG=35
    CONJ=36
    DISJ=37
    EQ=38
    NOEQ=39
    LESS=40
    GREAT=41
    LEEQ=42
    GREQ=43
    NOEQF=44
    LEF=45
    GRF=46
    LEQF=47
    GEQF=48
    LS=49
    RS=50
    LB=51
    RB=52
    INTLIT=53
    FLOATLIT=54
    BOOLLIT=55
    STRINGLIT=56
    WS=57
    INTTYPE=58
    BOOLEANTYPE=59
    STRINGTYPE=60
    ARRAYTYPE=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdeclprt(self):
            return self.getTypedRuleContext(BKITParser.FuncdeclprtContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def glovardeclprt(self):
            return self.getTypedRuleContext(BKITParser.GlovardeclprtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 90
                self.glovardeclprt()


            self.state = 93
            self.funcdeclprt()
            self.state = 94
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlovardeclprtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKITParser.VardeclContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_glovardeclprt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlovardeclprt" ):
                return visitor.visitGlovardeclprt(self)
            else:
                return visitor.visitChildren(self)




    def glovardeclprt(self):

        localctx = BKITParser.GlovardeclprtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_glovardeclprt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 96
                self.vardecl()
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.VAR):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def varlist(self):
            return self.getTypedRuleContext(BKITParser.VarlistContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKITParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(BKITParser.VAR)
            self.state = 102
            self.match(BKITParser.COLON)
            self.state = 103
            self.varlist()
            self.state = 104
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VariContext)
            else:
                return self.getTypedRuleContext(BKITParser.VariContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_varlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarlist" ):
                return visitor.visitVarlist(self)
            else:
                return visitor.visitChildren(self)




    def varlist(self):

        localctx = BKITParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.vari()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 107
                self.match(BKITParser.COMMA)
                self.state = 108
                self.vari()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_array(self):
            return self.getTypedRuleContext(BKITParser.Vari_arrayContext,0)


        def vari_scalar(self):
            return self.getTypedRuleContext(BKITParser.Vari_scalarContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_vari

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari" ):
                return visitor.visitVari(self)
            else:
                return visitor.visitChildren(self)




    def vari(self):

        localctx = BKITParser.VariContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vari)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.vari_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.vari_scalar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def indexop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.IndexopContext)
            else:
                return self.getTypedRuleContext(BKITParser.IndexopContext,i)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def lit(self):
            return self.getTypedRuleContext(BKITParser.LitContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_vari_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_array" ):
                return visitor.visitVari_array(self)
            else:
                return visitor.visitChildren(self)




    def vari_array(self):

        localctx = BKITParser.Vari_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vari_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(BKITParser.ID)
            self.state = 120 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 119
                self.indexop()
                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LS):
                    break

            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 124
                self.match(BKITParser.ASSIGN)
                self.state = 125
                self.lit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_scalarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def lit(self):
            return self.getTypedRuleContext(BKITParser.LitContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_vari_scalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_scalar" ):
                return visitor.visitVari_scalar(self)
            else:
                return visitor.visitChildren(self)




    def vari_scalar(self):

        localctx = BKITParser.Vari_scalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vari_scalar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(BKITParser.ID)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 129
                self.match(BKITParser.ASSIGN)
                self.state = 130
                self.lit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(BKITParser.LS, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def RS(self):
            return self.getToken(BKITParser.RS, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_indexop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexop" ):
                return visitor.visitIndexop(self)
            else:
                return visitor.visitChildren(self)




    def indexop(self):

        localctx = BKITParser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(BKITParser.LS)
            self.state = 134
            self.match(BKITParser.INTLIT)
            self.state = 135
            self.match(BKITParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(BKITParser.BOOLLIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = BKITParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclprtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.FuncdeclContext)
            else:
                return self.getTypedRuleContext(BKITParser.FuncdeclContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_funcdeclprt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdeclprt" ):
                return visitor.visitFuncdeclprt(self)
            else:
                return visitor.visitChildren(self)




    def funcdeclprt(self):

        localctx = BKITParser.FuncdeclprtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcdeclprt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 139
                self.funcdecl()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def bodyfun(self):
            return self.getTypedRuleContext(BKITParser.BodyfunContext,0)


        def parafun(self):
            return self.getTypedRuleContext(BKITParser.ParafunContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = BKITParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(BKITParser.FUNCTION)
            self.state = 146
            self.match(BKITParser.COLON)
            self.state = 147
            self.match(BKITParser.ID)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARA:
                self.state = 148
                self.parafun()


            self.state = 151
            self.bodyfun()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParafunContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self):
            return self.getToken(BKITParser.PARA, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def paralist(self):
            return self.getTypedRuleContext(BKITParser.ParalistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_parafun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParafun" ):
                return visitor.visitParafun(self)
            else:
                return visitor.visitChildren(self)




    def parafun(self):

        localctx = BKITParser.ParafunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parafun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(BKITParser.PARA)
            self.state = 154
            self.match(BKITParser.COLON)
            self.state = 155
            self.paralist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ParaContext)
            else:
                return self.getTypedRuleContext(BKITParser.ParaContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = BKITParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.para()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 158
                self.match(BKITParser.COMMA)
                self.state = 159
                self.para()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari(self):
            return self.getTypedRuleContext(BKITParser.VariContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = BKITParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.vari()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyfunContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def nulstmtlst(self):
            return self.getTypedRuleContext(BKITParser.NulstmtlstContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_bodyfun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyfun" ):
                return visitor.visitBodyfun(self)
            else:
                return visitor.visitChildren(self)




    def bodyfun(self):

        localctx = BKITParser.BodyfunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_bodyfun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(BKITParser.BODY)
            self.state = 168
            self.match(BKITParser.COLON)
            self.state = 169
            self.nulstmtlst()
            self.state = 170
            self.match(BKITParser.ENDBODY)
            self.state = 171
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmttypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asstmt(self):
            return self.getTypedRuleContext(BKITParser.AsstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(BKITParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(BKITParser.ForstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(BKITParser.WhilestmtContext,0)


        def dowhistmt(self):
            return self.getTypedRuleContext(BKITParser.DowhistmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(BKITParser.BreakstmtContext,0)


        def contstmt(self):
            return self.getTypedRuleContext(BKITParser.ContstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(BKITParser.CallstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(BKITParser.ReturnstmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmttype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmttype" ):
                return visitor.visitStmttype(self)
            else:
                return visitor.visitChildren(self)




    def stmttype(self):

        localctx = BKITParser.StmttypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmttype)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.asstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 175
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 176
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 177
                self.dowhistmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 178
                self.breakstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 179
                self.contstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 180
                self.callstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 181
                self.returnstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NulstmtlstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VarstmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.VarstmtContext,i)


        def stmttype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmttypeContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmttypeContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_nulstmtlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNulstmtlst" ):
                return visitor.visitNulstmtlst(self)
            else:
                return visitor.visitChildren(self)




    def nulstmtlst(self):

        localctx = BKITParser.NulstmtlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_nulstmtlst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 184
                self.varstmt()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE))) != 0):
                self.state = 190
                self.stmttype()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKITParser.VardeclContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_varstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarstmt" ):
                return visitor.visitVarstmt(self)
            else:
                return visitor.visitChildren(self)




    def varstmt(self):

        localctx = BKITParser.VarstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_varstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.vardecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(BKITParser.ValueContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_asstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsstmt" ):
                return visitor.visitAsstmt(self)
            else:
                return visitor.visitChildren(self)




    def asstmt(self):

        localctx = BKITParser.AsstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_asstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.value()
            self.state = 199
            self.match(BKITParser.ASSIGN)
            self.state = 200
            self.exp(0)
            self.state = 201
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LS(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LS)
            else:
                return self.getToken(BKITParser.LS, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def RS(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RS)
            else:
                return self.getToken(BKITParser.RS, i)

        def getRuleIndex(self):
            return BKITParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = BKITParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(BKITParser.ID)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 204
                    self.match(BKITParser.LS)
                    self.state = 205
                    self.exp(0)
                    self.state = 206
                    self.match(BKITParser.RS) 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfthenStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def stmtlst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtlstContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtlstContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def getRuleIndex(self):
            return BKITParser.RULE_ifthenStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfthenStmt" ):
                return visitor.visitIfthenStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifthenStmt(self):

        localctx = BKITParser.IfthenStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ifthenStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(BKITParser.IF)
            self.state = 214
            self.exp(0)
            self.state = 215
            self.match(BKITParser.THEN)
            self.state = 216
            self.stmtlst()
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 217
                self.match(BKITParser.ELSEIF)
                self.state = 218
                self.exp(0)
                self.state = 219
                self.match(BKITParser.THEN)
                self.state = 220
                self.stmtlst()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def stmtlst(self):
            return self.getTypedRuleContext(BKITParser.StmtlstContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elseStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStmt" ):
                return visitor.visitElseStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseStmt(self):

        localctx = BKITParser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_elseStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 227
                self.match(BKITParser.ELSE)
                self.state = 228
                self.stmtlst()


            self.state = 231
            self.match(BKITParser.ENDIF)
            self.state = 232
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifthenStmt(self):
            return self.getTypedRuleContext(BKITParser.IfthenStmtContext,0)


        def elseStmt(self):
            return self.getTypedRuleContext(BKITParser.ElseStmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = BKITParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.ifthenStmt()
            self.state = 235
            self.elseStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VarstmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.VarstmtContext,i)


        def stmttype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmttypeContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmttypeContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_stmtlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlst" ):
                return visitor.visitStmtlst(self)
            else:
                return visitor.visitChildren(self)




    def stmtlst(self):

        localctx = BKITParser.StmtlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmtlst)
        self._la = 0 # Token type
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.VAR:
                    self.state = 237
                    self.varstmt()
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 244 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 243
                        self.stmttype()

                    else:
                        raise NoViableAltException(self)
                    self.state = 246 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 248
                    self.varstmt()
                    self.state = 251 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BKITParser.VAR):
                        break

                self.state = 256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 253
                        self.stmttype() 
                    self.state = 258
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def scava(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ScavaContext)
            else:
                return self.getTypedRuleContext(BKITParser.ScavaContext,i)


        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ASSIGN)
            else:
                return self.getToken(BKITParser.ASSIGN, i)

        def inex(self):
            return self.getTypedRuleContext(BKITParser.InexContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def conExp(self):
            return self.getTypedRuleContext(BKITParser.ConExpContext,0)


        def upex(self):
            return self.getTypedRuleContext(BKITParser.UpexContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmtlst(self):
            return self.getTypedRuleContext(BKITParser.StmtlstContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = BKITParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(BKITParser.FOR)
            self.state = 262
            self.match(BKITParser.LB)
            self.state = 263
            self.scava()
            self.state = 264
            self.match(BKITParser.ASSIGN)
            self.state = 265
            self.inex()
            self.state = 266
            self.match(BKITParser.COMMA)
            self.state = 267
            self.conExp()
            self.state = 268
            self.match(BKITParser.COMMA)
            self.state = 269
            self.scava()
            self.state = 270
            self.match(BKITParser.ASSIGN)
            self.state = 271
            self.upex()
            self.state = 272
            self.match(BKITParser.RB)
            self.state = 273
            self.match(BKITParser.DO)
            self.state = 274
            self.stmtlst()
            self.state = 275
            self.match(BKITParser.ENDFOR)
            self.state = 276
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScavaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_scava

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScava" ):
                return visitor.visitScava(self)
            else:
                return visitor.visitChildren(self)




    def scava(self):

        localctx = BKITParser.ScavaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_scava)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(BKITParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_inex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInex" ):
                return visitor.visitInex(self)
            else:
                return visitor.visitChildren(self)




    def inex(self):

        localctx = BKITParser.InexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_inex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_conExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConExp" ):
                return visitor.visitConExp(self)
            else:
                return visitor.visitChildren(self)




    def conExp(self):

        localctx = BKITParser.ConExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_conExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_upex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpex" ):
                return visitor.visitUpex(self)
            else:
                return visitor.visitChildren(self)




    def upex(self):

        localctx = BKITParser.UpexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_upex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmtlst(self):
            return self.getTypedRuleContext(BKITParser.StmtlstContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_whilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestmt" ):
                return visitor.visitWhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def whilestmt(self):

        localctx = BKITParser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(BKITParser.WHILE)
            self.state = 287
            self.exp(0)
            self.state = 288
            self.match(BKITParser.DO)
            self.state = 289
            self.stmtlst()
            self.state = 290
            self.match(BKITParser.ENDWHILE)
            self.state = 291
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhistmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmtlst(self):
            return self.getTypedRuleContext(BKITParser.StmtlstContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dowhistmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhistmt" ):
                return visitor.visitDowhistmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhistmt(self):

        localctx = BKITParser.DowhistmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_dowhistmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(BKITParser.DO)
            self.state = 294
            self.stmtlst()
            self.state = 295
            self.match(BKITParser.WHILE)
            self.state = 296
            self.exp(0)
            self.state = 297
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = BKITParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(BKITParser.BREAK)
            self.state = 300
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_contstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContstmt" ):
                return visitor.visitContstmt(self)
            else:
                return visitor.visitChildren(self)




    def contstmt(self):

        localctx = BKITParser.ContstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_contstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(BKITParser.CONTINUE)
            self.state = 303
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def bet(self):
            return self.getTypedRuleContext(BKITParser.BetContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = BKITParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_callstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(BKITParser.ID)
            self.state = 306
            self.match(BKITParser.LB)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.ISUB) | (1 << BKITParser.FSUB) | (1 << BKITParser.NEG) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 307
                self.bet()


            self.state = 310
            self.match(BKITParser.RB)
            self.state = 311
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_bet

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBet" ):
                return visitor.visitBet(self)
            else:
                return visitor.visitChildren(self)




    def bet(self):

        localctx = BKITParser.BetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_bet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.exp(0)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 314
                self.match(BKITParser.COMMA)
                self.state = 315
                self.exp(0)
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = BKITParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(BKITParser.RETURN)
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.ISUB) | (1 << BKITParser.FSUB) | (1 << BKITParser.NEG) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 322
                self.exp(0)


            self.state = 325
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def NOEQ(self):
            return self.getToken(BKITParser.NOEQ, 0)

        def LESS(self):
            return self.getToken(BKITParser.LESS, 0)

        def GREAT(self):
            return self.getToken(BKITParser.GREAT, 0)

        def LEEQ(self):
            return self.getToken(BKITParser.LEEQ, 0)

        def GREQ(self):
            return self.getToken(BKITParser.GREQ, 0)

        def NOEQF(self):
            return self.getToken(BKITParser.NOEQF, 0)

        def LEF(self):
            return self.getToken(BKITParser.LEF, 0)

        def GRF(self):
            return self.getToken(BKITParser.GRF, 0)

        def LEQF(self):
            return self.getToken(BKITParser.LEQF, 0)

        def GEQF(self):
            return self.getToken(BKITParser.GEQF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.exp1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 330
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 331
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQ) | (1 << BKITParser.NOEQ) | (1 << BKITParser.LESS) | (1 << BKITParser.GREAT) | (1 << BKITParser.LEEQ) | (1 << BKITParser.GREQ) | (1 << BKITParser.NOEQF) | (1 << BKITParser.LEF) | (1 << BKITParser.GRF) | (1 << BKITParser.LEQF) | (1 << BKITParser.GEQF))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 332
                    self.exp1(0) 
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def CONJ(self):
            return self.getToken(BKITParser.CONJ, 0)

        def DISJ(self):
            return self.getToken(BKITParser.DISJ, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 341
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 342
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.CONJ or _la==BKITParser.DISJ):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 343
                    self.exp2(0) 
                self.state = 348
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def IADD(self):
            return self.getToken(BKITParser.IADD, 0)

        def FADD(self):
            return self.getToken(BKITParser.FADD, 0)

        def ISUB(self):
            return self.getToken(BKITParser.ISUB, 0)

        def FSUB(self):
            return self.getToken(BKITParser.FSUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 352
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 353
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.IADD) | (1 << BKITParser.FADD) | (1 << BKITParser.ISUB) | (1 << BKITParser.FSUB))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 354
                    self.exp3(0) 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def IMUL(self):
            return self.getToken(BKITParser.IMUL, 0)

        def FMUL(self):
            return self.getToken(BKITParser.FMUL, 0)

        def IDIV(self):
            return self.getToken(BKITParser.IDIV, 0)

        def FDIV(self):
            return self.getToken(BKITParser.FDIV, 0)

        def IREM(self):
            return self.getToken(BKITParser.IREM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 363
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 364
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.IMUL) | (1 << BKITParser.FMUL) | (1 << BKITParser.IDIV) | (1 << BKITParser.FDIV) | (1 << BKITParser.IREM))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 365
                    self.exp4() 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEG(self):
            return self.getToken(BKITParser.NEG, 0)

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp4)
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.match(BKITParser.NEG)
                self.state = 372
                self.exp5()
                pass
            elif token in [BKITParser.ID, BKITParser.ISUB, BKITParser.FSUB, BKITParser.LB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.BOOLLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def ISUB(self):
            return self.getToken(BKITParser.ISUB, 0)

        def FSUB(self):
            return self.getToken(BKITParser.FSUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ISUB, BKITParser.FSUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                _la = self._input.LA(1)
                if not(_la==BKITParser.ISUB or _la==BKITParser.FSUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 377
                self.exp6()
                pass
            elif token in [BKITParser.ID, BKITParser.LB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.BOOLLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(BKITParser.ValueContext,0)


        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def funccall(self):
            return self.getTypedRuleContext(BKITParser.FunccallContext,0)


        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def BOOLLIT(self):
            return self.getToken(BKITParser.BOOLLIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKITParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exp6)
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.match(BKITParser.LB)
                self.state = 383
                self.exp(0)
                self.state = 384
                self.match(BKITParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.funccall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 387
                self.match(BKITParser.INTLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 388
                self.match(BKITParser.FLOATLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 389
                self.match(BKITParser.STRINGLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 390
                self.match(BKITParser.BOOLLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def explist(self):
            return self.getTypedRuleContext(BKITParser.ExplistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = BKITParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(BKITParser.ID)
            self.state = 394
            self.match(BKITParser.LB)
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.ISUB) | (1 << BKITParser.FSUB) | (1 << BKITParser.NEG) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 395
                self.explist()


            self.state = 398
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def explist(self):
            return self.getTypedRuleContext(BKITParser.ExplistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_explist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = BKITParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_explist)
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.exp(0)
                self.state = 401
                self.match(BKITParser.COMMA)
                self.state = 402
                self.explist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[36] = self.exp_sempred
        self._predicates[37] = self.exp1_sempred
        self._predicates[38] = self.exp2_sempred
        self._predicates[39] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




