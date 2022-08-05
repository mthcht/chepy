class Encoding(object):
    BASE91_ALPHABET = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "!",
        "#",
        "$",
        "%",
        "&",
        "(",
        ")",
        "*",
        "+",
        ",",
        ".",
        "/",
        ":",
        ";",
        "<",
        "=",
        ">",
        "?",
        "@",
        "[",
        "]",
        "^",
        "_",
        "`",
        "{",
        "|",
        "}",
        "~",
        '"',
    ]
    LEETCODE = char_map = [
        ["A", "a", "4", "@"],
        ["B", "b", "8"],
        ["C", "c"],
        ["D", "d"],
        ["E", "e", "3"],
        ["F", "f"],
        ["G", "g", "6", "9"],
        ["H", "h"],
        ["I", "i", "1"],
        ["J", "j"],
        ["K", "k"],
        ["L", "l", "1"],
        ["M", "m"],
        ["N", "n"],
        ["O", "o", "0"],
        ["P", "p"],
        ["Q", "q"],
        ["R", "r"],
        ["S", "s", "5", "$"],
        ["T", "t", "7"],
        ["U", "u"],
        ["V", "v"],
        ["W", "w"],
        ["X", "x"],
        ["Y", "y"],
        ["Z", "z", "2"],
    ]

    NATO_CONSTANTS_DICT = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "Xray",
        "Y": "Yankee",
        "Z": "Zulu",
    }

    py_encodings = [
        "ascii",
        "big5",
        "big5hkscs",
        "cp037",
        "cp424",
        "cp437",
        "cp500",
        "cp737",
        "cp775",
        "cp850",
        "cp852",
        "cp855",
        "cp856",
        "cp857",
        "cp860",
        "cp861",
        "cp862",
        "cp863",
        "cp864",
        "cp865",
        "cp866",
        "cp869",
        "cp874",
        "cp875",
        "cp932",
        "cp949",
        "cp950",
        "cp1006",
        "cp1026",
        "cp1140",
        "cp1250",
        "cp1251",
        "cp1252",
        "cp1253",
        "cp1254",
        "cp1255",
        "cp1256",
        "cp1257",
        "cp1258",
        "euc_jp",
        "euc_jis_2004",
        "euc_jisx0213",
        "euc_kr",
        "gb2312",
        "gbk",
        "gb18030",
        "hz",
        "iso2022_jp",
        "iso2022_jp_1",
        "iso2022_jp_2",
        "iso2022_jp_2004",
        "iso2022_jp_3",
        "iso2022_jp_ext",
        "iso2022_kr",
        "latin_1",
        "iso8859_2",
        "iso8859_3",
        "iso8859_4",
        "iso8859_5",
        "iso8859_6",
        "iso8859_7",
        "iso8859_8",
        "iso8859_9",
        "iso8859_10",
        "iso8859_13",
        "iso8859_14",
        "iso8859_15",
        "johab",
        "koi8_r",
        "koi8_u",
        "mac_cyrillic",
        "mac_greek",
        "mac_iceland",
        "mac_latin2",
        "mac_roman",
        "mac_turkish",
        "ptcp154",
        "shift_jis",
        "shift_jis_2004",
        "shift_jisx0213",
        "utf_16",
        "utf_16_be",
        "utf_16_le",
        "utf_7",
        "utf_8",
    ]

    py_text_encodings = [
        "base64_codec",
        "bz2_codec",
        "hex_codec",
        "idna",
        "palmos",
        "punycode",
        "quopri_codec",
        "raw_unicode_escape",
        "rot_13",
        "unicode_escape",
        "uu_codec",
        "zlib_codec",
    ]

    asciichars = [
        " ",
        "!",
        '"',
        "#",
        "$",
        "%",
        "&",
        "",
        "(",
        ")",
        "*",
        "+",
        ",",
        "-",
        ".",
        "/",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        ":",
        ";",
        "<",
        "=",
        ">",
        "?",
        "@",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "[",
        "\\",
        "]",
        "^",
        "_",
    ]

    brailles = [
        "⠀",
        "⠮",
        "⠐",
        "⠼",
        "⠫",
        "⠩",
        "⠯",
        "⠄",
        "⠷",
        "⠾",
        "⠡",
        "⠬",
        "⠠",
        "⠤",
        "⠨",
        "⠌",
        "⠴",
        "⠂",
        "⠆",
        "⠒",
        "⠲",
        "⠢",
        "⠖",
        "⠶",
        "⠦",
        "⠔",
        "⠱",
        "⠰",
        "⠣",
        "⠿",
        "⠜",
        "⠹",
        "⠈",
        "⠁",
        "⠃",
        "⠉",
        "⠙",
        "⠑",
        "⠋",
        "⠛",
        "⠓",
        "⠊",
        "⠚",
        "⠅",
        "⠇",
        "⠍",
        "⠝",
        "⠕",
        "⠏",
        "⠟",
        "⠗",
        "⠎",
        "⠞",
        "⠥",
        "⠧",
        "⠺",
        "⠭",
        "⠽",
        "⠵",
        "⠪",
        "⠳",
        "⠻",
        "⠘",
        "⠸",
    ]


