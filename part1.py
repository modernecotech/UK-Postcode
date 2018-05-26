'''
implementing the regular expression from the example at
https://gist.github.com/edhiley/5da612c93e31c7e60355

regex snippet taken on 30th august 2016.
there is a mistake in the REGEX provided. AA99 has a [0-9] before the negative lookbehind.

  (GIR\s0AA) |
    (
        # A9 or A99 prefix
        ( ([A-PR-UWYZ][0-9][0-9]?) |
             # AA99 prefix with some excluded areas
            (([A-PR-UWYZ][A-HK-Y][0-9](?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[0-9])[0-9]) |
             # AA9 prefix with some excluded areas
             ([A-PR-UWYZ][A-HK-Y](?<!AB|LL|SO)[0-9]) |
             # WC1A prefix
             (WC[0-9][A-Z]) |
             (
                # A9A prefix
               ([A-PR-UWYZ][0-9][A-HJKPSTUW]) |
                # AA9A prefix
               ([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])
             )
            )
          )
          # 9AA suffix
        \s[0-9][ABD-HJLNP-UW-Z]{2}
        )
'''

import re, sys

def postcode_value(*args):
    postcode = str(sys.argv[1]+" "+sys.argv[2])
    return postcode


def regexmatch(postcode):
    result = re.fullmatch((r'(GIR\s0AA)|'\
           r'((([A-PR-UWYZ][0-9][0-9]?)|'\
           r'(([A-PR-UWYZ][A-HK-Y]'\
           r'(?<!(BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)))[0-9][0-9])|'\
	   r'([A-PR-UWYZ][A-HK-Y](?<!(AB|LL|SO))[0-9])|'\
	   r'(WC[0-9][A-Z])|'\
	   r'(([A-PR-UWYZ][0-9][A-HJKPSTUW])|'\
	   r'([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY])))'\
	   r'\s[0-9][ABD-HJLNP-UW-Z]{2})'),postcode)
    print(result)

if __name__ == "__main__":
    regexmatch(postcode_value(sys.argv))
