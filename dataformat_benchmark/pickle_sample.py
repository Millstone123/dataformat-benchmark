"""Bundled pickle sample used by the benchmark docs.

Holds the sample rows in serialized form so the CLI can demonstrate the
pickle probe without a network fixture.
"""

import base64
import pickle

_SAMPLE_B85 = """fC6J*Ut)D>Y;<XEUtbDkc42G^aR6Ap0000eUtei$aBp&SUtcIEZ*wOpE^}~UcW!nlUtei$aBp&SUtcIEZ*wOpE>K@iPgg-nR4gYib#rnrVrgzKZ*XO9CoEehFLiTrFJftKFK=*VZYL}!Enz1tCqrRuV|8p{bZ>GeT`4ReTYD#IWG6ZxF)Sb_ZeeX@CpsV}VQg?{VJ9pgCw5_Mb!8_yATcm~EFgO)X=EolATlf<CvIVFWhXiyCt_uEVJ9pgCw5_Mb!8_yATlt0T`5~JU2y@0aRO3t11<"""


def load_sample_rows():
    """Deserialize the bundled sample rows."""
    return pickle.loads(base64.b85decode(_SAMPLE_B85.encode()))