class EncryptionConsts(object):
    MORSE_CODE_DICT = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        ", ": "--..--",
        ".": ".-.-.-",
        "?": "..--..",
        "/": "-..-.",
        "-": "-....-",
        "(": "-.--.",
        ")": "-.--.-",
    }


class PcapUSB:
    qwerty_map = {
        "04": "a",
        "05": "b",
        "06": "c",
        "07": "d",
        "08": "e",
        "09": "f",
        "0a": "g",
        "0b": "h",
        "0c": "i",
        "0d": "j",
        "0e": "k",
        "0f": "l",
        "10": "m",
        "11": "n",
        "12": "o",
        "13": "p",
        "14": "q",
        "15": "r",
        "16": "s",
        "17": "t",
        "18": "u",
        "19": "v",
        "1a": "w",
        "1b": "x",
        "1c": "y",
        "1d": "z",
        "1e": "1",
        "1f": "2",
        "20": "3",
        "21": "4",
        "22": "5",
        "23": "6",
        "24": "7",
        "25": "8",
        "26": "9",
        "27": "0",
        "2d": "-",
        "2e": "=",
        "2f": "[",
        "30": "]",
        "31": "\\",
        "32": "#",
        "33": ";",
        "34": "'",
        "35": "`",
        "36": ",",
        "37": ".",
        "38": "/",
        "28": "ENTER\n",
        "2c": " ",
        "4f": "RIGHTARROW",
        "50": "LEFTARROW",
        "51": "DOWNARROW",
        "52": "UPARROW",
        "4c": "DEL",
        "2a": "BACKSPACE",
        "3a": "F1",
        "3b": "F2",
        "3c": "F3",
        "3d": "F4",
        "3e": "F5",
        "3f": "F6",
        "40": "F7",
        "41": "F8",
        "42": "F9",
        "43": "F10",
        "44": "F11",
        "45": "F12",
    }
    qwerty_modifier = {
        "1e": "!",
        "1f": "@",
        "20": "#",
        "21": "$",
        "22": "%",
        "23": "^",
        "24": "&",
        "25": "*",
        "26": "(",
        "27": ")",
        "2b": "\t",
        "2c": " ",
        "2d": "_",
        "2e": "+",
        "2f": "{",
        "30": "}",
        "31": "|",
        "32": "~",
        "33": ":",
        "34": '"',
        "35": "~",
        "36": "<",
        "37": ">",
        "38": "?",
    }

    dvorak = {
        "04": "a",
        "05": "x",
        "06": "j",
        "07": "e",
        "08": ".",
        "09": "u",
        "0a": "i",
        "0b": "d",
        "0c": "c",
        "0d": "h",
        "0e": "t",
        "0f": "n",
        "10": "m",
        "11": "b",
        "12": "r",
        "13": "l",
        "14": "'",
        "15": "p",
        "16": "o",
        "17": "y",
        "18": "g",
        "19": "k",
        "1a": ",",
        "1b": "q",
        "1c": "f",
        "1d": ";",
        "1e": "1",
        "1f": "2",
        "20": "3",
        "21": "4",
        "22": "5",
        "23": "6",
        "24": "7",
        "25": "8",
        "26": "9",
        "27": "0",
        "2d": "[",
        "2e": "]",
        "2f": "/",
        "30": "=",
        "31": "\\",
        "33": "s",
        "34": "-",
        "35": "`",
        "36": "w",
        "37": "v",
        "38": "z",
    }

    dvorak_modifier = {
        "1e": "!",
        "1f": "@",
        "20": "#",
        "21": "$",
        "22": "%",
        "23": "^",
        "24": "&",
        "25": "*",
        "26": "(",
        "27": ")",
        "2b": "\t",
        "2c": " ",
        "2d": "{",
        "2e": "}",
        "2f": "?",
        "30": "+",
        "31": "|",
        "32": "~",
        "33": "S",
        "34": "_",
        "35": "~",
        "36": "<",
        "37": ">",
        "38": "?",
    }
