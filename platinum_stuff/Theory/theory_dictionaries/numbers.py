# Platinum Numbers over 100
import re
import logging
from num2words import num2words # requires num2words to be installed so that plover can access it
# can be done by misusing the plugin installer as "plover -s plover_plugins install num2words"

LONGEST_KEY = 23


numbers = "1234506789"
quantifiers = ["HUPB", "THOU", "PH-L", "PW-L", "-DZ", "-S"]
written_money = ["SKP", "KREPBT", "-Z"]

def lookup(chord):

    chord = list(chord)
    chord = check_validity(chord)

    print("valid chord", chord)

    chordstring = "".join(chord)

    output = ""

    current_number = 0
    number_buffer = -1
    last_was_number = False
    is_dollars = False
    has_cents = False

    is_bl = False
    is_ml = False
    is_thou = False
    is_word_money = False

    # go through the chord to get the final number
    for stroke in chord:

        m = re.fullmatch("[0-9\-]*", stroke)

        if m is not None:
            stroke = stroke.replace("-", "")

        if not isinstance(stroke, str) or stroke == "":
            pass

        else:

            if stroke in numbers:

                # account for two-stroke numbers
                if last_was_number:
                    current_number = current_number-number_buffer + number_buffer*10+int(stroke)
                    number_buffer = number_buffer*10+int(stroke)
                else:
                    number_buffer = int(stroke)
                    current_number += number_buffer

                last_was_number = True

            elif stroke!="-S" and stroke!="-Z" and len(stroke)==2 and numbers.index(stroke[0]) < numbers.index(stroke[1]):

                number_buffer = int(stroke)
                current_number +=  number_buffer

            else:
                last_was_number = False

                if stroke == "-DZ":
                    is_dollars = True

                if stroke == "-S":
                    current_number -= number_buffer
                    has_cents = True
                    if not is_dollars:
                        raise KeyError

                # cannot modify if there are no numbers
                if number_buffer == -1:
                    raise KeyError

                if stroke == "-Z":
                    current_number = current_number-number_buffer
                    is_word_money = True

                if stroke == "HUPB":
                    current_number = current_number-number_buffer + number_buffer*100

                if stroke == "THOU":
                    is_thou = True
                    temp = current_number % 1000
                    current_number = current_number-temp + temp*1000

                if stroke == "PH-L":
                    is_ml = True
                    temp = current_number % 1000
                    current_number = current_number-temp + temp*1000000

                if stroke == "PW-L":
                    is_bl = True
                    current_number *= 1000000000


    output = str(current_number)

    if is_bl:
        output = output[:-9]+","+output[-9:-6]+","+output[-6:-3]+","+output[-3:]

    elif is_ml:
        output = output[:-6]+","+output[-6:-3]+","+output[-3:]

    elif is_thou:
        output = output[:-3]+","+output[-3:]

    # according to the transcription rule: When the amount is a million or above,
    # transcribe as words (million, billion) instead of the corresponding amount of zeroes
    # -> if the chord ends with ML or BL use the words
    # -> only use million if there is no billion quantifier before
    if is_dollars:
        output = "$"+output

    index = -1 if not is_dollars else -2

    if chord[index] == "PW-L":
        output = output[0:-12] + " billion"

    if chord[index] == "PH-L" and not is_bl:
        output = output[0:-8] + " million"


    if has_cents:
        n = str(number_buffer)
        if len(n)==1:
            n = "0"+n
        output = output+ "."+n

    if is_word_money:
        output = num2words(current_number)
        if current_number==1:
            output+=" dollar"
        else:
            output+=" dollars"
        output += " and "+num2words(number_buffer)
        if number_buffer==1:
            output+=" cent"
        else:
            output+=" cents"


    return output

def check_validity(chord):
    # entries are made up of at least 2 strokes
    if len(chord) < 2:
        raise KeyError

    # exclude empty start
    if chord[0] == "":
        raise KeyError

    # do not match if it starts with zero
    if chord[0][0] == "0":
        raise KeyError

    # only made up from the quantifiers and numbers
    for i, stroke in enumerate(chord):

        if stroke not in quantifiers and stroke not in written_money:
            m = re.fullmatch("[0-9\-]{0,3}", stroke)

            if m is None:
                raise KeyError
            else:
                stroke = stroke.replace("-", "")
                chord[i] = stroke

                if chord[0] == "":
                    raise KeyError

                if len(stroke)==2:
                    try:
                        if not numbers.index(stroke[0]) < numbers.index(stroke[1]):
                            raise KeyError
                    except ValueError: # if the stroke does not consist of two numbers it will not be in numbers, and index will throw this error
                        raise KeyError

                elif stroke not in numbers:
                    raise KeyError

        elif i==0: # has to start with a number
                raise KeyError

    # join only now because right hand numbers have been modified before
    chordstring = "".join(chord)

    # and never have more than 2 numbers in succession
    if re.search("\d{3}", chordstring) is not None:
        raise KeyError

    # if the money amount is written out, cents occurs at the end, proceeded by 1-2 numbers and AND
    m = re.search("(SKP)\d{1,2}(KREPBT-Z)", chordstring)
    if (not set(chord).isdisjoint(set(written_money))) and ( (m is None) or (m is not None and m.end(0) != len(chordstring)) ):
        raise KeyError

    elif m is not None:
        # modify chordstring for other matches to work
        chordstring = chordstring[:m.start(0)]


    # dollars can only occur at the end or followed by 1-2 numbers and cents
    m = re.search("-DZ", chordstring)
    #print("match dollar", m.end(0), len(chordstring), m.end(0) + 3)
    if m is not None and m.end(0) != len(chordstring) and m.end(0) + 3 > len(chordstring):
        print("dollar error")
        raise KeyError

    # cents can only occur at the end
    m = re.search("-S", chordstring)
    if m is not None and m.end(0) != len(chordstring):
        raise KeyError

    # return the modified chord list (with - removed for right side numbers)
    return chord

c = ['24', '-DZ', '14', '-S']
v = check_validity(c)
print("checked validity", v)


c = ['24', '-DZ', '1', '-S']
try:
    v = check_validity(c)
    print("checked validity", v)
except KeyError:
	print("key error, no matxh")
