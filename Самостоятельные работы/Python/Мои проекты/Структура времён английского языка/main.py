Times_symbols_plus = {
    "Present continuous": ":) to be Ving... .",
    "Present simple": ":) V1/s ... .",
    "Present perfect": ":) have/has ed/V3 ... .",
    "Present perfect continuous": ":) have/has been Ving ... .",

    "Past continuous": ":) was/were Ving ... .",
    "Past simple": ":) ed/V2 ... .",
    "Past perfect": ":) had ed/V3 ... .",
    "Past perfect continuous": ":) had been Ving ... .",

    "Future continuous": ":) will be Ving ... .",
    "Future simple": ":) will V1/s ... .",
    "Future perfect": ":) will by the time have ed/V3 ... .",
    "Future perfect continuous": ":) will have been Ving ... .",

    "Future in the past continuous": ":) would be Ving ... .",
    "Future in the past simple": ":) would V1/s ... .",
    "Future in the past perfect": ":) would have ed/V3 ... .",
    "Future in the past perfect continuous": ":) would have been Ving ... ."
}

Times_symbols_minus = {
    "Present continuous": ":) to be not Ving ... .",
    "Present simple": ":) do/does not V1 ... .",
    "Present perfect": ":) have/has not ed/V3 ... .",
    "Present perfect continuous": ":) have/has not been Ving ... .",

    "Past continuous": ":) was/were not Ving ... .",
    "Past simple": ":) did not V1 ... .",
    "Past perfect": ":) had not ed/V3 ... .",
    "Past perfect continuous": ":) had not been Ving ... .",

    "Future continuous": ":) will not be Ving ... .",
    "Future simple": ":) will not V1/s ... .",
    "Future perfect": ":) will not by the time have ed/V3 ... .",
    "Future perfect continuous": ":) will not have been Ving ... .",

    "Future in the past continuous": ":) would not be Ving ... .",
    "Future in the past simple": ":) would not V1/s ... .",
    "Future in the past perfect": ":) would not have ed/V3 ... .",
    "Future in the past perfect continuous": ":) would not have been Ving ... ."
}

Times_symbols_ask = {
    "Present continuous": "To be :) Ving ... ?",
    "Present simple": "Do/Does :) V1 ... ?",
    "Present perfect": "Have/Has :) ed/V3 ... ?",
    "Present perfect continuous": "Have/Has :) been Ving ... ?",

    "Past continuous": "Was/Were :) Ving ... ?",
    "Past simple": "Did :) V1 ... ?",
    "Past perfect": "Had :) ed/V3 ... ?",
    "Past perfect continuous": "Had :) been Ving ... ?",

    "Future continuous": "Will :) be Ving ... ?",
    "Future simple": "Will :) V1/s ... ?",
    "Future perfect": "Will :) have ed/V3 ... ?",
    "Future perfect continuous": "Will have :) been Ving ... ?",

    "Future in the past continuous": "Would :) be Ving ... ?",
    "Future in the past simple": "Would :) V1/s ... ?",
    "Future in the past perfect": "Would :) have ed/V3 ... ?",
    "Future in the past perfect continuous": "Would have :) been Ving ... ?"
}
print("-------------------------------------------------------------------------------")
print("Условные обозначения:")
print("  + - утверждение")
print("  - - отрицание")
print("  ? - вопрос")
print("  :) - подлежащее; Mark, he, you, I")
print("  V - verb - глагол:")
print("    1/s - 1-ой формы; do, play, does, plays (только Simple и - Past Simple):")
print("      1 - пишется при подлежащих в 1-ом и 2-ом лицах; do, play")
print("      s - пишется при подлежащих в 3-ем лице; does, plays")
print("    ed/2 - 2-ой формы; did, played (только в + Past Simple):")
print("      ed - пишется при правильных глаголах; played")
print("      2 - пишется при неправильных глаголах; did")
print("    ed/3 - 3-ей формы; done, played (только Perfect):")
print("      ed - пишется при правильных глаголах; played")
print("      3 - пишется при неправильных глаголах; done")
print("    ing - глагол с окончанием -ing; doing, playing (только Continuous)")
print("  have/has, do/does - вспомогательные глаголы:")
print("    have, do - пишется при подлежащих в 1-ом и 2-ом лицах")
print("    has, does - пишется при подлежащих в 3-ем лице")
print("  had, will, be, been, would, by the time - вспомогательные глаголы")
print('  not - отрицание (дословно на русский как "не")')
print("  to be, was/were - вспомогательный глагол (только Present и Past Continuous):")
print("    to be (только Present Continuous) принимает следующие формы:")
print("      is - пишется при подлежащих в 3-ем лице - he, she, it")
print("      are - пишется при подлежащих во 2-ом лице - you, we, they")
print("      am - пишется только при подлежащем в 1-ом лице - I")
print("    was/were (только Past Continuous):")
print('      was - пишется при подлежащих единственного числа (I, he, she, it)')
print('      were - пишется при подлежащих множ. числа (You, We, They')
print("  ... - прочее")
print("-------------------------------------------------------------------------------")
print("Здесь вы можете узнать, как строятся утвердительное, отрицательное и вопросительное "
      "предложения в том или ином времени! \nВремена вводятся без сокращений. \nВыше - условные обозначения.")
print("-------------------------------------------------------------------------------")
Time = input("Введите время: ").capitalize()
print("-------------------------------------------------------------------------------")
print("+: " + Times_symbols_plus[Time])
print("-: " + Times_symbols_minus[Time])
print("?: " + Times_symbols_ask[Time])

input()
