from darglint.parse.grammar import BaseGrammar
from darglint.parse.grammar import Production as P
from darglint.token import TokenType

# Generated on 2019-05-27 11:33:01.949675
class Grammar(BaseGrammar):
    productions = [
        P("start", ([], "short-description", "sections"), ([], "word", "line"), TokenType.WORD, TokenType.RETURNS, TokenType.COLON, TokenType.LPAREN, TokenType.RPAREN, TokenType.RAISES, TokenType.ARGUMENTS, TokenType.INDENT),
        P("sections", ([], "split", "sections0"), ([], "split", "sections1"), ([], "split", "sections2"), ([], "split", "sections3"), ([], "split", "sections4"), ([], "newline", "newlines"), TokenType.NEWLINE),
        P("short-description", ([], "word", "line"), TokenType.WORD, TokenType.RETURNS, TokenType.COLON, TokenType.LPAREN, TokenType.RPAREN, TokenType.RAISES, TokenType.ARGUMENTS, TokenType.INDENT),
        P("long-description", ([], "paragraph", "block0"), ([], "line", "paragraph0"), ([], "word", "line"), TokenType.WORD, TokenType.RETURNS, TokenType.COLON, TokenType.LPAREN, TokenType.RPAREN, TokenType.RAISES, TokenType.ARGUMENTS, TokenType.INDENT),
        P("returns-section", ([], "returns", "returns-section0")),
        P("yields-section", ([], "yields", "yields-section0")),
        P("arguments-section", ([], "arguments", "arguments-section0")),
        P("items-argument", ([], "item-argument", "items-argument0")),
        P("item-argument", ([], "head-argument", "item-argument0"), ([], "head-argument", "line")),
        P("head-argument", ([], "indent", "head-argument0")),
        P("argument", TokenType.WORD),
        P("raises-section", ([], "raises", "raises-section0")),
        P("items-exception", ([], "item-exception", "items-exception0")),
        P("item-exception", ([], "head-exception", "item-exception0"), ([], "head-exception", "line")),
        P("head-exception", ([], "indent", "head-exception0")),
        P("exception", TokenType.WORD),
        P("block-indented", ([], "paragraph-indented", "block-indented0"), ([], "indented", "paragraph-indented0"), ([], "indented", "line")),
        P("block", ([], "paragraph", "block0"), ([], "line", "paragraph0"), ([], "word", "line"), TokenType.WORD, TokenType.RETURNS, TokenType.COLON, TokenType.LPAREN, TokenType.RPAREN, TokenType.RAISES, TokenType.ARGUMENTS, TokenType.INDENT),
        P("paragraph-indented-two", ([], "indented-two", "paragraph-indented-two0"), ([], "indented-two", "line")),
        P("paragraph-indented", ([], "indented", "paragraph-indented0"), ([], "indented", "line")),
        P("paragraph", ([], "line", "paragraph0"), ([], "word", "line"), TokenType.WORD, TokenType.RETURNS, TokenType.COLON, TokenType.LPAREN, TokenType.RPAREN, TokenType.RAISES, TokenType.ARGUMENTS, TokenType.INDENT),
        P("line", ([], "word", "line"), TokenType.WORD, TokenType.RETURNS, TokenType.COLON, TokenType.LPAREN, TokenType.RPAREN, TokenType.RAISES, TokenType.ARGUMENTS, TokenType.INDENT),
        P("indented-two", ([], "indent", "indented-two0")),
        P("indented", ([], "indent", "indents"), TokenType.INDENT),
        P("indents", ([], "indent", "indents"), TokenType.INDENT),
        P("split", ([], "newline", "split0")),
        P("newlines", ([], "newline", "newlines"), TokenType.NEWLINE),
        P("word", TokenType.WORD, TokenType.RETURNS, TokenType.COLON, TokenType.LPAREN, TokenType.RPAREN, TokenType.RAISES, TokenType.ARGUMENTS),
        P("arguments", TokenType.ARGUMENTS),
        P("raises", TokenType.RAISES),
        P("returns", TokenType.RETURNS),
        P("yields", TokenType.YIELDS),
        P("colon", TokenType.COLON),
        P("indent", TokenType.INDENT),
        P("newline", TokenType.NEWLINE),
        P("sections0", ([], "long-description", "sections"), ([], "paragraph", "block0"), ([], "line", "paragraph0"), ([], "word", "line"), TokenType.WORD, TokenType.RETURNS, TokenType.COLON, TokenType.LPAREN, TokenType.RPAREN, TokenType.RAISES, TokenType.ARGUMENTS, TokenType.INDENT),
        P("sections1", ([], "returns-section", "sections"), ([], "returns", "returns-section0")),
        P("sections2", ([], "yields-section", "sections"), ([], "yields", "yields-section0")),
        P("sections3", ([], "raises-section", "sections"), ([], "raises", "raises-section0")),
        P("sections4", ([], "arguments-section", "sections"), ([], "arguments", "arguments-section0")),
        P("returns-section0", ([], "colon", "returns-section1")),
        P("returns-section1", ([], "newline", "block-indented")),
        P("yields-section0", ([], "colon", "yields-section1")),
        P("yields-section1", ([], "newline", "block-indented")),
        P("arguments-section0", ([], "colon", "arguments-section1")),
        P("arguments-section1", ([], "newline", "items-argument"), TokenType.NEWLINE),
        P("items-argument0", ([], "newline", "items-argument"), TokenType.NEWLINE),
        P("item-argument0", ([], "line", "item-argument1")),
        P("item-argument1", ([], "newline", "paragraph-indented-two")),
        P("head-argument0", ([], "argument", "colon")),
        P("raises-section0", ([], "colon", "raises-section1")),
        P("raises-section1", ([], "newline", "items-exception"), TokenType.NEWLINE),
        P("items-exception0", ([], "newline", "items-exception"), TokenType.NEWLINE),
        P("item-exception0", ([], "line", "item-exception1")),
        P("item-exception1", ([], "newline", "paragraph-indented-two")),
        P("head-exception0", ([], "exception", "colon")),
        P("block-indented0", ([], "split", "block-indented")),
        P("block0", ([], "split", "block")),
        P("paragraph-indented-two0", ([], "line", "paragraph-indented-two1")),
        P("paragraph-indented-two1", ([], "newline", "paragraph-indented-two")),
        P("paragraph-indented0", ([], "line", "paragraph-indented1")),
        P("paragraph-indented1", ([], "newline", "paragraph-indented")),
        P("paragraph0", ([], "newline", "paragraph")),
        P("indented-two0", ([], "indent", "indents"), TokenType.INDENT),
        P("split0", ([], "newline", "newlines"), TokenType.NEWLINE),
    ]

    start = "start"